#include <stdio.h>

int main() {
    int T; // number of test cases
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        int Hd, Ad, Hk, Ak, B, D; // health and attack power of dragon and knight, buff and debuff values
        scanf("%d %d %d %d %d %d", &Hd, &Ad, &Hk, &Ak, &B, &D);
        int turns = 0;
        while (Hd > 0 && Hk > 0) {
            // dragon attacks
            Hk -= Ad;
            if (Hk < 0) {
                Hk = 0;
            }
            turns++;
            // knight attacks
            Hd -= Ak;
            if (Hd < 0) {
                Hd = 0;
            }
            turns++;
            // dragon buffs or debuffs
            Ad += B;
            Ak -= D;
            if (Ak < 0) {
                Ak = 0;
            }
        }
        if (Hd > 0) {
            printf("Case #%d: %d\n", i, turns);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", i);
        }
    }
}