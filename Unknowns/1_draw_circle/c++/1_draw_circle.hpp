#pragma once

#include <vector>

class DrawCircle {
public:
    std::vector<std::vector<double>> draw_circle(int radius, int n) {
        std::vector<std::vector<double>> result;
        int steps = n / 2;

        for (int i = 0; i < steps; i++) {
            double x = (i * 1.0 / steps) * radius;
            double y = sqrt(radius * radius - x * x);

            x = round(x * 100) / 100;
            y = round(y * 100) / 100;

            result.push_back({x, y});
            result.push_back({x, -y});
        }

        if (n % 2 == 1)
            result.push_back({radius * 1.0, 0});

        return result;
    }
};