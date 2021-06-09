import tkinter as tk
from tkinter import *
import vgamepad as vg
import sys
import os
import random
from playsound import playsound
from PIL import ImageTk, Image


#iniciamos aplicacion
window = tk.Tk()
window.resizable(False, False)

iconFrame = Frame(window,height=150)
iconFrame.pack(side = 'bottom' )


#Botones
buttons = {}
window.clock = 0
gamepad = 0
title = ''


#funciones
def resource_path(relative_path):
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def pressGPButton(btn):
	global gamepad
	if btn == 'A':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
	elif btn == 'B':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
	elif btn == 'X':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
	elif btn == 'Y':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
	elif btn == 'UP':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
	elif btn == 'DOWN':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN )
	elif btn == 'LEFT':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT )
	elif btn == 'RIGHT':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT )
	elif btn == 'LB':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
	elif btn == 'RB':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER )
	elif btn == 'LoopCamara':
		window.clock = 1
		alarm()
	elif btn == 'Conectar':
		gamepad = vg.VX360Gamepad()
		bnt2.configure(image=controlConectado)
		buttons['LoopCamara'] = 0
	if gamepad is not 0:
		print(btn)
		gamepad.update()



def releaseGPButton(btn):
	global gamepad
	if btn == 'A':
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
	elif btn == 'B':
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
	elif btn == 'X':
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
	elif btn == 'Y':
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
	elif btn == 'UP':
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
	elif btn == 'DOWN':
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN )
	elif btn == 'LEFT':
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT )
	elif btn == 'RIGHT':
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT )
	elif btn == 'LB':
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
	elif btn == 'RB':
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER )
	elif btn == 'LoopCamara':
		window.clock = 0
	elif btn == 'Conectar':
		gamepad = 0
		bnt2.configure(image=controlDesconectado)
	if gamepad is not 0:
		print(btn)
		gamepad.update()

def click(btn,DB):
	playsound(resource_path('click.wav'))
	DB[btn] = 0 if DB[btn] else 1
	if DB[btn] == 1:
		pressGPButton(btn)
	else:
		releaseGPButton(btn)
	print(DB[btn])

def button(btn,master=window,photo='',side ='top',title=''):
	if title is  '':
		title = btn
	button = tk.Button(master=master,text=title,image=photo,compound = LEFT ,command = lambda:pressGPButton(btn))
	button.pack(side = side)

def Switch(name,master=window,DB=buttons,title=''):
	if title is  '':
		title = name
	DB[name] = 0
	button = tk.Button(master=master,text=title, width=80, height=10 , command = lambda:click(name,DB))
	button.pack(fill  = 'both')

def createSwitch(name):
	Switch(name,control)

def alarm():
	global gamepad
	window.wm_title(string="OFF")
	bnt1.configure(image=loopOff)
	if window.clock == 1 and gamepad is not 0:
		window.wm_title(string="ON")
		bnt1.configure(image=loopOn)
		window.after(1000, alarm)
		print('tick tack')
		pressGPButton('B')
		arrow = random.randint(1,4)
		if arrow == 1:
			pressGPButton('UP')
			gamepad.reset()
		elif arrow == 2:
			pressGPButton('DOWN')
			gamepad.reset()
		elif arrow == 3:
			pressGPButton('LEFT')
			gamepad.reset()
		elif arrow == 4:
			pressGPButton('RIGHT')
			gamepad.reset()


#iconos
controlConectado = PhotoImage(file = resource_path("connect.png"))
controlDesconectado = PhotoImage(file = resource_path("disconnect.png"))

loopOn = PhotoImage(file = resource_path("on.png"))
loopOff = PhotoImage(file = resource_path("off.png"))


#aplicacion

Switch('Conectar', title = 'CONECTAR EMULADOR')
Switch('LoopCamara', title = 'COMENZAR A GIRAR CAMARAS')

bnt2 = Label(iconFrame,image=controlDesconectado)
bnt2.pack(side ='left',fill  = 'both')
bnt1 = Label(iconFrame,image=loopOff)
bnt1.pack(side ='left',fill  = 'both')













window.after(1, alarm)
window.mainloop()
