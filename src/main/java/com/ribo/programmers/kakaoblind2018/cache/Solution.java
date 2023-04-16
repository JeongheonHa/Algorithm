package com.ribo.programmers.kakaoblind2018.cache;

import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int cacheSize = Integer.parseInt(input.nextLine());
        String[] cities = input.nextLine().replaceAll("[\\[\\],\"]", "").split(" ");
        System.out.println(solution(cacheSize, cities));
    }

    private static int solution(int cacheSize, String[] cities) {
        int answer = 0;

        Deque<String> cache = new LinkedList<>();

        cities = Arrays.stream(cities).map(String::toUpperCase).toArray(String[]::new);

        for (String city : cities) {
            if (cache.contains(city)) {
                cache.remove(city);
                cache.addFirst(city);
                answer++;
            } else {
                cache.addFirst(city);
                answer += 5;
            }

            if (cache.size() > cacheSize) {
                cache.removeLast();
            }

        }
        return answer;
    }
}
