# 实习学习笔记｜SQL × Python

## 10月15日

### SQL：牛客30到32题

#### substring函数：当需要选取某一列中除了相同字段的词语时使用

substring（字符串，起始位置<数字>）：从第几个字符开始截止到末尾
**示例：** eg. substring(code,6)----从第六个字符到末尾

> **注意：** substring换成substr效果相同

#### replace函数：当前缀相同时，提取后面的字段

replace（字符串，'固定前缀',''）：把固定前缀替换成字符串，剩下的就是后面部分
**示例：** eg. replace(code,'user_','')----提取user_后面的部分

#### substring_index函数：当提取字段前面或者后面有相同的分隔符时使用

substring_index(字符串，'相同分隔符'，数字)：正数代表从左往右数分隔符前面的部分，负数代表从右往左数分隔符后面的部分
**示例：** eg. (180cm,75kg,27,male) (175cm,65kg,25,female)
substring_index(substring_index(proflie,',',-2),',',1)----第一个括号提取的结果是后两个数据，第二个括号内提取的是后两个中的第一个

> **注意：** 有conunt函数时，有分组一定要使用group by函数

---

## 10月16日

### Python：基础语法

- bug类型：英文符号、缩进错误、语法错误（SyntaxError）、命名错误(nameerror)

#### 多行注释：三引号中间的内容就是多行注释，可以是三对单引号，也可以是三对双引号；

crtl+/既可以添加注释也可以取消注释，使用的是单行注释

#### 输出函数print()

**1、*value 值：表示一次可以输出多个对象，输出多个对象时，需要用“，”分隔**

**示例：** eg. print('哈哈'，'呵呵','嘿嘿')-----结果：哈哈 呵呵 嘿嘿
**2、sep: 用来间隔多个对象，默认值是一个空格**

**示例：** eg. print('哈哈'，'呵呵','嘿嘿',sep=',')---结果：哈哈,呵呵,嘿嘿<这里中间的空格用了逗号代替>
**3、end: 用来设定以...结尾，默认值是换行符\n，可以切换成其他字符**

**示例：** eg.  print(字符串，end='后面要拼接的值')
输入:

```python
print('hello')
print('world')
```

输出：
hello
world
输入：

```python
print('hello',end=',')
print('world')
```

输出：
hello,world

#### 变量：计算机的储存空间，用于保存数据

**1、定义变量格式：变量名 = 值**

**示例：** eg.

```python
num1 = 3 #变量1
num2 = 10 #变量2
total = num1 + num2
print(num1)----3
print('num1')----num1 #加上引号会打印引号里面的内容，没有引号就会打印变量的值，如果该变量没有被赋值，就会报命名错误
```

#### 标识符：程序员定义的变量名和函数名

标识符规定：只能由数字、字母、_（下划线）组成；#python3可以用中文命名，但不推荐，标识符被包含在（）内对标识符本身没有影响，（（print））
不能以数字开头；
不能是关键字；#关键字是python中已经使用了的标识符，具有特殊的功能和含义
**示例：** eg.False = 1 print(False)会报错
严格区分大小写

#### 数值类型：

**1、int整型：任意大小的整数**

```python
num = 1
```

> **注意：** 检验数据类型的方法 type()

```python
print(type(num))----<class'int'>
```

**2、float浮点数:小数**

**3、bool布尔型（重点）：有固定写法，一个为True(真)，一个为Flase(假)#通常用于判断**

```python
print(type(True))----<class'bool'>
```

> **注意：** 布尔值可以当作正值来对待，True相当于整数1，Flase相当于整数0

**4、complex复数型（了解）**

固定写法：z = a + bj

#### 字符串str

**1、特点：需要加上引号，单双引号都可以，包含了多行内容时用三引号**

**示例：** eg. name = sixstar----会报错 # sixstar没有被赋值
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name = 'sixstar'----加了引号后就正确了

#### 格式化输出

**1、占位符：生成一定格式的字符串**

**2、%:**

**① %s 字符串（常用）**

```python
name = 'kk'
print('我的名字：%s' % name)----我的名字：kk
```

