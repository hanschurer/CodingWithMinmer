#include <gtest/gtest.h>
#include "../../Unknowns/1_draw_circle/c++/1_draw_circle.hpp"

TEST(Unknown_DrawCircle, N1_ReturnsSingleCoordinate) {
    DrawCircle s;
    int radius = 4, n = 1;
    auto result = s.draw_circle(radius, n);

    EXPECT_EQ(result.size(), 1);
    EXPECT_EQ(result[0][0], radius);
    EXPECT_EQ(result[0][1], 0);
}

TEST(Unknown_DrawCircle, N0_ReturnsEmptyList) {
    DrawCircle s;
    int radius = 10, n = 0;
    auto result = s.draw_circle(radius, n);

    EXPECT_TRUE(result.empty());
}

TEST(Unknown_DrawCircle, N8_EvenInput_ReturnsAll8Coordinates) {
    DrawCircle s;
    int radius = 2, n = 8;
    auto result = s.draw_circle(radius, n);

    EXPECT_EQ(result.size(), n);
    std::vector<double> coordinate = {0.0, 2.0};
    EXPECT_EQ(result[0], coordinate);
    coordinate = {0.0, -2.0};
    EXPECT_EQ(result[1], coordinate);

    coordinate = {0.5, 1.94};
    EXPECT_EQ(result[2], coordinate);
    coordinate = {0.5, -1.94};
    EXPECT_EQ(result[3], coordinate);

    coordinate = {1.0, 1.73};
    EXPECT_EQ(result[4], coordinate);
    coordinate = {1.0, -1.73};
    EXPECT_EQ(result[5], coordinate);

    coordinate = {1.5, 1.32};
    EXPECT_EQ(result[6], coordinate);
    coordinate = {1.5, -1.32};
    EXPECT_EQ(result[7], coordinate);
}

TEST(Unknown_DrawCircle, N9_OddInput_ReturnsAll9Coordinates) {
    DrawCircle s;
    int radius = 2, n = 9;
    auto result = s.draw_circle(radius, n);

    EXPECT_EQ(result.size(), n);
    std::vector<double> coordinate = {0.0, 2.0};
    EXPECT_EQ(result[0], coordinate);
    coordinate = {0.0, -2.0};
    EXPECT_EQ(result[1], coordinate);

    coordinate = {0.5, 1.94};
    EXPECT_EQ(result[2], coordinate);
    coordinate = {0.5, -1.94};
    EXPECT_EQ(result[3], coordinate);

    coordinate = {1.0, 1.73};
    EXPECT_EQ(result[4], coordinate);
    coordinate = {1.0, -1.73};
    EXPECT_EQ(result[5], coordinate);

    coordinate = {1.5, 1.32};
    EXPECT_EQ(result[6], coordinate);
    coordinate = {1.5, -1.32};
    EXPECT_EQ(result[7], coordinate);

    coordinate = {2.0, 0.0};
    EXPECT_EQ(result[8], coordinate);
}