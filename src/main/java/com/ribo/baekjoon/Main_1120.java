package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_1120 {
    static int ans = Integer.MAX_VALUE;
    public static void main(String[] args) throws Exception{
        Scanner scanner = new Scanner(System.in);
        String a = scanner.next();
        String b = scanner.next();

        int len = b.length() - a.length() + 1;

        for (int i = 0; i < len; i++) {
            int cnt = 0;
            for (int j = 0; j < a.length(); j++) {
                if (a.charAt(j) != b.charAt(j+i)) {
                    cnt++;
                }
            }

            ans = Math.min(ans, cnt);
        }

        System.out.println(ans);
    }
}
