//
// Created by Conor on 5/28/2020.
//

#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int previous, today;
    int current = 1;
    int max = 1;
    cin >> previous;
    for (int i = 1; i < n; ++i) {
        cin >> today;
        if (today >= previous) {
            current++;
            if (current > max) {
                max = current;
            }
        } else {
            current = 1;
        }
        previous = today;
    }

    cout << max;

    return 0;
}