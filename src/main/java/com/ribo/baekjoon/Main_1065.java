package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_1065 {
    static int n, cnt;
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();

        for (int i = 1; i <= n; i++) {
            if (i < 100) {
                cnt++;
            } else {
                int third = i / 100;
                int second = (i % 100) / 10;
                int first = i % 10;
                if (second - first == third - second) {
                    cnt++;
                }
            }
        }

        System.out.println(cnt);
    }
}
