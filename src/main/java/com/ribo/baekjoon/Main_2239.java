package com.ribo.baekjoon;


import java.util.*;
import java.io.*;


public class Main_2239 {
    static int[][] graph = new int[9][9];
    static List<Node> blank = new ArrayList<>();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 9; i++) {
            String s = br.readLine();
            for (int j = 0; j < 9; j++) {
                graph[i][j] = s.charAt(j) - '0';
                if (graph[i][j] == 0) {
                    blank.add(new Node(i, j));
                }
            }
        }

        solve();
    }

    private static void solve() {
        dfs(0);
    }

    private static void dfs(int cnt) {
        if (cnt == blank.size()) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    System.out.print(graph[i][j]);
                }
                System.out.println();
            }

            System.exit(0);
        }

        for (int num = 1; num < 10; num++) {
            int x = blank.get(cnt).x;
            int y = blank.get(cnt).y;

            if (check(x, y, num)) {
                graph[x][y] = num;
                dfs(cnt+1);
                graph[x][y] = 0;
            }
        }
    }

    private static boolean check(int x, int y, int num) {
        for (int i = 0; i < 9; i++) {
            if (graph[i][y] == num) {
                return false;
            }
        }

        for (int j = 0; j < 9; j++) {
            if (graph[x][j] == num) {
                return false;
            }
        }

        x = x / 3;
        y = y / 3;

        for (int i = x*3; i < x*3+3; i++) {
            for (int j = y*3; j < y*3+3; j++) {
                if (graph[i][j] == num) {
                    return false;
                }
            }
        }

        return true;
    }

    static class Node {
        int x, y;

        public Node (int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
