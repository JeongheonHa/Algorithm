package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_2003 {

    static int n, m, s, e, sum, cnt;
    static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        while (true) {
            if (sum >= m) {
                sum -= arr[s++];
            } else if (e == arr.length) {
                break;
            } else if (sum < m) {
                sum += arr[e++];
            }

            if (sum == m) {
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}
