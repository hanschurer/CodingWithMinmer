#pragma once

#include <string>
#include <vector>

std::string customSortString_follow_up_791(std::string order, std::string s) {
    std::vector<int> freqs(26, 0);
    for (char ch : s)
        freqs[ch - 'a']++;

    std::string result;
    for (char ch : order) {
        result += std::string(freqs[ch - 'a'], ch);
        freqs[ch - 'a'] = 0;
    }

    for (int i = 0; i < freqs.size(); i++)
        result += std::string(freqs[i], i + 'a');

    return result;
}