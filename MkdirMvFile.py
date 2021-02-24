#!/usr/bin/python3.5
# #!/usr/bin/python

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# What it does: Move Files to a SubDirectory named after the File-Type.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
import os
import subprocess
import shutil

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Procedures:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def pMkdir(arg):
	if os.path.exists(arg):
		if os.path.isdir(arg):
			print('18:pMkdir(' + arg + '): Good: Directory already exists.')
		else:
			if os.path.isfile(arg):
				print('21:pMkdir(' + arg + '): Fail: Too Bad, it is already a File.')
			else:
				print('23:pMkdir(' + arg + '): Fail: Already exits, but not a Dir and not a File.')
	else:
		os.mkdir(arg)
	if os.path.exists(arg):
		if os.path.isdir(arg):
			print('28:pMkdir(' + arg + '): Good.')
		else:
			if os.path.isfile(arg):
				print('31:pMkdir(' + arg + '): Fail: Strange, it is now a File.')
			else:
				print('33:pMkdir(' + arg + '): Fail: Strange, it exits now but is not a Dir and not a File.')
	else:
		print('35:pMkdir(' + arg + '): Fail: Attempted mkdir but apparently failed.')

def pMkdirMv(  arg1,      arg2, arg3):
	if os.path.exists(arg2):
		pMkdir(arg1)
		if os.path.isdir(arg1):
			TargetPath=arg1 + '/' + arg3
			if os.path.exists(TargetPath):
				print('42: Fail: Target-Path already exists, move will not be attempted.')
			else:
				shutil.move(arg2, TargetPath)
				if os.path.exists(TargetPath):
					print('46: Good: Target-Path now exits.')
					if os.path.isdir(arg2):
						print('48: Fail: Source-Path still exits, even after move.')
				else:
					print('48: Fail: Target-Path does not exit after attempted move,')
					if os.path.isdir(arg2):
						print('51: and, as expected, Source-Path still exits.')
					else:
						print('53: and, Bad-News, Source-Path now is gone!')
		else:
			print('56:pMkdirMv(' + arg1 + ', ' + arg2 + ', ' + arg3 + '): Fail: Target Directory does not exist.')
	else:
		print('59:pMkdirMv(' + arg1 + ', ' + arg2 + ', ' + arg3 + '): Fail: Source does not exist.')
def pMkdirMvFile(DirTargetParent):
	pMkdir(DirTargetParent)
	for bLine in subprocess.Popen("file -N --mime-type * ", shell=True, stdout=subprocess.PIPE).stdout.readlines():
		sLine=bLine.decode('utf8')
		print(sLine)
		aLine = sLine.split(':')
		FileName0 = aLine[0].strip()
		FileName1 = FileName0.replace(' ', '_').replace('/', '_')
		aFileType = aLine[1].split(',')
		FileType0 = aFileType[0].strip()
		FileType1 = FileType0.replace(' ', '_').replace('/', '_')
		if os.path.isfile(FileName0):
			print(FileType0  + '\t' + FileType1  + '\t' + FileName0  + '\t' + FileName1)
			if os.path.dirname(FileName0) == FileType1:
				print( os.path.dirname(FileName0) == FileType1 )
				continue
			DirTarget = DirTargetParent + '/' + FileType1
			pMkdirMv(DirTarget, FileName0, FileName1)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Main:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

pMkdirMvFile(sys.argv[1])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# End
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
