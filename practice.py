# ```python
# print ("Hello, World!")
# ```
# 10-15日练习题
# sql
# 1、substring(code,9)
# 2、REPLACE(code,'Beijing_','')
# 3、SUBSTRING_INDEX（SUBSTRING_INDEX(code,'_',-2）,'_',1)
# 10—16日练习题
# Python
# ```python
# name = '函数团'
# age = 22
# university = 'HEU'
# GPA = 3.9
# print(f'我的名字是{name}，今年{age}岁，就读于{university},GPA为{GPA:.2f}')
# print(GPA >= 3.5)#直接print输出的就是布尔值
# name = '金宝宝'
# age = 23
# university = 'HEU'
# GPA = 4.0
# print(f'我的好朋友是{name},今年{age}岁,也在{university}上学,她的GPA为{GPA}')
# ```

# 10月22日课上笔记
## 1.算术运算符
# ```python
# print(1/1) #使用算术运算符/，商一定是浮点数(float) 
# a = 5
# b = 2
# print(a//b) #2 取整
# print(7.0//2) #取整除若有浮点数，结果也会用浮点数表示
# print(a%b) #1 取余（取模）
# print(a**b) #25 幂（乘方）
# print(3**2+5/2) # 9+2.5=11.5
# ```

## 2.赋值运算符
# 2.1 =
# ```python
# num1 = 5
# num2 = 8
# ```
# 将一个变量值赋给另外一个变量
# ```python
# num3 = num1
# print(num3) #5
# ```

# 2.2 +=
# ```python
# a = 1
# print(a) #1
# a= a+1
# a += 1  #等效于a = a + 1
# print(a) #2
# n1 = 99 #成本
# n2 = 55 #利润
# n3 = n2 + n1 # 售价
# n1 += n2 #等效于n1 = n1 + n2
# print(n1) #154
# ```

# 2.3 -=
# ```python
# b = 1
# b -= 1 #等效于b = b - 1
# print(b) #0 
# print(10 +=3) #语法错误，纯数字不能直接在print中使用赋值运算符，需要先赋值
# ```

## 3.input()输入函数
# ```python
# input(prompt) #prompt是提示信息，括号内的内容会显示在控制台上
# name = input("请输入你的姓名：") 
# print(f'你的姓名是{name}') #f-string格式化输出
# pwd = input("请输入你的密码：")
# print(f'你的密码是{pwd}') #f-string格式化输出
# ```

## 4.转义字符
# 4.1 \t 制表符  通常表示四个字符，也称缩进
# ```python
# print('sixstar') #sixstar
# print('six\tstar') #six    star
# print('姓名\t年龄\t性别') #姓名    年龄    性别
# ```

# 4.2 \n 换行符 表示将当前位置换到下一行的开头
# ```python
# print('姓名\n年龄\n性别') 
# ```
# 姓名
# 年龄
# 性别

# 4.3 \r 回车符 表示将当前位置换到本行的开头
# ```python
# print('sixstar\r123') #123star 是123把six替换掉了 从而输出结果是123star
# ```

# 4.4 \\ 反斜杠 
# ```python
# print('sixstar\\123') #sixstar\123
# print(r'sixstar\\\123') #sixstar\\\123  r表示原始字符串，里面的转义字符不生效
# ```

## 5. if判断语句
# 5.1if判断基本格式
# ```python
# if 判断条件：
#     满足条件做的事情
# age = 17
# if age<18:
#     print('未成年不能上网')
# ```

# 练习：用户从控制台输入成绩，如果满分，输出“你真棒！”，如果及格，输出“还要继续加油哈！”
# ```python
# score = input("请输入你的成绩：") #  input()函数获取的内容都是字符串类型
# if score == '100': #'=='是判断是否相等，'='是赋值运算符
#     print('你真棒！')
# if score == '60':
#     print('还要继续加油哈！')
# ```

## 6.运算符
# 6.1比较（关系）运算符
# == 比较的是两个变量的值是否相等，相等返回布尔值True，不相等返回布尔值False
# != 比较的是两个变量的值是否不相等，不相等返回布尔值True，相等返回布尔值False
# ```python
# a = 55
# b = 88
# print(a==b) #False
# print(a!=b) #True
# print(a>b) #False
# print(a<b) #True
# if a>b:
#     print('a大于b')
# ```

# 6.2逻辑运算符
# and 左右两边都符合才为真
# ```python
# a = 'Hello'
# b = 'World'
# if a == 'Hello' and b == 'World':
#     print('Hello World') #Hello World
# if a == 'Hello' and b == 'Python':
#     print('Hello Python') #不输出
# ```
# or 左右两边有一个符合就为真
# ```python
# fruit = 'apple'
# if fruit == 'apple' or fruit == 'banana':
#     print('带来了水果') #带来了水果
# ```
# not 表示相反的结果
# ```python
# print(not 3>9) #True
# ```

# 6.3 三目运算符（三元表达式）
# 语法格式：为真结果 if 判断条件 else 为假结果
# ```python
# a = 5
# b = 8
# if a <= b:
#     print('a小于等于b') #为真结果
# else:
#     print('a大于b') #为假结果
# print('a小于等于b' if a <= b else 'a大于b') #三目运算符
# ```

## 7. if-else
# 语法格式：
# ```python
# if 判断条件：
#     满足条件做的事情
# else:
#     不满足条件做的事情
# a = 666
# if a == 666:
#     print('你真棒！')
# else:
#     print('还要继续加油哈！')
# ```

