#include <gtest/gtest.h>
#include <iostream>
#include "Range.hpp"

using namespace std;

TEST(RangeTest, Simple) {
    ASSERT_TRUE(1 == 1);
}

TEST(RangeTest, Contains_Item) {
    ASSERT_TRUE(Range(1, 5).contains(3) == true);
    ASSERT_TRUE(Range(1, 5).contains(2) == true);
}

int main(int argc, char* argv[]) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}