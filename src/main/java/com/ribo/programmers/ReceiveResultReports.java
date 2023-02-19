package com.ribo.programmers;

import java.util.*;

public class ReceiveResultReports {
    public static void main(String[] args) {
        System.out.println(solution("one4seveneight"));
    }

    private static int solution(String s) {
        int answer = 0;
        String[] alphaNum = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

        for (int i = 0; i < alphaNum.length; i++) {
            if (s.contains(alphaNum[i])) {
                s = s.replace(alphaNum[i], Integer.toString(i));
            }
        }

        answer = Integer.parseInt(s);
        return answer;
    }
}
