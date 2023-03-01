#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;
string generatePassword(int length) {
    string password = "";
    const string characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+";
    srand(time(NULL));
    for (int i = 0; i < length; i++) {
        password += characters[rand() % characters.length()];
    }
    return password;
}
int main() {
    int length;
    cout << "Enter the desired length of the password: ";
    cin >> length;
    string password = generatePassword(length);
    cout << "Your password is: " << password << endl;
    return 0;
}
