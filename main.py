import os
import random
import sys
import tkinter as tk
from tkinter import *
import vgamepad as vg
import keyboard
import time

# iniciamos aplicacion
window = tk.Tk()

# frames
frameTop = Frame(window)
frameTop.pack(side='top',fill='both')

frameIcon = Frame(frameTop)
frameIcon.pack(side='right',fill='both',expand=YES)

frameActions = Frame(frameTop)
frameActions.pack(side='left')


frameBottom = Frame(window)
frameBottom.pack(side='bottom')

frameGamepad = Frame(frameBottom)
frameGamepad.pack()

# ------------------------------------------------------
# --------------funciones-------------------------------
# ------------------------------------------------------
def resourcePath(relative_path):
	try:  # PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def windowTitleSet(text=''):
    window.title(text)

# control xbox
def gpButtonPress(btn, value=0, x=0, y=0):
	x = min(x,1) if x > 0 else max(x,-1)
	y = min(y,1) if y > 0 else max(y,-1)
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
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
	elif btn == 'LEFT':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
	elif btn == 'RIGHT':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
	elif btn == 'LS':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
	elif btn == 'RS':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
	elif btn == 'RTHUM':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
	elif btn == 'LTHUM':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
	elif btn == 'START':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
	elif btn == 'BACK':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
	elif btn == 'HOME':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)
	elif btn == 'RT':
		gamepad.right_trigger_float(value)
	elif btn == 'LT':
		gamepad.left_trigger_float(value)
	elif btn == 'LJ':
		gamepad.left_joystick_float(x, y)
	elif btn == 'RJ':
		gamepad.right_joystick_float(x, y)
	gamepad.update()
def gpButtonRealease(btn):
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
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    elif btn == 'LEFT':
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    elif btn == 'RIGHT':
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    elif btn == 'LS':
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    elif btn == 'RS':
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    elif btn == 'RTHUM':
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    elif btn == 'LTHUM':
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    elif btn == 'START':
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    elif btn == 'BACK':
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    elif btn == 'HOME':
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)
    elif btn == 'RT':
        gamepad.left_trigger_float(0)
    elif btn == 'LT':
        gamepad.right_trigger_float(0)
    elif btn == 'LJ':
        gamepad.left_joystick_float(0, 0)
    elif btn == 'RJ':
        gamepad.right_joystick_float(0, 0)
    gamepad.update()
def gpReset():
	if gpState():
		global gamepad
		gamepad.reset()
		gamepad.update()
		accelReset()
		dirReset(btn='LJ')
		dirReset(btn='RJ')
def gpState():
	if gamepad is not 0:
		return 1
	else:
		windowTitleSet('control desconectado')
		return 0

#bonotes
def btnCreate(name):
	button_x = tk.Button(frameGamepad,text=name,width=8,height=4,compound = 'bottom', command= lambda:btnDriver(name))
	button_x.pack(side = LEFT)
def btnDriver(name):
	if gpState():
		gpButtonPress(name)
		window.after(500, lambda: btnAlarm(name))
def btnAlarm(name):
	gpButtonRealease(name)

# boton emulador on/off
gamepad = 0  # control emulado (0 == no esta conectado)
def emulatorConnect():
    global gamepad
    gamepad = vg.VX360Gamepad()  # conectar controll
    label_control_status.configure(image=img_control_connected)  # cambiar icono de coneccion
    windowTitleSet('control conectado')
def emulatorDisconnect():
	global gamepad,timesrotated
	gamepad = 0
	timesrotated = 0
	label_control_status.configure(image=img_control_disconnected)  # cambiar icono de coneccion
	camTestDriver()
	accelReset()
	dirReset(btn='LJ')
	dirReset(btn='RJ')
def emulatorDriver():
    if gamepad is 0:
        emulatorConnect()
    else:
        emulatorDisconnect()

# boton camaras giratorias
camtestalarm = 0
timesrotated = 0
camtestalarmjob = 0
precam = 0

def camTestDriver(time=1000):
	global camtestalarm,timesrotated
	if gamepad is 0:
		windowTitleSet('control desconectado')
		if camtestalarm == 1:
			camtestalarm = 0
			button_cam_test.configure(background = 'white')
			windowTitleSet('detenido camTestDriver')
	else:
		if camtestalarm == 0:
			camtestalarm = 1
			window.after(1, lambda: camTestAlarm(time))
			button_cam_test.configure(background = 'green')
			windowTitleSet('trabajando camTestDriver')
		else:
			camtestalarm = 0
			button_cam_test.configure(background = 'white')
			window.after_cancel(camtestalarmjob)
			windowTitleSet('detenido camTestDriver | Se Roto ' + str(timesrotated) + ' veces')
			timesrotated = 0
			gpReset()
def camTestAlarm(time=1000):
	global timesrotated, camtestalarmjob, precam
	if camtestalarm:
		timesrotated = timesrotated + 1
		windowTitleSet('No. de giros : ' + str(timesrotated))
		while True:
			nextcam = random.randint(1, 4)
			if precam != nextcam:
				precam = nextcam
				break
		camRotate(precam)
		camtestalarmjob = window.after(time, lambda: camTestAlarm(time))

# boton girar camaras
cam = 0
def camRotateDriver(value=0):
	global cam
	if gpState():
		cam = value + 1
		if cam > 4 :
			cam = 1
		camRotate(cam)
def camRotate(cam=1):
	gpButtonPress('B')
	time.sleep(.15)
	if cam == 1:
		gpButtonPress('UP')
	elif cam == 2:
		gpButtonPress('RIGHT')
	elif cam == 3:
		gpButtonPress('DOWN')
	elif cam == 4:
		gpButtonPress('LEFT')
	window.after(100, camRotateReset)
