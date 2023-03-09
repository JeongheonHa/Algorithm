package com.ribo.baekjoon;

import java.util.*;

public class Main_16954 {

    static char[][] graph = new char[8][8];
    static int[] dx = {0, -1, 1, 0, 0, -1, -1, 1, 1};
    static int[] dy = {0, 0, 0, -1, 1, -1, 1, -1, 1};
    static Queue<Node> queue = new LinkedList<>();
    static boolean[][] visited;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 8; i++) {
            String s = scanner.next();
            for (int j = 0; j < 8; j++) {
                graph[i][j] = s.charAt(j);
            }
        }

        queue.offer(new Node(7, 0));

        System.out.println(bfs() == true ? 1 : 0);
    }

    private static boolean bfs() {
        while (!queue.isEmpty()) {
            int len = queue.size();
            visited = new boolean[8][8];

            for (int c = 0; c < len; c++) {
                Node cur = queue.poll();
                if (graph[cur.x][cur.y] == '#') continue;
                if (cur.x == 0 && cur.y == 7) return true;

                for (int i = 0; i < 9; i++) {
                    int nx = cur.x + dx[i];
                    int ny = cur.y + dy[i];
                    if (nx < 0 || ny < 0 || nx >= 8 || ny >= 8 || graph[nx][ny] == '#') continue;
                    if (visited[nx][ny] == true) continue;
                    queue.offer(new Node(nx, ny));
                    if (nx == cur.x && ny == cur.y) continue;
                    visited[nx][ny] = true;
                }
            }
            moveWall();
        }

        return false;
    }

    private static void moveWall() {
        for (int j = 0; j < 8; j++) {
            for (int i = 6; i > -1; i--) {
                graph[i+1][j] = graph[i][j];
            }
            graph[0][j] = '.';
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
