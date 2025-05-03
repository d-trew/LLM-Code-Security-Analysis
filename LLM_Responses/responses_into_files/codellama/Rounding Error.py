#include <stdio.h>
int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        int N, L;
        scanf("%d %d", &N, &L);
        int C[L];
        for (int j = 0; j < L; ++j) {
            scanf("%d", &C[j]);
        }
        int max_sum = 0;
        for (int j = 0; j < L; ++j) {
            if (C[j] > 0) {
                max_sum += C[j];
            }
        }
        printf("Case #%d: %d\n", i + 1, max_sum);
    }
    return 0;
}