# 8. if-elif结构
# if-else 二选一 if-elif 多选一
# ```python
# if 条件1：
#     满足条件1做的事情
# elif 条件2：
#     满足条件2做的事情
# elif 条件3：
#     满足条件3做的事情
# ```
# ......
# ```python
# score = 85
# if 85 <= score <= 100:
#     print('优秀')
# elif 60 <= score <85:
#     print('及格')
# elif 0 <= score <60:
#     print('不及格')
# ```

# ```python
# question = input('你喜欢函数团吗？')
# if question == '喜欢':
#     print('函数团也喜欢你！')
# elif question == '不喜欢':
#     print('你叫什么名字？？！')
# else:
#     print('听不懂你在说什么.......')
# ```

# 10月23日上课笔记
## 1.if嵌套
# 基本格式
# ```python
# if 条件1：
#     事情1
#     if 条件2：
#         事情2
# else：
#     不满足条件做的事情
# ```
# 注意：内层if判断和外层if判断都可以是if-else结构

# 定义一个布尔型变量，表示是否有车票
# ```python
# ticket = True  #True代表有车票，False代表没车票
# # 定义一个浮点型变量保存体温
# temp = 38.5
# # 判断是否有车票
# if ticket == True:  #外层if判断
#     print('请进站',end=',')
#     # 正常人腋下体温是36.3到37.2
#     if 36.3 <= temp <= 37.2:
#         print("体温正常")
#     else:
#         print("体温异常，请隔离")
# else:
#     print('请先购买车票')
# ```

# 不管有没有车票都会询问体温，用input输入
# 输入是否有车票
# ```python
# ticket_input = input('请问您是否有车票？（有/无）：')
# ticket = ticket_input == '有'  # 输入“有”得到True，其他输入得到False
# ```

# ```python
# # 输入体温
# temp = float(input('请输入您的体温：'))  #因为temp是需要比较大小的，input里面默认是字符串，所以需要改成浮点数
# ```

# ```python
# # 判断是否有车票
# if ticket == True:
#     print('请进站', end=',')
#     # 正常人腋下体温是36.3到37.2
#     if 36.3 <= temp <= 37.2:
#         print('体温正常')
#     else:
#         print('体温异常，请隔离')
# else:
#     print('请先购买车票')
# ```


# ```python
# ticket_input = input('请问您是否有车票？（有/无）：')
#  #有布尔值判断就用==
# if ticket_input == '有':
#     print('请进站', end=',')
# ```

#     temp = float(input('请输入您的体温：'))

# ```python
#     if 36.3 <= temp <= 37.2:
#         print('体温正常')
#     else:
#         print('体温异常，请隔离')
# else:
#     print('请先购买车票')
# ```

# 10月29日
## 1.While循环
# 1.1基本语法 
# 定义初始变量
# ```python
# while 条件:
#     循环体
#     改变变量
# i = 1 #定义一个初始值,记录循环的次数,i = 1表示从第一次开始
# while i <= 100:
#     print('好好学习,天天向上')
#     i += 1 # 每执行一次i的值就加1
# ```
# 注意:如果没有改变变量,条件一直满足,就会一直循环下去,一直执行

# 1.2死循环
# 基本格式
# ```python
# while True:
#     循环体
# while True: # 条件只写True,说明一直为真,就会一直执行,从而形成一个死循环
#     print('不要长大')
# while False: # 条件只写False,说明一直为真,就会一直执行,从而形成一个死循环
#     print('不要长大')
# ```
# 只要不是False或0,其他单独存在的值也会是死循环

# 1.3 while循环应用:计算1+2+3+...+100的和
# ```python
# i = 1 #定义一个初始值,从1开始计算,记录循环次数
# s = 0 #定义一个变量保存计算结果,最开始计算结果为0,没有相加
# while i <= 100:
#     # print(i) # 循环打印1-100
#     s += i   # 每次循环的计算结果和i进行相加
#     i += 1   # 每循环一次,i的值加1
#     # print('计算结果是:',s) #在循环内,循环输出计算结果
# print('计算结果:',s) # print放循环外 只会打印出最终的s结果 
# ```

## 2.while循环嵌套
# 2.1含义
# 一个while循环里面还有一个while循环
# 2.2基本格式
# ```python
# while 条件1:
#     循环体1
#     while 条件2:
#         循环体2
#         改变变量2
#     改变变量1
# ```
# 注意:缩进决定层级,严格控制缩进,最好自动缩进
# ```python
# i = 1 # 定义一个变量记录外循环的次数
# while i <= 3: #外循环
#     print(f'这是第{i}次外循环')
#     j = 1 # 定义一个初始值记录内循环的次数
#     while j <= 5: # 内循环
#         print(f'内循环{j}次')
#         j += 1
#     i += 1
# ```

## 3.for循环
# 3.1基本格式
# ```python
# for 临时变量 in 可迭代对象:
#     循环体
# ```
# 注意:冒号和缩进
# ```python
# str = 'hellopython' #定义一个字符串
# # 可迭代对象就是要去遍历取值的整体,现在只需要记住字符串就是可迭代对象
# for i in str: # i是临时变量,可以随便写,i是常规写法
#     print(i)
# ```

# 3.2 range()
# 用来记录循环次数,相当于计数器
# ```python
# range(start,stop,step)
# for i in range(1,6): #从1开始,到6结束,遵循包前不包后规则,[)
# # 或者写for i in range(5) #从0开始:0 1 2 3 4
# ```
#     print(i)         # 1 2 3 4 5
# # range()里面只写一个数,这个数就是循环的次数,默认从0开始

# for循环应用:计算1+2+3+...+100的值
# ```python
# s = 0 #定义一个变量来保存计算结果
# for i in range(1,101): # 包前不包后,不包含101这个数
#     # print(i)
#     s += i #每循环一次计算结果与i相加
#     # print('计算结果是:',s) #在循环内,循环输出计算结果
# print('计算结果:',s) # print放循环外 只会打印出最终的s结果 
# ```

