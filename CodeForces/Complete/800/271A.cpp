//
// Created by Conor on 5/29/2020.
//

#include <iostream>
#include <string>

using namespace std;

int is_distinct(int n) {
    string number = to_string(n);

    for (int i = number.length() - 1; i > 0; i--) {
        for (int j = i - 1; j > -1; j--) {
            if (number[i] == number[j]) {
                return number.length() - i - 1;
            }
        }
    }

    return -1;
}

int pwer(int b, int e) {
    int result = 1;

    for (int i = 0; i < e; ++i) {
        result *= b;
    }

    return result;
}

int main() {
    int n;
    cin >> n;
    n++;

    while (true) {
        int step = is_distinct(n);

        if (step == -1) {
            cout << n;
            return 0;
        } else {
            int diff = pwer(10, step) - (n % pwer(10, step));
            n += diff;
        }
    }
}