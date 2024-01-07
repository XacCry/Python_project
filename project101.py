from tkinter import*
from tkinter import messagebox


import os
import csv
from types import TracebackType

price = 0
fun = 0
def clearsell():
    global price
    global total
    total = 0
    price = 0
    Label(text=price,font=("Arial",20),bg="skyblue",width=20).grid(row=5,column=1)
    messagebox.showinfo("แสดงข้อมูล","เคลียค่าสำเร็จ")
    try:
        os.remove("รายการสินค้า.csv")
        os.remove("รายการสินค้า-สำรอง.csv")
    except FileNotFoundError:
        pass
def clearsell2():
    if messagebox.askokcancel("ออกจากโปรแกรม", "คุณต้องการออกจากโปรแกมใช่ไหม ?"):
        sell.destroy()
        try:
            os.remove("รายการสินค้า.csv")
            os.remove("รายการสินค้า-สำรอง.csv")
        except FileNotFoundError:
            pass


def save2():
    with open("data.csv","w",encoding="utf-8")as f1:
        with open("data-สำรอง.csv","r",encoding="utf-8")as f1:
            rd = csv.reader(f1)
            list_id = list(rd)
            for id_u in list_id:
                id_user = int(id_u[0])
                id_name = str(id_u[1])
                id_price = int(id_u[2])
                id_num = int(id_u[3])
                lsdt_black = [[id_user,id_name,id_price,id_num]]
                with open("data.csv","a+",encoding="utf-8")as f1:
                    writer = csv.writer(f1,lineterminator="\n")
                    writer.writerows(lsdt_black)
def save3():
    with open("รายการสินค้า.csv","w",encoding="utf-8")as f1:
        with open("รายการสินค้า-สำรอง.csv","r",encoding="utf-8")as f1:
            rd = csv.reader(f1)
            list_id = list(rd)
            for id_u in list_id:
                id_user = int(id_u[0])
                id_name = str(id_u[1])
                id_price = int(id_u[2])
                id_num = int(id_u[3])
                lsdt_black = [[id_user,id_name,id_price,id_num,id_price*id_num]]
                with open("รายการสินค้า.csv","a+",encoding="utf-8")as f1:
                    writer = csv.writer(f1,lineterminator="\n")
                    writer.writerows(lsdt_black)

