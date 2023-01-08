package com.ribo.baekjoon;

import java.io.*;
import java.util.*;

public class Main_14891 {
    static String[] wheel;
    static int[] isRotate;
    static int k, num, d, total;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        wheel = new String[4];

        for(int i=0; i<4; i++) {
            wheel[i] = br.readLine();
        }
        k = Integer.parseInt(br.readLine());

        for(int i=0; i<k; i++) {
            st = new StringTokenizer(br.readLine());
            num = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            isRotate = new int[4];
            check(num-1, d);
        }

        for(int i=0; i<4; i++) {
            if(wheel[i].charAt(0) == '1') {
                total += Math.pow(2, i);
            }
        }
        System.out.println(total);

    }

    private static void check(int num, int d) {
        isRotate[num] = d;
        cw(num, d);
        ccw(num, d);

        for(int i=0; i<4; i++) {
            rotate(i, isRotate[i]);
        }
    }

    private static void rotate(int num, int d) {
        if(d == 1) {
            wheel[num] = wheel[num].charAt(7) + wheel[num].substring(0,7);
        }
        if(d == -1) {
            wheel[num] = wheel[num].substring(1) + wheel[num].charAt(0);
        }
    }

    private static void cw(int num, int d) {
        if(num == 3) return;

        if(wheel[num].charAt(2) != wheel[num+1].charAt(6)) {
            isRotate[num+1] = d * -1;
            cw(num+1, d*-1);
        }
    }

    private static void ccw(int num, int d) {
        if(num == 0) return;

        if(wheel[num].charAt(6) != wheel[num-1].charAt(2)) {
            isRotate[num-1] = d * -1;
            ccw(num-1, d*-1);
        }
    }
}
