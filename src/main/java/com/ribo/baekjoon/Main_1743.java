package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_1743 {

    static int n, m, k, cnt, ans;
    static int[][] graph;
    static boolean[][] visited;
    static List<Node> trash = new ArrayList<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        graph = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            graph[x-1][y-1] = 2;
            trash.add(new Node(x-1, y-1));
        }

        solve();
    }

    private static void solve() {
        for (Node cur : trash) {
            cnt = 1;
            if (visited[cur.x][cur.y]) continue;
            bfs(cur.x, cur.y);

            ans = Math.max(ans, cnt);
        }

        System.out.println(ans);
    }
    private static void bfs(int sx, int sy) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(sx, sy));
        visited[sx][sy] = true;

        while(!queue.isEmpty()) {
            Node cur = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (visited[nx][ny] || graph[nx][ny] == 0) continue;
                visited[nx][ny] = true;
                queue.add(new Node(nx, ny));
                cnt++;
            }
        }
    }

    private static class Node {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
