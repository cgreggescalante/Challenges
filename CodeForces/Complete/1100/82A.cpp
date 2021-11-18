//
// Created by Conor on 6/6/2020.
//

#include <iostream>

using namespace std;

int pwer(int b, int p) {
    int result = 1;
    for (int i = 0; i < p; ++i) {
        result *= b;
    }

    return result;
}


int main() {
    int n, c, count;
    cin >> n;
    c = 0;
    count = 1;

    string names[5] = {"Sheldon", "Leonard", "Penny", "Rajesh", "Howard"};
    while (true) {
        int temp;
        for (int i = 0; i < 5; ++i) {
            temp = count + (i + 1) * pwer(2, c);
            if (n >= count && n < temp) {
                cout << names[i];
                return 0;
            }
        }
        count += 5 * pwer(2, c);
        c++;
    }
}