#include <gtest/gtest.h>
#include "../23_merge_k_sorted_lists/first_variant_23_integer_arrays.hpp"
#include "../23_merge_k_sorted_lists/second_variant_23_iterator.hpp"

TEST(MergeKSortedLists_FirstVariant, ZeroLists) {
    std::vector<std::vector<int>> lists = {{}};
    Solution_23_First_Variant s;
    EXPECT_EQ(std::vector<int>(), s.mergeKLists(lists));
}

TEST(MergeKSortedLists_FirstVariant, AllNonEmptyLists) {
    std::vector<std::vector<int>> lists = {
        {1, 3},
        {2},
        {4, 5}
    };
    Solution_23_First_Variant s;
    std::vector<int> expected = {1, 2, 3, 4, 5};
    EXPECT_EQ(expected, s.mergeKLists(lists));
}

TEST(MergeKSortedLists_FirstVariant, SomeEmpty_SomeNotEmptyLists) {
    std::vector<std::vector<int>> lists = {
        {},
        {1, 3},
        {},
        {2},
        {4, 5},
        {},
        {},
        {}
    };
    Solution_23_First_Variant s;
    std::vector<int> expected = {1, 2, 3, 4, 5};
    EXPECT_EQ(expected, s.mergeKLists(lists));
}

