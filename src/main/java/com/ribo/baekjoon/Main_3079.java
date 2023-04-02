package com.ribo.baekjoon;

import java.util.*;

public class Main_3079 {

    static int n;
    static int[] gates;
    static long m, ans;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        m = input.nextInt();

        gates = new int[n];

        for (int i = 0; i < n; i++) {
            gates[i] = input.nextInt();
        }

        Arrays.sort(gates);
        long maxValue = gates[n-1] * 1000000000L;

        binarySearch(0L, maxValue, m);

        System.out.println(ans);
    }

    private static void binarySearch(long start, long end, long target) {
        while (start <= end) {
            long mid = (start + end) / 2;

            long people = 0;
            for (int i = 0; i < n; i++) {
                people += (mid / gates[i]);
            }

            if (target <= people) {
                end = mid - 1;
                ans = mid;
            } else {
                start = mid + 1;
            }
        }
    }
}
