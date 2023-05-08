package com.ribo.programmers.고득점kit.bfs.gamemapshortestpath;

import java.util.*;

public class Solution {
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};

    public int solution(int[][] maps) {
        int answer = 0;

        answer = bfs(maps);
        return answer;
    }

    private int bfs(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;

        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(0, 0, 0));

        while (!queue.isEmpty()) {
            Node cur = queue.poll();

            if (cur.x == n-1 && cur.y == m-1) {
                return cur.dist + 1;
            }
            for (int i=0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (visited[nx][ny] || maps[nx][ny] == 0) continue;
                visited[nx][ny] = true;
                queue.offer(new Node(nx, ny, cur.dist + 1));
            }
        }

        return -1;
    }

    private class Node {
        int x, y, dist;

        public Node (int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }
}