## 5.break 和 continue关键字
# 都是专门在循环中使用的关键字
# ```python
# i = 1
# if i <= 5:
#     print('我在吃苹果')
#     break# 会报错,break 和continue只能放在循环内
# ```
# 5.1 break
# 作用:某一条件满足时退出循环
# ```python
# i = 1
# while i <= 5:
#     print(f'小红在吃第{i}个苹果')
#     if i == 3:
#         print('吃饱了不吃了')
#         break # 结束break所在的循环
#     i += 1
# ```

# 5.2 continue
# 作用:退出本次循环,下一次循环继续执行
# ```python
# i = 1
# while i <= 5:
#     print(f'小明在吃第{i}个苹果')
#     if i == 3:
#         print(f'吃到了虫子,第{i}个苹果不吃了')
#         # 在continue之前,一定要修改计数器,否则会陷入死循环
#         i += 1# 加上这个之后是为了让他出了continue之后不在等于3 从而不会遍历if里的语句
#         continue # 会忽略continue之后的所有代码 所以他直接跳到开头之后会一直陷入循环
#     i += 1
# ```

# ```python
# for i in range(5):
#     if i == 3:
#         # break #i=3时结束循环 
#     #结果是0 1 2
#         continue #跳过了3
#     #结果是0 1 2 4
#     print(i)
# ```

## 11.3
# 1.1 字符串编码
# 本质上就是二进制与语言文字的一一对应关系
# Unicode：所有字符都是两个字节 ，好处：字符与数字之间转换速度更快一点 ， 坏处：占用空间大
# UTF-8：精准，对不同的字符用不同的长度表示， 好处：节省空间 ， 坏处：字符与数字之间转换速度慢一点，每次都需要计算字符需要用多少个字节来表示

# 1.2 字符串编码转换
# ```python
# a  = 'hello'
# # print(a,type(a)) # str,字符串是以字符为单位进行处理
# a1 = a.encode()      # 编码
# print('编码后：',a1)  # b'hello'
# print(type(a1))      # bytes,编码后是以字节为单位进行处理
# a2 = a1.decode()     # 解码
# print('解码后：',a2)  # hello
# print(type(a2))      # str,解码后是以字符为单位进行处理
# ```
# 注意：对于bytes，只需要知道它和字符串之间的相互转换

# ```python
# st = '函数团在此'
# st1 = st.encode('utf-8') #编码
# print(st1,type(st1))
# st2 = st1.decode('utf-8') #解码
# print(st2,type(st2))
# ```

# 2、字符串常见操作
# 2.1 + 字符串拼接
# ```python
# print('函数团'+'在此') # 函数团在此，字符串相加，+是字符串拼接
# ```

# 2.2 * 字符串重复
# ```python
# print('函数团'*3) # 函数团函数团函数团，字符串相乘，*是字符串重复
# print('函数团\n'*3) # 会换行
# ```

# 2.3 成员运算符
# 作用：检查字符串中是否包含了某个子字符串（即某个字符或多个字符）
# in 检查是否包含，返回布尔值True或False
# not in 检查是否不包含，返回布尔值True或False
# ```python
# name = '函数团'
# print('函数' in name) # True
# print('函数' not in name) # False
# ```

# 2.3 下标
# python中下标从0开始
# 作用：通过下标能够快速找到对应的数据
# 格式：字符串名[下标]
# ```python
# name = 'sylvive'
# print(name[0]) # s
# print(name[1]) # y
# # 从右往左数，下标从-1开始
# print(name[-1]) # e
# ```
# 注意：下标不能超过字符串的长度，否则会报错

# 2.4 切片
# 含义：指对操作的对象截取其中一部分的操作
# 语法：[开始位置:结束位置:步长]
# 注意：包前不包后原则，即从起始位置开始，到结束位置的前一个位置结束（不包含结束位置本身）
# ```python
# st = 'abcdefghijklmn'
# ```
# 从左往右
# ```python
# print(st[0:5]) # abcde
# print(st[4:7]) # efg
# print(st[3:])  # defghijklmn,下标从3开始，一直到最后
# print(st[:5])  # abcde,从开头到下标为5的前一个位置
# # 从右往左
# print(st[-1:])  # n,下标为-1的最后一个位置
# print(st[:-1])  # abcdefghijklm,从开头到下标为-1的前一个位置
# print(st[-1:-5]) # 空,从右往左切片时，起始位置要大于结束位置，否则会报错
# ```
# 步长 :表示选取间隔,不写步长,则默认是1
# 步长的绝对值大小决定切取的间隔,正负号决定切取的方向,正数代表从左往右取值,负数表示从右往左取值
# ```python
# print(st[-1::1]) # n,从下标为-1的最后一个位置开始，步长为1，向右取值
# print(st[-1::-1]) # nmlkjihgfedcba,从下标为-1的最后一个位置开始，步长为-1，向左取值
# print(st[-1:-5:-1]) # nmlk,从下标为-1的最后一个位置开始，步长为-1，向左取值，到下标为-5的前一个位置结束
# print(st[0:8:2]) # aceg,从下标为0的第一个位置开始，步长为2，向右取值，到下标为8的前一个位置结束
# ```

# 3、字符串常用方法
# 3.1 查找
# 3.1.1
# find :检测某个子字符串是否包含在字符串中,如果在就返回这个子字符串的第一个下标,如果不在就返回-1
# ```python
# find(子字符串,开始位置下标,结束位置下标)
# ```
# 注意:开始位置下标和结束位置下标可以省略,表示在整个字符串中查找
# ```python
# name = 'sylvive'
# print(name.find('v')) # 3
# print(name.find('z')) # -1
# print(name.find('sylv')) # 0--检测到第一个sylv,s的下标是0
# print(name.find('v',0,5)) # 3--在下标为0到下标为5的范围内查找v,找到了v,返回下标3
# print(name.find('v',0,3)) # -1--在下标为0到下标为3的范围内查找v,没有找到v,返回-1
# ```

