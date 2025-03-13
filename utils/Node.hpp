#pragma once

#include <vector>

class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;
    Node* parent;
    Node* random;
    std::vector<Node*> children;
    std::vector<Node*> neighbors;

    Node() : val(0), left(nullptr), right(nullptr), next(nullptr), parent(nullptr) {}

    Node(int val) : val(val), left(nullptr), right(nullptr), next(nullptr), parent(nullptr) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
            : val(_val), left(_left), right(_right), next(_next) {}
};

class Graph {
public:
    std::vector<Node*> roots;
};