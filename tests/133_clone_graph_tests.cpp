#include <gtest/gtest.h>
#include "../133_clone_graph/variant_133.hpp"

TEST(CloneGraph_Variant, HappyCase) {
    auto root1 = new Node(1);
    auto node2 = new Node(2);
    auto node3 = new Node(3);
    root1->neighbors.push_back(node2);
    root1->neighbors.push_back(node3);

    node2->neighbors.push_back(root1);
    node2->neighbors.push_back(node3);

    node3->neighbors.push_back(root1);
    node3->neighbors.push_back(node2);

    auto root2 = new Node(4);
    auto node5 = new Node(5);
    root2->neighbors.push_back(node5);
    node5->neighbors.push_back(root2);

    Graph input;
    input.roots.push_back(root1);
    input.roots.push_back(root2);

    Graph output = cloneGraph_133_first_variant(input);
    EXPECT_EQ(2, output.roots.size());
    EXPECT_EQ(root1->val, output.roots[0]->val);
    EXPECT_EQ(root2->val, output.roots[1]->val);

    // Testing the exact nodes in each graph.
    // This is a one-time thing since this is the OG LC problem
    EXPECT_EQ(2, output.roots[0]->neighbors.size());
    Node* first_output_root = output.roots[0];
    EXPECT_EQ(node2->val, first_output_root->neighbors[0]->val);
    EXPECT_EQ(node3->val, first_output_root->neighbors[1]->val);
    Node* node2_output = output.roots[0]->neighbors[0];
    EXPECT_EQ(root1->val, node2_output->neighbors[0]->val);
    EXPECT_EQ(node3->val, node2_output->neighbors[1]->val);
    Node* node3_output = output.roots[0]->neighbors[1];
    EXPECT_EQ(root1->val, node3_output->neighbors[0]->val);
    EXPECT_EQ(node2->val, node3_output->neighbors[1]->val);
    
    EXPECT_EQ(1, output.roots[1]->neighbors.size());
    Node* second_output_root = output.roots[1];
    EXPECT_EQ(node5->val, second_output_root->neighbors[0]->val);
    Node* node5_output = second_output_root->neighbors[0];
    EXPECT_EQ(root2->val, node5_output->neighbors[0]->val);
}

TEST(CloneGraph_Variant, NullptrRoots_Excluded) {
    auto root1 = new Node(1);
    auto node2 = new Node(2);
    auto node3 = new Node(3);
    root1->children.push_back(node2);
    root1->children.push_back(node3);

    node2->children.push_back(root1);
    node2->children.push_back(node3);

    node3->children.push_back(root1);
    node3->children.push_back(node2);

    auto root2 = new Node(4);
    auto node5 = new Node(5);
    root2->children.push_back(node5);
    node5->children.push_back(root2);

    Graph input;
    input.roots.push_back(root1);
    input.roots.push_back(nullptr);
    input.roots.push_back(root2);
    input.roots.push_back(nullptr);
    input.roots.push_back(nullptr);

    Graph output = cloneGraph_133_first_variant(input);
    EXPECT_EQ(2, output.roots.size());
    EXPECT_EQ(root1->val, output.roots[0]->val);
    EXPECT_EQ(root2->val, output.roots[1]->val);
}

TEST(CloneGraph_Variant, AllNullPtrs_Excluded) {
    Graph input;
    input.roots.push_back(nullptr);
    input.roots.push_back(nullptr);
    input.roots.push_back(nullptr);
    input.roots.push_back(nullptr);

    Graph output = cloneGraph_133_first_variant(input);
    EXPECT_TRUE(output.roots.empty());
}

