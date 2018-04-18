excel自动转换工具：

1、读取excel文件，每个excel中仅有一个sheet，同时每个sheet中仅有一个表头

2、获取sheet表头，并进行合并转换成对应的形式

3、使用相似度计算方法对sheet表头与标签库进行相似度计算，并使用阈值来进行调整

4、根据相似度计算结果来将对应的标签写入到原表格中，实现excel的自动转换

------------------------------------

01、read_xls_multiline.py: 读取excel表头（111.xlsx, 222.xls）

02、read_xls_lib.py: 读取目标表头对象库（lablib.xlsx）

03、代码顺序

![order](E:\python cookbook\excel\order.png)

04、代码修改

