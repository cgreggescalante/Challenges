//
// Created by Conor on 6/6/2020.
//

#include <iostream>

using namespace std;

int main() {
    int n, val;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> val;
        if (360 / (val - 180) == 360.0 / (val - 180.0)) {
            cout << "YES";
        } else {
            cout << "NO";
        }
        cout << endl;
    }
}