# 3.1.2
# index :检测某个子字符串是否包含在字符串中,如果在就返回这个子字符串的第一个下标,如果不在就报错
# ```python
# index(子字符串,开始位置下标,结束位置下标)
# name = '今晚早点睡觉'
# print(name.index('早')) # 2
# print(name.index('晚',2)) #报错,因为从下标为2开始查找晚,晚的下标是1,所以没有找到,报错
# print(name.index('晚',0,2)) # 1--在下标为0到下标为2的范围内查找晚,找到了晚,返回下标1
# ```
# 遵循包前不包后

# 3.1.3 
# count :统计某个子字符串在字符串中出现的次数
# ```python
# count(子字符串,开始位置下标,结束位置下标) 
# name = 'sylvive'
# print(name.count('v')) # 2
# print(name.count('s')) # 1
# print(name.count('z')) # 0
# ```
# 遵循包前不包后

# 3.2 修改元素
# 3.2.1 replace :替换字符串中的某个子字符串
# ```python
# replace(旧子字符串,新子字符串,替换次数)
# ```
# 注意:替换次数可以省略,表示替换所有的旧子字符串
# ```python
# name = 'sylvive'
# print(name.replace('v', 'n')) # sylnine
# print(name.replace('i', 'I', 1)) # sylvIve
# ```

# 3.2.2 split() :按照指定的分隔符将字符串分割成列表
# ```python
# split(分隔符,分割次数)
# ```
# 注意:分割次数可以省略,表示分割所有的分隔符
# ```python
# name = 'sylvive'
# print(name.split('v')) # ['syl', 'i', 'e']
# print(name.split('v', 1)) # ['syl', 'ive']
# ```

# 3.2.3 capitalize() :将字符串的首字母大写,其他字母小写
# ```python
# name = 'sylvive'
# print(name.capitalize()) # Sylvive
# name = 'SYLVIVE'
# print(name.capitalize()) # Sylvive
# ```

# 3.2.4lower() :将字符串中的所有字母转换为小写
# ```python
# name = 'SylVIve'
# print(name.lower()) # sylvive
# ```

# 3.2.5 upper() :将字符串中的所有字母转换为大写
# ```python
# name = 'SylVIve' 
# print(name.upper()) # SYLVIVE
# ```

# 3.3 判断
# 1.startswith() :判断字符串是否以指定的子字符串开头,返回布尔值True或False
# ```python
# startswith(子字符串,开始位置下标,结束位置下标)
# name = 'sylvive'
# print(name.startswith('s')) # True
# print(name.startswith('sylv')) # True
# print(name.startswith('v',3,5)) #True
# ```

# 2.endswitch():判断字符串是否以指定的子字符串结尾,返回布尔值True或False
# ```python
# endswith(子字符串,开始位置下标,结束位置下标)
# name = 'sylvive'
# ```

# 3.isupper():检测字符串中所有的字母是否都为大写,是的话就返回True

# 4.islower():检测字符串中所有的字母是否都为小写,是的话就返回True   


##11.4
# 1.列表
# 基本格式：
# 列表名=[元素1，元素2,元素3..]
# 所有元素放在[]内，元素与元素之间用，隔开
# 元素之间的数据类型可以各不相同
# ```python
# li=[1,2,'a',4]
# print(li,type(li)) #list
# print(li[2]) # a
# ```
# 列表也可以进行切片操作
# 列表是可迭代对象，可以for循环遍历取值
# ```python
# for i in li:
    # print(i) #1 2 a 4
# ```

# 2.列表的常见操作
# 2.1 添加元素
# ```python
# append()  extend()  insert()
# li=['one','two','three']
# li.append("four")   #attend 整体添加 #['one', 'two', 'three', 'four']
# li.extend('four')   #extend 分散添加，将另外一个类型中的元素逐一添加 #['one', 'two', 'three', 'f', 'o', 'u', 'r']
# li.insert(3,'four')  #insert 在指定位置插入元素 #['one', 'two', 'three', 'four']
# li.insert(0,'four')  #指定位置如果有元素，原有元素就会后移 #['four', 'one', 'two', 'three']
# li.insert("four")   #报错，没有指定下标
# print(li)
# li=[1,2,3]
# li.append(4)   #[1,2,3,4]
# li.extend(4)   #报错 #extend里要用可迭代对象 而整形不是可迭代对象
# li.insert(3,4)
# print(li)
# ```

# 2.2修改元素
# 直接通过下标就可以进行修改
# ```python
# li=[1,2,3]
# li[2]='a' #超过索引值会报错
# print(li) #[1, 2, 'a']
# ```

# 2.3 查找元素
# in：判断指定元素是否存在列表中，如果存在就返回Ture，不存在就返回False
# not in:判断指定元素是否存在列表中，如果不存在就返回Ture，存在就返回False
# ```python
# li=['a','b','c','d']
# print('b' in li) #True
# ```

# 用户输入昵称，昵称重复则不能使用
# 定义一个列表，保存已经存在的昵称
# ```python
# name_list=['baobao','jinbaobao','baobaojin']
# while True:
#   name=input("请输入您的昵称")
#   # 判断昵称是否已经存在
#   if name in name_list:
#       print (f"您输入的昵称{name}已经存在了哦")
#   # 如果昵称不存在
#   else:
#       print(f"昵称{name}已经被您使用")
#       # 把昵称新增到列表
#       name_list.append(name)
#       print(name_list)
#       break
# ```


