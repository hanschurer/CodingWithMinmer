#include <gtest/gtest.h>
#include "../348_tic_tac_toe/348_variant_is_win.hpp"

TEST(TicTacToe_Variant, Rows) {
    std::vector<std::vector<int>> board = {
        {1, 1, 0},
        {2, 2, 0},
        {0, 0, 0}
    };
    EXPECT_TRUE(isWin_348_Variant(board, 1, 0, 2)); // Player integer 1 wins
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 2)); // Player integer 1 doesn't win
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 0));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 2));

    EXPECT_TRUE(isWin_348_Variant(board, 2, 1, 2)); // Player integer 2 wins
    EXPECT_FALSE(isWin_348_Variant(board, 2, 0, 2)); // Player integer 2 doesn't win
    EXPECT_FALSE(isWin_348_Variant(board, 2, 2, 0));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 2, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 2, 2));

    board = {
        {1, 0, 1},
        {0, 0, 0},
        {0, 2, 2}
    };
    EXPECT_TRUE(isWin_348_Variant(board, 1, 0, 1)); // Player integer 1 wins
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 0)); // Player integer 1 doesn't win
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 0));

    EXPECT_TRUE(isWin_348_Variant(board, 2, 2, 0)); // Player integer 2 wins
    EXPECT_FALSE(isWin_348_Variant(board, 2, 0, 1)); // Player integer 2 doesn't win
    EXPECT_FALSE(isWin_348_Variant(board, 2, 1, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 1, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 1, 0));
}

TEST(TicTacToe_Variant, Cols) {
    std::vector<std::vector<int>> board = {
        {1, 0, 0},
        {1, 2, 0},
        {0, 2, 0}
    };
    EXPECT_TRUE(isWin_348_Variant(board, 1, 2, 0)); // Player integer 1 wins
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 1)); // Player integer 1 doesn't win
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 2));

    EXPECT_TRUE(isWin_348_Variant(board, 2, 0, 1)); // Player integer 2 wins
    EXPECT_FALSE(isWin_348_Variant(board, 2, 2, 1)); // Player integer 2 doesn't win
    EXPECT_FALSE(isWin_348_Variant(board, 2, 0, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 1, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 2, 2));

    board = {
        {0, 0, 1},
        {0, 0, 0},
        {0, 0, 1}
    };
    EXPECT_TRUE(isWin_348_Variant(board, 1, 1, 2)); // Player integer 1 wins
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 0)); // Player integer 1 doesn't win
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 0));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 0));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 1));
}

TEST(TicTacToe_Variant, Diagonals) {
    std::vector<std::vector<int>> board = {
        {1, 0, 0},
        {2, 1, 0},
        {0, 2, 0}
    };
    EXPECT_TRUE(isWin_348_Variant(board, 1, 2, 2)); // Player integer 1 wins
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 1)); // Player integer 1 doesn't win
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 0));

    board = {
        {1, 2, 1},
        {2, 0, 0},
        {2, 0, 1}
    };
    EXPECT_TRUE(isWin_348_Variant(board, 1, 1, 1)); // Player integer 1 wins
    EXPECT_TRUE(isWin_348_Variant(board, 1, 1, 2)); // Player integer 1 wins
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 1));
}

TEST(TicTacToe_Variant, Antidiagonals) {
    std::vector<std::vector<int>> board = {
        {0, 0, 1},
        {2, 1, 2},
        {0, 2, 0}
    };
    EXPECT_TRUE(isWin_348_Variant(board, 1, 2, 0)); // Player integer 1 wins
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 0)); // Player integer 1 doesn't win
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 2));
}
// Should not be valid input
TEST(TicTacToe_Variant, 4By4Matrix_Antidiagonals) {
    std::vector<std::vector<int>> board = {
        {2, 0, 1, 1},
        {2, 1, 1, 0},
        {0, 0, 0, 2},
        {1, 0, 2, 2}
    };
    EXPECT_TRUE(isWin_348_Variant(board, 1, 2, 1)); // Player integer 1 wins
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 1)); // Player integer 1 doesn't win
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 3));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 0));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 3, 1));
}

// Should not be valid input
TEST(TicTacToe_Variant, EmptyBoard) {
    std::vector<std::vector<int>> board = {
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    };
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 0));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 0, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 0));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 1, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 0));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 1, 2, 2));

    EXPECT_FALSE(isWin_348_Variant(board, 2, 0, 0));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 0, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 0, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 1, 0));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 1, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 1, 2));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 2, 0));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 2, 1));
    EXPECT_FALSE(isWin_348_Variant(board, 2, 2, 2));
}
// Should not be valid input
TEST(TicTacToe_Variant, AllPlayer1_ReturnsTrue) {
    std::vector<std::vector<int>> board = {
        {1, 1, 1},
        {1, 1, 1},
        {1, 1, 1}
    };
    EXPECT_TRUE(isWin_348_Variant(board, 1, 0, 0));
    EXPECT_TRUE(isWin_348_Variant(board, 1, 0, 1));
    EXPECT_TRUE(isWin_348_Variant(board, 1, 0, 2));
    EXPECT_TRUE(isWin_348_Variant(board, 1, 1, 0));
    EXPECT_TRUE(isWin_348_Variant(board, 1, 1, 1));
    EXPECT_TRUE(isWin_348_Variant(board, 1, 1, 2));
    EXPECT_TRUE(isWin_348_Variant(board, 1, 2, 0));
    EXPECT_TRUE(isWin_348_Variant(board, 1, 2, 1));
    EXPECT_TRUE(isWin_348_Variant(board, 1, 2, 2));

    board = {
        {2, 2, 2},
        {2, 2, 2},
        {2, 2, 2}
    };
    EXPECT_TRUE(isWin_348_Variant(board, 2, 0, 0));
    EXPECT_TRUE(isWin_348_Variant(board, 2, 0, 1));
    EXPECT_TRUE(isWin_348_Variant(board, 2, 0, 2));
    EXPECT_TRUE(isWin_348_Variant(board, 2, 1, 0));
    EXPECT_TRUE(isWin_348_Variant(board, 2, 1, 1));
    EXPECT_TRUE(isWin_348_Variant(board, 2, 1, 2));
    EXPECT_TRUE(isWin_348_Variant(board, 2, 2, 0));
    EXPECT_TRUE(isWin_348_Variant(board, 2, 2, 1));
    EXPECT_TRUE(isWin_348_Variant(board, 2, 2, 2));
}