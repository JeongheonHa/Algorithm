package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_1495 {

    static int n, m, s;
    static int[] volumes;
    static int[][] dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        volumes = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            volumes[i] = Integer.parseInt(st.nextToken());
        }

        dp = new int[m+1][n];

        for (int i = 0; i < m + 1; i++) {
            Arrays.fill(dp[i], -2);
        }

        System.out.println(dfs(s, 0));
    }

    private static int dfs(int volume, int idx) {

        if (volume < 0 || volume > m) return -1;

        if (idx == n) return volume;


        if(dp[volume][idx] != -2) return dp[volume][idx];

        int maxValue = Math.max(dfs(volume + volumes[idx], idx + 1), dfs(volume - volumes[idx], idx + 1));

        dp[volume][idx] = Math.max(dp[volume][idx], maxValue);

        return dp[volume][idx];
    }

}
