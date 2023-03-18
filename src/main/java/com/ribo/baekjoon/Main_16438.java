package com.ribo.baekjoon;

import java.util.*;

public class Main_16438 {

    static int n, divideCnt;
    static char[][] graph;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();

        graph = new char[7][n];

        for (int i = 0; i < 7; i++) {
            Arrays.fill(graph[i], 'A');
        }

        div(0, n-1, 0);

        if (divideCnt < 6) {
            int j = 0;
            for (int i = divideCnt; i < 7; i++) {
                graph[i][j%n] = 'B';
                j++;
            }
        }

        for (int i = 0; i < 7; i++) {
            System.out.println(graph[i]);
        }
    }

    private static void div(int start, int end, int cnt) {

        if (start == end) {
            divideCnt = cnt;
            return;
        }

        int mid = (start + end) / 2;

        for (int i = mid+1; i <= end; i++) {
            graph[cnt][i] = 'B';
        }

        div(start, mid, cnt+1);
        div(mid+1, end, cnt+1);
    }
}
