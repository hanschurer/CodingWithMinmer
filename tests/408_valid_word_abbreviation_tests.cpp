#include <gtest/gtest.h>
#include "../408_valid_word_abbreviation/variant_408_wildcard.hpp"

// OG LC408 testcases. Should not regress functionality
TEST(ValidWordAbbreviation_WildcardVariant, OnlyDigits) {
    std::string word = "internationalization";
    std::string pattern = "i12iz4n";
    Solution_408_Variant s;
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "apple";
    pattern = "a2e";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "unbelievable";
    pattern = "11e";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "internationalization";
    pattern = "19n";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "representation";
    pattern = "14";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "acknowledgment";
    pattern = "14";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "mississippi";
    pattern = "11";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
}
TEST(ValidWordAbbreviation_WildcardVariant, OnlyAlphabet_ExactMatch_ReturnsTrue) {
    std::string word = "abcdefg";
    std::string pattern = "abcdefg";
    Solution_408_Variant s;
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
}
TEST(ValidWordAbbreviation_WildcardVariant, OnlyAlphabet_ExactMatch_ReturnsFalse) {
    std::string word = "abcdefg";
    std::string pattern = "xyz";
    Solution_408_Variant s;
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "aa";
    pattern = "a";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));
}
////////////////////////////////////////////////////////////////////////

TEST(ValidWordAbbreviation_WildcardVariant, BothEmptyStrings_ReturnsTrue) {
    std::string word = "";
    std::string pattern = "";
    Solution_408_Variant s;
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
}

TEST(ValidWordAbbreviation_WildcardVariant, Wildcard_Matches_ReturnsTrue) {
    std::string word = "adcbdk";
    std::string pattern = "*a*bdk";
    Solution_408_Variant s;
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "aa";
    pattern = "*";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
}

TEST(ValidWordAbbreviation_WildcardVariant, LotsOfWildCards_MatchesNone_ReturnsTrue) {
    std::string word = "abc";
    std::string pattern = "ab****c";
    Solution_408_Variant s;
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
}

TEST(ValidWordAbbreviation_WildcardVariant, StillHavePatternLeft_NotAllWildcards_ReturnsFalse) {
    std::string word = "abc";
    std::string pattern = "ab****c**d";
    Solution_408_Variant s;
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));
}

TEST(ValidWordAbbreviation_WildcardVariant, StillHavePatternLeft_AllWildcards_ReturnsTrue) {
    std::string word = "abc";
    std::string pattern = "ab****c*****";
    Solution_408_Variant s;
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
}

TEST(ValidWordAbbreviation_WildcardVariant, SkipsLongerThanWord_ReturnsFalse) {
    std::string word = "testing";
    std::string pattern = "t32g";
    Solution_408_Variant s;
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "testing";
    pattern = "t7";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));
}

TEST(ValidWordAbbreviation_WildcardVariant, SkipsToEndOfWord_ReturnsTrue) {
    std::string word = "testing";
    std::string pattern = "t6";
    Solution_408_Variant s;
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
}

TEST(ValidWordAbbreviation_WildcardVariant, Wildcard_And_Digits) {
    std::string word = "validation";
    std::string pattern = "v2i*ion";
    Solution_408_Variant s;
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "zzzzzzzzzzp";
    pattern = "*p";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "zzzzzzzzzzp";
    pattern = "*";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "international";
    pattern = "i*n*l";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "developer";
    pattern = "d*ve*r";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "elephant";
    pattern = "e3h*";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "mechanical";
    pattern = "m*4l";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "dictionary";
    pattern = "d*o3y";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "automation";
    pattern = "a2o*ion";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "something";
    pattern = "s*m*hing";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "multiverse";
    pattern = "m*5e";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "extraordinary";
    pattern = "e*5*ary";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "mathematical";
    pattern = "m*3*3cal";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "unbelievable";
    pattern = "u1b*4*able";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "communication";
    pattern = "c2m*4*ion";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "programming";
    pattern = "p*6*ing";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "subterranean";
    pattern = "s*4*5n";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "revolutionary";
    pattern = "r3l*6y";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "balloon";
    pattern = "b2l2n";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "alphabet";
    pattern = "a1p1a1e1";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "elephant";
    pattern = "e1e1h*";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "subterranean";
    pattern = "s*4*6n";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "unbelievable";
    pattern = "u1b*6*ble";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "transformation";
    pattern = "t2a*5*ion";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "zzzzzzzzzzp";
    pattern = "*a";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "automation";
    pattern = "a4t*n";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "dictionary";
    pattern = "d*o4y";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "elephant";
    pattern = "e3z*";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "validation";
    pattern = "v2z*ion";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "submarine";
    pattern = "s*b*m";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "international";
    pattern = "i*o4l";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    // Complex with multi-digit numbers
    word = "extraordinary";
    pattern = "e*5*zary";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "mathematical";
    pattern = "m*3*4cals";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "transformation";
    pattern = "t2a*6tion";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "communication";
    pattern = "c2m*3*ition";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "programming";
    pattern = "p*5*ingg";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "revolutionary";
    pattern = "r3v*7y";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "balloon";
    pattern = "b12n";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "alphabet";
    pattern = "a1p1a2e1";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));

    word = "elephant";
    pattern = "e1e1z*";
    EXPECT_FALSE(s.validWordAbbreviation(word, pattern));
}

TEST(ValidWordAbbreviation_WildcardVariant, MultiDigits_And_Wildcards) {
    std::string word = "unbelievable";
    std::string pattern = "11*e";
    Solution_408_Variant s;
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
    
    word = "internationalization";
    pattern = "10*i5n";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
    
    word = "acknowledgment";
    pattern = "5*3*t";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
    
    word = "abbreviation";
    pattern = "1b10*";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
    
    word = "representation";
    pattern = "*14";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
    
    word = "extraordinary";
    pattern = "5*6*";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
    
    word = "multidimensionality";
    pattern = "4*6*5y";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));

    word = "predetermination";
    pattern = "3*d*10";
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
}

TEST(ValidWordAbbreviation_WildcardVariant, TLE) {
    std::string word = "bbbbbbbabbabbabaaabba";
    std::string pattern = "bb*ab**ba*bb***bba";
    Solution_408_Variant s;
    EXPECT_TRUE(s.validWordAbbreviation(word, pattern));
}