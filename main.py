import os
import random
import sys
import tkinter as tk
from tkinter import *
import vgamepad as vg

# iniciamos aplicacion
window = tk.Tk()

# frames
frameIcon = Frame(window, height=150)
frameIcon.pack(side='top',fill='both')

frameGamepad = Frame(window, height=150)
frameGamepad.pack(side='bottom')

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
def gpState():
	if gamepad is not 0:
		return 1
	else:
		windowTitleSet('control desconectado')
		return 0

#bonotes
def btnCreate(name):
	button_x = tk.Button(frameGamepad,text=name,width=6,height=3,compound = 'bottom', command= lambda:btnDriver(name))
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
	global gamepad
	gamepad = 0
	label_control_status.configure(image=img_control_disconnected)  # cambiar icono de coneccion
	camTestDriver()
	accelReset()
	dirReset()
def emulatorDriver():
    if gamepad is 0:
        emulatorConnect()
    else:
        emulatorDisconnect()

# boton camaras giratorias
camtestalarm = 0
def camTestDriver(time=1000):
    global camtestalarm
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
            windowTitleSet('detenido camTestDriver')
            gpReset()
def camTestReset():
    gpButtonRealease('UP')
    gpButtonRealease('DOWN')
    gpButtonRealease('LEFT')
    gpButtonRealease('RIGHT')
def camTestAlarm(time=1000):
    if camtestalarm:
        camTestReset()
        gpButtonPress('B')
        i = random.randint(1, 4)
        if i == 1:
            gpButtonPress('UP')
        elif i == 2:
            gpButtonPress('DOWN')
        elif i == 3:
            gpButtonPress('LEFT')
        elif i == 4:
            gpButtonPress('RIGHT')
        window.after(time, lambda: camTestAlarm(time))


def camChangeFront():
	if gpState():
		gpButtonPress('Y')
		gpButtonPress('UP')
		window.after(500, gpReset)

def camChangeBack():
	if gpState():
		gpButtonPress('Y')
		gpButtonPress('DOWN')
		window.after(500, gpReset)


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
def dirDriver(dir=0):
	if gpState():
		gpButtonPress('LJ',x=float(dir),y=0)
		slider_dir.set(dir)
	else:
		dirReset(0)
def dirReset(dir=0):
	slider_dir.set(0)

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
label_control_status.pack(side='right', fill='both')

# Botones
button_connect = tk.Button(frameIcon, text='CONECTAR EMULADOR',height=3, command=emulatorDriver)
button_connect.pack(fill='both')

#button_cam_test = tk.Button(frameIcon, text='GIRAR CAMARA',height=3, command=camTestDriver)
#button_cam_test.pack(fill='both')

button_cam_change_front = tk.Button(frameIcon, text='CAMBIAR CAMARA FRONTAL',height=3, command=camChangeFront)
button_cam_change_front.pack(fill='both')

button_cam_change_back = tk.Button(frameIcon, text='CAMBIAR CAMARA TRASERA',height=3, command=camChangeBack)
button_cam_change_back.pack(fill='both')

#button_stop = tk.Button(frameIcon, text='Frenar',height=3, command= stopDriver)
#button_stop.pack(fill='both')

slider_accel = tk.Scale(frameIcon,from_=0,to=1,resolution=.1,orient='horizontal',label='Velocidad',troughcolor='lightblue',command=accelerateDriver)
slider_accel.pack(fill='both')
slider_accel.bind('<ButtonRelease-1>', accelReset)

slider_dir = tk.Scale(frameIcon,from_=-1,to=1,resolution=.1,orient='horizontal',label='Direccion',troughcolor='lightpink',command=dirDriver)
slider_dir.pack(fill='both')
slider_dir.bind('<ButtonRelease-1>', dirReset)

#Control con teclado
window.bind('<Up>',lambda x: accelerateDriver(1))
window.bind('<Down>',lambda x: accelerateDriver(0))
window.bind('<KeyRelease-Up>',lambda x: accelerateDriver(0))

window.bind('<Left>',lambda x: dirDriver(-0.5))
window.bind('<Right>',lambda x: dirDriver(.5))

window.bind('<KeyRelease-Left>',lambda x: dirDriver(0))
window.bind('<KeyRelease-Right>',lambda x: dirDriver(0))

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
