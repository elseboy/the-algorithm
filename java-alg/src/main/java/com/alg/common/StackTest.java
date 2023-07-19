package com.alg.common;


import org.junit.Test;

import java.util.Stack;

public class StackTest {

    /**
     * create a stack with arrayList o(n)
     **/
    @Test
    public void createStackWithList() {
        Stack<Object> stack = new Stack<>();
        String str = "abcdefg";
        for (int i = 0; i < str.length(); i++) {
            stack.push(str.charAt(i));
        }
        System.out.println("stack = " + stack);
        System.out.println("stack.peek() = " + stack.peek());
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            builder.append(stack.pop());
        }
        System.out.println("builder = " + builder);
    }

    /**
     * prefix infix postfix
     * +23    2+3   23+
     **/
}