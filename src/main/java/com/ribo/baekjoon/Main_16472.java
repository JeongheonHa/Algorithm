package com.ribo.baekjoon;

import java.util.*;

public class Main_16472 {

    static int n, s, e, length, ans;
    static String str;
    static Map<Character, Integer> map = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        n = scanner.nextInt();
        str = scanner.next();

        while (true) {
            if (map.size() > n) {
                char curr = str.charAt(s++);
                map.put(curr, map.get(curr) - 1);
                if (map.get(curr) == 0) map.remove(curr);
                length--;
            } else if (e == str.length()) {
                break;
            } else if (map.size() <= n) {
                char curr = str.charAt(e++);
                map.put(curr, map.getOrDefault(curr, 0) + 1);
                length++;
            }

            if (map.size() > n) continue;
            ans = Math.max(ans, length);
        }


        System.out.println(ans);
    }
}
