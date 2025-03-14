#include <gtest/gtest.h>
#include "../1091_shortest_path_in_binary_matrix/first_variant_1091_return_shortest_path.hpp"
#include "../1091_shortest_path_in_binary_matrix/second_variant_1091_return_single_path.hpp"

TEST(ShortestPath_FirstVariant, OneMove) {
    std::vector<std::vector<int>> grid = {{0, 1},{1, 0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {1, 1}};
    Solution_1091_First_Variant s;
    EXPECT_EQ(expected, s.shortestPathBinaryMatrix(grid));
}

TEST(ShortestPath_FirstVariant, ThreeMoves) {
    std::vector<std::vector<int>> grid = {{0, 0, 0},
                                          {1, 1, 0},
                                          {1, 1, 0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {0, 1}, {1, 2}, {2, 2}};
    Solution_1091_First_Variant s;
    EXPECT_EQ(expected, s.shortestPathBinaryMatrix(grid));
}
TEST(ShortestPath_FirstVariant, OnlyDiagonalPath) {
    std::vector<std::vector<int>> grid = {{0, 1, 1, 1},
                                          {1, 0, 1, 1},
                                          {1, 1, 0, 1},
                                          {1, 1, 1, 0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {1, 1}, {2, 2}, {3, 3}};
    Solution_1091_First_Variant s;
    EXPECT_EQ(expected, s.shortestPathBinaryMatrix(grid));
}
TEST(ShortestPath_FirstVariant, PrioritizeShorterDiagonalPath) {
    std::vector<std::vector<int>> grid = {{0, 0, 0, 0},
                                          {0, 0, 1, 0},
                                          {0, 1, 0, 0},
                                          {0, 0, 0, 0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {1, 1}, {2, 2}, {3, 3}};
    Solution_1091_First_Variant s;
    EXPECT_EQ(expected, s.shortestPathBinaryMatrix(grid));
}
TEST(ShortestPath_FirstVariant, SingleRow) {
    std::vector<std::vector<int>> grid = {{0, 0, 0, 0, 0, 0, 0, 0, 0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {0, 1}, {0, 2}, {0, 3}, {0, 4}, {0, 5}, {0, 6}, {0, 7}, {0, 8}};
    Solution_1091_First_Variant s;
    EXPECT_EQ(expected, s.shortestPathBinaryMatrix(grid));
}

TEST(ShortestPath_FirstVariant, SingleColumn) {
    std::vector<std::vector<int>> grid = {{0}, 
                                          {0}, 
                                          {0}, 
                                          {0}, 
                                          {0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {1, 0}, {2, 0}, {3, 0}, {4, 0}};
    Solution_1091_First_Variant s;
    EXPECT_EQ(expected, s.shortestPathBinaryMatrix(grid));
}

TEST(ShortestPath_FirstVariant, TopLeftIsOne_NotPossible) {
    std::vector<std::vector<int>> grid = {{1, 0, 0},
                                          {1, 1, 0},
                                          {1, 1, 0}};
    Solution_1091_First_Variant s;
    EXPECT_TRUE(s.shortestPathBinaryMatrix(grid).empty());
}
TEST(ShortestPath_FirstVariant, BottomRightIsOne_NotPossible) {
    std::vector<std::vector<int>> grid = {{0, 0, 0},
                                          {1, 1, 0},
                                          {1, 1, 1}};
    Solution_1091_First_Variant s;
    EXPECT_TRUE(s.shortestPathBinaryMatrix(grid).empty());
}
TEST(ShortestPath_FirstVariant, PathNotPossible) {
    std::vector<std::vector<int>> grid = {{0, 0, 0},
                                          {1, 1, 1},
                                          {0, 0, 0}};
    Solution_1091_First_Variant s;
    EXPECT_TRUE(s.shortestPathBinaryMatrix(grid).empty());
}

//////////////////////////////////////////////////////////////////////////////////////////
TEST(ReturnSinglePathDfs_SecondVariant, OneMove) {
    std::vector<std::vector<int>> grid = {{0, 1},{1, 0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {1, 1}};
    Solution_1091_Second_Variant s;
    EXPECT_EQ(expected, s.pathBinaryMatrix(grid));
}

TEST(ReturnSinglePathDfs_SecondVariant, ThreeMoves) {
    std::vector<std::vector<int>> grid = {{0, 0, 0},
                                          {1, 1, 0},
                                          {1, 1, 0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {0, 1}, {0, 2}, {1, 2}, {2, 2}};
    Solution_1091_Second_Variant s;
    EXPECT_EQ(expected, s.pathBinaryMatrix(grid));
}
TEST(ReturnSinglePathDfs_SecondVariant, OnlyDiagonalPath) {
    std::vector<std::vector<int>> grid = {{0, 1, 1, 1},
                                          {1, 0, 1, 1},
                                          {1, 1, 0, 1},
                                          {1, 1, 1, 0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {1, 1}, {2, 2}, {3, 3}};
    Solution_1091_Second_Variant s;
    EXPECT_EQ(expected, s.pathBinaryMatrix(grid));
}
TEST(ReturnSinglePathDfs_SecondVariant, ReturnsOnePath) {
    // We take the top right to bottom right path because that's the order in which we defined the 'directions' variable
    std::vector<std::vector<int>> grid = {{0, 0, 0, 0},
                                          {0, 0, 1, 0},
                                          {0, 1, 0, 0},
                                          {0, 0, 0, 0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {0, 1}, {0, 2}, {0, 3}, {1, 3}, {2, 3}, {3, 3}};
    Solution_1091_Second_Variant s;
    EXPECT_EQ(expected, s.pathBinaryMatrix(grid));

    // We don't take the shortest path here.
    grid = {{0, 1, 1, 0},
            {0, 0, 1, 1},
            {0, 1, 1, 0},
            {0, 0, 0, 0}};
    expected = {{0, 0}, {1, 1}, {2, 0}, {3, 1}, {3, 2}, {2, 3}, {3, 3}};
    EXPECT_EQ(expected, s.pathBinaryMatrix(grid));
}
TEST(ReturnSinglePathDfs_SecondVariant, BacktrackOnDeadend) {
    std::vector<std::vector<int>> grid = {{0, 0, 1, 0, 0, 1},
                                          {1, 0, 0, 1, 1, 1},
                                          {0, 0, 1, 1, 1, 1},
                                          {0, 0, 0, 0, 0, 0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {0, 1}, {1, 2}, {2, 1}, {1, 1}, {2, 0}, {3, 1}, {3, 2}, {3, 3}, {3, 4}, {3, 5}};
    Solution_1091_Second_Variant s;
    EXPECT_EQ(expected, s.pathBinaryMatrix(grid));
}
TEST(ReturnSinglePathDfs_SecondVariant, SingleRow) {
    std::vector<std::vector<int>> grid = {{0, 0, 0, 0, 0, 0, 0, 0, 0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {0, 1}, {0, 2}, {0, 3}, {0, 4}, {0, 5}, {0, 6}, {0, 7}, {0, 8}};
    Solution_1091_Second_Variant s;
    EXPECT_EQ(expected, s.pathBinaryMatrix(grid));
}

TEST(ReturnSinglePathDfs_SecondVariant, SingleColumn) {
    std::vector<std::vector<int>> grid = {{0}, 
                                          {0}, 
                                          {0}, 
                                          {0}, 
                                          {0}};
    std::vector<std::vector<int>> expected = {{0, 0}, {1, 0}, {2, 0}, {3, 0}, {4, 0}};
    Solution_1091_Second_Variant s;
    EXPECT_EQ(expected, s.pathBinaryMatrix(grid));
}

TEST(ReturnSinglePathDfs_SecondVariant, TopLeftIsOne_NotPossible) {
    std::vector<std::vector<int>> grid = {{1, 0, 0},
                                          {1, 1, 0},
                                          {1, 1, 0}};
    Solution_1091_Second_Variant s;
    EXPECT_TRUE(s.pathBinaryMatrix(grid).empty());
}
TEST(ReturnSinglePathDfs_SecondVariant, BottomRightIsOne_NotPossible) {
    std::vector<std::vector<int>> grid = {{0, 0, 0},
                                          {1, 1, 0},
                                          {1, 1, 1}};
    Solution_1091_Second_Variant s;
    EXPECT_TRUE(s.pathBinaryMatrix(grid).empty());
}
TEST(ReturnSinglePathDfs_SecondVariant, PathNotPossible) {
    std::vector<std::vector<int>> grid = {{0, 0, 0},
                                          {1, 1, 1},
                                          {0, 0, 0}};
    Solution_1091_Second_Variant s;
    EXPECT_TRUE(s.pathBinaryMatrix(grid).empty());
}