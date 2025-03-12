class Solution:
    def sum(self, num1: int, num2: int)->int:
        if -100 <= num1 and  num2 <= 100:
            return num1 + num2
        else:
            return f'{num1} need to greater than or equal to -100, and {num2} need to less than or equal to 100 '
try:
    num1 = int(input('Please enter a number: '))
    num2 = int(input('Please enter the second number: '))
except ValueError:
    print('Please enter valid numbers.')
sum_nums = Solution()
print(sum_nums.sum(num1,num2))
