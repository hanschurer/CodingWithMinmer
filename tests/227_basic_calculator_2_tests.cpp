#include <gtest/gtest.h>
#include "../227_basic_calculator_2/variant_227_without_division_and_subtraction.hpp"

TEST(BasicCalculator_Variant, OnlyAddition) {
  Solution_227_Variant s;
  std::string input = " 1 + 2 + 33 + 4+5";
  EXPECT_EQ(45 , s.calculate(input));
}

TEST(BasicCalculator_Variant, OnlyMultiplication) {
  Solution_227_Variant s;
  std::string input = " 1 * 2 * 33 * 4*5";
  EXPECT_EQ(1320 , s.calculate(input));
}

TEST(BasicCalculator_Variant, AdditionAndMultiplication) {
  Solution_227_Variant s;
  std::string input = " 5 + 2 * 33 * 4*5 + 3 + 6";
  EXPECT_EQ(1334 , s.calculate(input));
}