package com.ribo.baekjoon;

import java.util.*;

public class Main_16922 {

    static int n;
    static Set<Integer> set = new HashSet<>();
    static int[] numbers = {1, 5, 10, 50};
    static int[] cases;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        n = input.nextInt();
        cases = new int[n];

        dfs(0, 0);

        System.out.println(set.size());
    }

    private static void dfs(int cnt, int idx) {
        if (cnt == n) {
            int temp = 0;
            for (int roma : cases) {
                temp += roma;
            }

            set.add(temp);
            return;
        }

        for (int i = idx; i < 4; i++) {
            cases[cnt] = numbers[i];
            dfs(cnt + 1, i);
        }
    }
}
