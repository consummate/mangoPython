#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
	# Backup the entire contents of "folder" into a ZIP file.

	folder = os.path.abspath(folder) # make sure folder is absolute
	# Figure out the filename this code should use based on
	# what files already exist.
	number = 1
	while True:
		zipfilename = os.path.basename(folder)+'_'+str(number)+'.zip'
		if not os.path.exists(zipfilename):
			break
		number = number+1

		#TODO: Create the Zip file.

		#TODO: Walk the entire folder tree and compress the files in each folder.

	backupToZip('C:\\delicious')
