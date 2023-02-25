package com.ribo.baekjoon;

import java.util.*;
import java.io.*;

public class Main_1786 {
    static int cnt;
    static List<Integer> list = new ArrayList<>();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String text = br.readLine();
        String pattern = br.readLine();
        kmp(text, pattern);

        System.out.println(cnt);

        for(int i = 0; i < cnt; i++)
            System.out.println(list.get(i));
    }

    private static int[] getPi(String ptn) {
        int[] pi = new int[ptn.length()];
        int j = 0;
        for(int i = 1; i < ptn.length(); i++) {
            while(j > 0 && ptn.charAt(i) != ptn.charAt(j)) {
                j = pi[j - 1];
            }
            if(ptn.charAt(i) == ptn.charAt(j))
                pi[i] = ++j;
        }
        return pi;
    }

    private static void kmp(String t, String ptn) {
        int pi[] = getPi(ptn);
        int j = 0;
        for(int i = 0; i < t.length(); i++) {
            while(j > 0 && t.charAt(i) != ptn.charAt(j)) {
                j = pi[j - 1];
            }
            if(t.charAt(i) == ptn.charAt(j)) {
                if(j == ptn.length() - 1) {
                    ++cnt;
                    list.add(i - j + 1);
                    j = pi[j];
                }
                else
                    j++;
            }
        }
    }
}
