package com.ribo.baekjoon;

import java.util.*;

public class Main_5582 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String s1 = input.nextLine();
        String s2 = input.nextLine();

        int n = s1.length();
        int m = s2.length();

        int[][] dp = new int[n+1][m+1];

        int maxValue = 0;

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (s1.charAt(i-1) == s2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                    if (maxValue < dp[i][j]) {
                        maxValue = Math.max(maxValue, dp[i][j]);
                    }
                }
            }
        }

        System.out.println(maxValue);
    }
}
