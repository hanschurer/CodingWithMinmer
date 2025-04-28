#include <gtest/gtest.h>
#include "../19_remove_nth_node_from_end/c++/variant_19_ith_from_beginning.hpp"

TEST(Remove_Ith_From_Beginning_Variant, Ith_MiddleNodes_ReturnsHead) {
    // 1 --> 2 --> 3 --> nullptr
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    
    Solution_19_Variant s;
    ListNode* result = s.removeIthFromBeginning(head, 0);
    ASSERT_EQ(2, result->val);
    ASSERT_EQ(3, result->next->val);
    ASSERT_EQ(nullptr, result->next->next);

    result = s.removeIthFromBeginning(head, 1);
    ASSERT_EQ(1, result->val);
    ASSERT_EQ(3, result->next->val);
    ASSERT_EQ(nullptr, result->next->next);
}

TEST(Remove_Ith_From_Beginning_Variant, Remove_LastNode_ReturnsHead) {
    // 1 --> 2 --> 3 --> nullptr
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    
    Solution_19_Variant s;
    ListNode* result = s.removeIthFromBeginning(head, 2);
    ASSERT_EQ(1, result->val);
    ASSERT_EQ(2, result->next->val);
    ASSERT_EQ(nullptr, result->next->next);
}

TEST(Remove_Ith_From_Beginning_Variant, Remove_OOBNode_RemovesNothing_ReturnsHead) {
    // 1 --> 2 --> 3 --> 4 --> nullptr
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    
    Solution_19_Variant s;
    ListNode* result = s.removeIthFromBeginning(head, 4);
    ASSERT_EQ(1, result->val);
    ASSERT_EQ(2, result->next->val);
    ASSERT_EQ(3, result->next->next->val);
    ASSERT_EQ(4, result->next->next->next->val);
    ASSERT_EQ(nullptr, result->next->next->next->next);

    result = s.removeIthFromBeginning(head, 5);
    ASSERT_EQ(1, result->val);
    ASSERT_EQ(2, result->next->val);
    ASSERT_EQ(3, result->next->next->val);
    ASSERT_EQ(4, result->next->next->next->val);
    ASSERT_EQ(nullptr, result->next->next->next->next);

    result = s.removeIthFromBeginning(head, 6);
    ASSERT_EQ(1, result->val);
    ASSERT_EQ(2, result->next->val);
    ASSERT_EQ(3, result->next->next->val);
    ASSERT_EQ(4, result->next->next->next->val);
    ASSERT_EQ(nullptr, result->next->next->next->next);

    result = s.removeIthFromBeginning(head, 9000);
    ASSERT_EQ(1, result->val);
    ASSERT_EQ(2, result->next->val);
    ASSERT_EQ(3, result->next->next->val);
    ASSERT_EQ(4, result->next->next->next->val);
    ASSERT_EQ(nullptr, result->next->next->next->next);
}

TEST(Remove_Ith_From_Beginning_Variant, NullptrHead_ReturnsNullptr) {
    ListNode* head = nullptr;
    Solution_19_Variant s;
    ListNode* result = s.removeIthFromBeginning(head, 0);
    ASSERT_EQ(nullptr, result);

    result = s.removeIthFromBeginning(head, 1);
    ASSERT_EQ(nullptr, result);

    result = s.removeIthFromBeginning(head, 2);
    ASSERT_EQ(nullptr, result);

    result = s.removeIthFromBeginning(head, 9000);
    ASSERT_EQ(nullptr, result);
}