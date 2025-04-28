#include "../../utils/ListNode.hpp"

class Solution_19_Variant {
public:
    ListNode* removeIthFromBeginning(ListNode* head, int n) {
        auto dummy = new ListNode();
        dummy->next = head;

        auto i = dummy;
        for (int _i = 0; _i < n; _i++) {
            if (i->next == nullptr)
                return dummy->next;
            i = i->next;
        }

        if (i->next == nullptr)
            return dummy->next;
            
        i->next = i->next->next;
        return dummy->next;
    }
};