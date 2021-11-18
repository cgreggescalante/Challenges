//
// Created by Conor on 11/6/2020.
//

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int count = 0;

    count += n / 100;
    n %= 100;
    count += n / 20;
    n %= 20;
    count += n / 10;
    n %= 10;
    count += n / 5;
    n %= 5;
    cout << count + n;
}