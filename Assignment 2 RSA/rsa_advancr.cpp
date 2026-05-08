#include <iostream>
#include <vector>
#include <utility>
#include <cstdlib>
#include <ctime>
using namespace std;


string asciiVectorToWord(const vector<int>& asciiValues) {
    string result = "";

    for (int val : asciiValues) {
        result += static_cast<char>(val);
    }

    return result;
}


bool isPrime(int n) {
    if (n <= 1)
        return false;
    if (n <= 3)
        return true;

    if (n % 2 == 0 || n % 3 == 0)
        return false;

    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    }

    return true;
}


pair<int, int> getRandomPrimes(int minProd = 128, int maxProd = 255) {
    static bool seeded = false;
    if (!seeded) {
        srand(time(nullptr));
        seeded = true;
    }

    vector<pair<int, int>> validPairs;

    for (int p = 2; p * p < maxProd; p++) {
        if (!isPrime(p)) continue;

        for (int q = p; q * p < maxProd; q++) {
            if (!isPrime(q)) continue;

            int product = p * q;
            if (product > minProd && product < maxProd) {
                validPairs.push_back({p, q});
            }
        }
    }

    if (validPairs.empty())
        return {-1, -1};

    return validPairs[rand() % validPairs.size()];
}


int find_d(int e, int fi_n)
{
    for (int d = 1; d < fi_n; d++)
    {
        if ((e * d) % fi_n == 1)
        {
            return d;
        }
    }
    return -1;
}

int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

vector<int> find_ascii_value(string message)
{
    int length = message.length();
    char character;
    int asciiValue = 0;
    vector<int> temp;
    for (int i = 0; i < length; i++)
    {
        character = message[i];
        asciiValue = static_cast<int>(character);
        temp.push_back(asciiValue);
    }
    return temp;
}

int find_e(int p, int q)
{
    int fi_n = (p - 1) * (q - 1);
    int e = 3;
    // e is co-prime to fi_n
    // gcd(e,fi_n) is 1
    while (gcd(e, fi_n) != 1)
    {
        e++;
    }
    return e;
}

int find_n(int p, int q)
{
    return p * q;
}

int find_fi_n(int p, int q)
{
    return (p - 1) * (q - 1);
}

int mod_exp(int base, int exp, int mod)
{
    int result = 1;

    for (int i = 0; i < exp; i++)
    {
        result = (result * base) % mod;
    }

    return result;
}

void find_keys(string message)
{
    auto primes = getRandomPrimes();
    int p, q;
    p = primes.first;
    q = primes.second;

    cout << "Selected Two Prime No's : " << p << " " << q << endl;

    int n = find_n(p, q);
    int e = find_e(p, q);
    int d = find_d(e, find_fi_n(p, q));

    cout << "Public Key : (" << e << "," << n << ")" << endl;
    cout << "Private Key : (" << d << "," << n << ")" << endl;
}

void Encrypt_Message(string message)
{
    int public_key_e, public_key_n;

    cout << "Enter Public Key (e,n) : ";
    cin >> public_key_e >> public_key_n;
    cout << endl;

    vector<int> message_v = find_ascii_value(message);

    cout << "Encrypted Message is : ";
    for (int i = 0; i < message_v.size(); i++)
    {
        int c = mod_exp(message_v[i], public_key_e, public_key_n);
        cout << c << " ";
    }
    cout<<endl;
}

void Decrypt_Message(int length)
{
    int d_message;
    int private_key_e, private_key_n;
    
    cout << "Enter Private Key (e,n) : ";
    cin >> private_key_e >> private_key_n;
   
    vector<int> dec_message;
    
    cout << "Enter the Encrypted message : ";
    for (int i = 0; i < length; i++)
    {
        cin >> d_message;
        int c = mod_exp(d_message, private_key_e, private_key_n);
        dec_message.push_back(c);
    }
    
    cout << "Decrypted Message is : ";
    for (int j = 0; j < length; j++)
    {
        cout << dec_message[j] << " ";
    }
    cout<<endl;

    string final_text = asciiVectorToWord(dec_message);
    cout<<"The Final Converted Text is : "<<final_text<<endl;
}
int main()
{
    int choice;
    string message;
    cout << "Enter Message : " << endl;
    cin >> message;
    int length = message.length();
    do
    {
        cout << "Please Select the no of operation you want to perform : " << endl;
        cout << "1. Generate Private and Public Keys" << endl;
        cout << "2. Encrypt The Message" << endl;
        cout << "3. Decrypt The Message" << endl;
        cout << "4. Exit" << endl;
        cin >> choice;
        switch (choice)
        {
        case 1:
            find_keys(message);
            cout << "****************************************************************************************************************************" << endl;
            break;
        case 2:
            Encrypt_Message(message);
            cout << "****************************************************************************************************************************" << endl;
            break;
        case 3:
            Decrypt_Message(length);
            cout << "****************************************************************************************************************************" << endl;
            break;
        case 4:
            cout << "Exiting Program" << endl;
            cout << "****************************************************************************************************************************" << endl;
            break;
        default:
            cout << "Invalid choice" << endl;
        }
    } while (choice != 4);

    return 0;
}