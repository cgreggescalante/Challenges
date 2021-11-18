//
// Created by Conor on 5/28/2020.
//

#include <iostream>

using namespace std;

int main() {
    int x, count;
    cin >> x;

    count = x / 5;
    x -= count * 5;

    count += x / 4;
    x -= x / 4 * 4;

    count += x / 3;
    x -= x / 3 * 3;

    count += x / 2;
    x -= x / 2 * 2;

    count += x;

    cout << count;
}