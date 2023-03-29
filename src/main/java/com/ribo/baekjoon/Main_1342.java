package com.ribo.baekjoon;

import java.util.*;

public class Main_1342 {

    static String str;
    static char[] arr;
    static int visited;
    static Set<String> set = new HashSet<>();

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        str = input.next();
        arr = new char[str.length()];

        dfs(0);

        System.out.println(set.size());
    }

    private static void dfs(int cnt) {
        if (cnt == str.length()) {
            StringBuilder sb = new StringBuilder();
            sb.append(arr[0]);
            for (int i = 1; i < str.length(); i++) {
                if (arr[i-1] == arr[i]) return;
                sb.append(arr[i]);
            }
            set.add(sb.toString());
            return;
        }

        for (int i = 0; i < str.length(); i++) {
            if ((visited & 1 << i) != 0) continue;
            visited |= 1 << i;
            arr[cnt] = str.charAt(i);
            dfs(cnt + 1);
            visited &= ~(1 << i);
        }
    }
}
