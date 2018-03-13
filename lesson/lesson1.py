#coding:utf-8
name = raw_input('你的名字\n') or '<unkown>'
info = name if name != '<unkown>' else ' 无名氏' 
print 'hello' + info