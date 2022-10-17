#!C:\Users\B24\AppData\Local\Programs\Python\Python36\python.exe
#main loader
import sys


print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()

with open("main.html",'rb') as fp:
    msg="message to replace"
    msg1=b"binary string to replace"
    st=fp.read()
    st=st.replace(b"###tag1###",msg.encode())
    st=st.replace(b"###tag2###",msg1)
    sys.stdout.buffer.write(st)
sys.stdout.flush()
