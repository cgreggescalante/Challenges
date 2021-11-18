//
// Created by Conor on 11/6/2020.
//

#include <iostream>
#include <vector>
using namespace std;

int gcd(int a, int b) {
    if (a == 0)
        return b;
    if (b == 0)
        return a;

    if (a == b)
        return a;

    if (a > b)
        return gcd(a-b, b);
    return gcd(a, b-a);
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n;
        int chair_max;
        cin >> n;
        chair_max = 4 * n;

        int start = 2;

        while (start < chair_max) {
            vector<int> chairs;
            chairs.push_back(start);

            int j = start + 2;

            while (j < chair_max && chairs.size() < n) {
                bool valid = true;
                for (int chair : chairs) {
                    if (j % chair == 0 || chair % j == 0 || gcd(j, chair) == 1) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {
                    chairs.push_back(j);
                }

                j += 2;
            }

            if (chairs.size() == n) {

                for (int chair : chairs) {
                    cout << chair << " ";
                }
                cout << "\n";
                break;
            }
            start += 2;
        }
    }
}