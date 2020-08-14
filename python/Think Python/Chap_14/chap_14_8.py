import os
import wc
import hashlib

'''
cmd = 'ls -1'
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(stat)
'''

filename = 'output.txt'
cmd = 'md5sum ' + filename
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(res)
print(stat)
print('hello')

wc.linecount('chap_14_8.py')