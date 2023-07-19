package com.alg;


import java.util.ArrayList;

public class LeeCode206 {
    public static void main(String[] args) {
        ArrayList<Object> objects = new ArrayList<>();

    }

    /**
     * 翻转单个链表
     *
     * @param head
     * @return
     */
    static Node reverseList(Node head) {
        if (head == null || head.next == null) {
            return head;
        }
        // 1:初始化两个指针 prev跟curr指针，prev指向头节点，curr指向头节点的下一位
        Node prev = head;
        Node curr = head.next;
        // 2:使用三指针法，反转链表的主体部分
        while (curr != null) {
            Node next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        // 3:修改头节点，将头节点的next指针指向空(防止出现链表回环)
        head.next = null;
        return prev;
    }
}


