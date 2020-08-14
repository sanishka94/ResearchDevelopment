import os
from datetime import datetime as dt

def get_os_methods():
	print(dir(os))

print(os.getcwd())
os.makedirs('os_module')
print(os.listdir())
os.chdir('D:/Dropbox/Python/Code/Chap_14/os_module')
print(os.getcwd())
os.chdir('D:/Dropbox/Python/Code/Chap_14')
os.rmdir('os_module')


#os.rename('output_1.txt', 'output.txt')

stat = os.stat('output.txt')
md_time = os.stat('output.txt').st_mtime
print(dt.fromtimestamp(md_time))

#print(os.environ.get('HOMEPATH'))

file_path = os.path.join(os.environ.get('HOMEPATH'), 'test.txt')
print(file_path)

print(os.path.basename('/temp/subtemp/test.txt'))
print(os.path.dirname('/temp/subtemp/test.txt'))
print(os.path.split('/temp/subtemp/test.txt'))
print(os.path.exists('/temp/subtemp/test.txt'))
print(os.path.isdir('/temp/subtemp/test.txt'))
print(os.path.isfile('/temp/subtemp/test.txt'))
print(os.path.splitext('/temp/subtemp/test.txt'))
print(dir(os.path))