## 11.5
# index:返回指定数据所在位置的下标，如果查找的数据不存在就会报错
# count：统计指定数据在当前列表出现的次数
# 跟字符串的用法相同

# 2.4 删除元素
# del
# ```python
# li = ['a','b','c','d']
# del li #删除列表，报错
# del li[2] #根据下标删除 #['a', 'b', 'd']
# print(li) 
# ```

# pop：删除指定下标的数据，python3版本默认删除最后一个元素
# ```python
# li = ['a','b','c','d']
# li.pop() #默认删除最后一个元素 #['a','b','c']
# li.pop(2) #不能指定元素删除，只能根据下标删除，下标不能超出范围 #['a', 'b', 'd']
# print(li)
# ```

# remove:根据元素的值进行删除
# ```python
# li = ['a','b','c','d']
# li.remove('a') #['b', 'c', 'd']
# ```
# 列表中不存在这个元素的时候就会报错
# ```python
# li = ['a','b','c','d','b']
# li.remove('b') #['a','c','d','b'] #默认删除最开始出现的指定元素
# print(li)
# ```

# 2.5排序
# sort:将列表按特定顺序重新排列,默认从小到大
# reverse:倒序,将列表倒置,不按大小排列
# ```python
# li = [1,4,67,45,8,9]
# # li.sort()  #[1, 4, 8, 9, 45, 67] 按照从小到大的顺序排列
# li.reverse() #[9, 8, 45, 67, 4, 1]
# ```
# 当上面两个命令同时运行时 就可以得到从大到小的排列
# ```python
# print(li)
# ```

# 2.6列表推导式
# 格式一:[表达式 for 变量 in 列表]
# 注意:in后面不仅可以放列表,还可以放range() 可迭代对象
# ```python
# li = [1,2,3,4,5,6]
# ```
# [print(i) for i in li] #1 2 3 4 5 6 #前面的i是表达式 也可以换成i*5之类的
# ```python
# li = []
# for i in range(1,6):
#     # print(i)
#     li.append(i)
# print(li) #[1,2,3,4,5]
# ```
# [li.append(i) for i in range(1,6)] #[1,2,3,4,5]
# ```python
# print(li)
# ```

#格式二:[表达式 for 变量 in 列表 if 条件]
# 把奇数放进列表里
# ```python
# li = []
# for i in range(1,11):
#     if i % 2 == 1:
#         print(i)
#         li.append(i)
# print(li) #[1,3,5,7,9]
# ```
# [li.append(i) for i in range(1,11) if i % 2 == 1]
# ```python
# print(li) #[1,3,5,7,9]
# ```

# # 2.7列表嵌套
# ```python
# # 含义:一个列表里面又有一个列表
# li = [1,2,3,[4,5,6]]
# # print(li[3]) #[4,5,6] 取出里面的列表
# print(li[3][0]) #4 取出内列表的下标为0的元素
# ```

# 3.元组
# 3.1基本格式:元组名 = (元素1,元素2,元素3...)
# 所有元素包含在小括号内,元素与元素之间用逗号隔开,不同元素也可以是不同的数据类型
# ```python
# tua = (1,2,3,4,5) #也可以写成tuq = (1,2,3,'a','b',[1,2,3])
# print(type(tua)) #tuple
# tub = (1,) #只有一个元素的时候末尾必须加上逗号,否则返回这个唯一的值的数据类型
# tua = ()   #定义空元组
# ```

#3.2 元组与列表的区别
#  1.元组只有一个元素末尾必须加,列表不需要
#  2.元组只支持查询操作,不支持增删改操作
# ```python
# li = [1,2,3]
# li[1] = 'a'  #[1, 'a', 3]
# print(li)
# ```

# ```python
# tua = (1,2,3)
# print(tua[2])  #3  #元组也有下标 也是从零开始
# tua[2] = 'a'   #报错,不支持修改
# count() index() len() 跟列表的用法相同
# print(tua.index(2)) #3 #tua中下标为2的元素
# print(tua.count(1)) #1 #tua中1出现的次数
# print(len(tua))     #3 #tua元组的长度
# print(tua[1:])        #(2,3) #切片,包前不包后原则 所以从2开始切,包含2本身到最后
# ```

# 3.3 应用场景
# 函数的参数和返回值
# 格式化输出后面的()本质上是一个元组
# ```python
# name = 'kk'
# age = 22
# # print('%s的年龄是:%d' %(name,age))
# info = (name,age)
# print('%s的年龄是:%d' %info)
# ```
# 数据不可以被修改的时候,保护数据的安全

# 4.字典
# 4.1基本格式:字典名 = {键1:值1,键2:值2...}
# 键值对形式保存,键和值之间用:隔开,每个键值对之间用,隔开
# ```python
# dic = {'name':'kk','age':22}
# print(type(dic)) #dict
# # 字典中的键具有唯一性,但是值可以重复
# dic2 = {'name':'kk','name':'bb'}
# print(dic2) #{'name': 'bb'} #不会报错,键名重复的值会被后面的值覆盖
# ```

# 4.2字典常见操作一
# 4.2.1 查看元素
# 格式1:变量名[键名]
# ```python
# dic = {'name':'kk','age':22}
# print(dic[2]) #报错,字典中没有下标,查找元素需要根据键名,键名相当于下标
# print(dic['age']) #22
# ```
# 注意:查看元素不存在时会报错

# 格式2:变量名.get(键名)
# ```python
# dic = {'name':'kk','age':22}
# print(dic.get('name'))  #kk
# print(dic.get('tel'))     #None  #当键名不存在时不会报错,会返回None
# print(dic.get('tel','不存在'))   #不存在 可以在后面设置返回的值是什么
# ```

