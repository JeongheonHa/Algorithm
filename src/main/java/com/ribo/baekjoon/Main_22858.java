package com.ribo.baekjoon;

import java.util.*;

public class Main_22858 {

    static int n, k;
    static int[] d, p, s;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        n = input.nextInt();
        k = input.nextInt();

        d = new int[n+1];
        p = new int[n+1];
        s = new int[n+1];

        for (int i = 1; i < n + 1; i++) {
            s[i] = input.nextInt();
        }

        for (int i = 1; i < n + 1; i++) {
            d[i] = input.nextInt();
        }

        while (k-- > 0) {
            for (int i = 1; i < n + 1; i++) {
                p[d[i]] = s[i];
            }

            s = Arrays.copyOf(p, n+1);
        }

        for (int i = 1; i < n + 1; i++) {
            System.out.printf("%d ", p[i]);
        }
    }
}

