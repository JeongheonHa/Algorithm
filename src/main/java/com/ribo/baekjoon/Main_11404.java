package com.ribo.baekjoon;

import java.io.*;
import java.util.*;

public class Main_11404 {

    static int n, m;
    static int[][] dist;
    static final int INF = 9999999;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());

        dist = new int[n+1][n+1];

        for (int i=1; i < n+1; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }

        for (int i=0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            dist[u][v] = Math.min(dist[u][v], w); // u -> v로 가는 간선이 한개가 아닌 경우
        }

        for (int k=1; k < n+1; k++) {
            for (int i=1; i < n+1; i++) {
                for (int j=1; j < n+1; j++) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        for (int i=1; i < n+1; i++) {
            for (int j=1; j < n+1; j++) {
                if (dist[i][j] == INF) {
                    System.out.print(0 + " ");
                } else {
                    System.out.print(dist[i][j] + " ");
                }
            }
            System.out.println();
        }
    }
}
