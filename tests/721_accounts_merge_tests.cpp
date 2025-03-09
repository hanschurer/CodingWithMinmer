#include <gtest/gtest.h>
#include "../721_accounts_merge/variant_721.hpp"

TEST(AccountsMerge_Variant, HappyCase) {
    std::unordered_map<std::string, std::vector<std::string>> input =
        {{"C1", {"a", "b"}},
        {"C2", {"c"}},
        {"C3", {"b", "d"}},
        {"C4", {"d"}},
        {"C5", {"e"}},
        {"C6", {"c"}},
        {"C7", {"a"}}};

    auto result = accountsMerge_variant_721(input);
    EXPECT_EQ(3, result.size());

    std::vector<std::string> ids{"C5"};
    EXPECT_EQ(ids, result[0]);
    ids = {"C1", "C3", "C7", "C4"};
    EXPECT_EQ(ids, result[1]);
    ids = {"C6", "C2"};
    EXPECT_EQ(ids, result[2]);
}

TEST(AccountsMerge_Variant, ActualEmailStrings) {
    std::unordered_map<std::string, std::vector<std::string>> input =
        {{"ID1", {"aa@gmail.com", "bb@gmail.com"}},
        {"ID2", {"cc@gmail.com"}},
        {"ID3", {"bb@gmail.com", "dd@gmail.com"}},
        {"ID4", {"dd@gmail.com"}},
        {"ID5", {"ee@gmail.com"}},
        {"ID6", {"cc@gmail.com"}},
        {"ID7", {"aa@gmail.com"}}};

    auto result = accountsMerge_variant_721(input);
    EXPECT_EQ(3, result.size());

    std::vector<std::string>ids = {"ID2", "ID6"};
    EXPECT_EQ(ids, result[0]);
    ids = {"ID3", "ID7", "ID4", "ID1"};
    EXPECT_EQ(ids, result[1]);
    ids = {"ID5"};
    EXPECT_EQ(ids, result[2]);
}

TEST(AccountsMerge_Variant, NoEdges) {
    std::unordered_map<std::string, std::vector<std::string>> input =
        {{"C1", {"a", "b"}},
        {"C2", {"c"}},
        {"C3", {"d", "e", "f"}},
        {"C4", {"g"}},
        {"C5", {"h"}},
        {"C6", {"i"}},
        {"C7", {"j", "k", "l", "m", "n"}}};
    auto result = accountsMerge_variant_721(input);
    EXPECT_EQ(7, result.size());

    std::vector<std::string> ids{"C4"};
    EXPECT_EQ(ids, result[0]);
    ids = {"C2"};
    EXPECT_EQ(ids, result[1]);
    ids = {"C7"};
    EXPECT_EQ(ids, result[2]);
    ids = {"C5"};
    EXPECT_EQ(ids, result[3]);
    ids = {"C1"};
    EXPECT_EQ(ids, result[4]);
    ids = {"C3"};
    EXPECT_EQ(ids, result[5]);
    ids = {"C6"};
    EXPECT_EQ(ids, result[6]);
}

TEST(AccountsMerge_Variant, OneConnectedComponentViaOneEmail) {
    std::unordered_map<std::string, std::vector<std::string>> input =
        {{"C1", {"a", "b"}},
        {"C2", {"a"}},
        {"C3", {"d", "a", "f"}},
        {"C4", {"a"}},
        {"C5", {"a"}},
        {"C6", {"a"}},
        {"C7", {"j", "a", "l", "m", "n"}}};
    auto result = accountsMerge_variant_721(input);
    EXPECT_EQ(1, result.size());

    std::vector<std::string> ids{ "C6", "C1", "C5", "C3", "C7", "C2", "C4"};
    EXPECT_EQ(ids, result[0]);
}

TEST(AccountsMerge_Variant, OneConnectedComponentViaTwoEmails) {
    std::unordered_map<std::string, std::vector<std::string>> input =
        {{"C1", {"a", "b"}},
        {"C2", {"a"}},
        {"C3", {"d", "a", "f"}},
        {"C4", {"a", "x", "y", "z"}},
        {"C5", {"a"}},
        {"C6", {"a", "o", "p", "b"}},
        {"C7", {"j", "a", "l", "m", "n"}}};
    auto result = accountsMerge_variant_721(input);
    EXPECT_EQ(1, result.size());

    std::vector<std::string> ids{"C6", "C1", "C5", "C3", "C7", "C2", "C4"};
    EXPECT_EQ(ids, result[0]);
}

TEST(AccountsMerge_Variant, OneIdOneEmail) {
    std::unordered_map<std::string, std::vector<std::string>> input =
        {{"C1", {"a"}}};
    auto result = accountsMerge_variant_721(input);
    EXPECT_EQ(1, result.size());
    std::vector<std::string> ids{"C1"};
    EXPECT_EQ(ids, result[0]);
}

TEST(AccountsMerge_Variant, OneIdMultipleEmails) {
    std::unordered_map<std::string, std::vector<std::string>> input =
        {{"C1", {"a@gmail.com", "b@gmail.com", "c@gmail.com"}}};
    auto result = accountsMerge_variant_721(input);
    EXPECT_EQ(1, result.size());
    std::vector<std::string> ids{"C1"};
    EXPECT_EQ(ids, result[0]);
}

TEST(AccountsMerge_Variant, SeparateConnectedComponents) {
    std::unordered_map<std::string, std::vector<std::string>> input =
        {{"C1", {"a", "b", "c", "d"}},
        {"C2", {"q", "r", "s", "t"}},
        {"C10", {"x", "y", "z"}}};

    auto result = accountsMerge_variant_721(input);
    EXPECT_EQ(3, result.size());

    std::vector<std::string> ids{"C1"};
    EXPECT_EQ(ids, result[0]);
    ids = {"C2"};
    EXPECT_EQ(ids, result[1]);
    ids = {"C10"};
    EXPECT_EQ(ids, result[2]);
}