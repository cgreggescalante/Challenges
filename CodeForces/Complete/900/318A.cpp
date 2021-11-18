//
// Created by Conor on 5/28/2020.
//

#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main() {
    double n, k;
    cin >> n >> k;

    if (remainder(n, 2.0) == 0) {
        if (k > n / 2) {
            printf("%.0lf\n", (k - n / 2) * 2);
        } else {
            printf("%.0lf\n", k * 2 - 1);
        }
    } else {
        if (k > n / 2.0 + .5) {
            printf("%.0lf\n", (k - n / 2.0 - .5) * 2);
        } else {
            printf("%.0lf\n", k * 2 - 1);
        }
    }

    return 0;
}