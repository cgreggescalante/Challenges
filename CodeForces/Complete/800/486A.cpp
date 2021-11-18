//
// Created by Conor on 5/30/2020.
//

#include <iostream>

using namespace std;


int main() {
    long long n;
    cin >> n;

    long long total = (n / 2) * (n / 2 + 1);
    long long a;
    if (n % 2 == 0) {
        a = n / 2;
    } else {
        a = n / 2.0 + .5;
    }
    long long min = a * a;

    cout << total - min;
}