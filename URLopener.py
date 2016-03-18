import os
import sys
import time

addressOfInputFile='siteLinks.txt'

numberOfLinks= 0;

with open(addressOfInputFile, 'r') as temp_f:
    numberOfLinks= sum(1 for _ in temp_f)
temp_f.close()

siteLinks= open(addressOfInputFile, 'r')

for i in range(0,numberOfLinks):
	url=siteLinks.readline().splitlines()[0]
	os.startfile(url)
	time.sleep(5)
	
siteLinks.close()