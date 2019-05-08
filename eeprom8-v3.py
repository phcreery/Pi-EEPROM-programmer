# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time, re
import os
GPIO.setmode(GPIO.BCM) #Use chip numbering scheme
#GPIO.setmode(GPIO.BOARD)
#ftd2
delay=0.1
#os.system('clear')



a0=10
a1=9
a2=11
a3=25
a4=8
#a5=7
a5=20
a6=5
#a7=6
a7=26
a8=12
a9=13
a10=19
a11=26
a12=16
a13=20
a14=21

a15=0
a16=0
a17=0

d0=14
d1=15
d2=18
d3=17
d4=27
d5=22
d6=23
d7=24

we=4
oe=3
ce=2


#CE, WE, OE pins (pull down to activate each mode):
GPIO.setup (ce, GPIO.OUT, initial=GPIO.HIGH) #CE
GPIO.setup (oe, GPIO.OUT, initial=GPIO.HIGH) #OE
GPIO.setup (we, GPIO.OUT, initial=GPIO.HIGH) #WE

#Set the chip in standby mode while setting up the rest GPIO:
GPIO.output(ce,1) #CE - high
GPIO.output(oe,1) #OE - high
GPIO.output(we,1) #WE - high

#Address pins set for output (A15, A16, A17 connected to ground):
GPIO.setup (a0, GPIO.OUT, initial=GPIO.LOW) #A0
GPIO.setup (a1,  GPIO.OUT, initial=GPIO.LOW) #A1
GPIO.setup (a2, GPIO.OUT, initial=GPIO.LOW) #A2
GPIO.setup (a3, GPIO.OUT, initial=GPIO.LOW) #A3
GPIO.setup (a4,  GPIO.OUT, initial=GPIO.LOW) #A4
GPIO.setup (a5,  GPIO.OUT, initial=GPIO.LOW) #A5
GPIO.setup (a6,  GPIO.OUT, initial=GPIO.LOW) #A6
GPIO.setup (a7,  GPIO.OUT, initial=GPIO.LOW) #A7
GPIO.setup (a8, GPIO.OUT, initial=GPIO.LOW) #A8
GPIO.setup (a9, GPIO.OUT, initial=GPIO.LOW) #A9
GPIO.setup (a10, GPIO.OUT, initial=GPIO.LOW) #A10
GPIO.setup (a11, GPIO.OUT, initial=GPIO.LOW) #A11
GPIO.setup (a12, GPIO.OUT, initial=GPIO.LOW) #A12
GPIO.setup (a13, GPIO.OUT, initial=GPIO.LOW) #A13
GPIO.setup (a14, GPIO.OUT, initial=GPIO.LOW) #A14

def writemode():
	GPIO.setmode(GPIO.BCM)
	#Data pins set for output (pull down for zeroes):
	#print d0,d1
	GPIO.setup (d0, GPIO.OUT, initial=GPIO.LOW) #D0
	GPIO.setup (d1, GPIO.OUT, initial=GPIO.LOW) #D1
	GPIO.setup (d2, GPIO.OUT, initial=GPIO.LOW) #D2
	GPIO.setup (d3, GPIO.OUT, initial=GPIO.LOW) #D3
	GPIO.setup (d4, GPIO.OUT, initial=GPIO.LOW) #D4
	GPIO.setup (d5, GPIO.OUT, initial=GPIO.LOW) #D5
	GPIO.setup (d6, GPIO.OUT, initial=GPIO.LOW) #D6
	GPIO.setup (d7, GPIO.OUT, initial=GPIO.LOW) #D7
	#print "Write Mode"

	return

