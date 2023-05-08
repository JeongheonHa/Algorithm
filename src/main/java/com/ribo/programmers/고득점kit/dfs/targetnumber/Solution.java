package com.ribo.programmers.고득점kit.dfs.targetnumber;

import java.util.*;

public class Solution {

    int ans = 0;

    public int solution(int[] numbers, int target) {

        dfs(0, 0, target, numbers);

        return ans;
    }

    private void dfs(int cnt, int num, int target, int[] nums) {
        if (cnt == nums.length) {
            if (num == target) {
                ans++;
            }

            return;
        }

        dfs(cnt+1, num + nums[cnt], target, nums);
        dfs(cnt+1, num - nums[cnt], target, nums);
    }
}
