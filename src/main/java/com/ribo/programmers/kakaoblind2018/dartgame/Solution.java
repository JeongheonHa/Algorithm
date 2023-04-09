package com.ribo.programmers.kakaoblind2018.dartgame;

import java.util.*;

public class Solution {

    static int[] score = new int[3];
    static int[] award = new int[3];
    static int[] bonusScore = new int[3];
    static int idx;

    public int solution(String dartResult) {
        int answer = 0;

        Arrays.fill(award, 1);

        for (int i=0; i < 3; i++) {
            isScore(i, dartResult);
            isBonus(i, dartResult);
            isAward(i, dartResult);
        }

        for (int i=0; i < 3; i++) {
            answer += bonusScore[i] * award[i];
        }

        return answer;
    }

    private static void isAward(int cur, String dartResult) {
        if (idx == dartResult.length()) return;

        char ch = dartResult.charAt(idx);
        int num = ch - '0';
        if (num >= 0 && num <= 10) return;

        if (cur == 0 && ch == '*') {
            award[cur] *= 2;
        }

        if (cur != 0 && ch == '*') {
            award[cur] *= 2;
            award[cur-1] *= 2;
        }

        if (ch == '#') {
            award[cur] *= -1;
        }

        idx++;
    }

    private static void isBonus(int cur, String dartResult) {
        char ch = dartResult.charAt(idx);
        if (ch == 'S') {
            bonusScore[cur] = (int) Math.pow(score[cur], 1);
        } else if (ch == 'D') {
            bonusScore[cur] = (int) Math.pow(score[cur], 2);
        } else if (ch == 'T') {
            bonusScore[cur] = (int) Math.pow(score[cur], 3);
        }

        idx++;
    }

    private static void isScore(int cur, String dartResult) {
        String temp = "";
        while (idx < dartResult.length()) {
            if (dartResult.charAt(idx) - '0' >= 0 && dartResult.charAt(idx) - '0' <= 10) {
                temp += dartResult.charAt(idx) - '0';
                idx++;
            } else {
                break;
            }
        }

        score[cur] = Integer.parseInt(temp);
    }
}
