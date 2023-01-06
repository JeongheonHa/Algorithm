package com.ribo.baekjoon;

import java.io.*;
import java.util.*;

public class Main_14890 {
        static int[][] graph1;
        static int[][] graph2;
        static int n, l;
        static int path;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());

        graph1 = new int[n][n];
        graph2 = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph1[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        graph2 = swapRowCol(graph1);
        findRoad(graph1);
        findRoad(graph2);

        System.out.println(path);
    }

    private static void findRoad(int[][] graph) {
        for (int i = 0; i < n; i++) {
            boolean flag = true;
            int cnt = 1;

            for (int j = 0; j < n-1; j++) {
                if (graph[i][j] == graph[i][j + 1]) {
                    ++cnt;
                } else if (graph[i][j] == graph[i][j + 1] + 1) {
                    if (canRoad(graph, i, j)) {
                        cnt = 0;
                        j = j + l - 1;
                    } else {
                        flag = false;
                        break;
                    }
                } else if (graph[i][j] == graph[i][j + 1] - 1) {
                    if (cnt >= l) {
                        cnt = 1;
                    } else {
                        flag = false;
                        break;
                    }
                } else if (Math.abs(graph[i][j] - graph[i][j + 1]) > 1) {
                    flag = false;
                    break;
                }
            }

            if (flag == true) {
                ++path;
            }
        }
    }

    static int[][] swapRowCol(int[][] graph) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph2[j][i] = graph[i][j];
            }
        }
        return graph2;
    }

    static boolean canRoad(int[][] graph, int x, int y) {

        int height = graph[x][y+1];
        for(int j=y+1; j<y+1+l; j++) {
            if (j > n-1 || graph[x][j] != height) {
                return false;
            }
        }
        return true;
    }
}
