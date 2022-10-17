#!C:\Users\B24\AppData\Local\Programs\Python\Python36\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
#import cgi

#enable error message output
import cgitb
cgitb.enable()

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")

print("Hello 你好!")

