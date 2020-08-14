from subprocess import *
import hashlib, os

d = {}

def checksum_old(afile):
	fin = open(afile, 'rb')
	hasher = hashlib.md5()
	hasher.update(fin.read())
	return hasher.hexdigest()

def checksum(afile):
	return hashlib.md5(afile.encode('utf-8')).hexdigest()
	

def has_duplicates(hfile):
	key = checksum(hfile)
	return key in d


for root, dirs, files in os.walk('D:/Dropbox', topdown = False):
	for file in files:
		try:
			if not has_duplicates(file):
				d[checksum(file)] = root
			else:
				print(file, 'has duplicates in:', sep=' ')
				print(d[checksum(file)])
				print(root)
				print('\n')
		except:
			print('A small problem, just ignore')
'''

for root, dirs, files in os.walk('D:/Dropbox', topdown = False):
	for file in files:
		if not has_duplicates(file):
			d[checksum(file)] = root
		else:
			print(file, 'has duplicates in:', sep=' ')
			print(d[checksum(file)])
			print(root)
			print('\n')
'''