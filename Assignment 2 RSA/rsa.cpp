#include <iostream>
#include<vector>
using namespace std;
int find_d(int e, int fi_n) {
    for (int d = 1; d < fi_n; d++) {
        if ((e * d) % fi_n == 1) {
            return d;
        }
    }
    return -1;
}

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int find_ascii_value(string message){
    int length = message.length();
    char character;
    int asciiValue = 0;
    for(int i=0;i<length;i++){
        character = message[i];
        asciiValue = asciiValue + static_cast<int>(character);
    }
    return (asciiValue/length);
      
}

bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

pair<int,int> findPrimeProduct(int start, int end) {
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


int find_e(int p,int q){
    int fi_n = (p-1) * (q-1);
    int e = 3; 
    //e is co-prime to fi_n
    //gcd(e,fi_n) is 1
    while(gcd(e,fi_n) != 1){
        e++;
    }
    return e;
}

int find_n(int p,int q){
    return p*q;
}

int find_fi_n(int p ,int q){
    return (p-1) * (q-1);
}

int mod_exp(int base, int exp, int mod) {
    int result = 1;

    for (int i = 0; i < exp; i++) {
        result = (result * base) % mod;
    }

    return result;
}


void find_keys(string message){
    
    int p,q;
    int start = find_ascii_value(message);
    int end = 255;
    pair<int, int> primePairs = findPrimeProduct(start, end);


    p = primePairs.first;
    q = primePairs.second;
    int n = find_n(p,q);
    int e = find_e(p,q);
    int d = find_d(e,find_fi_n(p,q));

    cout<<"Public Key : ("<<e<<","<<n<<")"<<endl;
    cout<<"Private Key : ("<<d<<","<<n<<")"<<endl;
}

void Encrypt_Message(string message){
  int message_v = find_ascii_value(message);

    int public_key_e,public_key_n;
    cout<<"Enter Public Key (e,n) : ";
    cin>>public_key_e>>public_key_n;
    cout<<endl;

    int c = mod_exp(message_v,public_key_e,public_key_n);
    cout<<"Encrypted Message is : "<<c<<endl;
}

void Decrypt_Message(){
    int d_message;
    cout<<"Enter the Encrypted message : ";
    cin>>d_message;
    cout<<endl;

    int private_key_e,private_key_n;
    cout<<"Enter Private Key (e,n) : ";
    cin>>private_key_e>>private_key_n;
    cout<<endl;

    int c = mod_exp(d_message,private_key_e,private_key_n);
    cout<<"Decrypted Message is : "<<c<<endl;
}
int main(){
    int choice;
    string message;
    cout<<"Enter Message : "<<endl;
    cin>>message;
    do{
        cout<<"Please Select the no of operation you want to perform : "<<endl;
        cout<<"1. Generate Private and Public Keys"<<endl;
        cout<<"2. Encrypt The Message"<<endl;
        cout<<"3. Decrypt The Message"<<endl;
        cout<<"4. Exit"<<endl;
        cin>>choice;
        switch(choice){
            case 1:
                find_keys(message);
                cout<<"****************************************************************************************************************************"<<endl;
                break;
            case 2:
                Encrypt_Message(message);
                cout<<"****************************************************************************************************************************"<<endl;
                break;
            case 3:
                Decrypt_Message();
                cout<<"****************************************************************************************************************************"<<endl;
                break;
            case 4:
                cout<<"Exiting Program"<<endl;
                cout<<"****************************************************************************************************************************"<<endl;
                break;
            default:
                cout<<"Invalid choice"<<endl;
        }
    }while (choice != 4);

return 0;
}