# 4.2.2 修改元素
# 格式:变量名[键名] = 值
# ```python
# dic = {'name':'kk','age':22}
# dic['age'] = 20     # {'name': 'kk', 'age': 20} #列表通过下标修改,字典通过键名修改
# print(dic)          
# ```

# 4.2.3 添加元素
# 格式:变量名[键名] = 值
# 注意 键名存在就更改 不存在就新增
# ```python
# dic = {'name':'kk','age':22}
# dic['tel'] = 123456789
# print(dic)        #{'name': 'kk', 'age': 22, 'tel': 123456789} #没有tel就新增
# ```

# 4.2.4 删除元素
# ```python
# del : 删除整个字典
# ```
# 基本格式: del 字典名
# ```python
# dic = {'name':'kk','age':22}
# del dic
# print(dic)   #报错 因为已经被删除了
# ```
# 删除指定键值对,键名不存在就会报错   格式: del 字典名[键名]
# ```python
# dic = {'name':'kk','age':22}
# # del dic['age']    #{'name': 'kk'}
# del dic['tel']      #报错
# print(dic)   
# ```

# ```python
# clear(): 清空整个字典里面的东西,保留了这个字典
# dic = {'name':'kk','age':22}
# dic.clear()
# print(dic)     #{} 返回为空
# ```

# pop :删除指定键值对,键不存在就会报错
# ```python
# dic = {'name':'kk','age':22}
# dic.pop('age')           #{'name': 'kk'}
# dic.pop('tel')           #报错
# dic.pop()                #报错,和列表不一样,列表是默认删除最后一个
# dic.popitem()            #默认删除最后一个,3.7版本之前任意删除一个,3.7之后默认删除最后一个
# print(dic)
# ```

# 4.3字典常见操作二
# 4.3.1 len()求长度
# ```python
# dic = {'name':'kk','age':22}
# print(len(dic))  #2 有两对键值对
# ```

# 4.3.2 keys() :返回字典里包含的所有键名
# ```python
# dic = {'name':'kk','age':22}
# print(dic.keys())   #dict_keys(['name', 'age'])  注意返回的不是列表类型
# ```
# for循环取出键名
# ```python
# for i in dic.keys():      #只取出键名
    # print(i)              #name age
# ```

# 4.3.3 values():返回字典里面包含的所有值
# ```python
# dic = {'name':'kk','age':22}
# # print(dic.values())       #dict_values(['kk', 22])
# for i in dic.values():
#     print(i)                #kk 22
# ```

# 4.3.4 item():返回字典里包含的所有键值对,键值对以元组形式
# ```python
# dic = {'name':'kk','age':22}
# # print(dic.items())             #dict_items([('name', 'kk'), ('age', 22)])
# for i in dic.items():
#     print(i)                     #('name', 'kk')  ('age', 22)  i是元组类型
# ```

# 4.4 字典的应用场景
# 使用键值对,存储描述一个物体的相关信息

## 11.6
# 1.集合
# 1.1 基本格式:集合名 = {元素1,元素2,元素3...}
# ```python
# s1 = {1,2,3}
# s1 = {}          #定义空字典
# s1 = set()       #定义空集合
# ```

# 1.2集合具有无序性
# ```python
# s1 = {'a','b','c','d','e','f'}
# print(s1)  #{'e', 'a', 'f', 'd', 'b', 'c'} 其中一次的结果,每次运行结果都不一样
# s2 = {1,2,3,4,5,6}
# print(s2)     #{1, 2, 3, 4, 5, 6}    数字运行结果一样
# ```

#集合无序的实现方式涉及哈希表
# ```python
# print(hash('a'))
# print(hash('b'))
# print(hash('c'))
# ```
# 每次运行结果都不同,hash(哈希)值不同,那么在hash表中的位置也不同,这就实现了集合的无序性
# ```python
# print(hash(1))
# print(hash(2))
# print(hash(3))
# ```
# python中int整型的hash值就是他本身,在hash表中的位置不会发生改变,所以顺序就不会改变
# 无序性:不能修改集合中的值

# 1.3 集合具有唯一性,可以自动去重
# ```python
# s1 = {1,2,4,6,3,4,2}  #{1, 2, 3, 4, 6} 没有重复的元素
# print(s1)
# ```

# 1.4 集合的常见操作
# 1.4.1 添加元素
# 1.add() 添加是是一个整体
# ```python
# s1 = {1,2,3,4}
# print('原集合:',s1)
# ```
# 集合的唯一性决定了,如果需要添加的元素在原集合中已经存在,就不进行任何操作
# ```python
# s1.add(5)
# s1.add(5,6)      #报错,一次只能添加一个元素
# print('现集合:',s1)
# ```
# 原集合: {1, 2, 3, 4}
# 现集合: {1, 2, 3, 4, 5}

# 2.update 把传入的元素拆分,一个个放入集合中
# ```python
# s2 = {1,2,3,4}
# print('原集合:',s2)
# s2.update(567)         #报错,因为update里要加入可迭代对象
# s2.update('567')         
# ```
# 原集合: {1, 2, 3, 4}
# 添加后: {'5', 1, 2, 3, 4, '7', '6'}
# ```python
# s2.update([5,6,7])     #{1, 2, 3, 4, 5, 6, 7}
# s2.update((5,6,7))     #{1, 2, 3, 4, 5, 6, 7}
# s2.update({5,6,7})     #{1, 2, 3, 4, 5, 6, 7}
# s2.update({'name':'kk','age':'22'})        #{1, 2, 3, 4, 'name', 'age'}
# print('添加后:',s2)
# ```

