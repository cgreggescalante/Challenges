//
// Created by Conor on 5/28/2020.
//

#include <iostream>

using namespace std;

int main() {
    string s, t;
    cin >> s;
    cin >> t;

    bool reversed = true;
    for (int i = s.length() - 1; i > -1; --i) {
        if (s[i] != t[t.size() - i - 1]) {
            reversed = false;
        }
    }

    if (reversed) {
        cout << "YES";
    } else {
        cout << "NO";
    }

    return 0;
}