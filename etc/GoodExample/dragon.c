/*
n은 45이하 자연수
//0일~1일 : 드래곤 알이 하나 있다.
//2일 : 초기 드래곤이 부화해, 알을 하나 낳는다. 따라서 드래곤 수와 알 수 의 합은 2
//3일 : 초기 드래곤이 한 번 더 알을 낳고, 드래곤 수와 드래곤 알의 수의 합은 3
//4일 이틀 차에 낳은 드래곤 알이 부화, 부화한 드래곤과 초기 드래곤이 알을 하나씩 낳았다.
들래곤 수와 드래곤 알 수의 합은 5

따라서 6일 후 드래곤과 드래곤 알은 총 12개가 된다.

일 수 : 0 1 2 3 4 5 6
알을 낳을 수 없는 드래곤: 0 0 0 0 0 0 1
알을 낳을 수 있는 드래곤 : 0 0 1 1 2 3 4
드래곤 알 수 : 1 1 1 2 3 5 7

Day 0: canNotLayDragon = 0, canLayDragon = 0, Eggs = 1-> Total : 1
Day 1: canNotLayDragon = 0, canLayDragon = 0, Eggs = 1-> Total : 1
Day 2: canNotLayDragon = 0, canLayDragon = 1, Eggs = 1-> Total : 2
Day 3: canNotLayDragon = 0, canLayDragon = 1, Eggs = 2-> Total : 3
Day 4: canNotLayDragon = 0, canLayDragon = 2, Eggs = 3-> Total : 5
Day 5: canNotLayDragon = 0, canLayDragon = 3, Eggs = 5-> Total : 8
Day 6: canNotLayDragon = 1, canLayDragon = 4, Eggs = 7-> Total : 12

*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int solution(int n) {
    long long laidEggs[46] = { 0 };       // day별 낳은 알 수
    long long dragonAgeCount[5] = { 0 };  // 나이 0~4인 드래곤 수 (0: 당일 부화한 드래곤, 4: 은퇴한 드래곤)
    long long total = 0;

    laidEggs[0] = 1;  // 0일차에 알 1개 낳음 (초기 알)

    for (int day = 0; day <= n; day++) {
        // 1) 부화: 2일 전에 낳은 알이 오늘 부화해 새 드래곤 생성
        long long hatched = (day >= 2) ? laidEggs[day - 2] : 0;

        // 2) 나이 증가: 나이 4인 드래곤(은퇴)은 사라지고, 나머지는 한 살 증가
        for (int age = 4; age > 0; age--) {
            dragonAgeCount[age] = dragonAgeCount[age - 1];
        }
        dragonAgeCount[0] = hatched;

        // 3) 산란 가능한 드래곤 수 (나이 0~3)
        long long canLay = 0;
        for (int age = 0; age <= 3; age++) {
            canLay += dragonAgeCount[age];
        }

        // 4) 오늘 낳은 알 수 = 산란 가능한 드래곤 수 (0일차 제외)
        if (day > 0) {
            laidEggs[day] = canLay;
        }

        // 5) 살아있는 알 수 = 오늘과 어제 낳은 알 (알은 2일까지만 존재)
        long long eggsAlive = laidEggs[day] + (day > 0 ? laidEggs[day - 1] : 0);

        // 6) 총합 = 산란 가능한 드래곤 + 은퇴한 드래곤 + 살아있는 알
        total = canLay + dragonAgeCount[4] + eggsAlive;
    }

    return (int)total;
}

int main() {
    for (int n = 0; n <= 7; n++) {
        int total = solution(n);
        printf("Total for n = %d: %d\n", n, total);
    }
    return 0;
}

/*

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int solution(int n) {
    long long laidEggs[46] = { 0 };       // day별 낳은 알 수
    long long dragonAgeCount[5] = { 0 };  // 나이 0~4인 드래곤 수 (0: 당일 부화한 드래곤, 4: 은퇴한 드래곤)
    long long total = 0;

    laidEggs[0] = 1;  // 0일차에 알 1개 낳음 (초기 알)

    for (int day = 0; day <= n; day++) {
        // 1) 부화: 2일 전에 낳은 알이 오늘 부화해 새 드래곤 생성
        long long hatched = (day >= 2) ? laidEggs[day - 2] : 0;

        // 2) 나이 증가: 나이 4인 드래곤(은퇴)은 사라지고, 나머지는 한 살 증가
        for (int age = 4; age > 0; age--) {
            dragonAgeCount[age] = dragonAgeCount[age - 1];
        }
        dragonAgeCount[0] = hatched;

        // 3) 산란 가능한 드래곤 수 (나이 0~3)
        long long canLay = 0;
        for (int age = 0; age <= 3; age++) {
            canLay += dragonAgeCount[age];
        }

        // 4) 오늘 낳은 알 수 = 산란 가능한 드래곤 수 (0일차 제외)
        if (day > 0) {
            laidEggs[day] = canLay;
        }

        // 5) 살아있는 알 수 = 오늘과 어제 낳은 알 (알은 2일까지만 존재)
        long long eggsAlive = laidEggs[day] + (day > 0 ? laidEggs[day - 1] : 0);

        // 6) 총합 = 산란 가능한 드래곤 + 은퇴한 드래곤 + 살아있는 알
        total = canLay + dragonAgeCount[4] + eggsAlive;


        printf("Day %2d: 낳지 못하는 드래곤 = %lld, 낳을 수 있는 드래곤 = %lld, 알 = %lld → 총합 = %lld\n",
            day, dragonAgeCount[4], canLay, eggsAlive, total);
    }

    return (int)total;
}

int main() {
    for (int n = 0; n <= 7; n++) {
        printf("\n=== n = %d ===\n", n);
        int total = solution(n);
        printf(">> Total for n = %d: %d\n", n, total);
    }
    return 0;
}

== = n = 0 == =
Day  0: 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
>> Total for n = 0 : 1

== = n = 1 == =
Day  0 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  1 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
>> Total for n = 1 : 1

== = n = 2 == =
Day  0 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  1 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  2 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 1, 알 = 1 → 총합 = 2
>> Total for n = 2 : 2

== = n = 3 == =
Day  0 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  1 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  2 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 1, 알 = 1 → 총합 = 2
Day  3 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 1, 알 = 2 → 총합 = 3
>> Total for n = 3 : 3

== = n = 4 == =
Day  0 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  1 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  2 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 1, 알 = 1 → 총합 = 2
Day  3 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 1, 알 = 2 → 총합 = 3
Day  4 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 2, 알 = 3 → 총합 = 5
>> Total for n = 4 : 5

== = n = 5 == =
Day  0 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  1 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  2 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 1, 알 = 1 → 총합 = 2
Day  3 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 1, 알 = 2 → 총합 = 3
Day  4 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 2, 알 = 3 → 총합 = 5
Day  5 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 3, 알 = 5 → 총합 = 8
>> Total for n = 5 : 8

== = n = 6 == =
Day  0 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  1 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  2 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 1, 알 = 1 → 총합 = 2
Day  3 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 1, 알 = 2 → 총합 = 3
Day  4 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 2, 알 = 3 → 총합 = 5
Day  5 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 3, 알 = 5 → 총합 = 8
Day  6 : 낳지 못하는 드래곤 = 1, 낳을 수 있는 드래곤 = 4, 알 = 7 → 총합 = 12
>> Total for n = 6 : 12

== = n = 7 == =
Day  0 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  1 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 0, 알 = 1 → 총합 = 1
Day  2 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 1, 알 = 1 → 총합 = 2
Day  3 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 1, 알 = 2 → 총합 = 3
Day  4 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 2, 알 = 3 → 총합 = 5
Day  5 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 3, 알 = 5 → 총합 = 8
Day  6 : 낳지 못하는 드래곤 = 1, 낳을 수 있는 드래곤 = 4, 알 = 7 → 총합 = 12
Day  7 : 낳지 못하는 드래곤 = 0, 낳을 수 있는 드래곤 = 7, 알 = 11 → 총합 = 18
>> Total for n = 7 : 18
*/