# 1.4.2 删除元素
# 1.remove :选择删除的元素,如果集合中有就删除,没有就会报错
# ```python
# s2 = {1,2,3,4}
# s2.remove(3)  #{1,2,4}
# s2.remove(5)  #报错
# ```

# 2.pop 对集合进行无序排列,然后将左边的第一个元素删除
# ```python
# s2 = {1,2,3,4}
# s2.pop()  #删除的是第一个元素 当集合内是字符串时,默认删除根据hash表排序后的第一个元素
# print(s2)
# ```

# 3.discard:选择要删除的元素,有就会删除,没有也不会发生改变
# ```python
# s2 = {1,2,3,4}
# print('原集合:',s2)
# s2.discard(3)          #{1,2,4}
# s2.discard(7)          #没有任何改变
# print('删除后:',s2)  
# ```

# 2.交集和并集
# 2.1交集 &
# 含义:共有的部分
# ```python
# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a & b)      #{3,4}
# ```
# 没有共有的部分 返回空集合set()

# 2.2并集 |
# ```python
# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a | b)     #{1, 2, 3, 4, 5, 6}
# ```

## 11.7
# 1.类型转换
# 1.1 int():转换成一个整数，只能转换由纯数字组成的字符串
# ```python
# a = 1.2 #浮点数 float
# b = int(a)
# print(b,type(b))  # 1 int  强制转换成整型了
# # 浮点型强制转整型只保留整数部分 不遵循四舍五入原则
# # str -> int
# a = int('123')
# print(a,type(a))    #123  int
# print(int('kk'))    #报错
# ```
# 如果字符串中有数字和正负号以外的字符就会报错

# 用户从控制台输入，判断年龄
# ```python
# age = input('请输入您的年龄：')    #会报错 因为input输出是字符串 要转整型
# age = int(input('请输入您的年龄：'))
# if age >= 18:
#     print('成年了')
# ```

# 1.2 float():转换为一个小数
# ```python
# print(float(11))     #11.0 整型转换成浮点型，会自动添加一位小数
# ```

# 1.3 str():转换成字符串类型，任何类型都可以转换成字符串类型
# ```python
# n = 100
# print(str(n))   #100   str
# st = str(1.80)
# print(st,type(st))     #1.8 str      float转换成str会去除末尾为0的小数部分
# ```
# 列表类型也可以转 反正就是万物几乎都可以转字符串

# 1.4eval() ：用来执行一个字符串表达式，并返回表达式的值
# ```python
# print(10+10)                #20
# print('10'+'10')            #1010
# print('10+10')              #10+10
# print(eval('10+10'))        #20   执行运算并返回运算值
# a = eval('10+10')
# print(type(a))              #int
# ```

# ```python
# eval() 可以实现list、dict、tuple和str之间的转换
# ```
# str ——> list
# ```python
# st1 = '[[1,2],[3,4],[5,6]]'
# li = eval(st1)
# print(li,type(li))                #[[1, 2], [3, 4], [5, 6]] <class 'list'>
# ```
# 同理可得字典、元组之间的转换
# ```python
# eval()强大但不够安全
# ```

# 1.5 list():将可迭代对象转换成列表
# 支持转换为list的类型：str、tuple、dict、set
# str->list
# ```python
# print(list('abcd'))                        #['a', 'b', 'c', 'd']
# ```

# tuple->list
# ```python
# print(list((1,2,3,4)))                     #[1, 2, 3, 4]
# ```

# dict->list
# ```python
# print(list({'namme':'kk','age':22}))      #['namme', 'age']      
# ```
# 字典转换成列表，会取键名作为列表的值

# set->list
# ```python
# print(list({1,2,3,4,5}))                  #[1, 2, 3, 4, 5]
# ```
# 集合转换成列表会先去重再转换


## 11.9
# 1.深浅拷贝
# 1.1赋值：会随着原对象一起变化
# ```python
# li = [1,2,3,4]
# li2 = li     #将li直接赋值给li2
# print(li,li2)         #[1, 2, 3, 4] [1, 2, 3, 4]
# ```
# 给li列表新增元素
# ```python
# li.append(5)
# print(li,li2)         #[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
# ```
# 赋值：等于完全共享资源，一个值的改变会完全被另一个值共享

# 1.2 浅拷贝（数据半共享）
# 会创建新的对象，拷贝第一层的数据，嵌套层会指向原来的内存地址
# ```python
# import copy         #导入copy模块
# li = [1,2,3,[4,5,6]]           #定义一个嵌套列表
# li2 = copy.copy(li)
# print(li,li2)                  #[1, 2, 3, [4, 5, 6]] [1, 2, 3, [4, 5, 6]]
# # 查看内存地址 id()
# print('li内存地址：',id(li))
# print('li2内存地址：',id(li2))
# # 内存地址不一样,说明不是同一个对象
# li.append(8)
# print(li,li2)          #[1, 2, 3, [4, 5, 6], 8] [1, 2, 3, [4, 5, 6]]
# # 往嵌套列表添加元素
# ```
# li[3].append(7)
# ```python
# print(li,li2)          #[1, 2, 3, [4, 5, 6, 7], 8] [1, 2, 3, [4, 5, 6, 7]]
# print('li[3]内存地址：',id(li[3]))
# print('li2[3]内存地址：',id(li2[3]))      #地址一样
# # 外层的内存地址不同，但是内层的是一样的
# ```

# 优点：拷贝速度快，占用空间少，拷贝效率高

