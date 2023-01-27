package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

class Main_17142 {
    static int n, m;
    static int[][] graph;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static List<Virus> viruses = new ArrayList<>();
    static Virus[] active;
    static int ans = Integer.MAX_VALUE;
    static int zeroCnt = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][n];
        active = new Virus[m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());

                if (graph[i][j] == 0) {
                    zeroCnt++;
                }
                if (graph[i][j] == 2) {
                    viruses.add(new Virus(i, j, 0));
                }
            }
        }

        solve();
    }

    private static void solve() {
        if (zeroCnt == 0) {
            System.out.println(0);
        } else {
            bf(0, 0);
            System.out.println(ans == Integer.MAX_VALUE ? -1 : ans);
        }
    }

    static void bf(int cnt, int idx) {
        if (cnt == m) {
            bfs(zeroCnt);
            return;
        }

        for (int i = idx; i < viruses.size(); i++) {
            active[cnt] = viruses.get(i);
            bf(cnt+1, i+1);
        }
    }

    static void bfs(int emptySpace) {
        Queue<Virus> q = new LinkedList<>();
        boolean[][] visited = new boolean[n][n];

        for (int i = 0; i < m; i++) {
            Virus virus = active[i];
            visited[virus.x][virus.y] = true;
            q.add(virus);
        }

        while (!q.isEmpty()) {
            Virus virus = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = virus.x + dx[i];
                int ny = virus.y + dy[i];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if (visited[nx][ny] || graph[nx][ny] == 1) continue;

                if (graph[nx][ny] == 0) {
                    emptySpace--;
                }

                if (emptySpace == 0) {
                    ans = Math.min(ans, virus.time + 1);
                    return;
                }

                visited[nx][ny] = true;
                q.add(new Virus(nx, ny, virus.time + 1));
            }
        }
    }

    static class Virus {
        int x, y, time;

        Virus(int x, int y, int time) {
            this.x = x;
            this.y = y;
            this.time = time;
        }
    }
}