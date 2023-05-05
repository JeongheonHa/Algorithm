package com.ribo.baekjoon;

import java.util.*;

public class Main_9466 {

    static final int UNVISITED = 0;
    static final int VISITED = 1;
    static final int VISITING = 2;
    static int t, n, cnt;
    static int[] visited;
    static int[] parent;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        t = Integer.parseInt(input.nextLine());

        while (t-- > 0) {
            n = Integer.parseInt(input.nextLine());
            String[] temp = input.nextLine().split(" ");

            visited = new int[n+1];
            parent = new int[n+1];

            cnt = 0;
            for (int i=0; i < n; i++) {
                parent[i+1] = Integer.parseInt(temp[i]);
            }

            findCycle();

            System.out.println(n-cnt);
        }
    }

    private static void findCycle() {
        for (int i=1; i < n+1; i++) {
            if (visited[i] == UNVISITED) {
                dfs(i);
            }
        }
    }

    private static void dfs(int u) {
        visited[u] = VISITING;

        int v = parent[u];
        if (visited[v] == UNVISITED) {
            dfs(v);
        } else if (visited[v] == VISITING) {
            for (int x = v; x != u; x = parent[x]) {
                cnt++;
            }
            cnt++;
        }

        visited[u] = VISITED;
    }
}
