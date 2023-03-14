package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_14938 {

    static int n, m, r, items, ans;
    static List<Node>[] adj;
    static int[] itemsInArea;
    static boolean[] visited;
    static int[] dist;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        itemsInArea = new int[n+1];

        for (int i = 1; i < n + 1; i++) {
            itemsInArea[i] = Integer.parseInt(st.nextToken());
        }

        adj = new List[n+1];

        for (int i = 1; i < n + 1; i++) {
            adj[i] = new LinkedList<>();
        }

        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());

            adj[a].add(new Node(b, l));
            adj[b].add(new Node(a, l));
        }

        for (int i = 1; i < n + 1; i++) {
            items = 0;
            dist = new int[n+1];
            Arrays.fill(dist, Integer.MAX_VALUE);

            bfs(i);

            for (int j = 0; j < n + 1; j++) {
                if (dist[j] != Integer.MAX_VALUE) {
                    items += itemsInArea[j];
                }
            }

            ans = Math.max(ans, items);
        }

        System.out.println(ans);

    }

    private static void bfs(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node.w));
        pq.add(new Node(start, 0));
        dist[start] = 0;

        while (!pq.isEmpty()) {
            Node here = pq.poll();

            if (dist[here.v] < here.w) continue;

            for (Node next : adj[here.v]) {
                int there = next.v;
                int weight = next.w;
                int nextWeight = weight + here.w;

                if (nextWeight < dist[there] && nextWeight <= m) {
                    dist[there] = nextWeight;
                    pq.add(new Node(there, nextWeight));
                }
            }
        }
    }

    private static class Node {
        int v, w;

        public Node(int v, int w) {
            this.v = v;
            this.w = w;
        }
    }
}
