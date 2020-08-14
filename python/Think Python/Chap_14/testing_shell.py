import os, subprocess

'''
'ABOVE_NORMAL_PRIORITY_CLASS', 'BELOW_NORMAL_PRIORITY_CLASS', 'CREATE_BREAKAWAY_FROM_JOB', 'CREATE_DEFAULT_ERROR_MODE', 'CREATE_NEW_CONSOLE', 'CREATE_NEW_PROCESS_GROUP', 
'CREATE_NO_WINDOW', 'CalledProcessError', 'CompletedProcess', 'DETACHED_PROCESS', 'DEVNULL', 'HIGH_PRIORITY_CLASS', 'Handle', 'IDLE_PRIORITY_CLASS', 'NORMAL_PRIORITY_CLASS', 
'PIPE', 'Popen', 'REALTIME_PRIORITY_CLASS', 'STARTF_USESHOWWINDOW', 'STARTF_USESTDHANDLES', 'STARTUPINFO', 'STDOUT', 'STD_ERROR_HANDLE', 'STD_INPUT_HANDLE', 'STD_OUTPUT_HANDLE', 
'SW_HIDE', 'SubprocessError', 'TimeoutExpired', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_active', 
'_args_from_interpreter_flags', '_cleanup', '_mswindows', '_optim_args_from_interpreter_flags', '_time', '_winapi', 'builtins', 'call', 'check_call', 'check_output', 'errno', 
'getoutput', 'getstatusoutput', 'io', 'list2cmdline', 'msvcrt', 'os', 'run', 'signal', 'sys', 'threading', 'time', 'warnings']
'''

def command_pro_v1(clist):
	slist = []
	for cde in clist:
		stat = subprocess.call(cde, shell=True)
		slist.append(stat)
	print(slist)

def command_pro_v2():
	c = 0
	cde = ''
	while cde != 'exit' or c == 3:
		cde = input('Enter your command:')
		stat = subprocess.call(cde, shell=True)
		if stat == 0: print('Success', c, sep='\t')
		elif stat == 1: print('Failed')
		c += 1

#command_pro_v1(['dir', 'start calc'])
command_pro_v2()