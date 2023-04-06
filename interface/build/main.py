import sys
# sys.path.append("../..")
# import v2.chat as chat
import api as API
from tkinter import messagebox
import gui
import threading

gBaseFontNum = 200;
allStr = "";
newStr = ""
def guiInit():
	# gui.entry_4.set(200);
	# print(dir(gui.entry_3))
	gui.entry_4.insert(0,"1")
	gui.entry_3.insert(0,"200")

def onClickStart():
	print(gui.entry_3.get())
	# print(gui.entry_4.get()) ;
	# print(gui.entry_2.get("1.0","end")) ;
	# print(gui.entry_1.get("1.0","end")) ;
	# print(entry_3.textvariable)
	str = gui.entry_2.get("1.0","end")
	count = int(gui.entry_3.get());
	doFile(str,count);

def onClickContinue():
	print(gui.entry_3.get())
	# print(gui.entry_4.get()) ;
	# print(gui.entry_2.get("1.0","end")) ;
	# print(gui.entry_1.get("1.0","end")) ;
	# print(entry_3.textvariable)
	str = allStr;
	count = int(gui.entry_3.get());
	doFile(str,count);

def doFile(startStr,count):
	print("start do AI");
	if(startStr == ""):
		print("no input!!");
		messagebox.showinfo("no input!!");
		return
	msg = startStr;
	def doAI():
		# print(msg + " count:" + count);
		# onMsg("???");
		allStr += msg;
		API.pipeline.generate(msg, token_count=count, args=API.args, callback=onMsg);

	th = threading.Thread(target=doAI)
	th.start();
	

def onMsg(str):
	gui.entry_1.insert("end",str)
	allStr += str;

	
gui.button_1['command'] = onClickStart
gui.button_2['command'] = onClickContinue

guiInit();
gui.window.mainloop()