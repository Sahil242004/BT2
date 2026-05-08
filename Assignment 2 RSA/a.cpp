#include <iostream>
#include<vector>
using namespace std;
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

vector<int,int> findPrimeProduct(int start, int end) {
    for (int p = 2; p * p <= end; p++) {
        if (isPrime(p)) {
            for (int q = p; q * p <= end; q++) {
                if (isPrime(q)) {
                    int product = p * q;
                    if (product >= start && product <= end) {
                        cout << "Primes found: " << p << " and " << q << endl;
                        cout << "Product: " << product << endl;
                        return {p,q};
                    }
                }
            }
        }
    }
    return {-1,-1};
}