def sellid():
    global price
    total = 0
    try:
        id_sell = sellinput.get()
        name_id = sellinput2.get()
        filepath = "data.csv"
        sellnum = 0
        num = 0
        ex = 0
    except  TclError:
         messagebox.showwarning("กรุณาตรวจสอบสินค้า","กรุณากรอกตัวเลขเท่านั้น")
    try:
        if id_sell != 0:
            if name_id != 0:
                try:
                    with open("data.csv","r",encoding="utf-8")as f1:
                        
                        rd = csv.reader(f1)
                        list_id = list(rd)
                        with open("data-สำรอง.csv","w",encoding="utf-8")as f1:
                            for id_u in list_id:
                        
                                id_user = int(id_u[0])
                                id_name = str(id_u[1])
                                id_price = int(id_u[2])
                                id_num = int(id_u[3])
                                lsdt_black = [[id_user,id_name,id_price,id_num]]
                                if id_user == id_sell:
                                    if id_num >= name_id:
                                        lsdt_black = [[id_user,id_name,id_price,id_num-name_id]]
                                        with open("data-สำรอง.csv","a+",encoding="utf-8")as f1:
                                            writer = csv.writer(f1,lineterminator="\n")
                                            writer.writerows(lsdt_black)
                                            num = 1
                                            ex = 1
                                    else:
                                        messagebox.showwarning("กรุณาตรวจสอบสินค้า","สินค้าไม่เพียงพอ")
                                        ex = 0
                                        
                                else:
                                    with open("data-สำรอง.csv","a+",encoding="utf-8")as f1:
                                        writer = csv.writer(f1,lineterminator="\n")
                                        writer.writerows(lsdt_black)
                    if num == 1:
                        save2()
                    else:
                        pass
                                            

                except:
                    pass
                if ex  != 0:
                    with open(filepath,"r",encoding="utf-8")as f1:
                        rd = csv.reader(f1)
                        mylist = list(rd)
                        for id_price in mylist:
                            id_user = int(id_price[0])
                            id_name = str(id_price[1])
                            xeez = int(id_price[2])
                            id_num = int(id_price[3])
                            if id_sell == id_user:
                                selldata = [[id_user,id_name,xeez,name_id,xeez*name_id]]
                                total = xeez*name_id
                                price = price + total
                            Label(sell,text=price,font=("Arial",20),bg="skyblue",width=20).grid(row=5,column=1)

                    try:
                        with open("รายการสินค้า.csv","r",encoding="utf-8")as f1:
                            rd = csv.reader(f1)
                            list_id = list(rd)
                            with open("รายการสินค้า-สำรอง.csv","w",encoding="utf-8")as f1:
                                for id_u in list_id:
                                    id_user = int(id_u[0])
                                    id_name = str(id_u[1])
                                    id_price = int(id_u[2])
                                    id_num = int(id_u[3])
                                    lsdt_sell = [[id_user,id_name,id_price,id_num,id_num,id_price*id_num]]
                                    if id_user == id_sell:
                                        lsdt_black = [[id_user,id_name,id_price,id_num+name_id]]
                                        with open("รายการสินค้า-สำรอง.csv","a+",encoding="utf-8")as f1:
                                            writer = csv.writer(f1,lineterminator="\n")
                                            writer.writerows(lsdt_black)
                                            sellnum = 1
                                    else:
                                        with open("รายการสินค้า-สำรอง.csv","a+",encoding="utf-8")as f1:
                                            writer = csv.writer(f1,lineterminator="\n")
                                            writer.writerows(lsdt_sell)
                                if sellnum ==1:
                                    save3()
                                else:
                                    pass

                            
                    except FileNotFoundError:
                            with open("รายการสินค้า.csv","a+",encoding="utf-8")as f1:
                                writer = csv.writer(f1,lineterminator="\n")
                                writer.writerows(selldata)
                                sellnum = 1
                    if sellnum == 0:   
                        with open("รายการสินค้า.csv","a+",encoding="utf-8")as f1:
                            writer = csv.writer(f1,lineterminator="\n")
                            writer.writerows(selldata)
            else:
                messagebox.showwarning("เกิดข้อผิดพลาด","กรุณากรอกจำนวนชิ้น")
        else:
            messagebox.showwarning("เกิดข้อผิดพลาด","กรุณากรอก ID")
    except UnboundLocalError:
        pass
            
def sathello():
    num = 0
    try:
        user_id = myinput.get()
        name_id = myinput1.get()
        try:
            price_id = myinput2.get()
            try:
                num_id = myinput3.get()
                if user_id != 0:
                    if len(name_id) != 0:
                        if price_id != 0:
                            if num_id != 0:
                                messagebox.showinfo("ลงทะเบียน","ลงทะเบียนเสร็จสิ้น")
                                lsdt = [[user_id,name_id,price_id,num_id]]
                                try:
                                    with open("data.csv","r",encoding="utf-8")as f1:
            
                                        rd = csv.reader(f1)
                                        list_id = list(rd)
                                        with open("data-สำรอง.csv","w",encoding="utf-8")as f1:
                                            for id_u in list_id:
            
                                                id_user = int(id_u[0])
                                                id_name = str(id_u[1])
                                                id_price = int(id_u[2])
                                                id_num = int(id_u[3])
                                                lsdt_black = [[id_user,id_name,id_price,id_num]]
                                                if id_user == user_id:
                                                    lsdt_black = [[id_user,id_name,id_price,id_num+num_id]]
                                                    with open("data-สำรอง.csv","a+",encoding="utf-8")as f1:
                                                        writer = csv.writer(f1,lineterminator="\n")
                                                        writer.writerows(lsdt_black)
                                                        num = 1
                                                else:
                                                    with open("data-สำรอง.csv","a+",encoding="utf-8")as f1:
                                                        writer = csv.writer(f1,lineterminator="\n")
                                                        writer.writerows(lsdt_black)
                                    if num == 1:
                                        save2()
                                    else:
                                        pass
                        
                                except:
                                    pass
                                if num == 0:
                                    with open("data.csv","a+",encoding="utf-8")as f1:
                                        writer = csv.writer(f1,lineterminator="\n")
                                        writer.writerows(lsdt)
                                else:
                                    pass
                            else:
                                messagebox.showwarning("เกิดข้อผิดพลาด","กรุณากรอกจำนวนชิ้น")
                        else:
                            messagebox.showwarning("เกิดข้อผิดพลาด","กรุณากรอกราคาสินค้า")
                    else:
                        messagebox.showwarning("เกิดข้อผิดพลาด","กรุณากรอกชื่อสินค้า")
                else:
                    messagebox.showwarning("เกิดข้อผิดพลาด","กรุณากรอกID")
            except TclError:
                messagebox.showwarning("เกิดข้อผิดพลาด","กรุณากรอก ตัวเลขเท่านั้น(จำนวนสินค้า)")
        except TclError:
            messagebox.showwarning("เกิดข้อผิดพลาด","กรุณากรอก ตัวเลขเท่านั้น(ราคา)")
    except TclError:
        messagebox.showwarning("เกิดข้อผิดพลาด","กรุณากรอกตัวเลขเท่านั้น(ID)ห้ามกรอกเลข 0 นำหน้า ")


