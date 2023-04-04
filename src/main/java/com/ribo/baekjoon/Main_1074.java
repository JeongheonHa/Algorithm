package com.ribo.baekjoon;

import java.util.*;

public class Main_1074 {

    static int n, r, c, size, cnt, ans;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        n = input.nextInt();
        r = input.nextInt();
        c = input.nextInt();

        size = (int) Math.pow(2, n);

        dfs(0, 0, size);

    }

    private static void dfs(int x, int y, int size) {
        if (x == r && y == c) {
            ans = cnt;
            System.out.println(ans);
            System.exit(0);
        }

        if (r >= x + size || c >= y + size) {
            cnt += size * size;
            return;
        }

        int half = size / 2;

        dfs(x, y, half);
        dfs(x, y + half, half);
        dfs(x + half, y, half);
        dfs(x + half, y + half, half);
    }
}
