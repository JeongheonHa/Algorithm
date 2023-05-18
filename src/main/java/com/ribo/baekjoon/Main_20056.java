package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_20056 {

    static int N, M, K;
    static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};

    static Queue<FireBall> q = new LinkedList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        for (int i=0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            q.add(new FireBall(x-1, y-1, m, s, d));
        }

        bfs();

        int ans = 0;
        for (FireBall ball : q) {
            ans += ball.m;
        }

        System.out.println(ans);
    }

    private static void bfs() {
        List<FireBall>[][] temp = new List[N][N];

        for (int a = 0; a < N; a++) {
            for (int b = 0; b < N; b++) {
                temp[a][b] = new ArrayList<>();
            }
        }

        while (K-- > 0) {

            for (int i=0; i < N; i++) {
                for (int j=0; j < N; j++) {
                    temp[i][j].clear();
                }
            }

            int oneSec = q.size();
            for (int i=0; i < oneSec; i++) {
                FireBall cur = q.poll();

                int nx = (N + cur.x + dx[cur.d] * (cur.s % N)) % N;
                int ny = (N + cur.y + dy[cur.d] * (cur.s % N)) % N;

                temp[nx][ny].add(new FireBall(nx, ny, cur.m, cur.s, cur.d));
            }

            for (int i=0; i < N; i++) {
                for (int j=0; j < N; j++) {
                    if (temp[i][j].size() == 0) continue;

                    if (temp[i][j].size() >= 2) {
                        int sumM = 0;
                        int sumS = 0;
                        boolean even = false;
                        boolean odd = false;
                        for (FireBall overlap : temp[i][j]) {
                            sumM += overlap.m;
                            sumS += overlap.s;
                            if (overlap.d % 2 == 0) even = true;
                            if (overlap.d != 0 && overlap.d % 2 != 0) odd = true;
                        }
                        sumM /= 5;
                        if (sumM == 0) continue;

                        sumS /= temp[i][j].size();

                        int idx = 1;
                        if (even ^ odd) idx = 0;
                        for (int dir = idx; dir < 8; dir += 2) {
                            q.add(new FireBall(i, j, sumM, sumS, dir));
                        }
                    } else if (temp[i][j].size() == 1) {
                        q.add(temp[i][j].get(0));
                    }
                }
            }
        }
    }

    private static class FireBall {
        int x, y, m ,s, d;

        public FireBall(int x, int y, int m, int s, int d) {
            this.x = x;
            this.y = y;
            this.m = m;
            this.s = s;
            this.d = d;
        }
    }
}
