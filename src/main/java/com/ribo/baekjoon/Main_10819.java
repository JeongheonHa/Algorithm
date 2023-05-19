package com.ribo.baekjoon;

import java.util.*;

public class Main_10819 {

    static int n, ans;
    static int[] arr;
    static int[] perm;
    static int visited;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        n = input.nextInt();
        arr = new int[n];
        for (int i=0; i < n; i++) {
            arr[i] = input.nextInt();
        }

        perm = new int[n];

        dfs(0);
        System.out.println(ans);
    }

    private static void dfs(int cnt) {
        if (cnt == n) {
            int total = 0;
            for (int i = 1; i < n; i++) {
                int value = Math.abs(perm[i - 1] - perm[i]);
                total += value;
            }

            ans = Math.max(ans, total);
            return;
        }

        for (int i=0; i < n; i++) {
            if ((visited & 1 << i) != 0) continue;
            visited |= 1 << i;
            perm[cnt] = arr[i];
            dfs(cnt+1);
            visited &= ~(1 << i);
        }
    }
}
