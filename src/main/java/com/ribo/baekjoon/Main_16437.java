package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_16437 {

    static int n;
    static List<Integer>[] adj;
    static char[] kinds;
    static long[] amounts;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        adj = new List[n + 1];

        for (int i = 1; i < n + 1; i++) {
            adj[i] = new LinkedList<>();
        }

        kinds = new char[n + 1];
        amounts = new long[n + 1];

        for (int i = 2; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            char kind = st.nextToken().charAt(0);
            int amount = Integer.parseInt(st.nextToken());
            int next = Integer.parseInt(st.nextToken());
            kinds[i] = kind;
            amounts[i] = amount;
            adj[next].add(i);
        }

        System.out.println(dfs(1));
    }

    private static long dfs(int here) {
        long sum = 0;
        for (int there : adj[here]) {
            sum += dfs(there);
        }

        if (kinds[here] == 'S') {
            return sum + amounts[here];
        } else {
            return (sum - amounts[here] >= 0) ? sum - amounts[here] : 0;
        }

    }
}