TEST(MergeKSortedLists_FirstVariant, NegativeNumbersAndZeroes) {
    std::vector<std::vector<int>> lists = {
        {-3, -2, 0, 8, 10},
        {-1, 1, 5, 11},
        {2, 3, 4, 6, 7, 9}
    };
    Solution_23_First_Variant s;
    std::vector<int> expected = {-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
    EXPECT_EQ(expected, s.mergeKLists(lists));
}

TEST(MergeKSortedLists_FirstVariant, NegativeNumbersAndZeroes_AndEmptyLists) {
    std::vector<std::vector<int>> lists = {
        {},{},{},{},{},
        {-3, -2, 0, 8, 10},
        {},{},{},{},{},
        {-1, 1, 5, 11},
        {2, 3, 4, 6, 7, 9},
        {},{},{},{},{}
    };
    Solution_23_First_Variant s;
    std::vector<int> expected = {-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
    EXPECT_EQ(expected, s.mergeKLists(lists));
}

TEST(MergeKSortedLists_FirstVariant, LotsOfLists) {
    std::vector<std::vector<int>> lists = {
        {1, 3, 5, 7, 9, 11, 13},
        {2, 4, 6, 8, 10, 12},
        {0},
        {14, 16, 18, 20},
        {15, 17, 19, 21, 23},
        {500, 1000},
        {250, 750, 1500}
    };
    Solution_23_First_Variant s;
    std::vector<int> expected = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                    15, 16, 17, 18, 19, 20, 21, 23, 250, 500, 750, 1000, 1500};
    EXPECT_EQ(expected, s.mergeKLists(lists));
}

TEST(MergeKSortedLists_FirstVariant, SingleList) {
    std::vector<std::vector<int>> lists = {
        {-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    };
    Solution_23_First_Variant s;
    std::vector<int> expected = {-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    EXPECT_EQ(expected, s.mergeKLists(lists));
}

TEST(MergeKSortedLists_FirstVariant, OneElementLists) {
    std::vector<std::vector<int>> lists = {
        {10}, {9}, {8}, {7}, {6}, {5}, {4}, {3}, {2}, {1}, {0}, {-1}
    };
    Solution_23_First_Variant s;
    std::vector<int> expected = {-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    EXPECT_EQ(expected, s.mergeKLists(lists));
}

TEST(MergeKSortedLists_FirstVariant, DuplicatesAmongLists) {
    std::vector<std::vector<int>> lists = {
        {1, 3, 5, 7, 9, 11, 13},
        {1, 3, 5, 7, 9, 11, 13},
        {1, 3, 5, 7, 9, 11, 13},
        {1, 3, 5, 7, 9, 11, 13},
        {1, 3, 5, 7, 9, 11, 13}
    };
    Solution_23_First_Variant s;
    std::vector<int> expected = {1, 1, 1, 1, 1,
                                3, 3, 3, 3, 3,
                                5, 5, 5, 5, 5,
                                7, 7, 7, 7, 7,
                                9, 9, 9, 9, 9,
                                11, 11, 11, 11, 11,
                                13, 13, 13, 13, 13};
    EXPECT_EQ(expected, s.mergeKLists(lists));

    lists = {
        {1, 3, 5, 7, 9, 11, 13},
        {2, 4, 6},
        {},{},{},{},{},
        {1, 3, 5, 7, 9, 11, 13},
        {2, 4, 6},
        {1000, 1001},
        {},{},{},{},{}
    };
    expected = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 9, 9,
        11, 11, 13, 13, 1000, 1001};
    EXPECT_EQ(expected, s.mergeKLists(lists));
}

//////////////////////////////////////////////////////////////////////
TEST(MergeKSortedLists_SecondVariant, ZeroLists) {
    std::vector<std::vector<int>> lists = {{}};
    Solution_23_Second_Variant s(lists);
    EXPECT_FALSE(s.hasNext());
    EXPECT_THROW(s.next(), std::out_of_range);
    EXPECT_THROW(s.next(), std::out_of_range);
    EXPECT_THROW(s.next(), std::out_of_range);
}

TEST(MergeKSortedLists_SecondVariant, AllNonEmptyLists) {
    std::vector<std::vector<int>> lists = {
        {1, 3},
        {2},
        {4, 5}
    };
    Solution_23_Second_Variant s(lists);
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(1, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(2, s.next());
    EXPECT_EQ(3, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(4, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(5, s.next());
    EXPECT_FALSE(s.hasNext());
    EXPECT_THROW(s.next(), std::out_of_range);
}

TEST(MergeKSortedLists_SecondVariant, SomeEmpty_SomeNotEmptyLists) {
    std::vector<std::vector<int>> lists = {
        {},
        {1, 3},
        {},
        {2},
        {4, 5},
        {},
        {},
        {}
    };
    Solution_23_Second_Variant s(lists);
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(1, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(2, s.next());
    EXPECT_EQ(3, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(4, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(5, s.next());
    EXPECT_FALSE(s.hasNext());
    EXPECT_THROW(s.next(), std::out_of_range);
}

TEST(MergeKSortedLists_SecondVariant, NegativeNumbersAndZeroes) {
    std::vector<std::vector<int>> lists = {
        {-3, -2, 0, 8, 10},
        {-1, 1, 5, 11},
        {2, 3, 4, 6, 7, 9}
    };
    Solution_23_Second_Variant s(lists);
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(-3, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(-2, s.next());
    EXPECT_EQ(-1, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(0, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(1, s.next());
    EXPECT_EQ(2, s.next());
    EXPECT_EQ(3, s.next());
    EXPECT_EQ(4, s.next());
    EXPECT_EQ(5, s.next());
    EXPECT_EQ(6, s.next());
    EXPECT_EQ(7, s.next());
    EXPECT_EQ(8, s.next());
    EXPECT_EQ(9, s.next());
    EXPECT_EQ(10, s.next());
    EXPECT_EQ(11, s.next());
    EXPECT_FALSE(s.hasNext());
    EXPECT_THROW(s.next(), std::out_of_range);
}

TEST(MergeKSortedLists_SecondVariant, NegativeNumbersAndZeroes_AndEmptyLists) {
    std::vector<std::vector<int>> lists = {
        {},{},{},{},{},
        {-3, -2, 0, 8, 10},
        {},{},{},{},{},
        {-1, 1, 5, 11},
        {2, 3, 4, 6, 7, 9},
        {},{},{},{},{}
    };
    Solution_23_Second_Variant s(lists);
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(-3, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(-2, s.next());
    EXPECT_EQ(-1, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(0, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(1, s.next());
    EXPECT_EQ(2, s.next());
    EXPECT_EQ(3, s.next());
    EXPECT_EQ(4, s.next());
    EXPECT_EQ(5, s.next());
    EXPECT_EQ(6, s.next());
    EXPECT_EQ(7, s.next());
    EXPECT_EQ(8, s.next());
    EXPECT_EQ(9, s.next());
    EXPECT_EQ(10, s.next());
    EXPECT_EQ(11, s.next());
    EXPECT_FALSE(s.hasNext());
    EXPECT_THROW(s.next(), std::out_of_range);
}

TEST(MergeKSortedLists_SecondVariant, LotsOfLists) {
    std::vector<std::vector<int>> lists = {
        {1, 3, 5, 7, 9, 11, 13},
        {2, 4, 6, 8, 10, 12},
        {0},
        {14, 16, 18, 20},
        {15, 17, 19, 21, 23},
        {500, 1000},
        {250, 750, 1500}
    };
    Solution_23_Second_Variant s(lists);
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(0, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(1, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(2, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(3, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(4, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(5, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(6, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(7, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(8, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(9, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(10, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(11, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(12, s.next());
    EXPECT_EQ(13, s.next());
    EXPECT_EQ(14, s.next());
    EXPECT_EQ(15, s.next());
    EXPECT_EQ(16, s.next());
    EXPECT_EQ(17, s.next());
    EXPECT_EQ(18, s.next());
    EXPECT_EQ(19, s.next());
    EXPECT_EQ(20, s.next());
    EXPECT_EQ(21, s.next());
    EXPECT_EQ(23, s.next());
    EXPECT_EQ(250, s.next());
    EXPECT_EQ(500, s.next());
    EXPECT_EQ(750, s.next());
    EXPECT_EQ(1000, s.next());
    EXPECT_EQ(1500, s.next());
    EXPECT_FALSE(s.hasNext());
    EXPECT_THROW(s.next(), std::out_of_range);
}

TEST(MergeKSortedLists_SecondVariant, SingleList) {
    std::vector<std::vector<int>> lists = {
        {-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    };
    Solution_23_Second_Variant s(lists);
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(-1, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(0, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(1, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(2, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(3, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(4, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(5, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(6, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(7, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(8, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(9, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(10, s.next());
    EXPECT_FALSE(s.hasNext());
    EXPECT_THROW(s.next(), std::out_of_range);
}

TEST(MergeKSortedLists_SecondVariant, OneElementLists) {
    std::vector<std::vector<int>> lists = {
        {10}, {9}, {8}, {7}, {6}, {5}, {4}, {3}, {2}, {1}, {0}, {-1}
    };
    Solution_23_Second_Variant s(lists);
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(-1, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(0, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(1, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(2, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(3, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(4, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(5, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(6, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(7, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(8, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(9, s.next());
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(10, s.next());
    EXPECT_FALSE(s.hasNext());
    EXPECT_THROW(s.next(), std::out_of_range);
}

TEST(MergeKSortedLists_SecondVariant, DuplicatesAmongLists) {
    std::vector<std::vector<int>> lists = {
        {1, 3, 5, 7, 9, 11, 13},
        {1, 3, 5, 7, 9, 11, 13},
        {1, 3, 5, 7, 9, 11, 13},
        {1, 3, 5, 7, 9, 11, 13},
        {1, 3, 5, 7, 9, 11, 13}
    };
    Solution_23_Second_Variant s(lists);
    EXPECT_TRUE(s.hasNext());
    EXPECT_EQ(1, s.next());
    EXPECT_EQ(1, s.next());
    EXPECT_EQ(1, s.next());
    EXPECT_EQ(1, s.next());
    EXPECT_EQ(1, s.next());
    EXPECT_EQ(3, s.next());
    EXPECT_EQ(3, s.next());
    EXPECT_EQ(3, s.next());
    EXPECT_EQ(3, s.next());
    EXPECT_EQ(3, s.next());
    EXPECT_EQ(5, s.next());
    EXPECT_EQ(5, s.next());
    EXPECT_EQ(5, s.next());
    EXPECT_EQ(5, s.next());
    EXPECT_EQ(5, s.next());
    EXPECT_EQ(7, s.next());
    EXPECT_EQ(7, s.next());
    EXPECT_EQ(7, s.next());
    EXPECT_EQ(7, s.next());
    EXPECT_EQ(7, s.next());
    EXPECT_EQ(9, s.next());
    EXPECT_EQ(9, s.next());
    EXPECT_EQ(9, s.next());
    EXPECT_EQ(9, s.next());
    EXPECT_EQ(9, s.next());
    EXPECT_EQ(11, s.next());
    EXPECT_EQ(11, s.next());
    EXPECT_EQ(11, s.next());
    EXPECT_EQ(11, s.next());
    EXPECT_EQ(11, s.next());
    EXPECT_EQ(13, s.next());
    EXPECT_EQ(13, s.next());
    EXPECT_EQ(13, s.next());
    EXPECT_EQ(13, s.next());
    EXPECT_EQ(13, s.next());
    EXPECT_FALSE(s.hasNext());
    EXPECT_THROW(s.next(), std::out_of_range);

    lists = {
        {1, 3, 5, 7, 9, 11, 13},
        {2, 4, 6},
        {},{},{},{},{},
        {1, 3, 5, 7, 9, 11, 13},
        {2, 4, 6},
        {1000, 1001},
        {},{},{},{},{}
    };
    Solution_23_Second_Variant s2(lists);
    EXPECT_TRUE(s2.hasNext());
    EXPECT_EQ(1, s2.next());
    EXPECT_EQ(1, s2.next());
    EXPECT_EQ(2, s2.next());
    EXPECT_EQ(2, s2.next());
    EXPECT_EQ(3, s2.next());
    EXPECT_EQ(3, s2.next());
    EXPECT_EQ(4, s2.next());
    EXPECT_EQ(4, s2.next());
    EXPECT_EQ(5, s2.next());
    EXPECT_EQ(5, s2.next());
    EXPECT_EQ(6, s2.next());
    EXPECT_EQ(6, s2.next());
    EXPECT_EQ(7, s2.next());
    EXPECT_EQ(7, s2.next());
    EXPECT_EQ(9, s2.next());
    EXPECT_EQ(9, s2.next());
    EXPECT_EQ(11, s2.next());
    EXPECT_EQ(11, s2.next());
    EXPECT_EQ(13, s2.next());
    EXPECT_EQ(13, s2.next());
    EXPECT_EQ(1000, s2.next());
    EXPECT_EQ(1001, s2.next());
    EXPECT_FALSE(s2.hasNext());
    EXPECT_THROW(s2.next(), std::out_of_range);
}