def camRotateReset():
	if gpState():
		gpButtonRealease('B')
		gpButtonRealease('UP')
		gpButtonRealease('DOWN')
		gpButtonRealease('LEFT')
		gpButtonRealease('RIGHT')

# boton cambiar camaras
def camChangeFront():
	if gpState():
		camReset()
		gpButtonPress('Y')
		time.sleep(.15)
		gpButtonPress('DOWN')
		window.after(500, camReset)
def camChangeBack():
	if gpState():
		camReset()
		gpButtonPress('Y')
		time.sleep(.15)
		gpButtonPress('UP')
		window.after(500, camReset)
def camReset():
	if gpState():
		gpButtonRealease('Y')
		gpButtonRealease('DOWN')
		gpButtonRealease('UP')

# boton acelerador
def accelerateDriver(value=0):
	if gpState() and value is not 0:
		gpButtonPress('RT', float(value))
		slider_accel.set(value)
	else:
		accelReset()
def accelReset(accel=0):
	slider_accel.set(0)

# boton freno
def stopDriver():
	accelerateDriver(0)

#control direccion
def dirDriver(dir=0,btn=0):
	if btn is not 0:
		if gpState():
			print(btn)
			print(dir)
			gpButtonPress(btn,x=float(dir),y=0)
			if btn == 'LJ':
				slider_dir_l.set(dir)

			elif btn == 'RJ':
				slider_dir_r.set(dir)
		else:
			dirReset(0,btn)
def dirReset(dir=0,btn=0):
	if btn == 'LJ':
		slider_dir_l.set(0)
	elif btn == 'RJ':
		slider_dir_r.set(0)

# ------------------------------------------------------
# --------Recursos--------------------------------------
# ------------------------------------------------------
# Imagenes
img_control_connected = PhotoImage(file=resourcePath("connect.png")).subsample(2,2)
img_control_disconnected = PhotoImage(file=resourcePath("disconnect.png")).subsample(2,2)

# ------------------------------------------------------
# ------------aplicacion--------------------------------
# ------------------------------------------------------
# configuracion de la ventana
window.resizable(False, False)
window.title('Emulador tortops')
window.iconbitmap(resourcePath("favicon.ico"))

# iconos
label_control_status = Label(frameIcon, image=img_control_disconnected)
label_control_status.pack(side='top',expand=YES)

button_reset = tk.Button(frameIcon, text='RESET',height=10,width=30,bg='red',fg='white',command= gpReset)
button_reset.pack(side='bottom',expand=YES)

# Botones
button_connect = tk.Button(frameActions, text='CONECTAR EMULADOR',height=4,width=75, command=emulatorDriver)
button_connect.pack(fill='both')

button_cam_test = tk.Button(frameActions, text='TEST GIRAR CAMARA',height=3, command=camTestDriver)
button_cam_test.pack(fill='both')

button_cam_change_front = tk.Button(frameActions, text='CAMBIAR CAMARA FRONTAL',height=4, command=camChangeFront)
button_cam_change_front.pack(fill='both')

button_cam_change_back = tk.Button(frameActions, text='CAMBIAR CAMARA TRASERA',height=4, command=camChangeBack)
button_cam_change_back.pack(fill='both')

button_cam_rotate = tk.Button(frameActions, text='GIRAR CAMARA',height=4, command=lambda: camRotateDriver(cam))
button_cam_rotate.pack(fill='both')

slider_accel = tk.Scale(frameActions,from_=0,to=1,resolution=.1,orient='horizontal',label='Velocidad',troughcolor='lightblue',command=accelerateDriver)
slider_accel.pack(fill='both')
slider_accel.bind('<ButtonRelease-1>', accelReset)

slider_dir_l = tk.Scale(frameActions,from_=-1,to=1,resolution=.1,orient='horizontal',label='Joystick Izquierdo',troughcolor='lightpink',command=lambda x: dirDriver(slider_dir_l.get(),'LJ'))
slider_dir_l.pack(fill='both')
slider_dir_l.bind('<ButtonRelease-1>', lambda x: dirReset(btn='LJ'))

slider_dir_r = tk.Scale(frameActions,from_=-1,to=1,resolution=.1,orient='horizontal',label='Joystick Derecho',troughcolor='lightpink',command=lambda x: dirDriver(slider_dir_r.get(),'RJ'))
slider_dir_r.pack(fill='both')
slider_dir_r.bind('<ButtonRelease-1>', lambda x: dirReset(btn='RJ'))

#Control con teclado
window.bind('<Up>',lambda x: accelerateDriver(1))
window.bind('<Down>',lambda x: accelerateDriver(0))
window.bind('<KeyRelease-Up>',lambda x: accelerateDriver(.5))

window.bind('<Left>',lambda x: dirDriver(-0.35,'LJ'))
window.bind('<Right>',lambda x: dirDriver(.35,'LJ'))

window.bind('<KeyPress-Shift_L>',lambda x: dirDriver(slider_dir_l.get()*2,'LJ'))

window.bind('<KeyRelease-Left>',lambda x: dirDriver(0,'LJ'))
window.bind('<KeyRelease-Right>',lambda x: dirDriver(0,'LJ'))
window.bind('<KeyRelease-Shift_L>',lambda x: dirDriver(slider_dir_l.get()/2,'LJ'))

# game pad

btnCreate('X')
btnCreate('Y')
btnCreate('B')
btnCreate('A')

btnCreate('UP')
btnCreate('LEFT')
btnCreate('RIGHT')
btnCreate('DOWN')

btnCreate('LS')
btnCreate('RS')

btnCreate('START')
btnCreate('BACK')


# ------------------------------------------------------
# ------Main Loop---------------------------------------
# ------------------------------------------------------
window.mainloop()
