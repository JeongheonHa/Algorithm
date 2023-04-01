package com.ribo.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main_2616 {

    static int n, m;
    static int[] train, preSum;
    static int[][] dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());

        train = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            train[i] = Integer.parseInt(st.nextToken());
        }

        m = Integer.parseInt(br.readLine());

        preSum = new int[n+1];
        int sumVal = 0;
        for (int i = 0; i < n; i++) {
            sumVal += train[i];
            preSum[i+1] = sumVal;
        }

        dp = new int[4][n+1];

        for (int i = 1; i < 4; i++) {
            for (int j = i * m; j < n + 1; j++) {
                dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-m] + preSum[j] - preSum[j-m]);
            }
        }

        System.out.println(dp[3][n]);
    }
}