**② %d 整数（常用）**

```python
age = 22
name = 'kk'
print('我的名字:%s,年龄:%d' %(name,age))----我的名字：kk,年龄：22
```

> **注意：** 注意！：这里的冒号也需要是英文的格式

**③ %数字d 整数：数字设置位数，补足前面的空白，数字一样时不变**

```python
a = 123
print('%6d' % a)---- &nbsp;&nbsp;&nbsp;123(前面多了三个空白)
```

当想用0补足时：print('%06d' % a)----000123
**④ %f 浮点数(常用)**

```python
a = 1.2
b = 1.23
print('%f' % a)----1.200000
print('%f' % b)----1.230000
```

> **注意：** 默认后六位小数，当位数超过时，遵循四舍五入原则

**⑤ %.数字f 浮点数：数字设置小数位数,同样遵循四舍五入原则(注意这里的百分号后有“.”)**

```python
a = 2.34567
print('%.3f' % a)----2.346
print('%.7f' % a)----2.3456700 # 默认显示7位小数
```

**⑥ %%**

```python
print('我是%%的1%%' % ())----我是%的%1
```

**3、f格式化**

**① 格式：f'{表达式}'**

```python
name  = kk
age = 22
print(f'我的名字是{name},我今年{age}岁了')----我的名字是kk，我今年22岁了
```

### SQL：牛客33题

#### sql33:找出每个学校GPA最低的同学————分组取极值

**1、窗口函数＋子查询：ROW_NUMBER() OVER (PARTITION BY 分组列 ORDER BY 排序列) as rn**

ROW_NUMBER():生成1、2、3的行号
PARTITION BY 列：按这个列分区，就是分组，每个区里独立编号
ORDER BY 列：区内按这个列排序，决定谁编号在前
rn:是ROW_NUMBER生成的编号列的命名，后续取极值的时候用

```sql
SELECT device_id,university,gpa
FROM (SELECT device_id,university,gpa,ROW_NUMVER() OVER (PARTITION BY university ORDER BY gpa ASC) as rn
FROM user_profile) as t
WHERE rn = 1
```

**2、子查询＋连接:先找每组最低值，再到原表中匹配**

子查询：把一个SELECT的结果，当作另一个查询的“数据源”或比较值
**①SELECT...FROM(SELECT...FROM) AS 表名**

**②SELECT(SELECT...FROM...) AS 列名**

**③SELECT...FROM...WHERE 表1中的列=(SELECT...FROM...WHERE)#这里的第二个WHERE被称为相关，把两个表给关联起来了**

连接：把两个不同的表连接起来，但是要求有一列有相同的数据作为对应关系

```sql
INNER JOIN 表2 ON 约束条件
SELECT t1.device_id,t1.university,t1.gpa
FROM user_profile as t1
INNER JOIN
(SELECT university,MIN(gpa) AS min_gpa
FROM user_profile
GROUP BY university) AS t2
ON t1.university = t2.university
AND t1.gpa = t2.min_gpa
ORDER BY t1.university
```

> **注意：** 注意！这里第一个SELECT里需要加上t1.，因为t2也在外层

**3、相关子查询：子查询的一种类型，加在WHERE后**

```sql
SELECT device_id,university,gpa
FROM user_profile as t1
WHERE gpa = (SELECT MIN(gpa) as min_gpa
FROM user_profile as t2
WHERE t1.university = t2.university)
ORDER by university
```

> **注意：** 这里第一个SELECT不用加是因为两个表一个在内层一个在外层

---

## 10月20日

### SQL

- 在SQL的语法里，WHERE一定要放到所有的INNER JOIN后；

- 遇到“没有记录返回0”的需求，一律用LEFT JOIN

- 子查询想用来做连接的时候，必须把该字段SELECT出来

- 想算某一列限定条件的数量，可以用SUM（IF( ，1，0)）来计算

- 只要写了GROUP BY ，SELECT 后面出现的所有列，要么必须包含在GROUP BY里，要么必须被聚合函数（如COUNT、SUM、MAX）包起来

