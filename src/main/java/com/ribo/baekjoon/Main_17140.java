package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_17140 {
    static class Pair implements Comparable<Pair> {
        int number;
        int count;

        Pair(int n, int c) {
            this.number = n;
            this.count = c;
        }

        public int compareTo(Pair o) {
            if (this.count < o.count) {
                return -1;
            } else if (this.count == o.count) {
                return this.number - o.number;
            } else {
                return 1;
            }
        }
    }

    static int r, c, k;
    static int[][] graph = new int[101][101];
    static int xLength = 3, yLength = 3;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // input
        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= 3; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1 ; j <= 3; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(solution());
    }

    static int solution() {
        for (int sec = 0; sec <= 100; sec++) {
            if (graph[r][c] == k) {
                return sec;
            }
            operating();
        }

        return -1;
    }

    static void operating() {
        if (xLength >= yLength) {
            for (int i = 1; i <= xLength; i++) {
                R(i);
            }
        } else {
            for (int i = 1; i <= yLength; i++) {
                C(i);
            }
        }
    }

    static void R(int key) {
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 1; i <= yLength; i++) {
            if (graph[key][i] == 0) continue;
            map.compute(graph[key][i], (num, count) -> count == null ? 1 : count + 1);
        }

        map.forEach((k, v) -> pq.add(new Pair(k, v)));

        int i = 1;
        while (!pq.isEmpty()) {
            Pair p = pq.poll();
            graph[key][i++] = p.number;
            graph[key][i++] = p.count;
        }

        yLength = Math.max(yLength, i);

        while (i <= 99) {
            graph[key][i++] = 0;
            graph[key][i++] = 0;
        }
    }

    static void C(int key) {
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 1; i <= xLength; i++) {
            if (graph[i][key] == 0) continue;
            map.compute(graph[i][key], (num, count) -> count == null ? 1 : count + 1);
        }

        map.forEach((k, v) -> pq.add(new Pair(k, v)));

        int i = 1;
        while (!pq.isEmpty()) {
            Pair p = pq.poll();
            graph[i++][key] = p.number;
            graph[i++][key] = p.count;
        }

        xLength = Math.max(xLength, i);

        while (i <= 99) {
            graph[i++][key] = 0;
            graph[i++][key] = 0;
        }
    }
}
