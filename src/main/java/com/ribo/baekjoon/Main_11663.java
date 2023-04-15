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

            System.out.println(rightIdx(0, n-1, y) - leftIdx(0, n-1, x) + 1);
        }
    }

    private static int rightIdx(int start, int end, int target) {
        while (start <= end) {
            int mid = (start + end) / 2;

            if (point[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return end;
    }

    private static int leftIdx(int start, int end, int target) {
        while (start <= end) {
            int mid = (start + end) / 2;

            if (point[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return start;
    }
}
