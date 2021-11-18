//
// Created by Conor on 5/30/2020.
//

#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int total = 0;
    int val;

    for (int i = 0; i < n; ++i) {
        cin >> val;
        total += val;
    }

    cout << total / (n * 1.0);
}