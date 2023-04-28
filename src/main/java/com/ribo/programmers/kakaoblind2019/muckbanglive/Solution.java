package com.ribo.programmers.kakaoblind2019.muckbanglive;

import java.util.*;

public class Solution {

    private static int cnt;
    private static PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node.time));

    public int solution(int[] food_times, long k) {
        int answer = 0;

        for (int i=0; i < food_times.length; i++) {
            pq.offer(new Node(i, food_times[i]));
        }

        while (pq.size() <= k) {
            k -= pq.size();
            cnt++;
            while (!pq.isEmpty() && pq.peek().time == cnt) {
                Node curr = pq.poll();
                food_times[curr.idx] = 0;
            }

            if (pq.size() == 0) break;
        }

        if (pq.size() == 0) return -1;

        k++;
        int eat = 0;
        for (int i=0; i < food_times.length; i++) {
            if (food_times[i] == 0) continue;
            eat++;
            if (eat == k) {
                answer = i+1;
                break;
            }
        }
        return answer;
    }

    private static class Node {
        int idx, time;

        public Node (int idx, int time) {
            this.idx = idx;
            this.time = time;
        }
    }
}
