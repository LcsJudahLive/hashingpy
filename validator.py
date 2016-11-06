import time
import hashlib
import getpass

times_plain = []
times_md5 = []
times_sha1 = []
times_sha256 = []

def Validator_Plain(file,username,password):
	for i in range(1,30):
		time_plain = time.time()
		for line in file.readlines():
			if(line.split('|')[0] == username):
				if(line.split('|')[1].split('\n')[0] == password):
					times_plain.append(time.time() - time_plain)
					break


def Validator_Hash(file,hash,password):
	for i in range(1,30):
		time_hash = time.time()
		for line in file.readlines():
			if(line[2:].split('\n')[0] == password):
				if(hash == "md5"):
					times_md5.append(time.time() - time_hash)
					break
				elif(hash == "sha1"):
					times_sha1.append(time.time() - time_hash)
					break
				elif(hash == "sha256"):
					times_sha256.append(time.time() - time_hash)
					break



if __name__ == '__main__':	
	plain = open("base.txt","r")
	md5 = open("MD5.txt","r")
	sha1 = open("SHA1.txt","r")
	sha256 = open("SHA256.txt","r")
	string_md5 = hashlib.md5()
	string_sha1 = hashlib.sha1()
	string_sha256 = hashlib.sha256()
	username = input("Type your username: ")
	password = getpass.getpass()
	username = '.'.join(username.split(' '))
	arg = username.split('\n')[0] + '|' + password.split('\n')[0]
	arg = arg.encode('utf-8')
	string_md5.update(arg)
	string_sha1.update(arg)
	string_sha256.update(arg)
	Validator_Plain(plain,username,password)
	Validator_Hash(md5,"md5",string_md5.hexdigest())
	Validator_Hash(sha1,"sha1",string_sha1.hexdigest())
	Validator_Hash(sha256,"sha256",string_sha256.hexdigest())
	plain.close()
	md5.close()
	sha1.close()
	sha256.close()
	average_plain = (sum(times_plain) / float(len(times_plain))) * 1000
	average_md5 = (sum(times_md5) / float(len(times_md5))) * 1000
	average_sha1 = (sum(times_sha1) / float(len(times_sha1))) * 1000
	average_sha256 = (sum(times_sha256) / float(len(times_sha256))) * 1000
	print("[+] Average Time for Auth in Plain Text (ms): %s" % str(average_plain))
	print("[+] Average Time for Auth in MD5 (ms): %s" % str(average_md5))
	print("[+] Average Time for Auth in SHA-1 (ms): %s" % str(average_sha1))
	print("[+] Average Time for Auth in SHA-256 (ms): %s" % str(average_sha256))
