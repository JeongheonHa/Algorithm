package com.ribo.baekjoon;

import java.util.*;

public class Main_1644 {

    static int n, s, e, sum, cnt;
    static List<Integer> primeNumberList = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        n = scanner.nextInt();

        boolean[] isPrime = new boolean[n+1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i*i <= n; i++) {
            if (isPrime[i] == false) continue;
            for (int j = i*i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }

        for (int i = 0; i < n + 1; i++) {
            if (!isPrime[i]) continue;
            primeNumberList.add(i);
        }

        while (true) {
            if (sum >= n) {
                sum -= primeNumberList.get(s++);
            } else if (e == primeNumberList.size()) {
                break;
            } else if (sum < n) {
                sum += primeNumberList.get(e++);
            }

            if (sum == n) cnt++;
        }

        System.out.println(cnt);
    }
}
