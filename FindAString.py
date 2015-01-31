# https://www.hackerrank.com/challenges/find-a-string
# encoding=utf-8
# Solution 1
# Input
string = raw_input()
substring = raw_input()
# Solve
count = len([True for i in range(0, len(string) - len(substring) + 1)
             if string[i:i + len(substring)] == substring])

# Output
print(count)

# ------------------------------------------------------------------------------
# Solustion 2
import fileinput

# Input
string, substring = fileinput.input()

# Solve
count = len([True for i in range(0, len(string) - len(substring))
             if string[i:i + len(substring)] == substring])
# Output
print(count)

# 方法一与方法二的不同在于一直接输入两个字符串，二是读取文件（区别在于方法二的string比方法一
# 中的string多一个字符'\n',所以方法中range第二个参数不需要加一）
# 事实上这里的可以不减len(substring)结果也还是对的，只是多做了几次循环
