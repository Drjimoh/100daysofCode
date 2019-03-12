import pythoncom, pyHook

def onMouseEvent(event):
	print("MessageName: {}".format(event.MessageName))
	return True

def onKeyBoardEvent(event):
	print("Key pressed: {}".format(event.Key))
	return True


hm = pyHook.HookManager()
#hm.MouseAll = onMouseEvent
hm.KeyDown = onKeyBoardEvent
#hm.HookMouse()
hm.HookKeyboard()
pythoncom.PumpMessages()

