package com.alg.common;


public class LinkedListTest {
    public static void main(String[] args) {
        LinkedListTest nodeOperation = new LinkedListTest();
        nodeOperation.createNode();
        // nodeOperation.headAdd(10);
        // nodeOperation.tailAdd(11);
        nodeOperation.reverseNode();
    }

    private ListNode head;

    public ListNode createNode() {
        ListNode node = new ListNode(0);
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        head = node;
        node.next = node1;
        node1.next = node2;
        node2.next = node3;
        System.err.println("original node is " + node);
        return node;
    }

    /**
     * add to head
     */
    public void headAdd(int val) {
        ListNode node = new ListNode(val);
        if (null == head) {
            head = node;
        }
        node.next = head;
        head = node;
        System.out.println("head = " + head);
    }

    /**
     * add to tail
     */
    public void tailAdd(int val) {
        ListNode node = new ListNode(val);
        if (null == head) {
            head = node;
        }
        ListNode temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = node;
        System.out.println("head = " + head);
    }

    /**
     * reverse linkedList
     */
    public void reverseNode() {
        ListNode next = null;
        ListNode prev = null;
        while (head != null) {
            next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        head = prev;
        System.out.println("head = " + head);
    }


    static class ListNode {
        public int val;
        public ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }
}
