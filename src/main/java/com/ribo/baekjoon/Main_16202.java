package com.ribo.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main_16202 {

    static int n, m, k, mstWeight;
    static int[] parent;
    static int[] rank;
    static List<Node> edges = new ArrayList<>();
    static int[] ans;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        parent = new int[n+1];
        rank = new int[n+1];
        initParentAndRank();

        for (int i = 1; i < m + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            edges.add(new Node(x, y, i));
        }

        Collections.sort(edges, Comparator.comparingInt(node -> node.w));

        ans = new int[k];
        solve();

        String[] ansArr = Arrays.stream(ans).mapToObj(i -> i + "").toArray(String[]::new);
        String ansStr = String.join(" ", ansArr);

        System.out.println(ansStr);
    }

    private static void solve() {
        for (int i = 0; i < k; i++) {
            initParentAndRank();
            mstWeight = 0;
            int minEdgeIdx = 0;
            int minEdge = 10000;
            for (int j = 0; j < edges.size(); j++) {
                Node cur = edges.get(j);

                if (union(cur.x, cur.y) == -1) continue;
                mstWeight += cur.w;

                if (minEdge > cur.w) {
                    minEdge = cur.w;
                    minEdgeIdx = j;
                }
            }

            int cnt = 0;
            for (int k = 1; k < parent.length; k++) {
                if (parent[k] == k) {
                    cnt++;
                }

                if (cnt > 1) {
                    mstWeight = 0;
                }
            }

            if (mstWeight == 0) break;
            ans[i] = mstWeight;

            edges.remove(minEdgeIdx);
        }
    }

    private static int union(int u, int v) {
        int rootU = find(u);
        int rootV = find(v);

        if (rootU == rootV) return -1;

        if (rank[rootU] > rank[rootV]) {
            parent[rootV] = rootU;
        }

        if (rank[rootU] < rank[rootV]) {
            parent[rootU] = rootV;
        }

        if (rank[rootU] == rank[rootV]) {
            parent[rootU] = rootV;
            rank[rootV]++;
        }

        return 1;
    }

    private static int find(int u) {
        if (u == parent[u]) return u;
        parent[u] = find(parent[u]);
        return parent[u];
    }

    private static void initParentAndRank() {
        for (int i = 1; i < n + 1; i++) {
            parent[i] = i;
        }

        Arrays.fill(rank, 0);
    }

    private static class Node {
        int x, y, w;

        public Node(int x, int y, int w) {
            this.x = x;
            this.y = y;
            this.w = w;
        }
    }
}
