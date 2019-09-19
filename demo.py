import keyword

money = 10
if money < 100:
    print("小于100")

print("hello world")

# 单行注释

s = '''
多行
注释
'''

print(s)

"""
另一种
多行注释
"""

a = 5
print(a)
print(type(a))

a = "string"
print(a)
print(type(a))

userName = "田烨"
userAge = 28

user_name = 1

# seq 分隔符，默认为空格   end(只能传字符串类型，不能传表达式) 指定输出后不换行，传入的参数会在后面不换行打印
print("姓名", userName, "年龄", userAge, sep='|', end="123")
print("姓名", userName, "年龄", userAge, sep='|', end=a)

# 写入文件
# f = open("t.txt", "w")
# print("dayin", file=f)
# f.close()

print()

print(keyword.kwlist)

# 以0x或0X开头的整型数值是十六进制形式的整数
hex_value1 = 0x13
hex_value2 = 0xaF
print("hexValue1 的值为：", hex_value1)
print("hexValue2 的值为：", hex_value2)
# 以0b或0B开头的整型数值是二进制形式的整数
bin_val = 0b111
print('bin_val的值为：', bin_val)
bin_val = 0B101
print('bin_val的值为：', bin_val)
# 以0o或0O开头的整型数值是八进制形式的整数
oct_val = 0o54
print('oct_val 的值为：', oct_val)
oct_val = 0O17
print('oct_val 的值为：', oct_val)

# 创建列表  列表可变
a_list = ["1", 1, "abc", -1]

# 创建元组  元组不可变
a_tuple = ("1", 1, "abc", -1)

print("================================================================================================")

count = 10

while count < 100:
    print("count:", count)
    count += 10
