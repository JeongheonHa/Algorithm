package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_1823 {

    static int n;
    static int[] arr;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        arr = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        dp = new int[n+1][n+1];

        System.out.println(findDP(1, n));

    }

    private static int findDP(int start, int end){

        if (start > end) {
            return 0;
        }

        if (dp[start][end] != 0) {
            return dp[start][end];
        }

        int index = n-(end-start);

        dp[start][end] = Math.max(findDP(start+1, end)+(arr[start]*index), findDP(start, end-1)+(arr[end]*index));

        return dp[start][end];
    }
}
