package com.ribo.baekjoon;

import java.util.*;


public class Main_22943 {

    static int k;
    static long m;

    static String max = "98765";
    static int maxValue;

    static boolean[] isPrime;
    static List<Integer> primeNumbers = new ArrayList<>();

    static int[] permutation;
    static int visited;
    static List<Integer> cases = new ArrayList<>();

    static Set<Integer> primeSumList = new HashSet<>();
    static int[] sumCase = new int[2];

    static Set<Integer> primeMultiList = new HashSet<>();
    static long[] multiCase = new long[2];


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        k = input.nextInt();
        m = input.nextLong();

        maxValue = Integer.parseInt(max.substring(0, k));

        findPrimeNumber();
        makePrimeNumbers();

        permutation = new int[k];
        makeCases(0);

        makePrimeSumList(0, 0);
        makePrimeMultiList(0, 0);

        int cnt = 0;
        for (int num : cases) {
            if (checkSum(num) && checkMulti(num)) cnt++;
        }

        System.out.println(cnt);
    }

    private static boolean checkMulti(int num) {
        while (true) {
            if (num % m == 0) num /= m;
            else break;
        }

        if (primeMultiList.contains(num)) return true;

        return false;
    }

    private static boolean checkSum(int num) {
        if (primeSumList.contains(num)) return true;

        return false;
    }

    private static void makePrimeMultiList(int cnt, int idx) {
        if (cnt == 2) {
            long multiValue = multiCase[0] * multiCase[1];
            if (multiValue > maxValue) return;
            primeMultiList.add((int)multiValue);
            return;
        }

        for (int i = idx; i < primeNumbers.size(); i++) {
            multiCase[cnt] = primeNumbers.get(i);
            makePrimeMultiList(cnt + 1, idx);
        }
    }

    private static void makePrimeSumList(int cnt, int idx) {
        if (cnt == 2) {
            int sumValue = sumCase[0] + sumCase[1];
            if (sumValue > maxValue) return;
            primeSumList.add(sumValue);
            return;
        }

        for (int i = idx; i < primeNumbers.size(); i++) {
            sumCase[cnt] = primeNumbers.get(i);
            makePrimeSumList(cnt + 1, i + 1);
        }
    }

    private static void makeCases(int cnt) {
        if (cnt == k) {
            String temp = "";
            for (int i = 0; i < k; i++) {
                temp += permutation[i];
            }

            cases.add(Integer.parseInt(temp));
            return;
        }

        for (int i = 0; i < 10; i++) {
            if ((i == 0 && cnt == 0) || (visited & 1 << i) != 0) continue;
            visited |= 1 << i;
            permutation[cnt] = i;
            makeCases(cnt + 1);
            visited &= ~(1 << i);
        }
    }

    private static void makePrimeNumbers() {
        for (int i = 0; i < maxValue + 1; i++) {
            if (isPrime[i] == false) continue;
            primeNumbers.add(i);
        }
    }

    private static void findPrimeNumber() {
        isPrime = new boolean[maxValue + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i < Math.sqrt(maxValue) + 1; i++) {
            if (isPrime[i] == false) continue;
            for (int j = i * i; j < maxValue + 1; j += i) {
                isPrime[j] = false;
            }
        }
    }
}