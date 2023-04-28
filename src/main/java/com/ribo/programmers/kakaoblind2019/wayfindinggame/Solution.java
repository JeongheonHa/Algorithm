package com.ribo.programmers.kakaoblind2019.wayfindinggame;

import java.util.*;

public class Solution {
    public int[][] solution(int[][] nodeinfo) {
        int[][] answer = new int[2][];
        List<Node> nodes = new ArrayList<>();

        for (int i=0; i < nodeinfo.length; i++) {
            nodes.add(new Node(i+1, nodeinfo[i][0], nodeinfo[i][1]));
        }

        Collections.sort(nodes);
        Node root = nodes.get(0);

        for (int i=1; i < nodes.size(); i++) {
            root.addNode(root, nodes.get(i));
        }

        List<Integer> preorderList = new ArrayList<>();
        List<Integer> postorderList = new ArrayList<>();

        preorder(root, preorderList);
        postorder(root, postorderList);

        answer[0] = preorderList.stream().mapToInt(Integer::intValue).toArray();
        answer[1] = postorderList.stream().mapToInt(Integer::intValue).toArray();

        return answer;
    }

    private static void preorder(Node root, List<Integer> preorderList) {
        if (root == null) return;
        preorderList.add(root.id);
        preorder(root.left, preorderList);
        preorder(root.right, preorderList);
    }

    private static void postorder(Node root, List<Integer> postorderList) {
        if (root == null) return;
        postorder(root.left, postorderList);
        postorder(root.right, postorderList);
        postorderList.add(root.id);
    }

    static class Node implements Comparable<Node> {
        int id;
        int x, y;
        Node left = null;
        Node right = null;

        public Node (int id, int x, int y) {
            this.id = id;
            this.x = x;
            this.y = y;
        }

        public void addNode(Node root, Node target) {
            if (target.x < root.x) {
                if (root.left != null) {
                    addNode(root.left, target);
                    return;
                }
                root.left = target;
                return;
            }

            if (root.x < target.x) {
                if (root.right != null) {
                    addNode(root.right, target);
                    return;
                }
                root.right = target;
                return;
            }

        }

        public int compareTo(Node node) {
            if (this.y > node.y) {
                return -1;
            } else if (this.y < node.y) {
                return 1;
            } else {
                return this.x - node.x;
            }
        }
    }
}
