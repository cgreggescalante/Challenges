//
// Created by Conor on 5/30/2020.
//

#include <iostream>

using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    for (int i = 0; i < a.length(); ++i) {
        if (a[i] == '0') {
            if (b[i] == '0') {
                cout << '0';
            } else {
                cout << '1';
            }
        } else {
            if (b[i] == '0') {
                cout << '1';
            } else {
                cout << '0';
            }
        }
    }
}