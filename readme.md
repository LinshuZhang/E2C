# 如何用python做一个小小词典
-----------------------
## 主要情况介绍
1. [数据来源] [1]是剑桥大学英译汉词典
2. 首先在python中执行main.py文件，之后使用快键键将要查询单词存入剪贴板，在正在执行的python那里会出现查询单词含义，同时记录至执行环境下名为new_word@today.txt的纯文本

## To Do
1. 将查询后含义存入数据库
2. 做出查询次数标记
3. 增加多个数据来源
4. 增加单词重要程度标记
5. 添加其他功能
6. 将其内容展现形式改为chrome插件形式
7. 尝试做成网页app

## 制作教程（待施工）
### create new environment by conda
1. create python2.7 environment named E2C by conda
run those command at Terminal(Mac)  
``conda create -n E2C python=2``


2. active E2C environment 
run those command at Terminal(Mac)  
``source activate E2C``

[1]: http://dictionary.cambridge.org/dictionary/english-chinese-simplified/