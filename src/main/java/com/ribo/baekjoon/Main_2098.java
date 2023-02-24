package com.ribo.baekjoon;


import java.util.*;
import java.io.*;


public class Main_2098 {
    static int n;
    static int[][] graph;
    static int[][] dp;
    static final int notVisited = 1000000000;
    static final int noHamil = 17 * 1000000 + 1;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        dp = new int[n][1 << n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
            Arrays.fill(dp[i], notVisited);
        }

        System.out.println(tsp(0, 1));
    }

    private static int tsp(int cur, int visited) {

        if (visited == (1<<n)-1) {

            if (graph[cur][0] == 0) {
                return noHamil;
            }

            return graph[cur][0];
        }

        if (dp[cur][visited] != notVisited) return dp[cur][visited];

        for (int i = 0; i < n; i++) {
            if ((visited & (1<<i)) != 0 || graph[cur][i] == 0) continue;

            dp[cur][visited] = Math.min(dp[cur][visited], tsp(i, visited | (1 << i)) + graph[cur][i]);
        }
        return dp[cur][visited];
    }
}
