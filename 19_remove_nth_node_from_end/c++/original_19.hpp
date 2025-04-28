#include "../../utils/ListNode.hpp"

class Solution_19 {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        auto dummy = new ListNode();
        dummy->next = head;

        auto r = dummy;
        for (int i = 0; i < n; i++)
            r = r->next;

        auto l = dummy;
        while (r->next != nullptr) {
            r = r->next;
            l = l->next;
        }

        l->next = l->next->next;
        return dummy->next;
    }
};