#include <gtest/gtest.h>
#include "../987_vertical_order_traversal_of_a_binary_tree/second_variant_987_return_one_list.hpp"
#include "../987_vertical_order_traversal_of_a_binary_tree/first_variant_987_print_order.hpp"

TEST(VerticalTraversalOrder_FirstVariant, TiedByValue) {
    TreeNode* root = new TreeNode(6);
    root->left = new TreeNode(8);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(15);
    root->left->left->right = new TreeNode(1);

    root->right = new TreeNode(7);
    root->right->right = new TreeNode(9);
    root->right->left = new TreeNode(10);
    Solution_987_First_Variant s;
    s.verticalTraversal(root);
    // Expected is 3
    // 8, 1
    // 6, 10, 15
    // 7
    // 9
    std::cout << '\n';

    // Leetcode Example 2
    root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right = new TreeNode(3);
    root->right->right = new TreeNode(7);
    root->right->left = new TreeNode(6);
    s.verticalTraversal(root);
    // Expected is 4
    // 2
    // 1, 5, 6
    // 3
    // 7
    std::cout << '\n';

    // Leetcode Example 3
    root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(6);
    root->right = new TreeNode(3);
    root->right->right = new TreeNode(7);
    root->right->left = new TreeNode(5);
    s.verticalTraversal(root);
    // Expected is 4
    // 2
    // 1, 5, 6
    // 3
    // 7
    std::cout << '\n';
}

TEST(VerticalTraversalOrder_FirstVariant, SortedByColRowOnly) {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->right = new TreeNode(7);
    root->right->left = new TreeNode(15);

    Solution_987_First_Variant s;
    s.verticalTraversal(root);
    // Expected is 9
    // 3, 15
    // 20
    // 7
    std::cout << '\n';
}

TEST(VerticalTraversalOrder_FirstVariant, OneNode) {
    TreeNode* root = new TreeNode(1);
    Solution_987_First_Variant s;
    s.verticalTraversal(root);
    // Expected is 1
    std::cout << '\n';
}

/////////////////////////////////////////////////////////////////////////////
TEST(VerticalTraversalOrder_SecondVariant, TiedByValue) {
    TreeNode* root = new TreeNode(6);
    root->left = new TreeNode(8);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(15);
    root->left->left->right = new TreeNode(1);

    root->right = new TreeNode(7);
    root->right->right = new TreeNode(9);
    root->right->left = new TreeNode(10);
    std::vector<int> expected = {3, 8, 1, 6, 10, 15, 7, 9};
    Solution_987_Second_Variant s;
    EXPECT_EQ(expected, s.verticalTraversal(root));

    // Leetcode Example 2
    root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right = new TreeNode(3);
    root->right->right = new TreeNode(7);
    root->right->left = new TreeNode(6);
    expected = {4, 2, 1, 5, 6, 3, 7};
    EXPECT_EQ(expected, s.verticalTraversal(root));

    // Leetcode Example 3
    root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(6);
    root->right = new TreeNode(3);
    root->right->right = new TreeNode(7);
    root->right->left = new TreeNode(5);
    expected = {4, 2, 1, 5, 6, 3, 7};
    EXPECT_EQ(expected, s.verticalTraversal(root));
}

TEST(VerticalTraversalOrder_SecondVariant, SortedByColRowOnly) {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->right = new TreeNode(7);
    root->right->left = new TreeNode(15);

    std::vector<int> expected = {9, 3, 15, 20, 7};
    Solution_987_Second_Variant s;
    EXPECT_EQ(expected, s.verticalTraversal(root));
}

TEST(VerticalTraversalOrder_SecondVariant, OneNode) {
    TreeNode* root = new TreeNode(1);
    std::vector<int> expected = {1};
    Solution_987_Second_Variant s;
    EXPECT_EQ(expected, s.verticalTraversal(root));
}
