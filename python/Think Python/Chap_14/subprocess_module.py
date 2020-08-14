import subprocess

print(dir(subprocess))

subprocess.check_call('md5sum book.tex', shell=True)