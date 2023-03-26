package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_14595 {

    private static class Node {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }
    }

    static int n, m, cnt;
    static int[] parent;
    static int[] rank;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());

        parent = new int[n + 1];
        rank = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            parent[i] = i;
        }

        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(Node::getX)
                .thenComparingInt(Node::getY));

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            pq.add(new Node(x, y));
        }

        int right = 0;
        int a, b;
        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            a = cur.x;
            b = cur.y;

            if (a <= right) a = right;
            if (b > right) right = b;

            for (int i = a; i < b; i++) {
                union(a, i+1);
            }
        }

        for (int i = 1; i < n + 1; i++) {
            if (parent[i] == i) cnt++;
        }

        System.out.println(cnt);
    }

    private static void union(int u, int v) {
        int rootU = find(u);
        int rootV = find(v);

        if (rootU == rootV) return;

        if (rank[rootU] < rank[rootV]) {
            parent[rootU] = rootV;
        }

        if (rank[rootU] > rank[rootV]) {
            parent[rootV] = rootU;
        }

        if (rank[rootU] == rank[rootV]) {
            parent[rootU] = rootV;
            rank[rootV]++;
        }
    }

    private static int find(int u) {
        if (u == parent[u]) return u;
        parent[u] = find(parent[u]);
        return parent[u];
    }
}
