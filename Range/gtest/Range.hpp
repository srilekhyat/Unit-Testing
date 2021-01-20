#include <iostream>

using namespace std;

class Range {
    private:
        int start;
        int stop;

    public:
        Range() {
            start = 0;
            stop = 0;
        }

        Range(int limit) {
            start = 0;
            stop = limit;
        }

        Range(int lower, int upper) {
            start = lower;
            stop = upper;
        }

        void reset() {
            start = 0;
            stop = 0;
        }

        int length() {
            return stop - start;
        }

        bool contains(int item) {
            return (start <= item) && (item < stop);
        }

        bool overlaps(Range rObj) {
            if (start < rObj.start)
                return rObj.start < stop;
            return start < rObj.stop;
        }

        bool is_sub_range(Range rObj) {
            return (start >= rObj.start) && stop <= rObj.stop;
        }

        bool is_disjoint(Range rObj) {
            return !overlaps(rObj);
        }

        bool is_touching(Range rObj) {
            return (stop == start) || (start == stop);
        }

        Range combine(Range rObj) {
            if (is_disjoint(rObj)) {
                return Range();
            }
            int new_start = min(start, rObj.start);
            int new_stop = max(stop, rObj.stop);
            return Range(new_start, new_stop);
        }

        bool is_equal_to(Range rObj) {
            return (start == rObj.start) && (stop == rObj.stop);
        }

        bool is_less_than(Range rObj) {
            return (stop < rObj.stop) && (start <= rObj.start);
        }

        bool is_more_than(Range rObj) {
            return (stop > rObj.stop && start >= rObj.start);
        }

        void shift(int shift_factor) {
            start += shift_factor;
            stop += shift_factor;

            if (start > stop)
                reset();
        }

        void rShift(int shift_factor) {
            stop += shift_factor;

            if (start > stop)
                reset();
        }

        void lShift(int shift_factor) {
            start += shift_factor;

            if (start > stop)
                reset();
        }

        void squeeze(int factor) {
            start += factor;
            stop -= factor;

            if (start > stop)
                reset();
        }

        void stretch(int factor) {
            start -= factor;
            stop += factor;

            if (start > stop)
                reset();
        }

        
};