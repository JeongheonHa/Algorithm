package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_3980 {

    static int t, ans;
    static int[][] graph;
    static boolean[] isUsed = new boolean[11];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        t = Integer.parseInt(st.nextToken());
        graph = new int[11][11];

        while (t-- > 0) {
            for (int i = 0; i < 11; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 11; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            ans = 0;

            dfs(0, 0);
            System.out.println(ans);
        }
    }

    private static void dfs(int cnt, int maxValue) {
        if (cnt == 11) {
            ans = Math.max(ans, maxValue);
            return;
        }

        for (int i = 0; i < 11; i++) {
            if (graph[cnt][i] == 0 || isUsed[i] == true) continue;
            isUsed[i] = true;
            dfs(cnt + 1, maxValue + graph[cnt][i]);
            isUsed[i] = false;
        }
    }
}
