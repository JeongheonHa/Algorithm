package com.ribo.programmers.kakaoblind2019.candidatekey;

import java.util.*;

public class Solution {

    private static int cardi, degree, ans;
    private static String[] combi;
    private static Set<String> keys = new HashSet<>();

    public int solution(String[][] relation) {
        int answer = 0;
        cardi = relation.length;
        degree = relation[0].length;

        for (int i=1; i < degree + 1; i++) {
            Set<String> checkList = new HashSet<>();
            combi = new String[i];
            dfs(0, 0, i, relation, checkList);
        }

        answer = ans;
        return answer;
    }

    private static void dfs(int cnt, int idx, int n, String[][] relation, Set<String> checkList) {
        if (cnt == n) {
            String str = String.join("", combi);
            for (String key : keys) {
                int keyCnt = 0;
                for (int a = 0; a < key.length(); a++) {
                    if (str.contains(key.charAt(a) + "")) {
                        keyCnt++;
                    }
                    if (keyCnt == key.length()) return;
                }
            }

            for (int i=0; i < cardi; i++) {
                String temp = "";
                for (String j : combi) {
                    temp += relation[i][Integer.parseInt(j)];
                }
                if (checkList.contains(temp)) {
                    checkList.clear();
                    return;
                }
                checkList.add(temp);
            }

            // 후보키 가능
            keys.add(String.join("", combi));

            checkList.clear();
            ans++;
            return;
        }

        for (int i=idx; i < degree; i++) {
            combi[cnt] = "" + i;
            dfs(cnt + 1, i + 1, n, relation, checkList);
        }
    }
}
