package com.ribo.baekjoon;

import java.io.*;
import java.util.*;

public class Main_17144 {
    static int[][] graph = new int[50][50];
    static int r, c, t, up, down, before, sum;
    static List<Integer> cleaner = new ArrayList<>(2);
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());
        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < c; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == -1) {
                    cleaner.add(i);
                }
            }
        }
        up = cleaner.get(0);
        down = cleaner.get(1);

        solve();

    }

    private static void solve() {
        while (t-- > 0) {
            bfs();
            ccw();
            cw();
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (graph[i][j] != 0 && graph[i][j] != -1) {
                    sum += graph[i][j];
                }
            }
        }

        System.out.println(sum);
    }

    private static void cw() {
        dx = new int[] {0, 1, 0, -1};
        dy = new int[] {1, 0, -1, 0};
        int x = down;
        int y = 1;
        int dir = 0;
        before = 0;
        while (true) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if (x == down && y == 0) break;
            if (nx < 0 || ny < 0 || nx >= r || ny >= c) {
                dir++;
                continue;
            }
            swap(x, y);
            x = nx;
            y = ny;
        }
    }

    private static void swap(int x, int y) {
        int temp;
        temp = graph[x][y];
        graph[x][y] = before;
        before = temp;
    }
    private static void ccw() {
        dx = new int[] {0, -1, 0, 1};
        dy = new int[] {1, 0, -1, 0};
        int x = up;
        int y = 1;
        int dir = 0;
        before = 0;
        while (true) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if (x == up && y == 0) break;
            if (nx < 0 || ny < 0 || nx >= r || ny >= c) {
                dir++;
                continue;
            }
            swap(x, y);
            x = nx;
            y = ny;
        }
    }
    private static void bfs() {
        int[][] temp = new int[50][50];
        for (int x = 0; x < r; x++) {
            for (int y = 0; y < c; y++) {
                int tmp = 0;
                if (graph[x][y] != 0 && graph[x][y] != -1) {
                    for (int i = 0; i < 4; i++) {
                        int nx = x + dx[i];
                        int ny = y + dy[i];

                        if (nx < 0 || ny < 0 || nx >= r || ny >= c || graph[nx][ny] == -1) continue;
                        temp[nx][ny] += graph[x][y] / 5;
                        tmp += graph[x][y] / 5;
                    }
                    graph[x][y] -= tmp;
                }
            }
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                graph[i][j] += temp[i][j];
            }
        }
    }
}
