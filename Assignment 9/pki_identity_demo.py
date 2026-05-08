import hashlib
import json
import random
from dataclasses import dataclass


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    t, new_t = 0, 1
    r, new_r = phi, e
    while new_r != 0:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r
    if r > 1:
        raise ValueError("No modular inverse")
    if t < 0:
        t += phi
    return t


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def random_prime(start=200, end=500):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p


def generate_rsa_keys():
    p = random_prime()
    q = random_prime()
    while q == p:
        q = random_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = mod_inverse(e, phi)
    return (e, n), (d, n)


def hash_to_int(text):
    return int(hashlib.sha256(text.encode()).hexdigest(), 16)


def rsa_sign(private_key, message):
    d, n = private_key
    h = hash_to_int(message) % n
    return pow(h, d, n)


def rsa_verify(public_key, message, signature):
    e, n = public_key
    h = hash_to_int(message) % n
    recovered = pow(signature, e, n)
    return recovered == h


@dataclass
class Certificate:
    subject_id: str
    subject_public_key: tuple
    issuer_name: str
    signature: int


class CertificateAuthority:
    def __init__(self, name):
        self.name = name
        self.public_key, self.private_key = generate_rsa_keys()

    def issue_certificate(self, subject_id, subject_public_key):
        payload = json.dumps(
            {
                "subject_id": subject_id,
                "subject_public_key": list(subject_public_key),
                "issuer_name": self.name,
            },
            sort_keys=True,
        )
        signature = rsa_sign(self.private_key, payload)
        return Certificate(subject_id, subject_public_key, self.name, signature)


class IdentityRegistry:
    def __init__(self, trusted_ca_public_key, trusted_ca_name):
        self.trusted_ca_public_key = trusted_ca_public_key
        self.trusted_ca_name = trusted_ca_name
        self.identities = {}

    def register(self, cert):
        payload = json.dumps(
            {
                "subject_id": cert.subject_id,
                "subject_public_key": list(cert.subject_public_key),
                "issuer_name": cert.issuer_name,
            },
            sort_keys=True,
        )
        if cert.issuer_name != self.trusted_ca_name:
            return False, "Rejected: untrusted issuer."
        if not rsa_verify(self.trusted_ca_public_key, payload, cert.signature):
            return False, "Rejected: invalid certificate signature."

        self.identities[cert.subject_id] = cert.subject_public_key
        return True, "Accepted: identity registered."


def main():
    print("Assignment 9: PKI-Based Identity Deployment (Simulated Infrastructure)")

    ca = CertificateAuthority("Campus-CA")
    print("\nCA initialized")
    print("CA Public Key:", ca.public_key)

    alice_pub, alice_priv = generate_rsa_keys()
    bob_pub, bob_priv = generate_rsa_keys()

    alice_cert = ca.issue_certificate("alice@college.edu", alice_pub)
    bob_cert = ca.issue_certificate("bob@college.edu", bob_pub)

    registry = IdentityRegistry(ca.public_key, "Campus-CA")

    ok_a, msg_a = registry.register(alice_cert)
    ok_b, msg_b = registry.register(bob_cert)

    print("\nCertificate registration")
    print("Alice:", msg_a)
    print("Bob  :", msg_b)

    secure_message = "Student transcript hash: 9f6f8ac2"
    signature = rsa_sign(alice_priv, secure_message)

    verified = rsa_verify(registry.identities["alice@college.edu"], secure_message, signature)
    print("\nIdentity-based message verification")
    print("Verified with Alice registered public key:", verified)


if __name__ == "__main__":
    random.seed(42)
    main()
