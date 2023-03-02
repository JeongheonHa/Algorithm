package com.ribo.baekjoon;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main_7569 {

    static int[] rx = {-1, 1, 0, 0, 0, 0};
    static int[] ry = {0, 0, -1, 1, 0, 0};
    static int[] rz = {0, 0, 0, 0, -1, 1};
    static Queue<Tomato> queue = new LinkedList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        int n = sc.nextInt();
        int h = sc.nextInt();

        int[][][] tomato = new int[h][n][m];

        int greenTomato = 0, days = 0;

        for (int i = 0; i < h; i++)
            for (int j = 0; j < n; j++)
                for (int k = 0; k < m; k++) {
                    tomato[i][j][k] = sc.nextInt();
                    if (tomato[i][j][k] == 0)
                        greenTomato++;
                    else if (tomato[i][j][k] == 1)
                        queue.add(new Tomato(i, j, k));
                }

        while (greenTomato > 0 && !queue.isEmpty()) {
            int size = queue.size();
            for(int i = 0; i < size; i++){
                Tomato l = queue.remove();
                int z = l.z;
                int y = l.y;
                int x = l.x;

                for (int j = 0; j < 6; j++) {
                    int nz = z + rz[j];
                    int ny = y + ry[j];
                    int nx = x + rx[j];

                    if (nz < 0 || ny < 0 || nx < 0 || nz >= h || ny >= n || nx >= m)
                        continue;
                    else if (tomato[nz][ny][nx] != 0)
                        continue;

                    greenTomato--;
                    tomato[nz][ny][nx] = 1;
                    queue.add(new Tomato(nz, ny, nx));
                }
            }
            days++;
        }

        System.out.println(greenTomato == 0 ? days : -1);
    }

    static class Tomato {
        int z;
        int y;
        int x;

        Tomato(int z, int y, int x) {
            this.z = z;
            this.y = y;
            this.x = x;
        }
    }
}