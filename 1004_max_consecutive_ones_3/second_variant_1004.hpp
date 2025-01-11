#pragma once

#include <vector>

int longestVacationTimeSecondVariant(std::vector<bool>& year, int pto) {
    int max_vacation = 0;
    int left = 0;
    for (int right = 0; right < year.size(); right++) {
        if (!year[right])
            pto--;

        while (pto < 0) {
            if (!year[left])
                pto++;
            left++;
        }

        max_vacation = std::max(max_vacation, right - left + 1);
    }

    return max_vacation;
}

void longestVacationTimeSecondVariant() {
	std::vector<bool> year = {false, true, true, false, false, true, false};
	int pto = 2;
    assert(5 == longestVacationTimeSecondVariant(year, pto));

    year = {false, false, true, true, false, false, false};
    pto = 0;
    assert(2 == longestVacationTimeSecondVariant(year, pto));

    year = {false, false, true, true, false, false, false};
    pto = 5;
    assert(7 == longestVacationTimeSecondVariant(year, pto));

    year = {false, false, true, true, false, false, false};
    pto = 10;
    assert(7 == longestVacationTimeSecondVariant(year, pto));

    year = {true, true, true, true, true, true, true};
    pto = 0;
    assert(7 == longestVacationTimeSecondVariant(year, pto));

    year = {false, true, false, false, false, true, false, true};
    pto = 1;
    assert(3 == longestVacationTimeSecondVariant(year, pto));
}
