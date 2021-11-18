//
// Created by Conor on 5/28/2020.
//

#include <iostream>

using namespace std;

int main() {
    string code;
    cin >> code;

    for (char c : code) {
        if (c == 'H' || c == 'Q' || c == '9') {
            cout << "YES";
            return 0;
        }
    }

    cout << "NO";

    return 0;
}