- 当一次性想在FROM写清楚所有表格时，每个表格后面需要加逗号，然后再用WHERE表示限定条件，这个可以替代INNER JOIN...ON...

- 在用INNER JOIN时，哪怕开头select里的数据不在第一个表中，也要按顺序去向左链接表

#### 正则表达：以SQL40为例

^：字符串开头  
[1-9]:是一个字符类，第一位必须是1到9之间的数字  
[0-9]{9}\$:前面的[0-9]也是一个字符类，后面的{9}是量词，表示在前面约束条件下的字符类出现9次，就是9个数字的意思  
<!-- 这里$之前的反斜杠只是为了防止转义 实际在SQL里不用写 -->
| ：或者  
^[1-9][0-9]{2}:以1到9开头，后面两个数字在0到9之间  
-[0-9]{3}:跟一个横线，再跟3个数字  
-[0-9]{4}\$:跟一个横线，再跟4个数字，并结束

---

## 10月21日

### SQL——窗口函数

#### 固定格式：函数 ( ) OVER (PARTITION BY 分组列 ORDER BY 排序列)

- 函数名 ( ) :想做的事  比如说SUM、ROW_NUMBER、找上一行(LAG)
- PARTITION BY : 开窗/分块，就是把数据按照某一个指标分成几个部分，可以省略，这时候整个表就是一块
- ORDER BY ： 在块内部按照什么顺序排。累加、排名类必须写，求平均值可以不写

#### 常用函数分类（三大派）

**① 聚合窗口函数(SUM/AVG/COUNT/MAX/MIN)**

在不合并行的情况下算出聚合值
- 累计求和：SUM (profit) OVER (ORDER BY date) (没写PARTITION BY,全表一块，按，按照日期一行行滑着叠加，最后每一行的结果都是之前的总和)———对应SQL40题
- 分组占比：SUM (profit) OVER (PARTITION BY department)(按每个部门进行分块，每个部门的销售总额，会重复显示在部门每个员工的行上)    
**常用形式:**  
SUM(profit) OVER (ORDER BY date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW):计算当前行加上一行的的滑动和，常用于算移动平均  

**② 排序窗口函数 (ROW_NUMBER/RANK/DENSE_RANK)**

给数据排名
- ROW_NUMBER ( ) :绝对序号，数字不重复。如1、2、3
- RANK ( ) :并列跳号，类似于比赛排名。如1、1、3
- DENSE_RANK ( ) :并列不跳号。如1、1、2  
典型用法：ROW_NUMBER ( ) OVER (PARTITION BY university ORDER BY gpa) = 1(取每个学校的第一名)  

**③ 偏移窗口函数(LEAD/LAG)**

```sql
LAG(列，1)：上一行的值
LEAD(列，1)：下一行的值
```

**示例：** eg：

```sql
SELECT  sale_date,  amount AS 今日销售额,
LAG(amount, 1) OVER (ORDER BY sale_date) AS 昨日销售额,
amount - LAG(amount, 1) OVER (ORDER BY sale_date) AS 比昨日差额   #可以直接拿函数相减
FROM daily_sales;
```

### SQL基础函数

- ABS ( ) :绝对值

- CEIL ( ) /CEILING ( ) :向上取整

- FLOOR ( ) :向下取整

- ROUND ( ,数字) :四舍五入

- TRUNCATE ( ，数字) :截断函数——直接截断保留规定位数小数，不进行四舍五入

---

## 10月22日

### Python

#### 算数运算符：加(+)、减(-)、乘(*)、除(/)、

