#include <gtest/gtest.h>
#include "../146_lru_cache/variant_146.hpp"

TEST(LRUCache_Variant, Get_MovesNodeToEnd) {
    LRUCache_146_Variant cache;
    cache.put(1, 1);
    cache.put(2, 2);
    cache.put(3, 3);
    
    EXPECT_EQ(1, cache.get(1));
    EXPECT_EQ(1, cache.last());

    EXPECT_EQ(3, cache.get(3));
    EXPECT_EQ(3, cache.last());

    EXPECT_EQ(2, cache.get(2));
    EXPECT_EQ(2, cache.last());
}

TEST(LRUCache_Variant, Put_MovesNodeToEnd) {
    LRUCache_146_Variant cache;
    cache.put(1, 1);
    EXPECT_EQ(1, cache.last());
    EXPECT_EQ(1, cache.get(1));

    cache.put(2, 2);
    EXPECT_EQ(2, cache.get(2));
    EXPECT_EQ(2, cache.last());

    cache.put(3, 3);
    EXPECT_EQ(3, cache.get(3));
    EXPECT_EQ(3, cache.last());
}

TEST(LRUCache_Variant, PutAndGet_DifferentKeyAndValue) {
    LRUCache_146_Variant cache;
    cache.put(1, 1000);
    cache.put(2, 2000);
    cache.put(3, 3000);
    
    EXPECT_EQ(1000, cache.get(1));
    EXPECT_EQ(1000, cache.last());

    EXPECT_EQ(3000, cache.get(3));
    EXPECT_EQ(3000, cache.last());

    EXPECT_EQ(2000, cache.get(2));
    EXPECT_EQ(2000, cache.last());
}

TEST(LRUCache_Variant, GetNotFound_ReturnsNegativeOne) {
    LRUCache_146_Variant cache;
    EXPECT_EQ(-1, cache.get(1));
    EXPECT_EQ(-1, cache.get(1));

    cache.put(1, 1);
    EXPECT_EQ(-1, cache.get(2));

    cache.put(2, 2);
    EXPECT_EQ(-1, cache.get(3));

    cache.put(3, 3);
    EXPECT_EQ(-1, cache.get(4));

    EXPECT_EQ(-1, cache.get(9000));
    
    EXPECT_EQ(1, cache.get(1));
    EXPECT_EQ(1, cache.last());
    EXPECT_EQ(3, cache.get(3));
    EXPECT_EQ(3, cache.last());
    EXPECT_EQ(2, cache.get(2));
    EXPECT_EQ(2, cache.last());
}

TEST(LRUCache_Variant, Put_CreateAndUpdate) {
    LRUCache_146_Variant cache;
    cache.put(1, 1);
    cache.put(2, 2);
    cache.put(3, 3);

    cache.put(1, 1000);
    EXPECT_EQ(1000, cache.last());

    cache.put(2, 2000);
    EXPECT_EQ(2000, cache.last());

    cache.put(3, 3000);
    EXPECT_EQ(3000, cache.last());
}

TEST(LRUCache_Variant, Delete_GetsAndLastsCorrectly) {
    LRUCache_146_Variant cache;
    cache.put(1, 1);
    cache.put(2, 2);
    cache.put(3, 3);
    cache.put(4, 4);
    cache.put(5, 5);
    cache.put(6, 6);
    cache.put(7, 7);
    cache.put(8, 8);

    EXPECT_TRUE(cache.del(8));
    EXPECT_EQ(7, cache.last());
    EXPECT_EQ(7, cache.get(7));

    EXPECT_TRUE(cache.del(7));
    EXPECT_EQ(6, cache.last());
    EXPECT_EQ(6, cache.get(6));

    EXPECT_TRUE(cache.del(6));
    EXPECT_EQ(5, cache.last());
    EXPECT_EQ(5, cache.get(5));

    EXPECT_TRUE(cache.del(5));
    EXPECT_EQ(4, cache.last());
    EXPECT_EQ(4, cache.get(4));

    EXPECT_TRUE(cache.del(4));
    EXPECT_EQ(3, cache.last());
    EXPECT_EQ(3, cache.get(3));

    EXPECT_TRUE(cache.del(3));
    EXPECT_EQ(2, cache.last());
    EXPECT_EQ(2, cache.get(2));

    EXPECT_TRUE(cache.del(2));
    EXPECT_EQ(1, cache.last());
    EXPECT_EQ(1, cache.get(1));

    EXPECT_TRUE(cache.del(1));
    EXPECT_EQ(-1, cache.last());
    EXPECT_EQ(-1, cache.get(1));
}

TEST(LRUCache_Variant, Delete_NotFound_ReturnsFalse) {
    LRUCache_146_Variant cache;
    EXPECT_FALSE(cache.del(9000));

    cache.put(1, 1);
    EXPECT_FALSE(cache.del(9000));

    cache.put(2, 2);
    EXPECT_FALSE(cache.del(9000));

    cache.put(3, 3);
    EXPECT_FALSE(cache.del(9000));

    cache.put(4, 4);
    EXPECT_FALSE(cache.del(9000));
}

TEST(LRUCache_Variant, Last_NotFound_ReturnsNegativeOne) {
    LRUCache_146_Variant cache;
    EXPECT_EQ(-1, cache.last());
    EXPECT_EQ(-1, cache.last());

    cache.put(9000, 9000);
    cache.del(9000);

    EXPECT_EQ(-1, cache.last());
}