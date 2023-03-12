package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_16947 {

    static int n;
    static List<Integer>[] adj;
    static boolean[] isCycle;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        adj = new List[n + 1];
        for(int i = 1; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            adj[u].add(v);
            adj[v].add(u);
        }

        isCycle = new boolean[n + 1];
        for(int i = 1; i <= n; i++) {
            if(checkCycle(i, i, i)) break;
            isCycle = new boolean[n + 1];
        }

        int[] result = new int[n + 1];
        for(int i = 1; i <= n; i++) {
            if(!isCycle[i]) result[i] = bfs(i);
        }

        for(int i = 1; i <= n; i++) {
            System.out.print(result[i] + " ");
        }
    }

    public static int bfs(int node) {
        Queue<Node> q = new LinkedList<>();
        boolean[] visited = new boolean[n + 1];
        q.add(new Node(node, 0));
        visited[node] = true;

        while(!q.isEmpty()) {
            Node curr = q.poll();
            if(isCycle[curr.v]) return curr.count;

            for (int there : adj[curr.v]) {
                if (!visited[there]) {
                    visited[there] = true;
                    q.add(new Node(there, curr.count + 1));
                }
            }
        }
        return 0;
    }

    public static boolean checkCycle(int prev, int here, int start) {
        isCycle[here] = true;

        for (int there : adj[here]) {
            if (!isCycle[there]) {
                if (checkCycle(here, there, start)) return true;
            } else if (there != prev && there == start) return true;
        }
        isCycle[here] = false;

        return false;
    }

    public static class Node {
        int v;
        int count;

        public Node(int v, int count) {
            this.v = v;
            this.count = count;
        }
    }
}