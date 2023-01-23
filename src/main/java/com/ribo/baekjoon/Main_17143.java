package com.ribo.baekjoon;

import java.io.*;
import java.util.*;

public class Main_17143 {
    static Shark[][] graph = new Shark[100][100];
    static int R, C, M, r, c, s, d, z, dir, ans;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            r = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            s = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            z = Integer.parseInt(st.nextToken());

            if (d == 2) {
                d = 3;
            } else if (d == 3) {
                d = 2;
            }
            graph[r-1][c-1] = new Shark(s, d-1, z);
            }

        solve();
        }
    private static void solve() {
        for (int j = 0; j < C; j++) {
            for (int i = 0; i < R; i++) {
                if (graph[i][j] != null) {
                    ans += graph[i][j].z;
                    graph[i][j] = null;
                    break;
                }
            }
            move();
        }
        System.out.println(ans);
    }
    private static void move() {
        Shark[][] temp = new Shark[100][100];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (graph[i][j] != null) {
                    Shark cur = graph[i][j];
                    int x = i;
                    int y = j;
                    dir = cur.d;
                    int sec = cur.s;
                    while (sec-- > 0) {
                        int nx = x + dx[dir];
                        int ny = y + dy[dir];
                        if (nx < 0 || ny < 0 || nx >= R || ny >= C) {
                            dir = (dir + 2) % 4;
                            sec++;
                            continue;
                        }
                        x = nx;
                        y = ny;
                    }

                    if (temp[x][y] == null || temp[x][y].z < cur.z) {
                        temp[x][y] = new Shark(cur.s, dir, cur.z);
                    }
                }
            }
        }
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                graph[i][j] = temp[i][j];
            }
        }
    }

    static class Shark {
            int s, d, z;

            public Shark(int s, int d, int z) {
                this.s = s;
                this.d = d;
                this.z = z;
            }
    }
}
