#include <iostream>

typedef long long int lli;

int main() {

    int n;
    std::cin >> n;

    int W[n - 1];
    for (int i = 0; i < n - 1; i++) {
        std::cin >> W[i];
    }
    lli G[n];
    for (int i = 0; i < n; i++) {
        std::cin >> G[i];
    }

    lli gas = 0;
    lli cost = 0;
    int i = 0;

    while (i < n - 1) {

        lli need = gas;
        // 필요한 거 챙기기
        if (i != n - 1) {
            while (gas < W[i]) {
                gas++;
                cost += G[i];
            }
        }
        gas = need;

        // 쌈@뽕하게 딴 친구들 것도 챙기기
        lli key = G[i];
        while (i < n - 2 && G[i + 1] > key) {
            cost += key * W[i + 1];
            i++;
        }
        i++;
//        printf("%d\n", gas);
    }

    std::cout << cost << std::endl;

    return 0;
}

//4
//1 1 1
//2 10000 9999 1

//4
//2 6 3
//2 5 4 6

//3
//999999999 1
//1000000000 999999999 1

//4
//2 3 1
//5 2 4 1