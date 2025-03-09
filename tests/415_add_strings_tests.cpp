#include <gtest/gtest.h>
#include "../415_add_strings/variant_415_decimals.hpp"

TEST(AddDecimalStrings_Variant, OnlyWholeNumbers) {
    std::string num1 = "11";
    std::string num2 = "123";
    EXPECT_EQ("134", addStringDecimals_415(num1, num2));

    num1 = "456", num2 = "77";
    EXPECT_EQ("533", addStringDecimals_415(num1, num2));

    num1 = "0", num2 = "0";
    EXPECT_EQ("0", addStringDecimals_415(num1, num2));

    num1 = "0", num2 = "2983435243982343";
    EXPECT_EQ("2983435243982343", addStringDecimals_415(num1, num2));

    num1 = "99999999", num2 = "2983435243982343";
    EXPECT_EQ("2983435343982342", addStringDecimals_415(num1, num2));

    num1 = "99999999", num2 = "99999999999";
    EXPECT_EQ("100099999998", addStringDecimals_415(num1, num2));
}

TEST(AddDecimalStrings_Variant, BothDecimals_With_And_Without_Carry) {
    std::string num1 = "123.53";
    std::string num2 = "11.2";
    EXPECT_EQ("134.73", addStringDecimals_415(num1, num2));

    num1 = "687345.3434321";
    num2 = "389457248.24374657243";
    EXPECT_EQ("390144593.58717867243", addStringDecimals_415(num1, num2));

    num1 = ".56", num2 = ".12";
    EXPECT_EQ(".68", addStringDecimals_415(num1, num2));

    num1 = ".5995495049556", num2 = ".12";
    EXPECT_EQ(".7195495049556", addStringDecimals_415(num1, num2));

    num1 = ".9479823748932", num2 = ".716400040030";
    EXPECT_EQ("1.6643824149232", addStringDecimals_415(num1, num2));

    num1 = ".00009479823748932", num2 = ".000000716400040030";
    EXPECT_EQ(".000095514637529350", addStringDecimals_415(num1, num2)); // Shows zeros even if not significant

    num1 = ".00009479823748932", num2 = ".00000071640004003000000";
    EXPECT_EQ(".00009551463752935000000", addStringDecimals_415(num1, num2)); // Shows zeros even if not significant

    num1 = "110.12", num2 = "9.";
    EXPECT_EQ("119.12", addStringDecimals_415(num1, num2));

    num1 = "111111110.0013430430433434454001", num2 = "9.";
    EXPECT_EQ("111111119.0013430430433434454001", addStringDecimals_415(num1, num2));

    num1 = "111111110.0013430430433434454001", num2 = "993483400013438854.";
    EXPECT_EQ("993483400124549964.0013430430433434454001", addStringDecimals_415(num1, num2));

    num1 = "910.99999", num2 = "999.9999";
    EXPECT_EQ("1910.99989", addStringDecimals_415(num1, num2));

    num1 = "999999.99999", num2 = "999999.9999";
    EXPECT_EQ("1999999.99989", addStringDecimals_415(num1, num2));

    num1 = "123.525", num2 = "11.2";
    EXPECT_EQ("134.725", addStringDecimals_415(num1, num2));

    num1 = "1234540458475845.", num2 = "8348736.";
    EXPECT_EQ("1234540466824581", addStringDecimals_415(num1, num2));
}

TEST(AddDecimalStrings_Variant, OneDecimal_OneWholeNumber) {
    std::string num1 = "110.75", num2 = "9";
    EXPECT_EQ("119.75", addStringDecimals_415(num1, num2));

    num1 = "110.75", num2 = "9999999";
    EXPECT_EQ("10000109.75", addStringDecimals_415(num1, num2));

    num1 = "150423434.00000000000", num2 = "9999999.";
    EXPECT_EQ("160423433.00000000000", addStringDecimals_415(num1, num2));

    num1 = "150423434.0000009184837483", num2 = "9999999.";
    EXPECT_EQ("160423433.0000009184837483", addStringDecimals_415(num1, num2));

    num1 = "110.9010479382798527", num2 = "9999999.";
    EXPECT_EQ("10000109.9010479382798527", addStringDecimals_415(num1, num2));
}