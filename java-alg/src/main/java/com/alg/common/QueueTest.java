package com.alg.common;

import org.junit.Test;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class QueueTest {


    /**
     * build queue with array
     */
    @Test
    public void buildQueueWithArray() {
        int[] array = {1, 2, 3, 4, 5};
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            arr.add(array[i]);
        }
        System.out.println("arr = " + arr);
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < arr.size(); i++) {
            queue.offer(arr.get(i));
        }
    }

}
