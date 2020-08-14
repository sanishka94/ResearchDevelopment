

def sed(str1, str2, file1, file2):
	fin = open(file1)
	fout = open(file2, 'w')
	for line in fin:
		if str1 in line:
			lline = line.strip().split(' ')
			for c in range(len(lline)):
				if lline[c] == str1:
					lline[c] = str2
				c += 1
			fout.write(' '.join(lline) + '\n')
		else:
			fout.write(line)
	fout.close()
	fin.close()


try:
	sed('dragon', 'chicken', 'output.txt', 'newfile.txt')
	print('Process successful')
except:
	print('something went wrong')
