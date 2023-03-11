package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_1890 {

    static int n;
    static int[][] graph;
    static long[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        graph = new int[n][n];
        dp = new long[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp[0][0] = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int cur = graph[i][j];
                if (dp[i][j] == 0 || cur == 0) continue;
                if (i + cur < n) dp[i+cur][j] += dp[i][j];
                if (j + cur < n) dp[i][j+cur] += dp[i][j];
            }
        }

        System.out.println(dp[n-1][n-1]);
    }
}
