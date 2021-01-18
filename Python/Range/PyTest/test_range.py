from Range import Range
import pytest

class TestRange:
    @pytest.fixture
    def range_obj(self):
        return Range(3, 7)
    
    @pytest.mark.parametrize("value, expected_op", [(6, True), (5, True), (4, True), (1, False), (2, False), (7, False)])
    def test_contains(self, range_obj, value, expected_op):
        assert range_obj.contains(value) == expected_op

    @pytest.mark.parametrize("sub_range, expected_op", [(Range(5), True), (Range(5, 10), True), (Range(3, 6), True), (Range(3), False), (Range(7, 10), False)])
    def test_overlaps(self, range_obj, sub_range, expected_op):
        assert range_obj.overlaps(sub_range) == expected_op
