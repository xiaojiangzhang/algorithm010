
import java.util.LinkedList;//给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
//
// 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
//
// 
//
// 示例: 
//
// 给定 1->2->3->4, 你应该返回 2->1->4->3.
// Related Topics 链表
//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) { val = x; }
 * }
 */
class Solution {
    /*
    * 1、递归求解：
    * 举例子说明，老师和同学玩游戏，同学们站成一排，依次是小明，小红，小王等等等。
    老师把玩法告诉小明，于是聪明的小明决定和小红互换位置，然后把玩法告诉小王，然后小王又和小明做一样的事。。。。。。
    时间复杂度：O(N)，其中 NN 指的是链表的节点数量。
    空间复杂度：O(N)，递归过程使用的堆栈空间。
      2、迭代求解：
      我们把链表分为两部分，即奇数节点为一部分，偶数节点为一部分，A 指的是交换节点中的前面的节点，B 指的是要交换节点中的后面的节点。在完成它们的交换，我们还得用 prevNode 记录 A 的前驱节点。
    算法：
    firstNode（即 A） 和 secondNode（即 B） 分别遍历偶数节点和奇数节点，即两步看作一步。
    交换两个节点：
     firstNode.next = secondNode.next
     secondNode.next = firstNode
    还需要更新 prevNode.next 指向交换后的头。
    prevNode.next = secondNode
    时间复杂度：O(N)，其中 NN 指的是链表的节点数量。
    空间复杂度：O(N)，递归过程使用的堆栈空间。
    * */
    public ListNode swapPairs1(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode firstNode = head;
        ListNode secondNode = head.next;
        firstNode.next = swapPairs(secondNode.next);
        secondNode.next = firstNode;
        return secondNode;
    }
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode prevNode = dummy;
        while (head != null && head.next != null) {
            ListNode first = head;
            ListNode second = head.next;
            prevNode.next = second;
            first.next = second.next;
            second.next = first;
            prevNode = first;
            head = first.next;
        }
        return dummy.next;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
