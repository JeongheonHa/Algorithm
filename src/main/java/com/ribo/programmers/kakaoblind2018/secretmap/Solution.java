package com.ribo.programmers.kakaoblind2018.secretmap;

import java.util.*;

public class Solution {

    static int[][] graph1, graph2;

    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];

        graph1 = new int[n][n];
        graph2 = new int[n][n];

        makeBinaryGraph(arr1, graph1, n);
        makeBinaryGraph(arr2, graph2, n);

        return compareGraph(answer, n);
    }

    private static String[] compareGraph(String[] answer, int n) {
        for (int i=0; i < n; i++) {
            String temp = "";
            for (int j=0; j < n; j++) {
                if (graph1[i][j] + graph2[i][j] > 0) {
                    temp += '#';
                } else {
                    temp += ' ';
                }
            }
            answer[i] = temp;
        }

        return answer;
    }

    private static void makeBinaryGraph(int[] arr, int[][] graph, int n) {
        for (int i=0; i < n; i++) {
            String binaryNum = Integer.toBinaryString(arr[i]);
            int len = binaryNum.length();
            int idx = n-len;
            int bIdx = 0;
            for (int j = idx; j < n; j++) {
                graph[i][j] = binaryNum.charAt(bIdx++) - '0';
            }
        }
    }
}
