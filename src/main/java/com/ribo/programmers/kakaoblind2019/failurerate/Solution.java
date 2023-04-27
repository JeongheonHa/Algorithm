package com.ribo.programmers.kakaoblind2019.failurerate;

import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = {};
        int[] fail = new int[N+2];
        int[] arrive = new int[N+2];

        for (int i=0; i < stages.length; i++) {
            for (int j=1; j <= stages[i]; j++) {
                arrive[j]++;
            }

            fail[stages[i]]++;
        }

        List<Node> failRates = new ArrayList<>();
        for (int i=1; i < N+1; i++) {
            if (arrive[i] == 0) {
                failRates.add(new Node(i, 0.0));
                continue;
            }
            failRates.add(new Node(i, (double) fail[i] / arrive[i]));
        }

        Collections.sort(failRates);

        List<Integer> result = new ArrayList<>();
        for (Node curr : failRates) {
            result.add(curr.stage);
        }

        answer = result.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }

    private static class Node implements Comparable<Node> {
        int stage;
        double fRate;

        public Node (int stage, double fRate) {
            this.stage = stage;
            this.fRate = fRate;
        }

        public int compareTo(Node node) {
            if (this.fRate > node.fRate) {
                return -1;
            } else if (this.fRate < node.fRate) {
                return 1;
            } else {
                return this.stage - node.stage;
            }
        }
    }
}