取整除(//)：返回除法的整数部分、取余数(%)、幂(**)
- 使用算数运算符/，商一定是浮点数
- 取整除就是向下取整，不管四舍五入的原则
- 使用算术运算符，其中若有浮点数，结果也会用浮点数表示
- 优先级排序：幂（最高优先级）> 乘、除、取余、取整除 > 加减

#### 赋值运算符：+= 、—= 、

- 赋值运算符必须连着写，中间不能有空格，否则会报错

- 输入函数：input()输入函数

#### if判断：

- 基本格式：

```python
if 要判断的条件：
条件成立时要做的事
```

---

## 10月23日

### SQL

- SQL中的视图(VIEW)本质上是基于SELECT查询定义的虚拟表，不储存物理数据，而是提供数据的逻辑表示。

- 删除触发器操作： DROP TRIGGER #DELETE是删除所有行记录

#### 事务控制语句：

- ROLLBACK代表回滚，会结束用户的事务，并撤销正在进行的所有未提交的修改
- SAVEPOINT identifier 表示在事务中创建一个保存点，一个事务可以有多个保存点
- COMMIT WORK可以提交事务，并使得已对数据库做的所有修改成为永久性的
- RELEASE SAVEPOINT identifier 的主要作用是删除一个保存点，但他不会自动撤销该保存点之后执行的操作
- ROLLBACK TO SAVEPOINT identifier 回滚到该保存点，撤销保存点之后执行的操作，但保存点本身仍然存在

#### JOIN类型：

- FULL JOIN ：会返回两表所有行，不匹配部分用NULL填充
- CROSS JOIN ：返回两表的笛卡尔积，无论NULL值

- 查看stu表中索引的索引信息时，应使用的存储过程是：sp_helpindex

#### ALL( ):对所有数据都满足才成立 ，>= all( )等价于max，<=all( )等价于min

- ANY( )：只要有一条数据满足条件，整个条件成立 ，和SOME( )的作用一样,>=any( )等价于 >min，<any( )等价于< max

#### 删除DELETE：

- 单表删除：DELETE FROM 表名 WHERE 条件
- 多关联表删除：要根据另一张表（或临时表）的数据来删除本表的数据，需要写
  - DELETE 别名 FROM 表名 别名 JOIN ----
- 多表删除的时候，delete和from之间必须要写明想删除记录的表名

- in( )括号里只能有一个字段

- 使用delete语句删除表中的数据，drop语句删除数据表 eg. DROP table example.tb_ack

- WITH CHECK OPTION在视图中用于强制通过视图插入或更新的数据必须满足视图定义中的WHERE条件

- COUNT()属于聚合函数 WHERE后面不能跟聚合函数

- 先分组再过滤：group by...having...

- 执行CREAT INDEX语句会触发隐式事务提交

- count(*)统计所有行数，哪怕是null也算一行；count(列名)统计这一列不含null的行数

---

## 10月26日

### SQL

#### 基础数据插入——INSERT基础语法：INSERT INTO 表名(列名1，列名2...) VALUES (值1，值2...)

- 注意只要前面的列名顺序和后面的值顺序一一对应即可，不需要和建表时的原始顺序一致

- 在MYSQL里，字符串(varchar)必须加单引号

#### LEFT JOIN、RIGHT JOIN、INNER JOIN的相同点和区别：

- 相同点：所有连接方式都是前表在左，后表在右
- LEFT JOIN 以左表为基准，去右表里找匹配的行，最终生成的行数只能是等于左表或者大于(这种情况是右表有重复条件)，如果说右表行数小于左表行数，那么剩下的右表就用NULL补齐
- RIGHT JOIN是以右表为基准，去左表里找匹配的行，其他都一样
- INNER JOIN是取“交集”，只保留两边都能匹配上的

#### SQL语言的四大分类

**1、DDL(数据定义类型-Data Definition Language)**

- 作用：定义和修改表结构、数据库结构
- 代表命令：CREAT(建表、建库)、DROP(删表删库，连结构一起端掉)、ALERT(修改表结构，比如加一列、改字段类型)、TURNCATE(清空表结构，保留数据)、RENAME(重命名)、MODIFY(对列进行修改)
**2、DML(数据操纵语言-Data Manipulation Language)**

- 作用：对表里面的数据进行增删减
- 代表命令：INSERT(插入数据)、UPDATE(更新数据)、DELETE(删除数据，是一行)
**3、DCL(数据控制语言-Data Control Language)**

- 作用：权限设置
- 代表命令：GRANT(授权，比如把查询权限给某个用户)、REVOKE(收回权限)
**4、DQL(数据查询语言-Data Query Language)**

- 作用：专门用于查询
- 代表命令：SELECT

#### 判断奇数

**1、MOD(数字，2) = 1 (取余)**

**2、数字 % 2 = 1，等价于取余函数**

**3、数字 & 1 = 1(按位与)**

- &是运算符，将数字转成二进制后与1(二进制也是1)进行AND运算
- 任何奇数的二进制末位一定是1；任何偶数的末位一定是0

- 子查询中，父查询中一般使用IN运算符的是：单列多值嵌套查询

---

## 10月27日

### SQL

- 数据库主从复制延迟时，读操作要求强一致性应选择直连主库查询

- FULL JOIN关键字只要其中某个表存在匹配，FULL JOIN关键字就会返回行

#### WHERE 和 HAVING的区别

**1、WHERE在分组前工作，过滤原始数据行；HAVING在分组后工作，过滤分组后的结果，专门用来筛选GROUP BY产生的结果或聚合函数的值**

**2、WHERE后不可以接聚合函数，而HAVING是专门处理这些的**

#### CONV( )函数：COVN(N, from_base, to_base)

- N :要转换的数字或字符串
- from_base :原来的进制
- to_base ：目标进制
- COVN( )函数中，from_base和to_base的有效范围是2到36，如果超出这个范围，会返回NULL

- 联合索引遵循最左前缀原则

- SELECT..FOR UPDATE：锁定行，事务内生效，可以匹配WHERE过滤；

- LOCK TABLES..IN EXCLUSIVE MODE：锁整张表，不依赖事务

#### 存储过程的优点：

**1、执行速度快**

**2、允许组件式编程**

**3、减少网络流量**

**4、提高系统安全性**

#### 存储过程的缺点：

**1、移植性差**

**2、难以调试维护**

**3、服务器不能负载均衡**

- USING FILESORT表名数据库对结果集进行排序但无法使用索引

#### DATE_FORMATE(date,formate)：日期格式化函数

```sql
DATE_FORMATE(create_time,'%Y%m')
```

占位符大全
- %Y：四位年份
- %y：两位年份
- %m：两位月份
- %c：月份
- %d：两位日期
- %H：24小时制
- %i：分钟
- %s：秒

- CURDATE( )/CURRENT_DATE( ):只返回当前日期(2023-10-27)

- CURTIME( ):只返回当前时间(15：30：00)

- NOW( )/SYSDATE( ):返回当前的日期和时间(2023-10-27 15：30：00)

#### TIMESTAMPDIFF(单位，开始时间，结束时间)

- 计算的是“结束时间-开始时间”

- 并发访问数据库时，各并发事务之间数据库是独立的

- UNION ALL连接去重

- UNION连接不去重

#### 向表中添加列的标准语法

- ALERT TABLE 表名 ADD [COLUMN] 列名 数据类型 [约束条件]（中括号里的CLOUMN）可写可不写
- eg：
- ALERT TABLE student ADD age INT；
或者
- ALERT TABLE student ADD CLOUMN age INT

- 视图是虚拟的表，只能动态检索数据，不存储任何数据，并且大部分视图都不可以更新

- 视图是一种数据库对象，是从数据库的表或其他视图中导出的基表

---

## 10月28日

### SQL

#### MODIFY(修改) 常和ALERT TABLE一起用

**1、数据类型(比如把INT改成VARCHAR)**

**2、长度(比如把VARCHAR(20)改成VARCHAR(100))**

**3、约束条件(比如加个默认值DEFAULT、改个非空NOT NULL、加个主键)**

- 主键：Primary Key 用来唯一标识表中每一行数据的那个字段（或字段组合）
必须满足的三个条件：
**① 唯一 (Unique) ：不能有两行数据的主键值相同**

**② 非空 (Not Null) ：不可以是Null**

**③ 一个表只能有一个主键**

**示例：** eg：

```sql
CREATE TABLE students（
id INT PRIMARY KEY,
name VARCHAR(20)
）
```

---

## 10月29日

### Python

