package com.ribo.baekjoon;

import java.util.*;

public class Main_1992 {
    static int N;
    public static int[][] graph;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        N = scanner.nextInt();
        graph = new int[N][N];

        for(int i = 0; i < N; i++) {
            String str = scanner.next();
            for(int j = 0; j < N; j++) {
                graph[i][j] = str.charAt(j) - '0';
            }
        }

        solve();
    }

    private static void solve() {

        dfs(0, 0, N);
        System.out.println(sb);
    }

    private static void dfs(int x, int y, int size) {

        int color = graph[x][y];

        for(int i = x; i < x + size; i++) {
            for(int j = y; j < y + size; j++) {
                if(color != graph[i][j]) {
                    int half = size / 2;
                    sb.append("(");
                    dfs(x, y, half);
                    dfs(x, y + half, half);
                    dfs(x + half, y, half);
                    dfs(x + half, y + half, half);
                    sb.append(")");
                    return;
                }
            }
        }

        sb.append(color);
    }
}