TEST(CloneGraph_Variant, OneGraph_SameAsOG) {
    auto root1 = new Node(1);
    auto node2 = new Node(2);
    auto node3 = new Node(3);
    root1->children.push_back(node2);
    root1->children.push_back(node3);
    node2->children.push_back(root1);
    node2->children.push_back(node3);
    node3->children.push_back(root1);
    node3->children.push_back(node2);

    Graph input;
    input.roots.push_back(root1);

    Graph output = cloneGraph_133_first_variant(input);
    EXPECT_EQ(1, output.roots.size());
    EXPECT_EQ(root1->val, output.roots[0]->val);
}

TEST(CloneGraph_Variant, OneGraph_DoublyLinkedList) {
    auto root1 = new Node(1);
    auto node2 = new Node(2);
    auto node3 = new Node(3);
    root1->children.push_back(node2);
    node2->children.push_back(root1);

    node2->children.push_back(node3);
    node3->children.push_back(node2);

    Graph input;
    input.roots.push_back(root1);

    Graph output = cloneGraph_133_first_variant(input);
    EXPECT_EQ(1, output.roots.size());
    EXPECT_EQ(root1->val, output.roots[0]->val);
}

TEST(CloneGraph_Variant, 5DisconnectedGraphs_EachOneNode) {
    auto root1 = new Node(1);
    auto root2 = new Node(2);
    auto root3 = new Node(3);
    auto root4 = new Node(4);
    auto root5 = new Node(5);

    Graph input;
    input.roots.push_back(root1);
    input.roots.push_back(root2);
    input.roots.push_back(root3);
    input.roots.push_back(root4);
    input.roots.push_back(root5);

    Graph output = cloneGraph_133_first_variant(input);
    EXPECT_EQ(5, output.roots.size());
    EXPECT_EQ(root1->val, output.roots[0]->val);
    EXPECT_EQ(root2->val, output.roots[1]->val);
    EXPECT_EQ(root3->val, output.roots[2]->val);
    EXPECT_EQ(root4->val, output.roots[3]->val);
    EXPECT_EQ(root5->val, output.roots[4]->val);
}

TEST(CloneGraph_Variant, 5DisconnectedGraphs_EachMultipleNodes) {
    auto root1 = new Node(1);
    auto node2 = new Node(2);
    auto node3 = new Node(3);
    root1->children.push_back(node2);
    root1->children.push_back(node3);
    node2->children.push_back(root1);
    node2->children.push_back(node3);
    node3->children.push_back(root1);
    node3->children.push_back(node2);

    auto root2 = new Node(4);
    auto node5 = new Node(5);
    root2->children.push_back(node5);
    node5->children.push_back(root2);

    auto root3 = new Node(6);
    auto node7 = new Node(7);
    auto node8 = new Node(8);
    root3->children.push_back(node7);
    root3->children.push_back(node8);
    node7->children.push_back(node8);
    node7->children.push_back(root3);
    node8->children.push_back(node7);
    node8->children.push_back(root3);

    auto root4 = new Node(9);
    auto node10 = new Node(10);
    root4->children.push_back(node10);
    node10->children.push_back(root4);

    auto root5 = new Node(11);
    auto node12 = new Node(12);
    auto node13 = new Node(13);
    auto node14 = new Node(14);
    root5->children.push_back(node12);
    root5->children.push_back(node14);
    node12->children.push_back(root5);
    node12->children.push_back(node13);
    node13->children.push_back(node12);
    node13->children.push_back(node14);
    node14->children.push_back(root5);
    node14->children.push_back(node13);

    Graph input;
    input.roots.push_back(root1);
    input.roots.push_back(root2);
    input.roots.push_back(root3);
    input.roots.push_back(root4);
    input.roots.push_back(root5);

    Graph output = cloneGraph_133_first_variant(input);
    EXPECT_EQ(5, output.roots.size());
    EXPECT_EQ(root1->val, output.roots[0]->val);
    EXPECT_EQ(root2->val, output.roots[1]->val);
    EXPECT_EQ(root3->val, output.roots[2]->val);
    EXPECT_EQ(root4->val, output.roots[3]->val);
    EXPECT_EQ(root5->val, output.roots[4]->val);
}