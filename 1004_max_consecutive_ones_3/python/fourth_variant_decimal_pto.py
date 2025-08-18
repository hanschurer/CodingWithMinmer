from typing import List
#PTO可以给小数
class Variant:
    def getMaxVacations(self, days: List[str], pto: float) -> float:
        max_vacation = 0.0
        whole_pto, partial_pto = int(pto), pto - int(pto)
        left = 0
        for right in range(len(days)):
            if days[right] == 'W':
                whole_pto -= 1

            while whole_pto < 0:
                if days[left] == 'W':
                    whole_pto += 1
                left += 1

            extension = 0.0
            #尝试用「小数 PTO」扩展窗口：
            # 若窗口左边界左侧（left-1）是工作日，说明可以用小数 PTO 覆盖部分该工作日，将窗口向左扩展 partial_pto 天。
            # 若窗口右边界右侧（right+1）是工作日，说明可以用小数 PTO 覆盖部分该工作日，将窗口向右扩展 partial_pto 天。
            # 满足任一条件，就可以获得 partial_pto 天的扩展长度。
            if left > 0 and days[left - 1] == 'W' or \
               right < len(days) - 1 and days[right + 1] == 'W':
               extension = partial_pto

            max_vacation = max(max_vacation, right - left + 1 + extension)

        return max_vacation