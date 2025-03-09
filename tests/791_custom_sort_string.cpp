#include <gtest/gtest.h>
#include "../791_custom_sort_string/variant_791.hpp"

TEST(CustomSortString_FirstVariant, Valid) {
    std::vector<char> order = {'b', 'c', 'a', 'f', 'g'};
    std::string s = "abcd";
    EXPECT_EQ("bcad", customSortString_variant_791(order, s));
}