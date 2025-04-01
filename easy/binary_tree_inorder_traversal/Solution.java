package easy.binary_tree_inorder_traversal;

import java.util.ArrayList;
import java.util.List;

import data_structures.TreeNode;
import java.util.List;

public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {

        if (root == null) {
            return x;
        }

    }

    public static void main(String args[]) {
        System.out.println("Hello world");

        Solution s = new Solution();

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(8);
        root.right.right.left = new TreeNode(6);
        root.right.right.left.left = new TreeNode(7);
        root.right.right.left.right = new TreeNode(9);

        // System.out.println(s.inorderTraversal(root));
        System.out.println(s.inorderTraversal(null));
    }
}
