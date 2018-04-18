@echo off  
cd E:\python cookbook\excel
start python add_to_test.py 
rem 使用ping命令暂停3s，这样可以看到调用python后的结果
ping -n 1 127.0.0.1 > nul 