package com.ribo.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main_1918 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Stack<Character> stack = new Stack<>();
        String str = br.readLine();
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if ('A' <= ch && ch <= 'Z') {
                sb.append(str.charAt(i));
                continue;
            }

            if (ch == '(') {
                stack.push(ch);
            } else if (ch == '*' || ch == '/') {
                while (!stack.empty() && (stack.peek() == '*' || stack.peek() == '/')) {
                    sb.append(stack.pop());
                }
                stack.push(ch);
            } else if (ch == '-' || ch == '+') {
                while (!stack.empty() && stack.peek() != '(') {
                    sb.append(stack.pop());
                }
                stack.push(ch);
            } else if (ch == ')') {
                while (!stack.empty() && stack.peek() != '(') {
                    sb.append(stack.pop());
                }
                stack.pop();
            }

        }
        while (!stack.empty()) {
            sb.append(stack.pop());
        }

        System.out.println(sb);
    }
}
