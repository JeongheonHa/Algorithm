package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_2178 {
    static int n, m;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = s.charAt(j) - '0';
            }
        }

        System.out.println(bfs());
    }

    private static int bfs() {

        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(0, 0, 1));
        visited[0][0] = true;

        while (!queue.isEmpty()) {

            Node cur = queue.poll();

            if (cur.x == n-1 && cur.y == m-1) {
                return cur.dist;
            }

            for (int i = 0; i < 4; i++) {

                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (graph[nx][ny] == 0 || visited[nx][ny] == true) continue;

                visited[nx][ny] = true;
                queue.add(new Node(nx, ny, cur.dist + 1));
            }
        }

        return -1;
    }

    static class Node {
        int x, y, dist;

        public Node (int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }
}
