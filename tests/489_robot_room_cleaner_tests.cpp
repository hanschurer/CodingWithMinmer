#include <gtest/gtest.h>
#include "../489_robot_room_cleaner/variant_489_mouse_and_cheese.hpp"

TEST(MouseCheeseVariant_489, HappyCase_NoObstacles) {
    std::vector<std::vector<char>> grid = {
      {' ', ' ', 'C'},
      {' ', ' ', ' '},
      {' ', ' ', ' '}  
    };
    auto cheese_location = std::pair{0, 2};
    Mouse m(grid, cheese_location);
    EXPECT_TRUE(m.getCheese());

    grid = {
        {' ', ' ', ' ', ' ', ' '},
        {' ', ' ', ' ', ' ', ' '},
        {' ', ' ', ' ', 'C', ' '},
        {' ', ' ', ' ', ' ', ' '},
        {' ', ' ', ' ', ' ', ' '},
      };
      cheese_location = std::pair{2, 3};
      m = Mouse(grid, cheese_location);
      EXPECT_TRUE(m.getCheese());
}
// // It's guaranteed 0,0 cannot have an obstacle
TEST(MouseCheeseVariant_489, HappyCase_ObstacleAtStartingCoordinate_DoesntMatter) {
    std::vector<std::vector<char>> grid = {
      {'X', ' ', ' '},
      {' ', ' ', ' '},
      {' ', 'C', ' '}  
    };
    auto cheese_location = std::pair{2, 1};
    Mouse m(grid, cheese_location);
    EXPECT_TRUE(m.getCheese());
}
TEST(MouseCheeseVariant_489, HappyCase_CheeseAtStartingCoordinate) {
    std::vector<std::vector<char>> grid = {
      {'C', ' ', ' '},
      {' ', ' ', ' '},
      {' ', ' ', ' '}  
    };
    auto cheese_location = std::pair{0, 0};
    Mouse m(grid, cheese_location);
    EXPECT_TRUE(m.getCheese());
}
TEST(MouseCheeseVariant_489, HappyCase_NoObstacles_SingleColumn) {
    std::vector<std::vector<char>> grid = {
      {' '},
      {' '},
      {' '},
      {' '},
      {' '},
      {' '},
      {'C'},
      {' '},
      {' '},
      {' '},
    };
    auto cheese_location = std::pair{6, 0};
    Mouse m(grid, cheese_location);
    EXPECT_TRUE(m.getCheese());
}
TEST(MouseCheeseVariant_489, HappyCase_NoObstacles_SingleRow) {
    std::vector<std::vector<char>> grid = {
      {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C'}
    };
    auto cheese_location = std::pair{0, 9};
    Mouse m(grid, cheese_location);
    EXPECT_TRUE(m.getCheese());
}

TEST(MouseCheeseVariant_489, HappyCase_ObstaclesBacktracking_ReturnsTrue) {
    std::vector<std::vector<char>> grid = {
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'X', 'X', 'X', 'X', 'X', 'X', 'X', ' '},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X'},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'X', 'X', 'X', 'X', 'X', 'X', 'X', ' '},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'C', 'X', 'X', 'X', 'X', 'X', 'X', 'X'}
      };
    auto cheese_location = std::pair{7, 0};
    Mouse m(grid, cheese_location);
    EXPECT_TRUE(m.getCheese());

    grid = {
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X'},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X'},
        {'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'X', 'X', ' ', 'X', 'X', 'X', ' ', 'X'},
        {' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '},
        {' ', 'C', 'X', ' ', ' ', 'X', ' ', ' '},
      };
    cheese_location = std::pair{7, 1};
    m = Mouse(grid, cheese_location);
    EXPECT_TRUE(m.getCheese());
}

TEST(MouseCheeseVariant_489, NoCheese_ReturnsFalse) {
  std::vector<std::vector<char>> grid = {
    {' ', ' ', ' '},
    {' ', ' ', ' '},
    {' ', ' ', ' '}  
  };
  auto cheese_location = std::pair{9000, 9000};
  Mouse m(grid, cheese_location);
  EXPECT_FALSE(m.getCheese());

  grid = {
      {' ', ' ', ' ', ' ', ' '},
      {' ', ' ', ' ', ' ', ' '},
      {' ', ' ', ' ', 'X', ' '},
      {' ', ' ', ' ', ' ', ' '},
      {' ', ' ', ' ', ' ', ' '},
    };
    cheese_location = std::pair{9000, 9000};
    m = Mouse(grid, cheese_location);
    EXPECT_FALSE(m.getCheese());
}

TEST(MouseCheeseVariant_489, CannotReachCheese_Obstacles_ReturnsFalse) {
    std::vector<std::vector<char>> grid = {
      {' ', 'X', 'C'},
      {' ', 'X', 'X'},
      {' ', ' ', ' '}  
    };
    auto cheese_location = std::pair{0, 2};
    Mouse m(grid, cheese_location);
    EXPECT_FALSE(m.getCheese());

    grid = {
        {' ', ' ', ' ', ' ', ' '},
        {' ', ' ', 'X', 'X', 'X'},
        {' ', ' ', 'X', 'C', ' '},
        {' ', ' ', 'X', ' ', ' '},
        {' ', ' ', 'X', ' ', ' '},
      };
    cheese_location = std::pair{2, 3};
    m = Mouse(grid, cheese_location);
    EXPECT_FALSE(m.getCheese());
}
TEST(MouseCheeseVariant_489, CannotReachCheese_ElaborateObstaclesBacktracking_ReturnsFalse) {
    std::vector<std::vector<char>> grid = {
        {' ', 'X', ' ', ' ', ' '},
        {' ', 'X', 'X', 'X', ' '},
        {' ', ' ', ' ', 'X', ' '},
        {'X', 'X', ' ', 'X', ' '},
        {'C', 'X', ' ', ' ', ' '},
      };
    auto cheese_location = std::pair{4, 0};
    Mouse m(grid, cheese_location);
    EXPECT_FALSE(m.getCheese());

    grid = {
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'X', 'X', 'X', 'X', 'X', 'X', 'X', ' '},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X'},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'X', 'X', 'X', 'X', 'X', 'X', 'X', ' '},
        {' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '},
        {'C', 'X', 'X', 'X', 'X', 'X', 'X', 'X'}
      };
    cheese_location = std::pair{7, 0};
    m = Mouse(grid, cheese_location);
    EXPECT_FALSE(m.getCheese());

    grid = {
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X'},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X'},
        {'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'X', 'X', ' ', 'X', 'X', 'X', ' ', 'X'},
        {' ', 'X', ' ', ' ', 'X', ' ', ' ', ' '},
        {' ', 'C', 'X', ' ', ' ', 'X', ' ', ' '},
      };
    cheese_location = std::pair{7, 1};
    m = Mouse(grid, cheese_location);
    EXPECT_FALSE(m.getCheese());
}

TEST(MouseCheeseVariant_489, CannotReachCheese_SingleColumn) {
    std::vector<std::vector<char>> grid = {
      {' '},
      {' '},
      {'X'},
      {' '},
      {' '},
      {' '},
      {'C'},
      {' '},
      {' '},
      {' '},
    };
    auto cheese_location = std::pair{6, 0};
    Mouse m(grid, cheese_location);
    EXPECT_FALSE(m.getCheese());
}
TEST(MouseCheeseVariant_489, CannotReachCheese_SingleRow) {
    std::vector<std::vector<char>> grid = {
      {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'C'}
    };
    auto cheese_location = std::pair{0, 9};
    Mouse m(grid, cheese_location);
    EXPECT_FALSE(m.getCheese());
}