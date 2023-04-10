package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_11663 {

    static int n, m;
    static int[] point;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        point = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            point[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(point);

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            System.out.println(yMinusX(y, x));
        }
    }

    private static int yMinusX(int y, int x) {
        int right = findRightIdx(y, 0, n-1);
        int left = findLeftIdx(x, 0, n-1);

        if (left > right) return 0;
        if (left == -1 && right == -1) return 0;
        if (left == -1) left = 0;
        return right - left + 1;
    }

    private static int findRightIdx(int y, int start, int end) {
        if (y > point[n-1]) return n-1;
        if (y < point[0]) return -1;

        int ret = 0;
        while (start <= end) {
            int mid = (start + end) / 2;

            if (point[mid] == y) {
                return mid;
            } else if (point[mid] > y) {
                end = mid - 1;
                ret = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return ret;
    }

    private static int findLeftIdx(int x, int start, int end) {
        if (x > point[n-1]) return n-1;
        if (x < point[0]) return -1;

        int ret = 0;
        while (start <= end) {
            int mid = (start + end) / 2;

            if (point[mid] == x) {
                return mid;
            } else if (point[mid] > x) {
                end = mid - 1;
            } else {
                start = mid + 1;
                ret = mid + 1;
            }
        }

        return ret;
    }
}
