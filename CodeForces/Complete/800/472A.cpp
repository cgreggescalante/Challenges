//
// Created by Conor on 11/9/2020.
//

#include <iostream>
#include <cmath>

using namespace std;

bool is_composite(int n) {
    for (int i = 2; i < pow(n, .5) + 1; ++i) {
        if (n % i == 0) {
            return true;
        }
    }

    return false;
}

int main() {
    int n;
    cin >> n;

    for (int i = 4; i < n; ++i) {
        if (is_composite(i) && is_composite(n - i)) {
            cout << i << " " << n - i;
            return 0;
        }
    }
}