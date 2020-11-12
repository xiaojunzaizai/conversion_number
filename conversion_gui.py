import conversion
import tkinter as tk
import tkinter.font
import re

def clean(n):
    c = re.sub(u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",n)
    return c


def clean_b(n):
    g = re.sub('[a-zA-Z2-9]+',"",n)
    return g

def clean_o(n):
    g = re.sub('[a-zA-Z89]+',"",n)
    return g

def clean_d(n):
    g = re.sub('[a-zA-Z]+',"",n)
    return g

def clean_h(n):
    g = re.sub('[g-zG-Z]+',"",n)
    return g

def convert(event):
    global up
    global dw
    global result
    global up_enter

    a = up.get()
    b = dw.get()
    c = up_enter.get()
    d = clean(c)
    e= ''
    f =''

    if '-' in c:
        result.set('No negative number')
    else:
        if a == 'b':
            g = clean_b(d)
            e= conversion.b_t_d(str(g))
        elif a == 'o':
            g = clean_o(d)
            e= conversion.o_t_d(str(g))
        elif a == 'd':
            g = clean_d(d)
            e= g
        elif a == 'h':
            g = clean_h(d)
            e = conversion.h_t_d(str(g))
        
        if b == 'b':
            f = conversion.d_t_b(e)
        elif b == 'o':
            f = conversion.d_t_o(e)
        elif b == 'd':
            f = e
        elif b == 'h':
            f = conversion.d_t_h(e) 

        result.set(str(f))





def main_window():
    global up
    global dw
    global result
    global up_enter


    root = tk.Tk(className= '进制转换')
    ft = tkinter.font.Font(family='Times New Roman',size='16',weight='bold')
    root.geometry('500x300+600+300')
    #上层单选
    up = tk.StringVar()
    up_r_b = tk.Radiobutton(root,variable = up, value = 'b', text = '二进制', height = 4, width = 8)
    up_r_o = tk.Radiobutton(root,variable = up, value = 'o', text = '八进制', height = 4, width = 8)
    up_r_d = tk.Radiobutton(root,variable = up, value = 'd', text = '十进制', height = 4, width = 8)
    up_r_h = tk.Radiobutton(root,variable = up, value = 'h', text = '十六进制', height = 4, width = 8)
    up_enter = tk.Entry(root,width = 40)
    up_enter.bind('<Return>',convert)
    
    #上层布局
    up_r_b.grid(row = 1, column = 0,padx = 10,sticky = 'w')
    up_r_o.grid(row = 1, column = 1,padx = 10, sticky = 'w')
    up_r_d.grid(row = 1, column = 2,sticky = 'w', padx = 10)
    up_r_h.grid(row = 1, column = 3, sticky = 'w', padx =10)
    # enter.grid(row = 1,column = 4,padx = 10)
    up_enter.place(x = 10, y = 55)
    # 中层按钮
    cvt = tk.Button(root,text = '转换', width = 8)
    cvt.bind('<Button-1>',convert)

    #中层布局
    cvt.place(x = 400, y = 90)
    
    #下层单选
    dw = tk.StringVar()
    result = tk.StringVar()
    dw_r_b = tk.Radiobutton(root,variable = dw, value = 'b', text = '二进制', height = 4, width = 8)
    dw_r_o = tk.Radiobutton(root,variable = dw, value = 'o', text = '八进制', height = 4, width = 8)
    dw_r_d = tk.Radiobutton(root,variable = dw, value = 'd', text = '十进制', height = 4, width = 8)
    dw_r_h = tk.Radiobutton(root,variable = dw, value = 'h', text = '十六进制', height = 4, width = 8)
    dw_enter = tk.Entry(root,textvariable = result,width = 40)


    #下层布局
    dw_r_b.place(x = 10, y = 100)
    dw_r_o.place(x = 105, y = 100)
    dw_r_d.place(x = 205, y = 100)
    dw_r_h.place(x = 300, y = 100)
    dw_enter.place(x = 10, y = 160)


    root.mainloop()



if __name__ == "__main__":
    main_window()