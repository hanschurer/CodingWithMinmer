#include <gtest/gtest.h>
#include "../249_group_shifted_strings/variant_249_rotational_cipher.hpp"

TEST(GroupShiftedStrings_Variant, HappyCase) {
    Solution_249_Variant s;
    EXPECT_EQ("Cheud-726?", s.rotationalCipher("Zebra-493?", 3));
    EXPECT_EQ("nopqrstuvwxyzABCDEFGHIJKLM9012345678", s.rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39));
    EXPECT_EQ("Epp-gsrzsCw-3-fi:Epivx5.", s.rotationalCipher("All-convoYs-9-be:Alert1.", 4));
    EXPECT_EQ("stuvRPQrpq-999.@", s.rotationalCipher("abcdZXYzxy-999.@", 200));
}

TEST(GroupShiftedStrings_Variant, All_NonAlphaNumericCharacters_Unchanged) {
    Solution_249_Variant s;
    EXPECT_EQ("$(&*#$&(#&$(#)))", s.rotationalCipher("$(&*#$&(#&$(#)))", 1000));
    EXPECT_EQ("_____________________", s.rotationalCipher("_____________________", 1));
    EXPECT_EQ(".-.-.-.-.-.", s.rotationalCipher(".-.-.-.-.-.", 90));
}

TEST(GroupShiftedStrings_Variant, CasesOnMinmerYT) {
    Solution_249_Variant s;
    EXPECT_EQ("rnsRjwe-349", s.rotationalCipher("minMerz-894", 5));
    EXPECT_EQ("KLM_nob_001177", s.rotationalCipher("XYZ_abo_112288", 39));
    EXPECT_EQ("12-biCC@", s.rotationalCipher("89-yfZZ@", 3));
}

TEST(GroupShiftedStrings_Variant, ZeroRotationalFactor) {
    Solution_249_Variant s;
    EXPECT_EQ("minMerz-894", s.rotationalCipher("minMerz-894", 0));
    EXPECT_EQ("XYZ_abo_112288", s.rotationalCipher("XYZ_abo_112288", 0));
}