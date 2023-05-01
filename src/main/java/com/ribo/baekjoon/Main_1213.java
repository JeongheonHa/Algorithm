package com.ribo.baekjoon;

import java.util.*;

public class Main_1213 {

    static int odd;
    static int oddIdx = -1;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String engName = input.nextLine();

        int[] aToZ = new int[26];

        for (int i=0; i < engName.length(); i++) {
            char ch = engName.charAt(i);
            aToZ[ch - 'A']++;
        }

        for (int i=0; i < aToZ.length; i++) {
            if (aToZ[i] % 2 != 0) {
                odd++;
                oddIdx = i;
            }
        }

        if (odd > 1) {
            System.out.println("I'm Sorry Hansoo");
            System.exit(0);
        }

        String ans = "";
        for (int i=0; i < 26; i++) {
            for (int j=0; j < aToZ[i] / 2; j++) {
                ans += (char)('A' + i);
            }
        }

        if (oddIdx != -1) ans += (char)('A' + oddIdx);

        for (int i=25; i > -1; i--) {
            for (int j=0; j < aToZ[i] / 2; j++) {
                ans += (char)('A' + i);
            }
        }

        System.out.println(ans);
    }
}
