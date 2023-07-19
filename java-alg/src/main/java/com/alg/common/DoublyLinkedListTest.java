package com.alg.common;


import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class DoublyLinkedListTest<T> {



    DoublyLinkedListTest<Integer> list;

    @Before
    public void setup() {
        list = new DoublyLinkedListTest<>();
    }

    @Test
    public void testAdd() {
        list.addFirst(3);
        assertEquals(list.size(), 1);
        list.addFirst(5);
        assertEquals(list.size(), 2);
        list.addLast(1);
        assertEquals(list.size(), 3);
        list.addLast(2);
        assertEquals(list.size(), 4);
        System.out.println("list = " + list);
    }

    @Test
    public void testReverse() {
        testAdd();
        list.reverseList();
    }
    



    private int size = 0;
    private Node<T> head = null;
    private Node<T> tail = null;


    // Add an element to the beginning of this linked list, O(1)
    public void addFirst(T elem) {
        Node<T> node = new Node<>(elem);
        if (0 == size) {
            head = node;
            tail = head;
        } else {
            node.next = head;
            head.prev = node;
            head = node;
        }
        size++;
    }

    // Add a node to the tail of the linked list, O(1)
    public void addLast(T elem) {
        Node<T> node = new Node<>(elem);
        if (0 == size) {
            tail = node;
            head = tail;
        } else {
            tail.next = node;
            node.prev = tail;
            tail = node;
        }
        size++;
    }


    public void reverseList() {
        Node prev = null;
        Node next = null;

        while (head != null) {
            next = head.next;
            head.next = prev;
            head.prev = next;
            prev = head;
            head = next;
        }
        while (prev != null) {
            System.out.printf("%d ", prev.val);
            prev = prev.next;
        }
    }


    public int size() {
        return size;
    }

    private static class Node<T> {
        private T val;
        private Node<T> prev, next;

        public Node(T val) {
            this.val = val;
        }

        public Node(T val, Node<T> prev, Node<T> next) {
            this.val = val;
            this.prev = prev;
            this.next = next;
        }

        @Override
        public String toString() {
            return val.toString();
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[ ");
        Node<T> trav = head;
        while (trav != null) {
            sb.append(trav.val + ", ");
            trav = trav.next;
        }
        sb.append(" ]");

        return sb.toString();
    }

}


