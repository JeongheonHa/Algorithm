package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_15686 {

    static int n, m, ans;
    static int[][] graph;
    static List<Node> houses = new ArrayList<>();
    static List<Node> stores = new ArrayList<>();
    static Node[] comb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][n];

        for (int i=0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());

                if (graph[i][j] == 1) {
                    houses.add(new Node(i, j));
                }

                if (graph[i][j] == 2) {
                    stores.add(new Node(i, j));
                }
            }
        }

        comb = new Node[m];
        ans = Integer.MAX_VALUE;
        dfs(0, 0);

        System.out.println(ans);
    }

    private static void dfs(int cnt, int idx) {
        if (cnt == m) {
            int total = 0;
            for (Node house : houses) {
                int minDist = Integer.MAX_VALUE;
                for (Node store : comb) {
                    int dist = Math.abs(house.x - store.x) + Math.abs(house.y - store.y);
                    minDist = Math.min(dist, minDist);
                }
                total += minDist;
            }

            ans = Math.min(total, ans);
            return;
        }

        for (int i = idx; i < stores.size(); i++) {
            Node cur = stores.get(i);
            comb[cnt] = new Node(cur.x, cur.y);
            dfs(cnt+1, i+1);
        }
    }
    private static class Node {
        int x, y;

        public Node (int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
