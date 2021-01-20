#include <gtest/gtest.h>
#include <iostream>
#include "Range.hpp"

using namespace std;

TEST(RangeTest, Contains_Item) {
    Range rng(1, 5);
    EXPECT_EQ(rng.contains(3), true);
    EXPECT_EQ(rng.contains(2), true);
    EXPECT_EQ(rng.contains(-3), false);
    EXPECT_EQ(rng.contains(8), false);
}

TEST(RangeTest, Overlaps_Range) {
    Range rng(3, 7);
    EXPECT_EQ(rng.overlaps(Range(4, 8)), true);
    EXPECT_EQ(rng.overlaps(Range(1, 5)), true);
    EXPECT_EQ(rng.overlaps(Range()), false);
    EXPECT_EQ(rng.overlaps(Range(2)), false);
}

TEST(RangeTest, Is_Sub_Range) {
    Range rng(2, 6);
    EXPECT_EQ(rng.is_sub_range(Range(1, 8)), true);
    EXPECT_EQ(rng.is_sub_range(Range(7)), true);
    EXPECT_EQ(rng.is_sub_range(Range()), false);
    EXPECT_EQ(rng.is_sub_range(Range(2)), false);
}

int main(int argc, char* argv[]) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}