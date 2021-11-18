//
// Created by Conor on 5/28/2020.
//

#include <iostream>

using namespace std;

int main() {
    int a, b, years;
    cin >> a >> b;
    years = 0;

    while (a <= b) {
        years++;
        a *= 3;
        b *= 2;
    }

    cout << years;

    return 0;
}