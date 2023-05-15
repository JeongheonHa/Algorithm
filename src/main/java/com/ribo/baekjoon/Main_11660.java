package com.ribo.baekjoon;

import java.util.*;

public class Main_11660 {

    static int n, m;
    static int[][] graph, pSum;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        n = input.nextInt();
        m = input.nextInt();

        graph = new int[n][n];
        pSum = new int[n+1][n+1];

        for (int i=0; i < n; i++) {
            for (int j=0; j < n; j++) {
                graph[i][j] = input.nextInt();
            }
        }

        for (int i=1; i < n+1; i++) {
            for (int j=1; j < n+1; j++) {
                pSum[i][j] = pSum[i-1][j] + pSum[i][j-1] - pSum[i-1][j-1] + graph[i-1][j-1];
            }
        }

        while (m-- > 0) {
            int x1 = input.nextInt()-1;
            int y1 = input.nextInt()-1;
            int x2 = input.nextInt()-1;
            int y2 = input.nextInt()-1;

            int ans = pSum[x2 + 1][y2 + 1] - pSum[x2 + 1][y1] - pSum[x1][y2 + 1] + pSum[x1][y1];
            System.out.println(ans);
        }
    }
}
