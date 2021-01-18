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
    
    @pytest.mark.parametrize("super_range, expected_op", [(Range(2, 7), True), (Range(8), True), (Range(-1, 8), True), (Range(1, 5), False), (Range(4, 9), False), (Range(3), False)])
    def test_sub_range(self, range_obj, super_range, expected_op):
        assert range_obj.is_sub_range(super_range) == expected_op
    
    @pytest.mark.parametrize("range_obj2, expected_op", [(Range(5), False), (Range(5, 10), False), (Range(3, 6), False), (Range(3), True), (Range(7, 10), True)])
    def test_is_disjoint(self, range_obj, range_obj2, expected_op):
        assert range_obj.is_disjoint(range_obj2) == expected_op

    @pytest.mark.parametrize("range_obj2, expected_op", [(Range(3), True), (Range(7, 10), True), (Range(5), False), (Range(5, 8), False)])
    def test_is_touching(self, range_obj, range_obj2, expected_op):
        assert range_obj.is_touching(range_obj2) == expected_op

    @pytest.mark.parametrize("range_obj2, expected_range", [(Range(5), Range(7)), (Range(5, 10), Range(3, 10)), (Range(3, 6), Range(3, 7)), (Range(3), Range(7)), (Range(7, 10), Range(3, 10)), (Range(10, 15), Range(3, 15))])
    def test_combine(self, range_obj, range_obj2, expected_range):
        combined_range = range_obj.combine(range_obj2)
        assert combined_range.start == expected_range.start and combined_range.end == expected_range.end

    @pytest.mark.parametrize("range_obj2, expected_op", [(Range(3, 7), True), (Range(3), False), (Range(5, 10), False)])
    def test_is_equal_to(self, range_obj, range_obj2, expected_op):
        assert range_obj.is_equal_to(range_obj2) == expected_op

    @pytest.mark.parametrize("range_obj2, expected_op", [(Range(4, 9), True), (Range(3, 8), True), (Range(4, 6), False), (Range(9), False)])
    def test_is_less_than(self, range_obj, range_obj2, expected_op):
        assert range_obj.is_less_than(range_obj2) == expected_op

    @pytest.mark.parametrize("range_obj2, expected_op" ,[(Range(3, 6), True), (Range(2, 5), True), (Range(2, 8), False)])
    def test_is_more_than(self, range_obj, range_obj2, expected_op):
        assert range_obj.is_more_than(range_obj2) == expected_op
    
    @pytest.mark.parametrize("rObj, expected_len", [(Range(7), 7), (Range(3, 5), 2), (Range(4, 9), 5)])
    def test_length(self, rObj, expected_len):
        assert rObj.length() == expected_len
    
    @pytest.mark.parametrize("given_range, n, expected_range", [(Range(3, 7), 2, Range(5, 9)), (Range(5, 9), -3, Range(2, 6))])
    def test_shift(self, given_range, n, expected_range):
        given_range.shift(n)
        assert given_range.start == expected_range.start and given_range.end == expected_range.end

    @pytest.mark.parametrize("given_range, n, expected_range", [(Range(2, 6), 3, Range(2, 9)), (Range(3, 4), 0, Range(3, 4))])
    def test_rshift(self, given_range, n, expected_range):
        given_range.rshift(n)
        assert given_range.start == expected_range.start and given_range.end == expected_range.end
    
    @pytest.mark.parametrize("given_range, n, expected_range", [(Range(2, 6), 3, Range(5, 6)), (Range(3, 4), 0, Range(3, 4))])
    def test_lshift(self, given_range, n, expected_range):
        given_range.lshift(n)
        assert given_range.start == expected_range.start and given_range.end == expected_range.end

    def test_reset(self, range_obj):
        range_obj.reset()
        assert range_obj.start == 0 and range_obj.end == 0
