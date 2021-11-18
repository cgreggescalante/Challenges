//
// Created by Conor on 11/6/2020.
//

#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int a, b;
        cin >> a >> b;

        int m = 0;
        if (a % b != 0) {
            m = b - a + (b * (a / b));
        }

        cout << m << endl;
    }
}