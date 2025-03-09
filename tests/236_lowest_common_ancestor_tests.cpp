#include <gtest/gtest.h>
#include "../236_lowest_common_ancestor/first_variant_236_nary_tree.hpp"

TEST(LowestCommonAncestor_Variant_NAryTree, P_Q_Separate_Subtrees) {
    //       1
    //    /  |  \
    //   2   3   4
    //  / \     / | \
    // 5   6   7  8  9
    Node* root = new Node(1);
    Node* n2 = new Node(2);
    Node* n3 = new Node(3);
    Node* n4 = new Node(4);
    Node* n5 = new Node(5);
    Node* n6 = new Node(6);
    Node* n7 = new Node(7);
    Node* n8 = new Node(8);
    Node* n9 = new Node(9);
    root->children = {n2, n3, n4};
    n2->children = {n5, n6};
    n4->children = {n7, n8, n9};

    // Root as the LCA
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, n5, n7));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, n5, n8));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, n5, n9));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, n6, n7));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, n6, n8));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, n6, n9));

    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, n2, n9));

    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, n2, n4));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, n2, n3));

    // Node 4 as the LCA
    EXPECT_EQ(n4, lowestCommonAncestor_236_variant(root, n7, n8));
    EXPECT_EQ(n4, lowestCommonAncestor_236_variant(root, n7, n9));

    // Node 2 as the LCA
    EXPECT_EQ(n2, lowestCommonAncestor_236_variant(root, n5, n6));
}

TEST(LowestCommonAncestor_Variant_NAryTree, P_Q_Same_Subtrees_Returns_P) {
    //       1
    //    /  |  \
    //   2   3   4
    //  / \     / | \
    // 5   6   7  8  9
    Node* root = new Node(1);
    Node* n2 = new Node(2);
    Node* n3 = new Node(3);
    Node* n4 = new Node(4);
    Node* n5 = new Node(5);
    Node* n6 = new Node(6);
    Node* n7 = new Node(7);
    Node* n8 = new Node(8);
    Node* n9 = new Node(9);
    root->children = {n2, n3, n4};
    n2->children = {n5, n6};
    n4->children = {n7, n8, n9};

    // Root as the LCA
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, root, n2));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, root, n3));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, root, n4));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, root, n5));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, root, n6));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, root, n7));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, root, n8));
    EXPECT_EQ(root, lowestCommonAncestor_236_variant(root, root, n9));

    // Node 4 as the LCA
    EXPECT_EQ(n4, lowestCommonAncestor_236_variant(root, n4, n8));
    EXPECT_EQ(n4, lowestCommonAncestor_236_variant(root, n4, n9));

    // Node 2 as the LCA
    EXPECT_EQ(n2, lowestCommonAncestor_236_variant(root, n2, n6));
}