def checkitem():
    eroe = 0
    filepath = "data.csv"
    id_user = myinput4.get()
    namefile = myinput4.get()
    try:
        with open(filepath,"r",encoding="utf-8")as f1:
            rd = csv.reader(f1)
            mylist = list(rd)
        for xd in mylist:
            id_namess = int(xd[0])
            name_idss = str(xd[1])
            id_sellss = int(xd[2])
            id_numsss = int(xd[3])
            if id_user == id_namess:
                item = Tk()
                item.title("เช็คสินค้า")
                Label(item,text="ID :  ",font=("Arial",15)).grid(row=0,column=0)
                Label(item,text=id_namess,font=("Arial",15)).grid(row=0,column=1)

                Label(item,text="    ชื่อสินค้า :  ",font=("Arial",15)).grid(row=0,column=2)
                Label(item,text=name_idss,font=("Arial",15)).grid(row=0,column=3)
                
                Label(item,text="    ราคาสินค้าชิ้นละ :  ",font=("Arial",15)).grid(row=0,column=4)
                Label(item,text=id_sellss,font=("Arial",15)).grid(row=0,column=5)
                Label(item,text="บาท",font=("Arial",15)).grid(row=0,column=6)

                Label(item,text="    จำนวนชิ้น :  ",font=("Arial",15)).grid(row=0,column=7)
                Label(item,text=id_numsss,font=("Arial",15)).grid(row=0,column=8)
                Label(item,text="    ชิ้น",font=("Arial",15)).grid(row=0,column=9)

                Button(item,text="ออกจากโปรแกรม",command=item.destroy,font=("Arial",15),width="30",fg="red").grid(row=5,columnspan=10,pady=50,sticky="news")
                item.mainloop()
                eroe = 1
    except FileNotFoundError:
        eroe = 1
        messagebox.showwarning("เกิดข้อผิดพลาด","ไม่พบข้อมูล") 
    if eroe == 0:
        messagebox.showwarning("เกิดข้อผิดพลาด","ไม่พบข้อมูล") 

def checksell():
    global total
    i = 0
    try:
        with open("รายการสินค้า.csv","r",encoding="utf-8")as f1:
            rd = csv.reader(f1)
            list_id = list(rd)
            check = Tk()
            check.title("เช็คสินค้า")
            total = 0
            for id_u in list_id:
                id_user = int(id_u[0])
                id_name = str(id_u[1])
                id_price = int(id_u[2])
                id_num = int(id_u[3])
                id_all = int(id_u[4])
                i = i+1
                Label(check,text="ID :",font=("Arial",15)).grid(row=i,column=0)
                Label(check,text=id_user,font=("Arial",15)).grid(row=i,column=1)
                Label(check,text="    ชื่อสินค้า :",font=("Arial",15)).grid(row=i,column=2)
                Label(check,text=id_name,font=("Arial",15)).grid(row=i,column=3)
                Label(check,text="     ราคาสินค้าชิ้นละ :",font=("Arial",15)).grid(row=i,column=4)
                Label(check,text=id_price,font=("Arial",15)).grid(row=i,column=5)
                Label(check,text="บาท",font=("Arial",15)).grid(row=i,column=6)
                Label(check,text="จำนวนชิ้น :",font=("Arial",15)).grid(row=i,column=7)
                Label(check,text=id_num,font=("Arial",15)).grid(row=i,column=8)
                Label(check,text="    ราคารวม :",font=("Arial",15)).grid(row=i,column=9)
                Label(check,text=id_all,font=("Arial",15)).grid(row=i,column=10)
                total = total +id_all
            Label(check,text="ราคารวม",font=("Arial",30)).grid(row=i+1,column=4)
            Label(check,text=total,font=("Arial",30)).grid(row=i+1,column=6)
    except FileNotFoundError:
        messagebox.showwarning("เกิดข้อผิดพลาด","ยังไม่มีสินค้าในระบบ") 




