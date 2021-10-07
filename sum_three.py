x = [2, -3, 7, 3, 2, -5, 3, -46, 86, -42, 5, -31, 14, -12, 8, 9, 6, -4, 3, -2, 1, -1]

def closest_sum(nums, goal):
    nums.sort()
    res = nums[:3]
    
    for i in range(len(nums)-2):
        low, high = i+1, len(nums) - 1
        while low < high:
            if abs(goal - (nums[low] + nums[i] + nums[high])) < abs(goal - sum(res)):
                res = [nums[low], nums[i], nums[high]]

            curr = sum(res)
            if curr == goal:
                return res
            elif curr < goal:
                low += 1
            elif curr > goal:
                high -= 1
    return res

goalex = -125
print(x)
print(f"The goal is {goalex}!")
y = closest_sum(x, goalex)
print(f"The numbers are {y}.")
print(f"The sum is {sum(y)} and missed by {abs(goalex - sum(y))}")
