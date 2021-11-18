//
// Created by Conor on 5/28/2020.
//

#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    string scores;
    cin >> scores;

    int a = 0;
    int d = 0;

    for (char c : scores) {
        if (c == 'A') {
            a++;
        } else {
            d++;
        }
    }

    if (a > d) {
        cout << "Anton";
    } else if (d > a) {
        cout << "Danik";
    } else {
        cout << "Friendship";
    }
}