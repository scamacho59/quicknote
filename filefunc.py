#!/usr/bin/env python3
# Created on July 24, 2020. remember-file.py
# contains the functions for adding and removing
# files for the Quick Note software

import sys
import os.path
from os import path


"""
Given a filename, adds a dot file with
the given name, which will then be set 
as the default file for memories
"""
def add_file(args):
	filename = ''
	for word in args:
		filename += word + ' '
	filename = filename.strip() 
	if path.isfile(filename):
		print('A note with this name already exists. Please choose a different name, delete the other note, or rename the other note.')
		return;
	else:
		dot_name = '.' + filename
		open(dot_name, 'w+')
		with open('.filelist', 'a') as f:
			f.write(filename)
		print('Added new note with name \'' + filename + '\'')


"""
Prints the list of current memory files
"""
def list_files():
	counter = 1
	with open('.filelist', 'r') as f:
		for filename in f:
			filename = str(counter) + '. ' + filename
			print(filename)
			counter += 1
