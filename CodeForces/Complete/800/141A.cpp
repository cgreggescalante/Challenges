//
// Created by Conor on 11/6/2020.
//

#include <iostream>
using namespace std;

int main() {
    string host, guest, pile;

    cin >> host >> guest >> pile;

    for (char i : host) {
        bool found = false;
        int j = 0;
        while (j < pile.size()) {
            if (i == pile[j]) {
                pile.erase(j, 1);
                found = true;
                break;
            }
            j++;
        }

        if (!found) {
            cout << "NO ";
            return 0;
        }
    }

    for (char i : guest) {
        bool found = false;
        for (int j = 0; j < pile.size(); ++j) {
            if (i == pile[j]) {
                pile.erase(j, 1);
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "NO";
            return 0;
        }
    }

    if (pile.empty()) {
        cout << "YES";
    } else {
        cout << "NO";
    }
}