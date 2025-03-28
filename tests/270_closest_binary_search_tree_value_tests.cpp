#include <gtest/gtest.h>
#include "../270_closest_binary_search_tree_value/variant_270_integer_target.hpp"

TEST(ClosestBSTValue_Variant, ExactMatch) {
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right = new TreeNode(5);

    Solution_270_Variant s;
    EXPECT_EQ(1, s.closestValue(root, 1));
    EXPECT_EQ(2, s.closestValue(root, 2));
    EXPECT_EQ(3, s.closestValue(root, 3));
    EXPECT_EQ(4, s.closestValue(root, 4));
    EXPECT_EQ(5, s.closestValue(root, 5));
}

TEST(ClosestBSTValue_Variant, GreaterTargetThanNodes) {
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right = new TreeNode(6);
    root->right->left = new TreeNode(5);
    root->right->right = new TreeNode(7);

    Solution_270_Variant s;
    EXPECT_EQ(7, s.closestValue(root, 8));
    EXPECT_EQ(7, s.closestValue(root, 9));
    EXPECT_EQ(7, s.closestValue(root, 10));
    EXPECT_EQ(7, s.closestValue(root, 9000));
}

TEST(ClosestBSTValue_Variant, LowerTargetThanNodes) {
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right = new TreeNode(6);
    root->right->left = new TreeNode(5);
    root->right->right = new TreeNode(7);

    Solution_270_Variant s;
    EXPECT_EQ(1, s.closestValue(root, 0));
    EXPECT_EQ(1, s.closestValue(root, -1));
    EXPECT_EQ(1, s.closestValue(root, -2));
    EXPECT_EQ(1, s.closestValue(root, -9000));
}

TEST(ClosestBSTValue_Variant, InBetweenTarget) {
    TreeNode* root = new TreeNode(50);
    root->left = new TreeNode(22);
    root->left->left = new TreeNode(10);
    root->left->right = new TreeNode(48);
    root->right = new TreeNode(9000);

    Solution_270_Variant s;
    EXPECT_EQ(50, s.closestValue(root, 55));
    EXPECT_EQ(50, s.closestValue(root, 70));
    EXPECT_EQ(50, s.closestValue(root, 1000));
    EXPECT_EQ(50, s.closestValue(root, 3000));

    EXPECT_EQ(9000, s.closestValue(root, 9000));
    EXPECT_EQ(9000, s.closestValue(root, 9500));
    EXPECT_EQ(9000, s.closestValue(root, 9888));
    EXPECT_EQ(9000, s.closestValue(root, 10000));
    EXPECT_EQ(9000, s.closestValue(root, 11000));
    EXPECT_EQ(9000, s.closestValue(root, 8000));
    EXPECT_EQ(9000, s.closestValue(root, 7500));

    EXPECT_EQ(22, s.closestValue(root, 30));
    EXPECT_EQ(22, s.closestValue(root, 25));
    EXPECT_EQ(22, s.closestValue(root, 21));

    EXPECT_EQ(10, s.closestValue(root, 10));
    EXPECT_EQ(10, s.closestValue(root, -10));

    // Ties between nodes 48 and 50, so we go with the smaller value, the 48
    EXPECT_EQ(48, s.closestValue(root, 49));
    EXPECT_EQ(48, s.closestValue(root, 48));
    EXPECT_EQ(48, s.closestValue(root, 39));
}