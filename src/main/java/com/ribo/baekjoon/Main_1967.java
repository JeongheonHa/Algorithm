package com.ribo.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main_1967 {
    static class Node {
        int node;
        int weight;

        public Node(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }
    }
    static int n, maxDist, maxNode;
    static ArrayList<Node>[] tree;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk;

        n = Integer.parseInt(br.readLine());
        tree = new ArrayList[n+1];
        visited = new boolean[n+1];

        for (int i = 0; i < n+1; i++) {
            tree[i] = new ArrayList<>();
        }

        for (int i = 0; i < n-1; i++) {
            stk = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(stk.nextToken());
            int v = Integer.parseInt(stk.nextToken());
            int w = Integer.parseInt(stk.nextToken());

            tree[u].add(new Node(v, w));
            tree[v].add(new Node(u, w));
        }

        dfs(1, 0);

        visited = new boolean[n+1];
        maxDist = 0;
        dfs(maxNode, 0);

        System.out.println(maxDist);
    }

    private static void dfs(int node, int dist) {
        if (visited[node] == true) {
            return;
        }

        if (maxDist < dist) {
            maxDist = dist;
            maxNode = node;
        }

        visited[node] = true;

        for (Node there : tree[node]) {
            int nextDist = dist + there.weight;
            dfs(there.node, nextDist);
        }
    }
}
