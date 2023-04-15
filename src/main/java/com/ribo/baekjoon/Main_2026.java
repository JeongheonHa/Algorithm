package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_2026 {

    static int k, n, f;
    static List<Integer>[] graph;
    static int[] comb;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        f = Integer.parseInt(st.nextToken());

        graph = new List[n+1];
        for (int i = 1; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < f; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph[u].add(v);
            graph[v].add(u);
        }

        comb = new int[k];
        dfs(0, 1);
        System.out.println(-1);
    }

    private static boolean check() {
        for (int i = 0; i < comb.length; i++) { // comb의 원소를 돌면서
            for (int j = 0; j < comb.length; j++) { // 그래프가 모두 이어져있는지
                if (comb[i] == comb[j]) continue;
                if (!graph[comb[j]].contains(comb[i])) return false;
            }
        }

        return true;
    }

    private static void dfs(int cnt, int idx) {
        if (cnt == k) {
            if (check() == true) {
                Arrays.stream(comb).forEach(System.out::println);
                System.exit(0);
            }
            return;
        }

        for (int i = idx; i < n + 1; i++) {
            if (1 + graph[i].size() < k) continue;
            comb[cnt] = i;
            dfs(cnt + 1, i + 1);
        }
    }
}
