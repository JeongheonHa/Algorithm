package com.ribo.programmers.kakaoblind2020.convertparenthesis;

import java.util.*;

public class Solution {

    static int pos;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println(solution(input.nextLine()));
    }

    private static String solution(String p) {

        if (p.isEmpty()) return p;

        boolean correct = isCorrect(p);
        String u = p.substring(0, pos);
        String v = p.substring(pos);

        if (correct) {
            return u + solution(v);
        }

        String answer = "(" + solution(v) + ")";

        for (int i=1; i < u.length()-1; i++) {
            char ch = u.charAt(i);
            if (ch == '(') {
                answer += ')';
            } else {
                answer += '(';
            }
        }
        return answer;
    }

    private static boolean isCorrect(String w) {
        Stack<Character> stack = new Stack<>();
        int left = 0;
        int right = 0;
        boolean ret = true;

        for (int i=0; i < w.length(); i++) {
            char ch = w.charAt(i);

            if (ch == '(') {
                stack.push('(');
                left++;
            } else {
                if (stack.isEmpty()) {
                    ret = false;
                } else {
                    stack.pop();
                }
                right++;
            }

            if (left == right) {
                pos = i + 1;
                return ret;
            }
        }

        return ret;
    }
}