# 1.3深拷贝（数据完全不共享）
# 外层的对象和内部的元素都拷贝了一遍
# ```python
# import copy
# li = [1,2,3,[4,5,6]]
# li2 = copy.deepcopy(li)      #深拷贝
# print(li,li2)                #相同
# print(li,id(li))
# print(li2,id(li2))           #地址不同
# # 在嵌套列表添加
# ```
# li[3].append(7)
# ```python
# print(li,li2)                #[1, 2, 3, [4, 5, 6, 7]] [1, 2, 3, [4, 5, 6]]
# # 深拷贝数据变化只影响自己本身，和原来的对象没有关联
# ```

# 2.可变类型
# 含义：变量对应的值可以修改，但是内存地址不会改变
# 常见可变类型：list 、dict 、set
# ```python
# li = [1,2,3,4]
# print(li,'原内存地址：',id(li))         #[1, 2, 3, 4] 原内存地址： 1284879735168
# li.append(5)
# print(li,'现内存地址：',id(li))         #[1, 2, 3, 4, 5] 现内存地址： 1284879735168
# ```
# 内存地址未改变

# 3.不可变对象
# 含义：变量对应的值不能被修改，如果修改就会生成一个新的值从而分配新的内存空间
# 常见不可变对象：数值类型（int，bool，float，complex）、字符串、元组
# ```python
# n = 10  #整型
# print(n,'原地址：',id(n))
# n = 15
# print(n,'现地址：',id(n))
# ```
# 内存地址不一样：修改n的值就会生成新的值
# 注意：深浅拷贝只针对可变类型，不可变对象没有拷贝说法

##11.10
# 1.函数
# 1.1含义：将独立的代码块组织成一个整体，使其具有特殊功能的代码集，在需要的时候再去调用即可
# 1.2作用：提高代码的重用性，使整体代码看上去更加简练
# 1.3基本格式
# ```python
# def 函数名():
#     函数体
# ```

# 2.调用函数
# 函数名()
# ```python
# def login():
#     print('这是登录函数')
# login()
# ```
# 调用几次，函数里面的代码就会运行几次，每次调用的时候，函数都会从头开始执行
# 编写一个打招呼的函数并调用它
# ```python
# def hello():
#     name = input('你叫什么名字：')
#     print(f'你好呀{name}')
# hello()
# ```
# 调用函数前，必须保证函数已经存在

# 3.返回值  return
# 函数执行结束后，最后给调用者的一个结果
# 作用：
# 1.return会给函数的执行者返回值
# ```python
# def buy():
#     return'杨枝甘露'
# buy()
# print(buy())          #函数里有return必须要打印才有结果
# ```
# 2.函数中遇到return，表示此函数结束，不继续执行
# ```python
# def buy():
#     return'杨枝甘露',20     #return返回多个值，以元组的形式返回给调用者
#     return'20'             #不会输出，因为第一个return下面的代码不会被执行
# print(buy())
# ```
# 返回值的三种情况：None（没有返回值），单个，多个（以元组的形式）
# return和print的区别
#     1.return表示此函数结束，print会一直执行
# ```python
# def funa():
#     return 123
#     print(456)
# print(funa())               #没有结果
# ```
# 2.return是返回计算值，print是打印结果
# ```python
# def add():
#     a = 1
#     b = 2
#     # return a+b
#     print(a+b)
# print(add())        #3
# add()               #3
# ```

# 4.参数
# 4.1形参和实参
# 定义格式：
# ```python
# def 函数名(形参a，形参b):       #形参：定义函数时，小括号里面的变量
#         函数体
#      ...(如a=1，b=2)
# ```
# 调用格式；
# 函数名(实参1，实参2)            #实参：调用函数时，小括号里面具体的值
# ```python
# def add(a,b):
#     return a+b
# print(add(1,3))         #4
# ```

# 4.2函数参数
# 4.2.1.必备参数(位置参数)
# 含义：传递和定义参数的顺序及个数必须一致
# 格式：def func(a,b)
# ```python
# def func(name1,name2):
#     print(name1)
#     print(name2)
# # func()      #报错
# func('kk','bb')         #写了几个就传几个，多传少传都不行
# ```

# 4.2.2默认参数
# 含义：为参数提供默认值，调用参数时可不传该默认参数的值
# 注意：所有的位置参数必须出现在默认参数前，包括函数定义和调用
# 格式：def func(a=12):
# ```python
# def funb(a=8):
#     print(a)
# funb()           #8
# funb(22)         #22
# ```
# 设置默认值，没有传值会根据默认值来执行代码，传了值根据传入的值来执行代码
# ```python
# def funb(b,a=8):
#     print(a,b)
# funb(33)
# ```

# 4.2.3可变参数
# 含义：传入的值的数量是可以改变的，可以传入多个，也可以不传
# 格式：def func(*args)      #args可以改成其他名字 但是args符合代码的规范性
# ```python
# def func(*args):
#     print(args)
# # func(1)                 #(1,)  以元组形式接受
# func('金宝宝','函数团')    #('金宝宝', '函数团')
# ```

# 4.2.4 关键字参数
# 格式：def func(**kwargs)
# ```python
# def func(**kwargs):
#     print(kwargs)
# # func()                          #{} 返回字典
# func(name = 'kk',age = 22)        #{'name': 'kk', 'age': 22}     传值的时候，需要采用键=值的形式
# ```
# 作用：可以扩展函数的功能

# 5.函数嵌套
# 5.1嵌套调用
# 含义：在一个函数里面调用另一个函数
# ```python
# def study():
#     print('晚上在学习')
# def course():
#     study()
#     print('Python基础')
# course()            #晚上在学习/Python基础        /是换行的意思
# ```

# 5.2嵌套定义
# 含义：在一个函数中定义另一个函数
# ```python
# def study():              #外函数
#     print('晚上在学习')
#     def course():         #内函数
#         print('Python基础')
#     course()              #内函数需要先调用    定义和调用是同级的
# study()                   #晚上在学习/Python基础
# ```
