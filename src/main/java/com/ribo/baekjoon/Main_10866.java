package com.ribo.baekjoon;

import java.io.*;
import java.util.*;

public class Main_10866 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        Deque deque = new Deque();
        String[] inputArr;

        for (int i = 0; i < n; i++) {
            inputArr = br.readLine().split(" ");

            switch(inputArr[0]) {
                case "push_front":
                    deque.push_front(Integer.parseInt(inputArr[1]));
                    break;
                case "push_back":
                    deque.push_back(Integer.parseInt(inputArr[1]));
                    break;
                case "pop_front":
                    System.out.println(deque.pop_front());
                    break;
                case "pop_back":
                    System.out.println(deque.pop_back());
                    break;
                case "size":
                    System.out.println(deque.size());
                    break;
                case "empty":
                    System.out.println(deque.empty());
                    break;
                case "front":
                    System.out.println(deque.front());
                    break;
                case "back":
                    System.out.println(deque.back());
                    break;
            }
        }
    }

    private static class Deque {
        private LinkedList<Integer> list;

        public Deque() {
            this.list = new LinkedList<>();
        }

        public void push_front(int x) {
            list.offerFirst(x);
        }

        public void push_back(int x) {
            list.offerLast(x);
        }

        public int pop_front() {
            return list.isEmpty() ? -1 : list.pollFirst();
        }

        public int pop_back() {
            return list.isEmpty() ? -1 : list.pollLast();
        }

        public int size() {
            return list.size();
        }

        public int empty() {
            return list.isEmpty() ? 1 : 0;
        }

        public int front() {
            return list.isEmpty() ? -1 : list.peekFirst();
        }

        public int back() {
            return list.isEmpty() ? -1 : list.peekLast();
        }
    }
}
