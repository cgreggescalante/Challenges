//
// Created by Conor on 11/9/2020.
//

#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        int place = 0;
        vector<int> summands;
        while (n > 0) {
            if (n % 10 > 0) {
                summands.push_back((n % 10) * (int) (pow(10, place) + .5));
            }
            n /= 10;
            place++;
        }

        cout << summands.size() << endl;
        for (int summand : summands) {
            cout << summand << " ";
        }
        cout << endl;
    }
}