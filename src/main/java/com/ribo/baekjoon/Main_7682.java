package com.ribo.baekjoon;

import java.util.*;

public class Main_7682 {

    static char[][] graph = new char[3][3];
    static int xCnt, oCnt;
    static int xRowBingo, xColBingo;
    static int oRowBingo, oColBingo;
    static int xLeftCrossBingo, oLeftCrossBingo;
    static int xRightCrossBingo, oRightCrossBingo;
    static boolean flag;

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            String s = scanner.next();

            if (s.equals("end")) break;

            xRowBingo = xColBingo = 0;
            oRowBingo = oColBingo = 0;
            xLeftCrossBingo = oLeftCrossBingo = 0;
            xRightCrossBingo = oRightCrossBingo = 0;

            xCnt = oCnt = 0;

            for (int i = 0; i < 9; i++) {
                graph[i/3][i%3] = s.charAt(i);
                if (graph[i/3][i%3] == 'X') xCnt++;
                if (graph[i/3][i%3] == 'O') oCnt++;
            }

            flag = false;

            System.out.println(isValid() ? "valid" : "invalid");
        }
    }

    private static boolean isValid() {
        if (xCnt > oCnt + 1 || oCnt > xCnt) return false;

        isCol();
        isRow();
        isLeftCross();
        isRightCross();

        int xBingo = xColBingo + xRowBingo + xLeftCrossBingo + xRightCrossBingo;
        int oBingo = oColBingo + oRowBingo + oLeftCrossBingo + oRightCrossBingo;

        if (xCnt > oCnt && xBingo > 0 && oBingo == 0) return true;
        if (xCnt == oCnt && oBingo > 0 && xBingo == 0) return true;
        if (xCnt + oCnt == 9 && xBingo == 0 && oBingo == 0) return true;

        return false;
    }

    private static void isCol() {
        for (int i = 0; i < 3; i++) {
            flag = true;
            if (graph[i][0] == '.') continue;

            for (int j = 0; j < 2; j++) {
                if (graph[i][j] != graph[i][j+1]) {
                    flag = false;
                    break;
                }
            }

            if (flag == true) {
                if (graph[i][0] == 'X') xColBingo++;
                if (graph[i][0] == 'O') oColBingo++;
            }
        }
    }

    private static void isRow() {
        for (int j = 0; j < 3; j++) {
            flag = true;

            if (graph[0][j] == '.') continue;

            for (int i = 0; i < 2; i++) {
                if (graph[i][j] != graph[i+1][j]) {
                    flag = false;
                    break;
                }
            }

            if (flag == true) {
                if (graph[0][j] == 'X') xRowBingo++;
                if (graph[0][j] == 'O') oRowBingo++;
            }
        }
    }

    private static void isLeftCross() {
        if (graph[0][0] == '.') return;

        for (int i = 0; i < 2; i++) {
            if (graph[i][i] != graph[i+1][i+1]) return;
        }

        if (graph[0][0] == 'X') xLeftCrossBingo++;
        if (graph[0][0] == 'O') oLeftCrossBingo++;
    }

    private static void isRightCross() {
        if (graph[2][0] == '.') return;

        for (int i = 0; i < 2; i++) {
            if (graph[2-i][i] != graph[2-i-1][i+1]) return;
        }

        if (graph[2][0] == 'X') xRightCrossBingo++;
        if (graph[2][0] == 'O') oRightCrossBingo++;
    }
}

