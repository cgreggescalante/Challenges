//
// Created by Conor on 6/3/2020.
//

#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> horseshoes;
    int needed = 4;
    int val;
    for (int i = 0; i < 4; ++i) {
        cin >> val;
        needed -= 1;
        for (int j : horseshoes) {
            if (j == val) {
                needed++;
                break;
            }
        }
        horseshoes.push_back(val);
    }

    cout << needed;
}