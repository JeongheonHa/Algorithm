package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_1504 {

    static int n, e;
    static List<List<Node>> adj = new ArrayList<>();
    static int[] dist;
    static final int INF = 200_000_000;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        for (int i=0; i < n+1; i++) {
            adj.add(new ArrayList<>());
        }

        dist = new int[n+1];
        Arrays.fill(dist, INF);

        for (int i=0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            adj.get(u).add(new Node(v, w));
            adj.get(v).add(new Node(u, w));
        }

        st = new StringTokenizer(br.readLine());
        int v1 = Integer.parseInt(st.nextToken());
        int v2 = Integer.parseInt(st.nextToken());

        int minDist1 = bfs(1, v1) + bfs(v1, v2) + bfs(v2, n);
        int minDist2 = bfs(1, v2) + bfs(v2, v1) + bfs(v1, n);

        if (minDist1 >= INF && minDist2 >= INF) System.out.println(-1);
        else System.out.println(Math.min(minDist1, minDist2));
    }

    private static int bfs(int u, int v) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(u, 0));
        Arrays.fill(dist, INF);
        dist[u] = 0;

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            if (dist[cur.v] < cur.w) continue;

            for (Node next : adj.get(cur.v)) {
                int nextDist = next.w + cur.w;
                if (nextDist < dist[next.v]) {
                    pq.add(new Node(next.v, nextDist));
                    dist[next.v] = nextDist;
                }
            }
        }

        return dist[v];
    }

    private static class Node implements Comparable<Node> {
        int v, w;

        public Node (int v, int w) {
            this.v = v;
            this.w = w;
        }

        public int compareTo(Node node) {
            return this.w - node.w;
        }
    }
}
