import os
import time

old = set(os.listdir("/media/tanmay"))
oldCount = len(old)

print(oldCount)

while (True):
	newCount = oldCount

	newCount = len(os.listdir("/media/tanmay"))

	if(newCount > oldCount):
		new = set(os.listdir("/media"))
		print("Found new",newCount)
		print(new-old)
		old = new
		oldCount = newCount
		


