# -*- coding: utf-8 -*-
import hashlib
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import time

md5 = []
sha1 = []
sha256 = []

average = []
	
def makemd5():
	for line in file.readlines():
		m = hashlib.md5()
		line = line.split('\n')
		line = line[0].encode('utf-8')
		#print(line)
		m.update(line)	
		out.write('+ ' + m.hexdigest() + '\n')
def makesha1():
	for line in file.readlines():
		m = hashlib.sha1()
		line = line.split('\n')
		line = line[0].encode('utf-8')
		#print(line)
		m.update(line)	
		out.write('+ ' + m.hexdigest() + '\n')
def makesha256():
	for line in file.readlines():
		m = hashlib.sha256()
		line = line.split('\n')
		line = line[0].encode('utf-8')
		#print(line)
		m.update(line)	
		out.write('+ ' + m.hexdigest() + '\n')

for i in range(1,30):
	file  = open("base.txt","r")
	out = open("MD5.txt","w")
	start_time = time.time()
	makemd5()
	md5.append(time.time() - start_time)
	file.close()
	out.close()
print('md5 OK!')
for i in range(1,30):
	file  = open("base.txt","r")
	out = open("SHA1.txt","w")
	start_time = time.time()
	makesha1()
	sha1.append(time.time() - start_time)
	file.close()
	out.close()
print('SHA1 OK!')
for i in range(1,30):
	file  = open("base.txt","r")
	out = open("SHA256.txt","w")
	start_time = time.time()
	makesha256()
	sha256.append(time.time() - start_time)
	file.close()
	out.close()
print('SHA256 OK!')

average.append((sum(md5)/float(len(md5))))
average.append((sum(sha1)/float(len(sha1))))
average.append((sum(sha256)/float(len(sha256))))
average = average * 1000
print('average OK')


hashs = ['MD5','SHA-1','SHA-256']
x = np.arange(len(hashs))
y = average
width = 1/1.5
plt.bar(x,y,width,align='center',alpha=0.5)
plt.xticks(x,('MD5','SHA-1','SHA-256'))
plt.ylabel('Average Time for Base Migration in Milliseconds')
plt.title('Comparison among Hash Functions')
plt.show()


#print('[+] Average: %s seconds for md5 hash' % str(sum(average)/float(len(average))))
