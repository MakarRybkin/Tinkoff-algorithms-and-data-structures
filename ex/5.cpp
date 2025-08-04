#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int q;
    cin >> q;

    while (q--) {
        int type;
        cin >> type;

        if (type == 1) {  // Запрос суммы
            int l, r;
            cin >> l >> r;
            l--; r--;  // Переводим в 0-индексацию

            long long sum = 0;
            for (int i = l; i <= r; i++) {
                sum += arr[i];
            }
            cout << sum << "\n";
        }
        else {  // XOR обновление
            int l, r, x;
            cin >> l >> r >> x;
            l--; r--;  // Переводим в 0-индексацию

            for (int i = l; i <= r; i++) {
                arr[i] ^= x;
            }
        }
    }

    return 0;
}