package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_4779 {

    static int n;
    static String[] arr;
    static String s;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNext()) {
            n = scanner.nextInt();

            arr = new String[(int) Math.pow(3, n)];

            Arrays.fill(arr, "-");

            div(0, (int) Math.pow(3, n));
            s = String.join("", arr);
            System.out.println(s);
        }
    }

    private static void div(int start, int length) {
        if (length < 3) return;
        int left = start + length / 3;
        int right = start + length / 3 * 2;

        for (int i = left; i < right; i++) {
            arr[i] = " ";
        }

        div(start, length / 3);
        div(right, length / 3);
    }
}