def readmode():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup (d0, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D0
	GPIO.setup (d1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D1
	GPIO.setup (d2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D2
	GPIO.setup (d3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D3
	GPIO.setup (d4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D4
	GPIO.setup (d5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D5
	GPIO.setup (d6, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D6
	GPIO.setup (d7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D7


	return

def readone():
	i=0
	try:
		while (i==0):
			A=[]
			A=raw_input("Type memory address to read (11 bits): ")

			if not re.match("^[0-1]*$", A) or (len(A) != 11):
				print "Error! Only 1 and 0 allowed. Please type 15 bits."

			else:
				i=1
				A=map(int, A)
	except KeyboardInterrupt:
		print "Keyboard Interrupt.\nPerforming GPIO cleanup."
		#GPIO.cleanup()
	print A[0],A[1],A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9],A[10]
	#Set address bus:
	GPIO.output(a0,A[10])    #A0
	GPIO.output(a1,A[9])     #A1
	GPIO.output(a2,A[8])    #A2
	GPIO.output(a3,A[7])    #A3
	GPIO.output(a4,A[6])     #A4
	GPIO.output(a5,A[5])     #A5
	GPIO.output(a6,A[4])     #A6
	GPIO.output(a7,A[3])     #A7
	GPIO.output(a8,A[2])    #A8
	GPIO.output(a9,A[1])    #A9
	GPIO.output(a10,A[0])   #A10
	#GPIO.output(26,A[11])   #A11
	#GPIO.output(16,A[12])   #A12
	#GPIO.output(20,A[13])   #A13
	#GPIO.output(21,A[14])   #A14
	#time.sleep(20)
	#Operation Loop
	try:
		print "Turning on the chip and setting it to output mode."
		GPIO.output(3,0) #OE - low - enable output
		GPIO.output(2,0) #CE - low - turn on the chip
		time.sleep(delay)
		print "Reading the address."

		#set data variables
		D0= GPIO.input(14)
		D1= GPIO.input(15)
		D2= GPIO.input(18)
		D3= GPIO.input(17)
		D4= GPIO.input(27)
		D5= GPIO.input(22)
		D6= GPIO.input(23)
		D7= GPIO.input(24)

		#print "D0 D1 D2 D3 D4 D5 D6 D7"
		print str(D7)+" "+str(D6)+" "+str(D5)+" "+str(D4)+" "+str(D3)+" "+str(D2)+" "+str(D1)+" "+str(D0)
		GPIO.output(2,1) #CE - high - standby mode
		GPIO.output(3,1) #OE - high - disable output
		#GPIO.cleanup()

	except KeyboardInterrupt:
		print "Keyboard Interrupt.\nPerforming GPIO cleanup."
		#GPIO.cleanup()

	return

def readone2(A):
	#A= array ex. [1,1,0,0,1,...]
	i=0
	
	#Set address bus:
	GPIO.output(a0,A[10])    #A0
	GPIO.output(a1,A[9])     #A1
	GPIO.output(a2,A[8])    #A2
	GPIO.output(a3,A[7])    #A3
	GPIO.output(a4,A[6])     #A4
	GPIO.output(a5,A[5])     #A5
	GPIO.output(a6,A[4])     #A6
	GPIO.output(a7,A[3])     #A7
	GPIO.output(a8,A[2])    #A8
	GPIO.output(a9,A[1])    #A9
	GPIO.output(a10,A[0])   #A10
	#GPIO.output(26,A[11])   #A11
	#GPIO.output(16,A[12])   #A12
	#GPIO.output(20,A[13])   #A13
	#GPIO.output(21,A[14])   #A14

	#Operation Loop
	try:
		#print "Turning on the chip and setting it to output mode."
		GPIO.output(3,0) #OE - low - enable output
		GPIO.output(2,0) #CE - low - turn on the chip
		time.sleep(delay)
		#print "Reading the address."

		#set data variables
		D0= GPIO.input(14)
		D1= GPIO.input(15)
		D2= GPIO.input(18)
		D3= GPIO.input(17)
		D4= GPIO.input(27)
		D5= GPIO.input(22)
		D6= GPIO.input(23)
		D7= GPIO.input(24)

		#print "D0 D1 D2 D3 D4 D5 D6 D7"
		#print str(D7)+" "+str(D6)+" "+str(D5)+" "+str(D4)+" "+str(D3)+" "+str(D2)+" "+str(D1)+" "+str(D0)
		data=str(D7)+str(D6)+str(D5)+str(D4)+str(D3)+str(D2)+str(D1)+str(D0)
		GPIO.output(2,1) #CE - high - standby mode
		GPIO.output(3,1) #OE - high - disable output
		#GPIO.cleanup()

	except KeyboardInterrupt:
		print "Keyboard Interrupt.\nPerforming GPIO cleanup."
		#GPIO.cleanup()

	return	data
	
def writeone():

	j=0
	while (j==0):
		A=[]
		A=raw_input("Type memory address (11 bits): ")

		if not re.match("^[0-1]*$", A) or (len(A) != 11):
			print "Error! Only 1 and 0 allowed. Please type 11 bits."
		else:
			j=1
			A=map(int, A)
			#number = bin(int("AF", 16))[2:].zfill(8)
			#print "AF=",number
	i=0
	while (i==0):
		D=[]
		D=raw_input("Type data byte: ")

		if not re.match("^[0-1]*$", D) or (len(D) !=8):
			print "Error! Only 1 and 0 allowed. Please type 8 bits"
		else:
			i=1
			D=map(int, D)

	#print"Are you sure you wish to write to the chip?(Y/n):"
	#answer=raw_input()
	answer="y"

	#Operation Loop
	try:

		if (answer=="y" or answer=="Y"):
			print "Turning on the chip."
			GPIO.output(ce,0) #CE - low - turn on the chip
			time.sleep(delay+0.1)
			print "Starting chip programming sequence."
			print "Writing", D, " to address: ", A

			#Actual write operation:
			print "Writing user data to selected address."
			#Set address bus:
			GPIO.output(a0,A[10])
			GPIO.output(a1,A[9])
			GPIO.output(a2,A[8])
			GPIO.output(a3,A[7])
			GPIO.output(a4,A[6])
			GPIO.output(a5,A[5])
			GPIO.output(a6,A[4])
			GPIO.output(a7,A[3])
			GPIO.output(a8,A[2])
			GPIO.output(a9,A[1])
			GPIO.output(a10,A[0])
	#		GPIO.output(a11,A[11])
	#		GPIO.output(a12,A[12])
	#		GPIO.output(a13,A[13])
	#		GPIO.output(a14,A[14])
			time.sleep(delay)

			GPIO.output(we,0) #WE - low - latched address
			print "User address latched."
			time.sleep(delay)
			#Set data bus:
			GPIO.output(d0,D[7])
			GPIO.output(d1,D[6])
			GPIO.output(d2,D[5])
			GPIO.output(d3,D[4])
			GPIO.output(d4,D[3])
			GPIO.output(d5,D[2])
			GPIO.output(d6,D[1])
			GPIO.output(d7,D[0])
			time.sleep(delay)
	#		GPIO.output(we,0)
			GPIO.output(we,1) #WE - high - latched data
			print "User data latched."

			GPIO.output(ce,1) #CE - high - standby chip
			print "Chip on standby."
			time.sleep(0.1)
			#GPIO.cleanup()
			print "Performing GPIO cleanup.\nOperation Completed."

		else:
			print "Operation Aborted.\nPerforming GPIO cleanup."
			#GPIO.cleanup()

	except KeyboardInterrupt:
		print "Keyboard Interrupt.\nPerforming GPIO cleanup."
		#GPIO.cleanup()

	return


def eraseall():
	i=0
	while (i==0):
		D=[]
		D=raw_input("Type data byte: ")
	
		if not re.match("^[0-1]*$", D) or (len(D) !=8):
			print "Error! Only 1 and 0 allowed. Please type 8 bits"
		else:
			i=1
			D=map(int, D)

	#D="00000000"
	D=map(int, D)
	Aa=0
	print"Are you sure you want to erase the entire chip?(Y/n):"
	answer=raw_input()

	#Operation Loop
	try:

		if (answer=="y" or answer=="Y"):
			print "Turning on the chip."
			GPIO.output(ce,0) #CE - low - turn on the chip
			time.sleep(delay)

			run=1
			while (run==1):
				#Aa=Aa+1
				#A=map(int, Aa)
				A="{0:011b}".format(Aa)
				print "Erasing line:", A
				A=map(int, A)
				#Actual write operation:
				#print "Writing user data to selected address."
				#Set address bus:
				GPIO.output(a0,A[0])
				GPIO.output(a1,A[1])
				GPIO.output(a2,A[2])
				GPIO.output(a3,A[3])
				GPIO.output(a4,A[4])
				GPIO.output(a5,A[5])
				GPIO.output(a6,A[6])
				GPIO.output(a7,A[7])
				GPIO.output(a8,A[8])
				GPIO.output(a9,A[9])
				GPIO.output(a10,A[10])
	#			GPIO.output(a11,A[11])
	#			GPIO.output(a12,A[12])
	#			GPIO.output(a13,A[13])
	#			GPIO.output(a14,A[14])
				GPIO.output(we,0) #WE - low - latched address
				#print "User address latched."
				time.sleep(0.005)
				
				#Set data bus:
				GPIO.output(d0,D[7])
				GPIO.output(d1,D[6])
				GPIO.output(d2,D[5])
				GPIO.output(d3,D[4])
				GPIO.output(d4,D[3])
				GPIO.output(d5,D[2])
				GPIO.output(d6,D[1])
				GPIO.output(d7,D[0])
				GPIO.output(we,1) #WE - high - latched data
				#print "User data latched."
				time.sleep(0.005)
				if (A==[1,1,1,1,1,1,1,1,1,1,1]):
					run=0
				Aa=Aa+1

			time.sleep(delay)
			GPIO.output(ce,1) #CE - high - standby chip
			print "Chip on standby."
			print "Erase Successful."
			time.sleep(delay)
			#GPIO.cleanup()
			print "Performing GPIO cleanup.\nOperation Completed."
	
		else:
			print "Operation Aborted.\nPerforming GPIO cleanup."
		#GPIO.cleanup()
	
	except KeyboardInterrupt:
		print "Keyboard Interrupt.\nPerforming GPIO cleanup."
		#GPIO.cleanup()
	return


def readsection():

	i=0
	try:
		while (i==0):
			A=[]
			A=raw_input("Type memory address to read (11 bits): ")
	
			if not re.match("^[0-1]*$", A) or (len(A) != 11):
				print "Error! Only 1 and 0 allowed. Please type 11 bits."
	
			else:
				i=1
				#A=map(int, A)
	except KeyboardInterrupt:
		print "Keyboard Interrupt.\nPerforming GPIO cleanup."
		GPIO.cleanup()
	i=0
	try:
		n=[]
		n=raw_input("Number of addresses to read: ")
	except KeyboardInterrupt:
		print "Keyboard Interrupt.\nPerforming GPIO cleanup."
		GPIO.cleanup()
	GPIO.output(2,0) #CE - low - turn on the chip
	n=int(n)
	n2=0
	while (n2 < n):
		
		A=map(int, A)               #convert str to array
		
		#Set address bus:
		GPIO.output(a0,A[10])	#A0
		GPIO.output(a1,A[9])     #A1
		GPIO.output(a2,A[8])    #A2
		GPIO.output(a3,A[7])    #A3
		GPIO.output(a4,A[6])     #A4
		GPIO.output(a5,A[5])     #A5
		GPIO.output(a6,A[4])     #A6
		GPIO.output(a7,A[3])     #A7
		GPIO.output(a8,A[2])    #A8
		GPIO.output(a9,A[1])    #A9
		GPIO.output(a10,A[0])   #A10
#		GPIO.output(26,A[11])   #A11
#		GPIO.output(16,A[12])   #A12
#		GPIO.output(20,A[13])   #A13
#		GPIO.output(21,A[14])   #A14


		#Operation Loop
		try:
			#print "Turning on the chip and setting it to output mode."
			GPIO.output(3,0) #OE - low - enable output
			#GPIO.output(2,0) #CE - low - turn on the chip
			time.sleep(0.01)
			#print "Reading the address."
		
			#set data variables
			D0= GPIO.input(14)
			D1= GPIO.input(15)
			D2= GPIO.input(18)
			D3= GPIO.input(17)
			D4= GPIO.input(27)
			D5= GPIO.input(22)
			D6= GPIO.input(23)
			D7= GPIO.input(24)
			
			data=str(D7)+str(D6)+str(D5)+str(D4)+str(D3)+str(D2)+str(D1)+str(D0)
			address=''.join(str(e) for e in A)
			#print data
			#print ''.join(str(e) for e in A),str(D7)+str(D6)+str(D5)+str(D4)+str(D3)+str(D2)+str(D1)+str(D0)
			
			if (n2 % 2 == 0):
				if (data=="00000001"):
					print address,data,"Add"
				elif (data=="00000011"):
					print address,data,"Load A"
				elif (data=="00000010"):
					print address,data,"Subtract"
				elif (data=="00000100"):
						print address,data,"Load B"
				elif (data=="00000101"):
						print address,data,"Load C"
				elif (data=="00000110"):
						print address,data,"Store C"
				elif (data=="00001010"):
						print address,data,"Halt"
				elif (data=="00001011"):
						print address,data,"Jump"
				elif (data=="00001100"):
						print address,data,"Display (Command)"
				elif (data=="00001101"):
						print address,data,"Display (Text)"
				elif (data=="00001110"):
						print address,data,"Display (From RAM)"
				elif (data=="00001111"):
						print address,data,"Get Key (Put into RAM)"
				else:
					print address,data,"!UNKNOW COMMAND!"
			else:
				print address,data,"-"

			#GPIO.output(2,1) #CE - high - standby mode
			GPIO.output(3,1) #OE - high - disable output
#			GPIO.cleanup()
			time.sleep(0.01)
		except KeyboardInterrupt:
			print "Keyboard Interrupt.\nPerforming GPIO cleanup."
			GPIO.cleanup()
		

		A = ''.join(str(e) for e in A)   #array to str

                #print "1",A
                a=int(A, 2)                      #convert str to int       binary to  dec
                #print "2",a
                a=a+1
                #print "3",a
                A="{0:011b}".format(a)            #back to  binary (dec to str)
                #print "4",A
                A=map(int, A)                     #back to array    (str to array)
                #print "5",A
                n2=n2+1



	GPIO.output(2,1) #CE - high - turn off the chip



def readsection2():

	i=0
	try:
		while (i==0):
			A=[]
			A=raw_input("Type initial memory address to read (11 bits)(Blank=0): ")
	
			if (A==""):
				A="00000000000"
			if not re.match("^[0-1]*$", A) or (len(A) != 11):
				print "Error! Only 1 and 0 allowed. Please type 11 bits."
			
			else:
				i=1
				#A=map(int, A)
	except KeyboardInterrupt:
		print "Keyboard Interrupt.\nPerforming GPIO cleanup."
		GPIO.cleanup()
	i=0
	try:
		n=[]
		n=raw_input("Number of addresses to read: ")
	except KeyboardInterrupt:
		print "Keyboard Interrupt.\nPerforming GPIO cleanup."
		GPIO.cleanup()
	GPIO.output(2,0) #CE - low - turn on the chip
	n=int(n)
	print "     Address:   Binary:    Command: 	  Data: Binary  Int Hex Ascii" 
	n2=0
	while (n2 < n):
		
		A=map(int, A)               #convert str to array
		
		#Set address bus:
		GPIO.output(a0,A[10])	#A0
		GPIO.output(a1,A[9])     #A1
		GPIO.output(a2,A[8])    #A2
		GPIO.output(a3,A[7])    #A3
		GPIO.output(a4,A[6])     #A4
		GPIO.output(a5,A[5])     #A5
		GPIO.output(a6,A[4])     #A6
		GPIO.output(a7,A[3])     #A7
		GPIO.output(a8,A[2])    #A8
		GPIO.output(a9,A[1])    #A9
		GPIO.output(a10,A[0])   #A10
#		GPIO.output(26,A[11])   #A11
#		GPIO.output(16,A[12])   #A12
#		GPIO.output(20,A[13])   #A13
#		GPIO.output(21,A[14])   #A14


		#Operation Loop
		try:
			#print "Turning on the chip and setting it to output mode."
			GPIO.output(3,0) #OE - low - enable output
			#GPIO.output(2,0) #CE - low - turn on the chip
			time.sleep(0.01)
			#print "Reading the address."
		
			#set data variables
			D0= GPIO.input(14)
			D1= GPIO.input(15)
			D2= GPIO.input(18)
			D3= GPIO.input(17)
			D4= GPIO.input(27)
			D5= GPIO.input(22)
			D6= GPIO.input(23)
			D7= GPIO.input(24)
			
			data1=str(D7)+str(D6)+str(D5)+str(D4)+str(D3)+str(D2)+str(D1)+str(D0)
			address1=''.join(str(e) for e in A)
			#print data
			#print ''.join(str(e) for e in A),str(D7)+str(D6)+str(D5)+str(D4)+str(D3)+str(D2)+str(D1)+str(D0)
			
			#GPIO.output(2,1) #CE - high - standby mode
			GPIO.output(3,1) #OE - high - disable output
#			GPIO.cleanup()
			time.sleep(0.01)
		except KeyboardInterrupt:
			print "Keyboard Interrupt.\nPerforming GPIO cleanup."
			GPIO.cleanup()
			
		A = ''.join(str(e) for e in A)   #array to str
		#print "1",A
		a=int(A, 2)                      #convert str to int       binary to  dec
		#print "2",a
		a=a+1
		#print "3",a
		A="{0:011b}".format(a)            #back to  binary (dec to str)
		#print "4",A
		A=map(int, A)                     #back to array    (str to array)
		#print "5",A
		n2=n2+1
		
		
		#second round
		A=map(int, A)               #convert str to array
		
		#Set address bus:
		GPIO.output(a0,A[10])	#A0
		GPIO.output(a1,A[9])     #A1
		GPIO.output(a2,A[8])    #A2
		GPIO.output(a3,A[7])    #A3
		GPIO.output(a4,A[6])     #A4
		GPIO.output(a5,A[5])     #A5
		GPIO.output(a6,A[4])     #A6
		GPIO.output(a7,A[3])     #A7
		GPIO.output(a8,A[2])    #A8
		GPIO.output(a9,A[1])    #A9
		GPIO.output(a10,A[0])   #A10
#		GPIO.output(26,A[11])   #A11
#		GPIO.output(16,A[12])   #A12
#		GPIO.output(20,A[13])   #A13
#		GPIO.output(21,A[14])   #A14


		#Operation Loop
		try:
			#print "Turning on the chip and setting it to output mode."
			GPIO.output(3,0) #OE - low - enable output
			#GPIO.output(2,0) #CE - low - turn on the chip
			time.sleep(0.01)
			#print "Reading the address."
		
			#set data variables
			D0= GPIO.input(14)
			D1= GPIO.input(15)
			D2= GPIO.input(18)
			D3= GPIO.input(17)
			D4= GPIO.input(27)
			D5= GPIO.input(22)
			D6= GPIO.input(23)
			D7= GPIO.input(24)
			
			data2=str(D7)+str(D6)+str(D5)+str(D4)+str(D3)+str(D2)+str(D1)+str(D0)
			address2=''.join(str(e) for e in A)
			#print data
			#print ''.join(str(e) for e in A),str(D7)+str(D6)+str(D5)+str(D4)+str(D3)+str(D2)+str(D1)+str(D0)
			#GPIO.output(2,1) #CE - high - standby mode
			GPIO.output(3,1) #OE - high - disable output
#			GPIO.cleanup()
			time.sleep(0.01)
		except KeyboardInterrupt:
			print "Keyboard Interrupt.\nPerforming GPIO cleanup."
			GPIO.cleanup()
			
		A = ''.join(str(e) for e in A)   #array to str
		#print "1",A
		a=int(A, 2)                      #convert str to int       binary to  dec
		#print "2",a
		a=a+1
		#print "3",a
		A="{0:011b}".format(a)            #back to  binary (dec to str)
		#print "4",A
		A=map(int, A)                     #back to array    (str to array)
		#print "5",A
		n2=n2+1
		
		if (n2 % 2 == 0):
			if (data1=="00000001"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Add			",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00000011"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Load A			",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00000010"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Subtract			",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00000100"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Load B			",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00000101"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Load C			",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00000110"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Store C		",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00001010"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Halt			",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00001011"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Jump			",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00001100"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Display (Command)	",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00001101"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Display (Text)		",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00001110"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Display (From RAM)	",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00001111"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Get Key (Put into RAM)",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00001001"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Compare & Jump		",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00010000"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"C > A			",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00010001"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"C > B			",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00010010"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"Jump from RAM			",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00010011"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"DISP command from RAM	",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			elif (data1=="00000000"):
				print '{:03d}'.format(int(address1, 2)),address1,data1,"			",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			else:
				print '{:03d}'.format(int(address1, 2)),address1,data1,"!UNKNOW COMMAND!	",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
		else:
			print address1,data1,"error"


	GPIO.output(2,1) #CE - high - turn off the chip

def writesection():
	i=0
	while (i==0):
		Ainit=[]
		Ainit=raw_input("Type starting address (Enter=0): ")
		if (Ainit==""):
				Ainit="00000000000"
		if not re.match("^[0-1]*$", Ainit) or (len(Ainit) !=(11 or 0)):
			print "Error! Only 1 and 0 allowed. Please type 11 bits"
		else:
			i=1
			#A=map(int, Ainit)

	

	#D="00000000"
	#D=map(int, D)
	#Aa=0
	#print"Are you sure you want to erase the entire chip?(Y/n):"
	#answer=raw_input()

	#Operation Loop
	try:
		print "Turning on the chip."
		GPIO.output(ce,0) #CE - low - turn on the chip
		time.sleep(delay)
		GPIO.output(oe,1)
		
		
		
		run2=1
		try:    # total run 2
			
			Astr1=Ainit
			run=1
			while (run==1):   #total run 
													#read both
				readmode()
				
				Aa1=map(int, Astr1)                 
				#print "Address1:",Astr1,Aa1
				data1=readone2(Aa1)
				#print "Data1:",data1
				
				#Aa = ''.join(str(e) for e in Astr)   #array to str
				Aint1=int(Astr1, 2)                      #convert str to int       binary to  dec
				Aint2=Aint1+1
				Astr2="{0:011b}".format(Aint2)            #back to  binary (dec to str)
				Aa2=map(int, Astr2)                     #back to array    (str to array)
				
				
				#Aint=Aint+1
				#Aa=map(int, Aint)
				
				#print "Address2:",Aint2,Aa2
				data2=readone2(Aa2)
				address1=Astr1
				address2=Astr2
				#print "Data2",data2
				
				
				Aint2=int(Astr2, 2)                      #convert str to int       binary to  dec
				Aint1=Aint2+1
				Astr1="{0:011b}".format(Aint1)            #back to  binary (dec to str)
				Aa1=map(int, Astr1) 
				#print '{:03d}'.format(int(address1, 2)),address1,data1,"Add		",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			
				print
				print
				#print "Line:       Command:"
				print "     Address:   Binary:    Command: 	  Data: Address     Binary   Int Ascii" 
	
				#print "Currently:"
				if (data1=="00000001"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Add			", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00000011"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Load A		", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00000010"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Subtract		", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00000100"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Load B		", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00000101"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Load C		", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00000110"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Store C		", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00001010"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Halt			", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00001001"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Compare			", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00001011"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Jump			", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00001100"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Display (Command)	", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00001101"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Display (Text)	", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00001110"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Display (From RAM)	", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00001111"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Get Key (put into RAM)	", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00010000"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"C > A	", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00010001"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"C > B	", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00010010"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Jump from RAM	", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00010011"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"Disp Command from RAM	", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				elif (data1=="00000000"):
					print '{:03d}'.format(int(address1, 2)),address1,data1,"-			", address2,data2,'{:03d}'.format(int(data2, 2)), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
				else:
					print '{:03d}'.format(int(address1, 2)),address1,data1,"!UNKNOW COMMAND!", address2,data2

				print
				
				
				
				
				
				#first write command
				
				#writemode()
				write=False
				i=0
				while (i==0):
					D=[]
					D=raw_input("New Command  (q=Quit)(Enter=Do not change): ")
					if (D=="add"):
						D="00000001"
						i=1
						write=True
					elif (D=="sub"):
						D="00000010"
						i=1
						write=True
					elif (D=="lda"):
						D="00000011"
						i=1
						write=True
					elif (D=="ldb"):
						D="00000100"
						i=1
						write=True
					elif (D=="ldc"):
						D="00000101"
						i=1
						write=True
					elif (D=="stc"):
						D="00000110"
						i=1
						write=True
					elif (D=="comp"):
						D="00001001"
						i=1
						write=True
					elif (D=="halt"):
						D="00001010"
						i=1
						write=True
					elif (D=="jmp"):
						D="00001011"
						i=1
						write=True
					elif (D=="dispc"):
						D="00001100"
						i=1
						write=True
					elif (D=="dispt"):
						D="00001101"
						i=1
						write=True
					elif (D=="dispr"):
						D="00001110"
						i=1
						write=True
					elif (D=="getkey"):
						D="00001111"
						i=1
						write=True
					elif (D=="c2a"):
						D="00010000"
						i=1
						write=True
					elif (D=="c2b"):
						D="00010001"
						i=1
						write=True
					elif (D=="jmpr"):
						D="00010010"
						i=1
						write=True
					elif (D=="dispcr"):
						D="00010011"
						i=1
						write=True
					elif (D==""):
						D="00000000"
						i=1
						write=False
					elif (D=="q"):
						D="00000000"
						i=1
						run=0
						run2=0
						break
						write=False
					else:
						print "Unknown Command"
						write=False
				if (run==0):
					break
				
				#writemode()
				if (write==True):
					writemode()
					GPIO.output(ce,0)
					time.sleep(0.005)
					
					print "Writing:", address1, D 
					D=map(int, D)
					#Aa=Aa+1
					A=map(int, address1)
					#A="{0:011b}".format(Aint2)
					#A=Astr1
					time.sleep(delay)
					#print A,D
					#Aa=map(int, A)
					#Actual write operation:
					#print "Writing user data to selected address."
					#Set address bus:
					GPIO.output(a0,A[10])
					GPIO.output(a1,A[9])
					GPIO.output(a2,A[8])
					GPIO.output(a3,A[7])
					GPIO.output(a4,A[6])
					GPIO.output(a5,A[5])
					GPIO.output(a6,A[4])
					GPIO.output(a7,A[3])
					GPIO.output(a8,A[2])
					GPIO.output(a9,A[1])
					GPIO.output(a10,A[0])
	#				GPIO.output(a11,A[11])
	#				GPIO.output(a12,A[12])
	#				GPIO.output(a13,A[13])
	#				GPIO.output(a14,A[14])
					GPIO.output(we,0) #WE - low - latched address
					#print "User address latched."
					time.sleep(0.05)
					
					#Set data bus:
					GPIO.output(d0,D[7])
					GPIO.output(d1,D[6])
					GPIO.output(d2,D[5])
					GPIO.output(d3,D[4])
					GPIO.output(d4,D[3])
					GPIO.output(d5,D[2])
					GPIO.output(d6,D[1])
					GPIO.output(d7,D[0])
					GPIO.output(we,1) #WE - high - latched data
					#print "User data latched."
					time.sleep(0.05)
					GPIO.output(ce,1)
				
				#second write 2 arguement
				
				write=False
				i=0
				while (i==0):
					Dstr=[]
					Dstr=raw_input("New Arguement (0-255)(Enter=Do not change): ")
					if (Dstr==""):
						i=1
						write=False
						break
					Dint=int(Dstr)
					if (Dint<0 or Dint>255):
						print "Only 0 through 255 allowed"
						write=False
						i=0
					elif (D==0):
						write=False
						
						i=1
					else:
						i=1
						write=True
				
				
				
				if (write==True):
					writemode()
					time.sleep(0.005)
					GPIO.output(ce,0)
					time.sleep(0.005)
					Dstr="{0:08b}".format(int(Dint))
					print "Writing:", address2, Dstr
					time.sleep(delay)
					D=map(int, Dstr)
					A=map(int, address2)
					#print A,D
					#Actual write operation:
					#print "Writing user data to selected address."
					#Set address bus:
					GPIO.output(a0,A[10])
					GPIO.output(a1,A[9])
					GPIO.output(a2,A[8])
					GPIO.output(a3,A[7])
					GPIO.output(a4,A[6])
					GPIO.output(a5,A[5])
					GPIO.output(a6,A[4])
					GPIO.output(a7,A[3])
					GPIO.output(a8,A[2])
					GPIO.output(a9,A[1])
					GPIO.output(a10,A[0])
	#				GPIO.output(a11,A[11])
	#				GPIO.output(a12,A[12])
	#				GPIO.output(a13,A[13])
	#				GPIO.output(a14,A[14])
					time.sleep(0.05)
					GPIO.output(we,0) #WE - low - latched address
					#print "User address latched."
					time.sleep(0.05)
					
					#Set data bus:
					GPIO.output(d0,D[7])
					GPIO.output(d1,D[6])
					GPIO.output(d2,D[5])
					GPIO.output(d3,D[4])
					GPIO.output(d4,D[3])
					GPIO.output(d5,D[2])
					GPIO.output(d6,D[1])
					GPIO.output(d7,D[0])
					GPIO.output(we,1) #WE - high - latched data
					#print "User data latched."
					time.sleep(0.05)
					GPIO.output(ce,1)
				
				if (Aa2==[1,1,1,1,1,1,1,1,1,1,1]):
					run=0
					run2=0
				Aint1=Aint1+1
	
			#time.sleep(delay)
			GPIO.output(ce,1) #CE - high - standby chip
			print "Chip on standby."

			time.sleep(delay)
			#GPIO.cleanup()
			#print "Performing GPIO cleanup.\nOperation Completed."
	
		except KeyboardInterrupt:
			print "Operation Aborted.\nPerforming GPIO cleanup."
		#GPIO.cleanup()
	
	except KeyboardInterrupt:
		print "Keyboard Interrupt.\nPerforming GPIO cleanup."
		#GPIO.cleanup()
	return
	
def writesection2():
	

		
		
		
		
		
		
		

	GPIO.output(2,1) #CE - high - turn off the chip	

	
def saveprog():
	os.system("ls *.txt")
	name=raw_input("Program Name: ")
	print "Opening: "+name
	file = open(name+'.txt','w') 
	
	#file.write(“Hello World”) 
	
	
	i=0
	
	A="00000000000"
	n="256"
	
	GPIO.output(2,0) #CE - low - turn on the chip
	n=int(n)
	n2=0
	while (n2 < n):
		
		A=map(int, A)               #convert str to array
		
		#Set address bus:
		GPIO.output(a0,A[10])	#A0
		GPIO.output(a1,A[9])     #A1
		GPIO.output(a2,A[8])    #A2
		GPIO.output(a3,A[7])    #A3
		GPIO.output(a4,A[6])     #A4
		GPIO.output(a5,A[5])     #A5
		GPIO.output(a6,A[4])     #A6
		GPIO.output(a7,A[3])     #A7
		GPIO.output(a8,A[2])    #A8
		GPIO.output(a9,A[1])    #A9
		GPIO.output(a10,A[0])   #A10
#		GPIO.output(26,A[11])   #A11
#		GPIO.output(16,A[12])   #A12
#		GPIO.output(20,A[13])   #A13
#		GPIO.output(21,A[14])   #A14


		#Operation Loop
		try:
			#print "Turning on the chip and setting it to output mode."
			GPIO.output(3,0) #OE - low - enable output
			#GPIO.output(2,0) #CE - low - turn on the chip
			time.sleep(0.01)
			#print "Reading the address."
		
			#set data variables
			D0= GPIO.input(14)
			D1= GPIO.input(15)
			D2= GPIO.input(18)
			D3= GPIO.input(17)
			D4= GPIO.input(27)
			D5= GPIO.input(22)
			D6= GPIO.input(23)
			D7= GPIO.input(24)
			
			data=str(D7)+str(D6)+str(D5)+str(D4)+str(D3)+str(D2)+str(D1)+str(D0)
			file.write(data+"\n") 
			address=''.join(str(e) for e in A)
			#print data
			#print ''.join(str(e) for e in A),str(D7)+str(D6)+str(D5)+str(D4)+str(D3)+str(D2)+str(D1)+str(D0)
			
			if (n2 % 2 == 0):
				if (data=="00000001"):
					print address,data,"Add"
				elif (data=="00000011"):
					print address,data,"Load A"
				elif (data=="00000010"):
					print address,data,"Subtract"
				elif (data=="00000100"):
						print address,data,"Load B"
				elif (data=="00000101"):
						print address,data,"Load C"
				elif (data=="00000110"):
						print address,data,"Store C"
				elif (data=="00001010"):
						print address,data,"Halt"
				elif (data=="00001011"):
						print address,data,"Jump"
				elif (data=="00001100"):
						print address,data,"Display (Command)"
				elif (data=="00001101"):
						print address,data,"Display (Text)"
				elif (data=="00001110"):
						print address,data,"Display (From RAM)"
				elif (data=="00001111"):
						print address,data,"Get Key (Put into RAM)"
				else:
					print address,data,"!UNKNOW COMMAND!"
			else:
				print address,data,"-"

			#GPIO.output(2,1) #CE - high - standby mode
			GPIO.output(3,1) #OE - high - disable output
#			GPIO.cleanup()
			time.sleep(0.01)
		except KeyboardInterrupt:
			print "Keyboard Interrupt.\nPerforming GPIO cleanup."
			GPIO.cleanup()
		

		A = ''.join(str(e) for e in A)   #array to str

                #print "1",A
                a=int(A, 2)                      #convert str to int       binary to  dec
                #print "2",a
                a=a+1
                #print "3",a
                A="{0:011b}".format(a)            #back to  binary (dec to str)
                #print "4",A
                A=map(int, A)                     #back to array    (str to array)
                #print "5",A
                n2=n2+1



	GPIO.output(2,1) #CE - high - turn off the chip
	
	
	
	file.close()
	

	
def writeprog():
	print
	os.system("ls *.txt")
	name=raw_input("Program Name (Without .txt): ")
	print "Opening: "+name
	File = open(name+'.txt','r') 
	
	
	i=0
	Ainit="00000000000"
	
	


	#Operation Loop
	try:
		print "Turning on the chip."
		GPIO.output(ce,0) #CE - low - turn on the chip
		time.sleep(delay)
		GPIO.output(oe,1)
		
		
		
		run2=1
		try:    # total run 2
			
			Astr1=Ainit
			Aint1=int(Astr1, 2) 
			run=1
			while (run==1):   #total run 
													#read both
													
				#readmode()
				
				#Aa1=map(int, Astr1)                 
				#print "Address1:",Astr1,Aa1
				#data1=readone2(Aa1)
				#print "Data1:",data1
				
				#Aa = ''.join(str(e) for e in Astr)   #array to str
				#Aint1=int(Astr1, 2)                      #convert str to int       binary to  dec
				#Aint1=Aint1+1
				Astr1="{0:011b}".format(Aint1)            #back to  binary (dec to str)
				Aa1=map(int, Astr1)                     #back to array    (str to array)
				
				
				#Aint=Aint+1
				#Aa=map(int, Aint)
				
				#print "Address2:",Aint2,Aa2
				#data2=readone2(Aa2)
				address1=Astr1
				#address2=Astr2
				#print "Data2",data2
				
				
				#Aint2=int(Astr2, 2)                      #convert str to int       binary to  dec
				#Aint1=Aint2+1
				#Astr1="{0:011b}".format(Aint1)            #back to  binary (dec to str)
				#Aa1=map(int, Astr1) 
				#print '{:03d}'.format(int(address1, 2)),address1,data1,"Add		",data2,'{:03d}'.format(int(data2, 2)), hex(int(data2, 2))[2:].zfill(2), str(hex(int(data2, 2))[2:].zfill(2)).decode("hex")
			
				
				#first write command
				
				#writemode()
				write=True
				i=0
				
				if (run==0):
					break
				D= File.readline() 
				#print D[:-1]
				D=D[:-1]
				#time.sleep(2)
				#writemode()
				if (write==True):
					writemode()
					GPIO.output(ce,0)
					time.sleep(0.005)
					
					print "Writing:", address1, D 
					#D=map(float, D)
					D=map(int, D)
					#Aa=Aa+1
					A=map(int, address1)
					#A="{0:011b}".format(Aint2)
					#A=Astr1
					#time.sleep(0.05)
					#print A,D
					#time.sleep(20)
					#Aa=map(int, A)
					#Actual write operation:
					#print "Writing user data to selected address."
					#Set address bus:
					GPIO.output(a0,A[10])
					GPIO.output(a1,A[9])
					GPIO.output(a2,A[8])
					GPIO.output(a3,A[7])
					GPIO.output(a4,A[6])
					GPIO.output(a5,A[5])
					GPIO.output(a6,A[4])
					GPIO.output(a7,A[3])
					GPIO.output(a8,A[2])
					GPIO.output(a9,A[1])
					GPIO.output(a10,A[0])
	#				GPIO.output(a11,A[11])
	#				GPIO.output(a12,A[12])
	#				GPIO.output(a13,A[13])
	#				GPIO.output(a14,A[14])
					GPIO.output(we,0) #WE - low - latched address
					#print "User address latched."
					time.sleep(0.05)
					
					#Set data bus:
					GPIO.output(d0,D[7])
					GPIO.output(d1,D[6])
					GPIO.output(d2,D[5])
					GPIO.output(d3,D[4])
					GPIO.output(d4,D[3])
					GPIO.output(d5,D[2])
					GPIO.output(d6,D[1])
					GPIO.output(d7,D[0])
					GPIO.output(we,1) #WE - high - latched data
					#print "User data latched."
					time.sleep(0.05)
					GPIO.output(ce,1)
				
				
				#print Aa1
				if (address1=="00011111111"):
					run=0
					run2=0
				Aint1=Aint1+1
	
			#time.sleep(delay)
			GPIO.output(ce,1) #CE - high - standby chip
			print "Chip on standby."

			time.sleep(delay)
			#GPIO.cleanup()
			#print "Performing GPIO cleanup.\nOperation Completed."
	
		except KeyboardInterrupt:
			print "Operation Aborted.\nPerforming GPIO cleanup."
		#GPIO.cleanup()
	
	except KeyboardInterrupt:
		print "Keyboard Interrupt.\nPerforming GPIO cleanup."
		#GPIO.cleanup()
	return
	File.close() 
	
	
print ""
print "EEPROM PROGRAMMER v3"	
run=1
while (run==1):
	#os.system('clear')
	print ""
	#print ""
	print "         >MENU<"
	print ""
	print "1)Read 1                             (Bianry)"
	print "2)Write 1                            (Binary)"
	print "3)Read Section              (Linear) (Binary)  (Unsupported)"
	print "4)Read Section              (Paired) (Full) "
	print "5)Write section             (Paired) (Text/Dec)          "
	print "6)Erase Section             (Linear)           (Developmental)"
	print "7)Erase entire rom         "
	print "8)Save ROM Contents to file"
	print "9)Write file to ROM"
	print "10)Exit"
	answer=raw_input()
	if (answer=="1"):
		readmode()
		readone()
	elif (answer=="2"):
		writemode()
		writeone()
	elif (answer=="3"):
		readmode()
		readsection()
	elif (answer=="4"):
		readmode()
		readsection2()
	elif (answer=="5"):
		#writemode()
		writesection()
	elif (answer=="6"):
		writemode()
		erasesection()
	elif (answer=="7"):
		writemode()
		eraseall()
	elif (answer=="8"):
		readmode()
		saveprog()
	elif (answer=="9"):
		writemode()
		writeprog()
	elif (answer=="10"):
		GPIO.output(ce,1) #CE - high - standby chip
		print "Chip on standby."
		GPIO.cleanup()
		quit()
	else:
		print "Incorrect Response"
