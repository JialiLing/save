# !/user/bin/env Python3
# -*- coding:utf-8 -*- 
# autour: lingjiali
# 2020/1/3
from tkinter import *
import tkinter as tk
from tkinter import filedialog, dialog
import os
import time
import tkinter.messagebox
from tkinter import ttk
import shutil
import sys

window = tk.Tk()
window.title('SAVE') 
window.geometry('500x500') # window size


# choose the video
file_path = ''
video_prompt = tk.StringVar()
video_prompt.set('please choose one video file')
def open_file():
	global file_path
	# you can only choose video file
	file_path = filedialog.askopenfilename(title=u'select video', initialdir=(os.path.expanduser('H:/')), filetypes =[('video', ('.mp4','.avi','.m4v','.mkv','.webm','.mov','.wmv','.mpg','.flv'))])
	print('select file：', file_path)
	file_name = file_path.split('/')[-1]
	video_type = file_path.split('/')[-1].split('.')[1]
	print(video_type)
	print_videoinfo(file_path,file_name)

def print_videoinfo(fpath,fname):
    print(fpath)
    print(fname)
    video_prompt.set('the video you choose is:'+ fname )



def convert_audio(video_path):
    # """
    # convert other vedio type into mp4
    # :param video_path:
    # :return:
    # """
	video_type = video_path.split('/')[-1].split('.')[1]
	file_name = video_path.split('/')[-1]
	print(video_path)
	if video_type == 'mp4':
		shutil.copyfile(video_path,'/home/ubuntu/Desktop/save-master/mp4/'+file_name)
		temp_name = '/home/ubuntu/Desktop/save-master/mp4/'+video_path.split('/')[-1].split('.')[0] + ".mp4"
		if(ifadd):
			print('add subtitle')
			os.system('autosub -S en -D en '+str(temp_name))
			srtname = '/home/ubuntu/Desktop/save-master/mp4/'+video_path.split('/')[-1].split('.')[0] + ".srt"
			os.system('ffmpeg -i '+str(temp_name)+' -i '+str(srtname)+' -c:s mov_text -c:v copy -c:a copy /home/ubuntu/Desktop/save-master/mp4/output.mp4')
		else:
			print("don't add subtitle")
		# os.system('ffmpeg -i '+aaaaa+' -i '+aaaaa+'.srt -c:s mov_text -c:v copy -c:a copy output.mp4')


	else:	
		temp_name = '/home/ubuntu/Desktop/save-master/mp4/'+ video_path.split('/')[-1].split('.')[0]
		os.system("ffmpeg -i " + video_path + " " + temp_name + ".mp4")
		ttname = temp_name+".mp4"
		os.system('autosub -S en -D en  '+str(ttname))
		os.system('ffmpeg -i '+str(ttname)+' -i '+str(temp_name)+'.srt -c:s mov_text -c:v copy -c:a copy /home/ubuntu/Desktop/save-master/mp4/output.mp4')

	arg0=ctl
	arg1=ssim
	arg2=frame
	# os.system('./run.sh '+arg0+' '+arg1+' '+arg2)

bt1 = tk.Button(window, text='select file', width=15, height=2, command=open_file)
bt1.pack()

video_info = tk.Label(window,textvariable = video_prompt)

video_info.pack()

# choose the controller
ctl =''
group = tk.LabelFrame(window,text="choose the controller you want")
group.pack(padx=10,pady=10)


LANGS = [("mpc",1),("bangbang",2),("random",3),("PID",4)]
prompt = tk.StringVar()
prompt.set(' please choose one controller ')
def prin1():

	global ctl

	l = v.get()
	# print (l)
	if l == 1:
		prompt.set(' you choose the mpc controller ')
		ctl='mpc'
	elif l == 2:
		prompt.set(' you choose the bangbang controller ')
		ctl = 'bangbang'
	elif l == 3:
		prompt.set(' you choose the random controller ')
		ctl='random'
	elif l==4:
		prompt.set(' you choose the pid controller ')
		ctl='pid'
	else:
		prompt.set(' please choose one controller ')
		ctl=''

	# print(prompt)


v = tk.IntVar()
for lang,num in LANGS:
	b = tk.Radiobutton(group,text=lang,variable = v ,value =num, command=prin1)
	b.pack(side=tk.LEFT)

controller_info = tk.Label(window,textvariable = prompt)

controller_info.pack()


# choose the ssim value
ssim = '0'
group2 = tk.LabelFrame(window,text="set the ssim value as: ")
group2.pack(padx=10,pady=10)
def go(*args):   
	global ssim

	print(comboxlist.get()) 

	ssim = comboxlist.get()
 
comvalue=tkinter.StringVar()
comvalue.set('set the ssim value as: ')
comboxlist=ttk.Combobox(group2,textvariable=comvalue) 
comboxlist["values"]=("please choose an ssim point","0.7","0.8","0.9","1.0")
comboxlist.current(0)  
comboxlist.bind("<<ComboboxSelected>>",go) 
comboxlist.pack()



def validate(event):
    #text = e.get()
	text = event.widget.get()
	if is_integer(text):    
		if int(text) > 50000 or int(text)<1:
			l['text'] ="number out of range"
			return
		else:
			l['text'] = ''
	else:
		l['text'] = 'Not an integer'

def is_integer(text):
    try:
        value = int(text)
        return True
    except ValueError:
        return False
# input the frame value and it should only be an integer
frame = ''
L1 = Label(window, text="please enter frame(an interger from 0-50000):")
L1.pack()
E1 = Entry(window, bd =5)
E1.bind("<KeyRelease>", validate)
E1.pack()
l = tk.Label(window)
l.pack()


def ifsub():
	global ifadd
	ifadd = 0
	ifadd = CheckVar1.get()
	print(ifadd)

CheckVar1 = IntVar()
C1 = Checkbutton(window, text = "add subtitle", variable = CheckVar1,  onvalue = 1, offvalue = 0, height=5, width = 20,command= ifsub)
print
C1.pack()


def show():
	global frame
	print('frame:'+E1.get())
	frame = E1.get()
	print(file_path)
	print(ctl)
	print(ssim)
	print(frame)
	convert_audio(file_path)


def dele():
	
	E1.delete(0,END)
	prompt.set(' please choose one controller ')
	video_prompt.set('please choose one video file')
	comboxlist.current(0)


theButton1 = Button(window, text ="convert", width =10,command =show)
theButton2 = Button(window, text ="clear",width =10,command =dele)
theButton1.pack()
theButton2.pack()

window.mainloop() 
