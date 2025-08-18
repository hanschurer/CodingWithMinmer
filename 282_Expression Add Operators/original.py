# Context:
# There's a pattern with Meta and Math-related Hard LC problems: they make em' all a bit easier. We take those. Something that's been resurfacing is LC282 Expression Add Operators.

# Variant:
# The variant is simple. You don't have to implement the subtraction sign (This one is way more popular)
# Another variant is where you don't have to implement the multiplication sign.

# Yet another variant is where you're allowed to have operators at the very beginning as well. So something like -3+6*3 would be allowed.

# How important is this variant?
# If you've studied the Top 50, I'd take a look at this one. The twists make the OG problem technically simpler but it's important to know how to transform the full implementation into what you need. 

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        def dfs(cur_index, cur_res, cur_sum, prev):
            if cur_index == len(num):
                if cur_sum == target:
                    res.append("".join(cur_res))
                return

            for i in range(cur_index, len(num)):
                cur_str = num[cur_index: i+1]
                cur_num = int(cur_str)

                if not cur_res:
                    dfs(i+1, [cur_str], cur_num, cur_num)
                    dfs(i+1, ['-'] + [cur_str], -cur_num)
                else:
                    dfs(i+1, cur_res + ['+'] + [cur_str], cur_sum + cur_num, cur_num)
                    dfs(i+1, cur_res + ['-'] + [cur_str], cur_sum - cur_num, -cur_num)
                    dfs(i+1, cur_res + [''] + [cur_str], cur_sum-prev + prevcur_num, prev*cur_num)
                if num[cur_index] == "0":
                    break

        res = []
        dfs(0,[], 0, 0)
        return res