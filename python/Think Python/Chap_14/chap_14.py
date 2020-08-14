import os
import pickle

'''
fout = open('output.txt', 'w')

line1 = 'This here is the wattle,\n'
line2 = 'the emblem of our land.\n'
fout.write(line1)
fout.write(line2)
fount.close()
'''

'''
camel = 42.5
check = '%d' % camel
print('%d' % camel)

line3 = 'I have spotted %d camels.' % camel
print(line3)

line4 = 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
print(line4)

cwd = os.getcwd()
print(cwd)
print(os.path.abspath('output.txt'))
print(os.path.exists('memo.txt'))
print(os.path.isdir('New Folder'))
print(os.listdir(cwd))
'''

def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)
		if os.path.isfile(path):
			print(path)
		else:
			walk(path)

#walk('Chap_13')

def walk_py(dirname):
	for root, dirs, files in os.walk(dirname, topdown = True):
		for filename in files:
			print(os.path.join(root, filename))

#walk_py('D:\Dropbox\Python\Code')

def test_pickle(t1):
	s = pickle.dumps(t1)
	t2 = pickle.loads(s)
	print(t2)
	cmd = 'ls -1'
	fp = os.popen('ls', '-1')
	print(fp.read)
	stat = fp.close()

#test_pickle([1, 2, 3])

def test_checksum(filename):
	cmd = 'md5sum ' + filename
	fp = os.system('md tet')
	#res = fp.read()
	#fp.close()
	#print(res)

#test_checksum('output.txt')

