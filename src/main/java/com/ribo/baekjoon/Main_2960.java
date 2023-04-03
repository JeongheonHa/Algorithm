package com.ribo.baekjoon;

import java.util.*;

public class Main_2960 {

    static int n, k, cnt;
    static boolean[] isPrime;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        n = input.nextInt();
        k = input.nextInt();

        isPrime = new boolean[n+1];

        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        System.out.println(solve());
    }

    private static int solve() {
        for (int i = 2; i < n + 1; i++) {
            if (isPrime[i] == false) continue;
            for (int j = i; j < n + 1; j += i) {
                if (isPrime[j] == false) continue;
                isPrime[j] = false;
                cnt++;
                if (cnt == k) return j;
            }
        }

        return -1;
    }
}
