//
// Created by Conor on 11/15/2020.
//

#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int pos = 1;
    long long count = 0;
    int a;

    for (int i = 0; i < m; ++i) {
        cin >> a;
        if (a == pos) {
            continue;
        } else if (a > pos) {
            count += a - pos;
            pos = a;
        } else {
            count += n - pos + a;
            pos = a;
        }
    }

    cout << count;
}