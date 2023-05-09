package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_18352 {

    static int n, m, k, x;
    static List<List<Integer>> adj = new ArrayList<>();
    static int[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        for (int i=0; i < n+1; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i=0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            adj.get(u).add(v);
        }

        dist = new int[n+1];
        Arrays.fill(dist, -1);
        bfs(x);

        List<Integer> ans = new ArrayList<>();

        for (int i=1; i < n+1; i++) {
            if (dist[i] != k) continue;
            ans.add(i);
        }

        if (ans.isEmpty()) {
            System.out.println(-1);
        } else {
            for (int i=0; i < ans.size(); i++) {
                System.out.println(ans.get(i));
            }
        }
    }

    private static void bfs(int x) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(x);
        boolean[] visited = new boolean[n+1];
        visited[x] = true;
        dist[x] = 0;

        while (!q.isEmpty()) {
            int u = q.poll();

            for (int v : adj.get(u)) {
                if (visited[v]) continue;
                visited[v] = true;
                q.offer(v);
                dist[v] = dist[u] + 1;
            }
        }
    }
}
