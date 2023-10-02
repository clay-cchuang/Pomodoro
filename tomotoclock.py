#%%
import tkinter as tk
import tkinter.ttk as ttk
import datetime 
from datetime import datetime as dt
import time

GMT = datetime.timezone(datetime.timedelta(hours=8)) 
s_f_num = 0
start_finish = 'Start'
p_c_num = 0
pause_continue = 'Pause'
event_time = 0 
counter = 0 # 初始化一開始的事件時間用
total = 0
total_pause = 0
pause_time = 0
left_time = 0
end_time = ''
work_list_time = []
today_do = []
day_work_time = []
dict1 = {}
s = 0


def s_f(): 
    global s_f_num
    if s_f_num%2 == 0:
        start_finish = 'Finish'
    else:
        start_finish = 'Start'
    button2['text'] = start_finish
    s_f_num += 1
    showeventTime()

def p_c(): 
    global p_c_num
    if p_c_num%2 == 1:
        pause_continue = 'Pause'
    else:
        pause_continue = 'Continue'
    button3['text'] = pause_continue
    p_c_num += 1


root = tk.Tk()                
root.title('Clockify')
root.geometry('505x525')     

working_list = []
time_text = tk.StringVar()  
event_time_text = tk.StringVar()     
event_time_text.set('00:00')

def showTime():
    now = datetime.datetime.now(tz=GMT).strftime('%H:%M:%S')   
    time_text.set(now)                   
    root.after(1000, showTime)   

def showeventTime():
    global counter
    global event_time
    global total
    global total_pause
    global pause_time
    global left_time
    global end_time
    global p_c_num
    global day_work_time
    global s 
    global dict1
    s = 0

    if counter == 0:
        event_time = time.time()

    if s_f_num%2 == 1 and p_c_num%2==0:           
        counter += 1
        total_pause = total_pause + pause_time
        pause_time = 0
        total = time.time() - event_time - total_pause
        end_time = f'{(str(round(total)//60).zfill(2))}:{str(round(total%60)).zfill(2)}' 
        event_time_text.set(end_time)   
        left_time = time.time()
        root.after(1000, showeventTime)

    elif s_f_num%2 == 1 and p_c_num%2 ==1: 

        pause_time = time.time() - left_time
        root.after(1000, showeventTime)

    else:
        counter = 0
        event_time_text.set('00:00')
        button3['text'] = 'Pause'
        p_c_num = 0
        pause_time = 0
        total_pause = 0      
        today_do.append(box.get())
        work_list_time.append(end_time)
        for s1 in list(set(today_do)):
            indices = [k for k, ee in enumerate(today_do) if ee == s1]
            time1 = 0
            for j1 in indices:
                if j1%2 == 0:
                    time1 = time1 + int(work_list_time[j1].split(':')[0])*60 + int(work_list_time[j1].split(':')[1])
            
            time2 = f'{str(time1//60).zfill(2)}:{str(time1%60).zfill(2)}'
            dict1[s1] = time2 
        
        label3['text'] = list(dict1.keys())[0]
        label4['text'] = list(dict1.values())[0]
        label5['text'] = list(dict1.keys())[1]
        label6['text'] = list(dict1.values())[1]
        label7['text'] = list(dict1.keys())[2]
        label8['text'] = list(dict1.values())[2]
        label9['text'] = list(dict1.keys())[3]
        label10['text'] = list(dict1.values())[3]
        end_time = '00:00'
        return 0
    s = s+1 



def click():
    working_list.append(entry.get())
    label2['text'] = '    '.join(working_list)
    box['value'] = working_list

time_info_text = tk.Label(root, text='Current Time', font=('Arial',28))
time_info_text.grid(row=0, column=0, pady=5, padx=30)  

now_time = tk.Label(root, textvariable=time_text, font=('Arial',35))
now_time.grid(row=0, column=1, columnspan=3, padx=80) 

sep1=ttk.Separator(root, orient='horizontal',style='red.TSeparator')
sep1.grid(row=1, column=0, columnspan=3, pady=10, padx=10, sticky='WE')

work_list = tk.Label(root, text='Working Item', font=('Arial', 24))
work_list.grid(row=2, column=0) 

entry = tk.Entry(root, width = 10) 
entry.grid(row=2, column=1, padx=2, pady=2)

button1 = tk.Button(root, width = 5, text='Create', font=('Arial', 16), command=click)
button1.grid(row=2, column=2, sticky='W')

label2 = tk.Label(root,  text='', font=('Arial', 20))
# label2.grid(row=3, column=0, columnspan=10, sticky='W',  padx = 10, pady=10)

sep2 = ttk.Separator(root, orient='horizontal',style='red.TSeparator')
sep2.grid(row=4, column=0, columnspan=3, pady=10, padx=10, sticky='WE')

box = ttk.Combobox(root,width = 10, values=[])
box.grid(row=5, column=0, pady=10, padx=10, sticky='WE')

button2 = tk.Button(root, width = 8, text=start_finish, font=('Arial', 16), command=s_f)
button2.grid(row=5, column=1, sticky='W')

button3 = tk.Button(root, width = 8, text=pause_continue, font=('Arial', 16), command=p_c)
button3.grid(row=5, column=2, sticky='W')

event_time = tk.Label(root, textvariable=event_time_text, font=('Arial',50))
event_time.grid(row=6, column=0, columnspan=3, padx=80) 

label3 = tk.Label(root,  text='', font=('Arial', 25))
label3.grid(row=8, column=0, columnspan=2, sticky='W',  padx = 50, pady=10)

label4 = tk.Label(root,  text='', font=('Arial', 25))
label4.grid(row=8, column=2, columnspan=2, sticky='W',  padx = 20, pady=10)

label5 = tk.Label(root,  text='', font=('Arial', 25))
label5.grid(row=9, column=0, columnspan=2, sticky='W',  padx = 50, pady=10)

label6 = tk.Label(root,  text='', font=('Arial', 25))
label6.grid(row=9, column=2, columnspan=2, sticky='W',  padx = 20, pady=10)

label7 = tk.Label(root,  text='', font=('Arial', 25))
label7.grid(row=10, column=0, columnspan=2, sticky='W',  padx = 50, pady=10)

label8 = tk.Label(root,  text='', font=('Arial', 25))
label8.grid(row=10, column=2, columnspan=2, sticky='W',  padx = 20, pady=10)

label9 = tk.Label(root,  text='', font=('Arial', 25))
label9.grid(row=11, column=0, columnspan=2, sticky='W',  padx = 50, pady=10)

label10 = tk.Label(root,  text='', font=('Arial', 25))
label10.grid(row=11, column=2, columnspan=2, sticky='W',  padx = 20, pady=10)

label11 = tk.Label(root,  text='', font=('Arial', 25))
label11.grid(row=21, column=2, columnspan=2, sticky='W',  padx = 20, pady=10)

sep2 = ttk.Separator(root, orient='horizontal',style='red.TSeparator')
sep2.grid(row=7, column=0, columnspan=3, pady=10, padx=10, sticky='WE')

sep3 = ttk.Separator(root, orient='vertical',style='red.TSeparator')
sep3.grid(row=7, column=1, rowspan=20, pady=10, padx=10, sticky='NS')

if __name__ == '__main__':
    showTime()   
    root.mainloop()

