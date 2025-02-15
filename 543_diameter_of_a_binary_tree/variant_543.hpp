#pragma once

#include "../utils/Node.hpp"


int diameterOfNAryTree(Node* node, int& diameter) {
    if (node == nullptr)
        return 0;

    int max_height = 0;
    int second_max_height = 0;
    for (Node* child : node->children) {
        int height = diameterOfNAryTree(child, diameter);
        if (height > max_height) {
            second_max_height = max_height;
            max_height = height;
        }
        else if (height > second_max_height)
            second_max_height = height;
    }

    diameter = std::max(diameter, max_height + second_max_height);
    
    return max_height + 1;
}

int diameterOfNAryTree(Node* root) {
    int diameter = 0;
    diameterOfNAryTree(root, diameter);
    return diameter;
}