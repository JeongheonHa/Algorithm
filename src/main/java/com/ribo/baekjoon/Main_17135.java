package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_17135 {

    static int n, m, d, totalEnemyCount, ans;
    static int[][] graph;
    static Archer[] archerList;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        graph = new int[n+1][m];
        archerList = new Archer[3];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 1) {
                    totalEnemyCount++;
                }
            }
        }

        dfs(0, 0);
        System.out.println(ans);
    }

    private static void dfs(int cnt, int idx) {
        if (cnt == 3) {
            int[][] copyGraph = copy(graph);
            int currentEnemyCountInGraph = totalEnemyCount;
            int deadEnemyByMove = 0;
            int deadEnemyByAttack = 0;

            while (true) {
                deadEnemyByAttack += attackEnemy(copyGraph, 0);
                deadEnemyByMove += moveToDown(copyGraph, 0);

                if (currentEnemyCountInGraph == deadEnemyByAttack + deadEnemyByMove) {
                    break;
                }
            }

            ans = Math.max(ans, deadEnemyByAttack);

            return;
        }

        for (int i = idx; i < m; i++) {
            archerList[cnt] = new Archer(n, i);
            dfs(cnt + 1, i + 1);
        }
    }

    private static int moveToDown(int[][] copyGraph, int deadEnemyByMove) {

        for (int j = 0; j < m; j++) {
            for (int i = n - 1; i > -1; i--) {
                copyGraph[i+1][j] = copyGraph[i][j];
            }
            copyGraph[0][j] = 0;

            if (copyGraph[n][j] == 1) {
                deadEnemyByMove++;
                copyGraph[n][j] = 0;
            }
        }

        return deadEnemyByMove;
    }

    private static int attackEnemy(int[][] copyGraph, int deadEnemyCountByAttack) {

        List<Enemy> enemyList = new ArrayList<>();

        for (Archer archer : archerList) {

            PriorityQueue<Enemy> temp = new PriorityQueue<>(Comparator.comparingInt(Enemy::getDist)
                    .thenComparingInt(Enemy::getY)
            );

            for (int j = 0; j < m; j++) {
                for (int i = n - 1; i > -1; i--) {
                    int dist = Math.abs(archer.x - i) + Math.abs(archer.y - j);
                    if (copyGraph[i][j] == 1 && dist <= d) {
                        temp.add(new Enemy(i, j, dist));
                        break;
                    }
                }
            }

            if (temp.isEmpty()) continue;
            enemyList.add(temp.poll());
        }

        if (enemyList.isEmpty()) return 0;

        for (Enemy enemy : enemyList) {
            if (copyGraph[enemy.x][enemy.y] == 0) continue;
            copyGraph[enemy.x][enemy.y] = 0;
            deadEnemyCountByAttack++;
        }

        return deadEnemyCountByAttack;
    }

    private static int[][] copy(int[][] graph) {
        int[][] copyGraph = new int[n+1][m];

        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < m; j++) {
                copyGraph[i][j] = graph[i][j];
            }
        }

        return copyGraph;
    }

    static class Archer {
        int x, y;

        public Archer (int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static class Enemy {
        int x, y, dist;

        private Enemy (int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public int getDist() {
            return dist;
        }
    }
}
