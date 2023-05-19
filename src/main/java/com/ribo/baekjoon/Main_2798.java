package com.ribo.baekjoon;

import java.util.*;

public class Main_2798 {
    
    static int n, m, ans;
    static int[] arr;
    static int[] comb;
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        n = input.nextInt();
        m = input.nextInt();
        
        arr = new int[n];
        comb = new int[n];
        
        for (int i=0; i < n; i++) {
            arr[i] = input.nextInt();
        }
        
        dfs(0, 0);

        System.out.println(ans);
    }
    
    private static void dfs(int cnt, int idx) {
        if (cnt == 3) {
            int sum = Arrays.stream(comb).sum();
            if (sum > m) return;
            ans = Math.max(ans, sum);
            return;
        }
        
        for (int i=idx; i < n; i++) {
            comb[cnt] = arr[i];
            dfs(cnt+1, i+1);
        }
    }
}
