import javax.swing.tree.TreeNode;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class PostorderTraversalIterative {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        
        if (root == null) {
            return result;
        }
        
        Stack<TreeNode> st = new Stack<TreeNode>();
        st.push(root);
        
        while (!st.isEmpty()) {
            TreeNode r = st.pop();
            result.add(0, r.val);
            
            if (r.left != null) {
                st.push(r.left);
            }
            if (r.right != null) {
                st.push(r.right);
            }
        }
        return result;
        
    }
}
