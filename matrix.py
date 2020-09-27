import sys, os
def main():
	byte = r"\x"; os.system("")
	try:
		if os.path.exists(sys.argv[-1]) and len(sys.argv)>=2:
			with open(sys.argv[-1], "rb") as hexfile: 
				hexlist = list(map(lambda x: x[:2].upper(), str(hexfile.read()).split(byte))); hexfile.seek(0)
				reshexlist = ''.join(map(str, list(map(lambda x: x[2:], str(hexfile.read()).split(byte))))); hexfile.seek(0)
				if len(hexlist) <= 0: reshexlist = ''.join(str(hexfile.read()).split(byte))			
			if os.name == "nt": os.system("title Hacking in progess..."); print('\033[92m')
			for cnt, pr in enumerate(hexlist[1:]): 
				if cnt % int(os.get_terminal_size()[0]/3)== 0: print("\n",end="")	
				elif (cnt // int(os.get_terminal_size()[0]/3)) % int(os.get_terminal_size()[1]) == 0: print("\033[0;0H",end="")	
				else: print(pr, end=" ")
			for cnt, pr in enumerate(reshexlist):
				if cnt % int(os.get_terminal_size()[0] - 1)== 0:print("\n",end="")					
				elif (cnt // int(os.get_terminal_size()[0])) % int(os.get_terminal_size()[1]) == 0: print("\033[0;0H",end="")
				else: print(pr, end="")
			print('\033[0m')	
		else: print("No file")
		input()
	except KeyboardInterrupt: print('\033[0m')			
if __name__ == "__main__": main()