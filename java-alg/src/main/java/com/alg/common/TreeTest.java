package com.alg.common;

import org.junit.Test;

import java.util.LinkedList;
import java.util.Queue;


public class TreeTest {

    /**
     * {array, linkedList, stack, queue} these are all linear data structures.
     * binary tree:
     * 1): maximum nodes: 2^(h+1)-1, if height of the tree is 4(3+1), we will have 2^4 - 1 = 15 nodes tops
     * 2): maximum height: log_2_(n+1)-1, if there are 15 nodes, we will have log_2_16-1=4-1=3
     * 3): maximum height: log_2_15 = 3.906891 = ⌊3.906891⌋ = 3
     * <p>
     * best o(log2n) = o(log n)
     * worst o(n)
     */

    BinaryTreeNode tree = null;

    //
    // if we want to keep the time complexity o(log n), then we have to make tree balanced
    //

    /**
     * breadth-search first
     */
    @Test
    public void BFS() {
        createNodeWithLetters();
        Queue<BinaryTreeNode> queue = new LinkedList<>();
        queue.add(tree);
        while (!queue.isEmpty()) {
            BinaryTreeNode current = queue.peek();
            System.out.print(current.val);
            if (null != current.left)
                queue.add(current.left);
            if (null != current.right)
                queue.add(current.right);
            queue.poll();
        }
    }

    /**
     * depth-search first
     */
    @Test
    public void DFSPreOrder() {

    }

    /**
     * check if a given binary tree is BST
     */
    @Test
    public void checkBST() {

    }

    @Test
    public void deleteNode() {

    }

    @Test
    public void findInorderSuccessor() {

    }

    /**
     * first shift to the parent node of last element,then add node
     */
    public void insert(int val) {
        BinaryTreeNode curr = tree;
        BinaryTreeNode parent = null;
        while (null != curr) {
            parent = curr;
            if (val <= Integer.parseInt(curr.val.toString())) {
                curr = curr.left;
            } else {
                curr = curr.right;
            }
        }
        if (null == tree) {
            tree = new BinaryTreeNode(val);
        } else if (val <= Integer.parseInt(parent.val.toString())) {
            parent.left = new BinaryTreeNode(val);
        } else {
            parent.right = new BinaryTreeNode(val);
        }
    }

    @Test
    public void finMinVal() {
        testInsertInt();
        BinaryTreeNode curr = tree;
        BinaryTreeNode parent = null;
        while (null != curr) {
            parent = curr;
            curr = curr.left;
        }
        System.out.println("Min " + parent.val);
    }

    @Test
    public void finMaxVal() {
        testInsertInt();
        BinaryTreeNode curr = tree;
        BinaryTreeNode parent = null;
        while (null != curr) {
            parent = curr;
            curr = curr.right;
        }
        System.out.println("Max " + parent.val);
    }

    @Test
    public void testInsertInt() {
        insert(5);
        insert(3);
        insert(2);
        insert(1);
        insert(6);
        insert(7);
        insert(8);
        System.out.println("tree = " + tree);
    }

    @Test
    public void createNodeWithLetters() {
        BinaryTreeNode<String> F = new BinaryTreeNode<>("F");
        BinaryTreeNode<String> D = new BinaryTreeNode<>("D");
        BinaryTreeNode<String> J = new BinaryTreeNode<>("J");
        BinaryTreeNode<String> B = new BinaryTreeNode<>("B");
        BinaryTreeNode<String> E = new BinaryTreeNode<>("E");
        BinaryTreeNode<String> G = new BinaryTreeNode<>("G");
        BinaryTreeNode<String> K = new BinaryTreeNode<>("K");
        BinaryTreeNode<String> A = new BinaryTreeNode<>("A");
        BinaryTreeNode<String> C = new BinaryTreeNode<>("C");
        BinaryTreeNode<String> I = new BinaryTreeNode<>("I");
        BinaryTreeNode<String> H = new BinaryTreeNode<>("H");
        F.left = D;
        F.right = J;
        D.left = B;
        D.right = E;
        J.left = G;
        J.right = K;
        B.left = A;
        B.right = C;
        G.right = I;
        I.left = H;
        tree = F;
        System.out.println("F = " + F);
    }

    private static class BinaryTreeNode<T> {
        T val;
        BinaryTreeNode left;
        BinaryTreeNode right;

        public BinaryTreeNode(T val) {
            this.val = val;
        }

        @Override
        public String toString() {
            return "{" + "val=" + val + ", left=" + left + ", right=" + right + '}';
        }
    }

    @Override
    public String toString() {
        return "TreeTest{" + "tree=" + tree + '}';
    }
}
