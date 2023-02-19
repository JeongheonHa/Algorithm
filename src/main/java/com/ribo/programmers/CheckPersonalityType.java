package com.ribo.programmers;


import java.util.*;

public class CheckPersonalityType {
    
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        HashMap<Character, Integer> type = new HashMap<>();
        for (int i=0; i<survey.length; i++) {
            char first = survey[i].charAt(0);
            char second = survey[i].charAt(1);
            int num = choices[i];
            if (num < 4) {
                type.put(first, type.getOrDefault(first, 0) + 4 - num);
            } else if (num > 4) {
                type.put(second, type.getOrDefault(second, 0) + num - 4);
            }
        }

        if (type.getOrDefault('R', 0) >= type.getOrDefault('T', 0)) {
            answer += "R";
        } else {
            answer += "T";
        }

        if (type.getOrDefault('C', 0) >= type.getOrDefault('F', 0)) {
            answer += "C";
        } else {
            answer += "F";
        }

        if (type.getOrDefault('J', 0) >= type.getOrDefault('M', 0)) {
            answer += "J";
        } else {
            answer += "M";
        }

        if (type.getOrDefault('A', 0) >= type.getOrDefault('N', 0)) {
            answer += "A";
        } else {
            answer += "N";
        }

        return answer;
    }
}
