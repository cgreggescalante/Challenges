//
// Created by Conor on 5/28/2020.
//

#include <iostream>
#include <string>

using namespace std;

bool is_lucky(int n) {
    string num = to_string(n);

    for (char c : num) {
        if (c != '4' && c != '7') {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    cin >> n;

    int c = 4;

    while (c <= n) {
        if (is_lucky(c)) {
            if (n % c == 0) {
                cout << "YES";
                return 0;
            }
            c += 2;
        }
        c++;
    }

    cout << "NO";

    return 0;
}