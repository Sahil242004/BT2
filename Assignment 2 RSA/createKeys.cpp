#include <iostream>
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

int main(){

int p,q;
int message;
cout<<"Enter Two Prime No : (p,q) : "<<" ";
cin>>p>>q;

cout<<"Enter The Message : ";
cin>>message;

int n = find_n(p,q);
int e = find_e(p,q);
int d = find_d(e,find_fi_n(p,q));

cout<<"Public Key : ("<<e<<","<<n<<")"<<endl;
cout<<"Private Key : ("<<d<<","<<n<<")"<<endl;

int c = mod_exp(message,e,n);
cout<<"Value  of Encrypted Message is : "<<c<<endl;

int orignal_message = mod_exp(c,d,n);
cout<<"Original Message is : "<<orignal_message<<endl;

return 0;
}