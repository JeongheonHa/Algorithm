package com.ribo.programmers;

import java.util.*;


class ExpirationDate {
    public static int[] solution(String today, String[] terms, String[] privacies) {
        int year = Integer.parseInt(today.substring(0, 4));
        int month = Integer.parseInt(today.substring(5, 7));
        int day = Integer.parseInt(today.substring(8, 10));

        int todayMin = year * 12 * 28 + month * 28 + day;

        HashMap<String, Integer> map = new HashMap<>();

        for (String term : terms) {
            String[] temp = term.split(" ");
            map.put(temp[0], Integer.parseInt(temp[1]));
        }

        List<Integer> list = new ArrayList<>();

        for (int i=0; i<privacies.length; i++) {
            String privacy = privacies[i];
            String pri = privacy.replace(".", " ");
            String[] temp = pri.split(" ");
            int priYear = Integer.parseInt(temp[0]);
            int priMonth = Integer.parseInt(temp[1]);
            int priDay = Integer.parseInt(temp[2]);
            int plus = map.get(temp[3]);
            int priMin = priYear * 12 * 28 + (priMonth + plus) * 28 + priDay;
            if (todayMin >= priMin) {
                list.add(i+1);
            }
        }

        return Arrays.stream(list.toArray()).mapToInt((i) -> (int)i).toArray();
    }
}