def tesead():
    global fun
    fun = 2
    main.destroy()

def tesead1():
    global fun
    fun = 1
    main.destroy()


if __name__== "__main__": 

    main = Tk()
    
    main.title("โปรแกรมเพื่อร้านสะดวกซื้อ")

    button = Button(text="ลงทะเบียนสินค้า",command=tesead1,font=("Arial",25),width=20,height=3,bg="skyblue",fg="Red").grid(row=0,columnspan=3,sticky="news",pady=30)
    button = Button(text="คิดราคาสินค้า",width=20,height=3,command=tesead,font=("Arial",25),bg="skyblue",fg="Red").grid(row=1,columnspan=3,sticky="news")
    main.mainloop()
    if fun == 1 :
        root = Tk()
        root.geometry("900x500")
    
        myinput =  IntVar()
        myinput1 = StringVar()
        myinput2 = IntVar()
        myinput3 = IntVar()
        myinput4 = IntVar()
    

        root.title("โปรแกรมเพื่อร้านสะดวกซื้อ (ลงทะเบียนสินค้า) ")

        Label(root,text="ชื่อ ID ที่ต้องการเช็ค",font=("Arial",30)).grid(row=0,column=1)

        Label(root,text="ID",font=("Arial",30)).grid(row=3,column=0)

        Label(root,text="ชื่อสินค้า",font=("Arial",30)).grid(row=4,column=0)

        Label(root,text="ราคา",font=("Arial",30)).grid(row=5,column=0)
    
        Label(root,text="จำนวนสินค้า",font=("Arial",30)).grid(row=6,column=0)




        et1 = Entry(root,textvariable=myinput,font=("Arial",30))
        et1.grid(row=3,column=1)

        et2 = Entry(root,textvariable=myinput1,font=("Arial",30))
        et2.grid(row=4,column=1)


        et3 = Entry(root,textvariable=myinput2,font=("Arial",30))
        et3.grid(row=5,column=1)

        et4 = Entry(root,textvariable=myinput3,font=("Arial",30))
        et4.grid(row=6,column=1)

        et5 = Entry(root,textvariable=myinput4,font=("Arial",30))
        et5.grid(row=1,column=1)

        button = Button(text="ลงทะเบียนสินค้า",command=sathello,font=("Arial",30)).grid(row=7,column=1)

        button = Button(text="เช็คข้อมูล",command=checkitem,font=("Arial",30)).grid(row=2,column=1,)


        mymenu = Menu()

        root.config(menu=mymenu)

        menuitem = Menu()

        root.mainloop()
    elif fun == 2 :
        sell = Tk()
        sell.geometry("600x400")
        sell.configure(bg="skyblue")
    
        sellinput =  IntVar()
        sellinput1 = StringVar()
        sellinput2 = IntVar()
    

        sell.title("โปรแกรมเพื่อร้านสะดวกซื้อ (คิดราคา) ")


        Label(sell,text="ID",font=("Arial",20),width="10").grid(row=1,column=0,pady=15)

    
        Label(sell,text="จำนวนสินค้า",font=("Arial",20),width="10").grid(row=2,column=0)

        Label(sell,text="ราคารวม",font=("Arial",20)).grid(row=4,column=1,pady=15)

        Label(text="0",font=("Arial",20),bg="skyblue",width=20).grid(row=5,column=1)



        et1 = Entry(sell,textvariable=sellinput,font=("Arial",20))
        et1.grid(row=1,column=1)

       # et2 = Entry(sell,textvariable=sellinput1,font=("Arial",20))
       # et2.grid(row=2,column=1)


        et3 = Entry(sell,textvariable=sellinput2,font=("Arial",20))
        et3.grid(row=2,column=1)


        button = Button(sell,text="คิดราคา",command=sellid,font=("Arial",15),width="30").grid(row=6,column=1,pady=10)

        button = Button(sell,text="เช็คใบเสร็จสินค้า",command=checksell,font=("Arial",15),width="30").grid(row=7,column=1,pady=10)
        button = Button(sell,text="เคลียค่าสินค้า",command=clearsell,font=("Arial",15),width="30").grid(row=8,column=1,pady=10)
        sell.protocol("WM_DELETE_WINDOW", clearsell2)

        sell.mainloop()
