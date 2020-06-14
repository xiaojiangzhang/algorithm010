package week01;

import java.util.LinkedList;
import java.util.ArrayDeque;

import java.util.Deque;

public class Deque_use_addfirst {
    public static void main(String[] args) {
        Deque<String> deque = new LinkedList<>();
        deque.addFirst("a");
        deque.addFirst("b");
        deque.addFirst("c");
        System.out.println(deque);

        System.out.println(deque.peekFirst());
        System.out.println(deque.peekLast());
        System.out.println(deque);
        while (deque.size() > 0) {
            System.out.println(deque.pollFirst());
        }
        System.out.println(deque);
    }
}
