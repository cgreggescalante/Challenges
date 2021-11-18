//
// Created by Conor on 6/6/2020.
//

#include <iostream>

using namespace std;

int main() {
    int top = 0;
    int vals[3];
    int option;

    cin >> vals[0] >> vals[1] >> vals[2];

    option = vals[0] + vals[1] * vals[2];
    if (option > top) {
        top = option;
    }
    option = vals[0] * (vals[1] + vals[2]);
    if (option > top) {
        top = option;
    }
    option = vals[0] * vals[1] * vals[2];
    if (option > top) {
        top = option;
    }
    option = (vals[0] + vals[1]) * vals[2];
    if (option > top) {
        top = option;
    }
    option = vals[0] + vals[1] + vals[2];
    if (option > top) {
        top = option;
    }

    cout << top;

}