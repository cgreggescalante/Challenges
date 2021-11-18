//
// Created by Conor on 5/29/2020.
//

#include <iostream>

using namespace std;

int main() {
    int n, val;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> val;

        if (val) {
            cout << "HARD";
            return 0;
        }
    }

    cout << "EASY";
}