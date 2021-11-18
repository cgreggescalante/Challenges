//
// Created by Conor on 11/13/2020.
//

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int nums[n];
    int count_evens = 0;

    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
        nums[i] %= 2;
        if (nums[i] == 0) {
            count_evens++;
        }
    }

    for (int i = 0; i < n; ++i) {
        if (count_evens == 1) {
            if (nums[i] == 0) {
                cout << i + 1;
                return 0;
            }
        } else if (nums[i] == 1) {
            cout << i + 1;
            return 0;
        }
    }
}