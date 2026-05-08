#include <iostream>
using namespace std;
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
int main(){

string mess = "Hello";
int value = find_ascii_value(mess);
cout<<value;

return 0;
}