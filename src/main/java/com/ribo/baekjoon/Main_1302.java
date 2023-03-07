package com.ribo.baekjoon;

import java.util.*;

public class Main_1302 {
    static int n;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();

        Map<String, Integer> bookList = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String s = scanner.next();
            bookList.put(s, bookList.getOrDefault(s, 0) + 1);
        }

        int maxValue = Collections.max(bookList.values());

        PriorityQueue<String> keyList = new PriorityQueue<>(String::compareTo);

        for (String key : bookList.keySet()) {
            if (bookList.get(key) == maxValue) {
                keyList.add(key);
            }
        }

        System.out.println(keyList.poll());
    }
}
