#--------------------------------------------------------------Start------------------------------------------------------------
import mysql.connector as p
import matplotlib.pyplot as plt             #importing required modules
import tkinter as tk
cn=p.connect(host='localhost',user='root',passwd='batakh',database='Project32')       #establishing connection
#--------------------------------------------------------------Insert------------------------------------------------------------
def p_insert():
    def extra():
        z=var.get()
        def extra2():
            ins.destroy()
            menu()
        if z=='vendor':
            def extra1():
                a=E1.get()
                b=E2.get()
                c=E3.get()     #getting values from entries
                d=E4.get()
                e=E5.get()
                w=(a,b,c,d,e)
                cr=cn.cursor()
                q="insert into vendor values {}".format(w)
                cr.execute(q)  #executing query
                cn.commit()
                ins.destroy()
                menu()
            ins=tk.Tk()#creating window
            Choices.destroy() #destroying old window
            ins.geometry('800x400')
            ins['background']='light cyan'
            ins.title('Insert')
            M1=tk.Label(ins,text='Kousheya Silk Mills',justify='center',font=('Algerian',20))
            M1.place(relx=0.5,rely=0.1,anchor='center')
            M1['background']='light cyan'
            M2=tk.Label(ins,text='Insert The Values:',justify='center',font=('Calibri',15))
            M2.place(relx=0.5,rely=0.2,anchor='center')
            M2['background']='light cyan'
            L1=tk.Label(ins,text='Vid:',justify='center')
            L1.place(relx=0.4,rely=0.3,anchor='center')
            L1['background']='light cyan'#labels&Entries
            E1=tk.Entry(ins)
            E1.place(relx=0.5,rely=0.3,anchor='center')
            L2=tk.Label(ins,text='Vname:',justify='center')
            L2.place(relx=0.4,rely=0.4,anchor='center')
            L2['background']='light cyan'
            E2=tk.Entry(ins)
            E2.place(relx=0.5,rely=0.4,anchor='center')
            L3=tk.Label(ins,text='DOF:',justify='center')
            L3.place(relx=0.4,rely=0.5,anchor='center')
            L3['background']='light cyan'
            E3=tk.Entry(ins)
            E3.place(relx=0.5,rely=0.5,anchor='center')
            L4=tk.Label(ins,text='Nworth:',justify='center')
            L4.place(relx=0.4,rely=0.6,anchor='center')
            L4['background']='light cyan'
            E4=tk.Entry(ins)
            E4.place(relx=0.5,rely=0.6,anchor='center')
            L5=tk.Label(ins,text='City:',justify='center')
            L5.place(relx=0.4,rely=0.7,anchor='center')
            L5['background']='light cyan'
            E5=tk.Entry(ins)
            E5.place(relx=0.5,rely=0.7,anchor='center')
            B1=tk.Button(ins,text='SUBMIT',command=extra1,justify='center')
            B1.place(relx=0.5,rely=0.8,anchor='center')
            Bx=tk.Button(ins,text='Back',command=extra2)
            Bx.place(relx=0.1,rely=0.9,anchor='se')
        elif z=='fabric':
            def extra1():
                a=E1.get()
                b=E2.get()
                c=E3.get()     #getting values from entries
                d=E4.get()
                e=E5.get()
                w=(a,b,c,d,e)
                cr=cn.cursor()
                q="insert into fabric values {}".format(w)
                cr.execute(q)  #executing query
                cn.commit()
                ins.destroy()
                menu()
            ins=tk.Tk() #creating window
            Choices.destroy() #destroying old window
            ins.geometry('800x400')
            ins['background']='light cyan'
            ins.title('Insert')
            M1=tk.Label(ins,text='Kousheya Silk Mills',justify='center',font=('Algerian',20))
            M1.place(relx=0.5,rely=0.1,anchor='center')
            M1['background']='light cyan'
            M2=tk.Label(ins,text='Insert The Values:',justify='center',font=('Calibri',15))
            M2.place(relx=0.5,rely=0.2,anchor='center')
            M2['background']='light cyan'
            L1=tk.Label(ins,text='Fcode:',justify='center')
            L1.place(relx=0.4,rely=0.3,anchor='center')
            L1['background']='light cyan'#labels&Entries
            E1=tk.Entry(ins)
            E1.place(relx=0.5,rely=0.3,anchor='center')
            L2=tk.Label(ins,text='Fname:',justify='center')
            L2.place(relx=0.4,rely=0.4,anchor='center')
            L2['background']='light cyan'
            E2=tk.Entry(ins)
            E2.place(relx=0.5,rely=0.4,anchor='center')
            L3=tk.Label(ins,text='Cost:',justify='center')
            L3.place(relx=0.4,rely=0.5,anchor='center')
            L3['background']='light cyan'
            E3=tk.Entry(ins)
            E3.place(relx=0.5,rely=0.5,anchor='center')
            L4=tk.Label(ins,text='Quantity:',justify='center')
            L4.place(relx=0.4,rely=0.6,anchor='center')
            L4['background']='light cyan'
            E4=tk.Entry(ins)
            E4.place(relx=0.5,rely=0.6,anchor='center')
            L5=tk.Label(ins,text='Vid:',justify='center')
            L5.place(relx=0.4,rely=0.7,anchor='center')
            L5['background']='light cyan'
            E5=tk.Entry(ins)
            E5.place(relx=0.5,rely=0.7,anchor='center')
            B1=tk.Button(ins,text='SUBMIT',command=extra1,justify='center')
            B1.place(relx=0.5,rely=0.8,anchor='center')
            Bx=tk.Button(ins,text='Back',command=extra2)
            Bx.place(relx=0.1,rely=0.9,anchor='se')
    var=tk.StringVar()
    R1=tk.Radiobutton(Choices, text="Vendor", variable=var, value='vendor',command=extra)
    R1.place(relx=0.2,rely=0.3,anchor='center')
    R1['background']='light cyan'
    R2=tk.Radiobutton(Choices, text="Fabric", variable=var, value='fabric',command=extra)
    R2.place(relx=0.8,rely=0.3,anchor='center')
    R2['background']='light cyan'
#-------------------------------------------------------------Display------------------------------------------------------------ 
def p_display():
    from tkinter import ttk
    def extra():
        x=var.get()
        if x=='vendor':
            def extra2():
                disp.destroy()
                menu()
            Choices.destroy()
            disp=tk.Tk()
            disp.geometry('800x400')
            disp['background']='light cyan'
            disp.title('Display')
            M1=tk.Label(disp,text='Kousheya Silk Mills',justify='center',font=('Algerian',20))
            M1.pack(side=tk.TOP)
            M2=tk.Label(disp,text='Details of the Vendors',justify='center',font='Bahnschrift')
            M2.pack(side=tk.TOP)
            M1['background']='light cyan'
            M2['background']='light cyan'
            Bx=tk.Button(disp,text='Back',command=extra2)
            Bx.place(relx=0.1,rely=0.9,anchor='se')
            h=p_display1()
            fr=tk.Frame(disp)
            fr.pack(side=tk.BOTTOM)
            table=ttk.Treeview(disp)
            table['columns'] = ('Vid', 'Vname', 'DOF', 'Nworth', 'City')
            table.column("#0", width=0,  stretch='NO')
            table.column("Vid",anchor='center', width=80)
            table.column("Vname",anchor='center',width=80)
            table.column("DOF",anchor='center',width=80)
            table.column("Nworth",anchor='center',width=80)
            table.column("City",anchor='center',width=80)

            table.heading("#0",text="",anchor='center')
            table.heading("Vid",text="Id",anchor='center')
            table.heading("Vname",text="Name",anchor='center')
            table.heading("DOF",text="DOF",anchor='center')
            table.heading("Nworth",text="Nworth",anchor='center')
            table.heading("City",text="City",anchor='center')

            for k in range(len(h)):
                table.insert(parent='',index='end',iid=k,text='',values=h[k])
                table.pack()
        elif x=='fabric':
            def extra2():
                disp.destroy()
                menu()
            Choices.destroy()
            disp=tk.Tk()
            disp.geometry('800x400')
            disp['background']='light cyan'
            disp.title('Display')
            i=p_display2()
            M1=tk.Label(disp,text='Kousheya Silk Mills',justify='center',font=('Algerian',20))
            M1.pack(side=tk.TOP)
            M2=tk.Label(disp,text='Details of the Fabrics',justify='center',font='Bahnschrift')
            M2.pack(side=tk.TOP)
            M1['background']='light cyan'
            M2['background']='light cyan'
            Bx=tk.Button(disp,text='Back',command=extra2)
            Bx.place(relx=0.1,rely=0.9,anchor='se')
            h=p_display2()
            fr=tk.Frame(disp)
            fr.pack(side=tk.BOTTOM)
            table=ttk.Treeview(disp)
            table['columns'] = ('Fcode', 'Fname', 'Cost', 'Quantity', 'Vid')
            table.column("#0", width=0,  stretch='NO')
            table.column("Fcode",anchor='center', width=80)
            table.column("Fname",anchor='center',width=80)
            table.column("Cost",anchor='center',width=80)
            table.column("Quantity",anchor='center',width=80)
            table.column("Vid",anchor='center',width=80)

            table.heading("#0",text="",anchor='center')
            table.heading("Fcode",text="Id",anchor='center')
            table.heading("Fname",text="Name",anchor='center')
            table.heading("Cost",text="Cost",anchor='center')
            table.heading("Quantity",text="Quantity",anchor='center')
            table.heading("Vid",text="Vid",anchor='center')

            for k in range(len(h)):
                table.insert(parent='',index='end',iid=k,text='',values=h[k])
                table.pack()
    var=tk.StringVar()
    R1=tk.Radiobutton(Choices, text="Vendor", variable=var, value='vendor',command=extra)
    R1.place(relx=0.2,rely=0.2,anchor='center')
    R1['background']='light cyan'
    R2=tk.Radiobutton(Choices, text="Fabric", variable=var, value='fabric',command=extra)
    R2.place(relx=0.8,rely=0.2,anchor='center')
    R2['background']='light cyan'
#-------------------------------------------------------------Vendor-------------------------------------------------------------
def p_display1():
    cr=cn.cursor()
    cr.execute("Select * from vendor")
    d=cr.fetchall()
    return d
#-------------------------------------------------------------Fabric-------------------------------------------------------------
def p_display2():
    cr=cn.cursor()
    cr.execute("Select * from fabric")
    d=cr.fetchall()
    return d
#-------------------------------------------------------------Delete-------------------------------------------------------------
def p_delete():
    def func():
        z=var1.get()
        if z=='vendor':
            def extra2():
                delt.destroy()
                menu()
            delt=tk.Tk()                                                        #new window
            Choices.destroy()
            delt.geometry('800x400')
            delt['background']='light cyan'
            delt.title('Delete')
            M1=tk.Label(delt,text='Kousheya Silk Mills',justify='center',font=('Algerian',20))
            M1.place(relx=0.5,rely=0.1,anchor='center')
            M1['background']='light cyan'
            L1=tk.Label(delt,text='Vid of Vendor:',justify='center')
            L1.place(relx=0.4,rely=0.3,anchor='center')
            L1['background']='light cyan'#label&entries
            E1=tk.Entry(delt,justify='center')
            E1.place(relx=0.6,rely=0.3,anchor='center')
            def extra():
                a=E1.get()
                cr=cn.cursor()
                q="delete from vendor where Vid={}".format(a)       #executing queries
                cr.execute(q)
                cn.commit()
                delt.destroy()
                menu()
            B1=tk.Button(delt,text='Ok',command=extra)
            B1.place(relx=0.5,rely=0.5,anchor='center')
            Bx=tk.Button(delt,text='Back',command=extra2)
            Bx.place(relx=0.1,rely=0.9,anchor='se')
        elif z=='fabric':
            def extra2():
                delt.destroy()
                menu()
            delt=tk.Tk()                                                        #new window
            Choices.destroy()
            delt.geometry('800x400')
            delt['background']='light cyan'
            delt.title('Delete')
            M1=tk.Label(delt,text='Kousheya Silk Mills',justify='center',font=('Algerian',20))
            M1.place(relx=0.5,rely=0.1,anchor='center')
            M1['background']='light cyan'
            L1=tk.Label(delt,text='Fcode of Fabric:',justify='center')
            L1.place(relx=0.4,rely=0.3,anchor='center')
            L1['background']='light cyan'#label&entries
            E1=tk.Entry(delt,justify='center')
            E1.place(relx=0.6,rely=0.3,anchor='center')
            def extra():
                a=E1.get()
                cr=cn.cursor()
                q="delete from fabric where Fcode='{}'".format(a)       #executing queries
                cr.execute(q)
                cn.commit()
                delt.destroy()
                menu()
            B1=tk.Button(delt,text='Ok',command=extra)
            B1.place(relx=0.5,rely=0.5,anchor='center')
            Bx=tk.Button(delt,text='Back',command=extra2)
            Bx.place(relx=0.1,rely=0.9,anchor='se')
    var1=tk.StringVar()
    R1=tk.Radiobutton(Choices, text="Vendor", variable=var1, value='vendor',command=func)
    R1.place(relx=0.2,rely=0.6,anchor='center')
    R1['background']='light cyan'
    R2=tk.Radiobutton(Choices, text="Fabric", variable=var1, value='fabric',command=func)
    R2.place(relx=0.8,rely=0.6,anchor='center')
    R2['background']='light cyan'
#-------------------------------------------------------------Update-------------------------------------------------------------
def p_update():
    def func():
        w=var1.get()
        if w=='vendor':
            def extra2():
                upd.destroy()
                menu()
            def sel():
                cr=cn.cursor()
                x=var.get()
                if x=='vid' or x=='Nworth':
                    def extra():
                        xx=E1.get()
                        yy=E2.get()
                        q="update vendor set {}={} where Vid={}".format(x,xx,yy)
                        cr.execute(q)
                        cn.commit()
                        upd.destroy()
                        menu()
                    L1=tk.Label(upd,text='New Value:',justify='center')
                    L1.place(relx=0.54,rely=0.3,anchor='center')
                    L1['background']='light cyan'#1
                    E1=tk.Entry(upd,justify='center')
                    E1.place(relx=0.54,rely=0.35,anchor='center')#2
                    L2=tk.Label(upd,text='Whose value is to be updated:',justify='center')
                    L2.place(relx=0.54,rely=0.4,anchor='center')
                    L2['background']='light cyan'#3
                    E2=tk.Entry(upd,justify='center')
                    E2.place(relx=0.54,rely=0.45,anchor='center')#4
                    B1=tk.Button(upd,text='OK',command=extra,justify='center')
                    B1.place(relx=0.54,rely=0.5,anchor='center')#5
                elif x=='vname' or x=='dof' or x=='city':
                    def extra():
                        xx=E1.get()
                        yy=E2.get()
                        q="update vendor set {}='{}' where Vid={}".format(x,xx,yy)
                        cr.execute(q)
                        cn.commit()
                        upd.destroy()
                        menu()
                    L1=tk.Label(upd,text='New Value:',justify='center')
                    L1.place(relx=0.54,rely=0.3,anchor='center')
                    L1['background']='light cyan'#1
                    E1=tk.Entry(upd,justify='center')
                    E1.place(relx=0.54,rely=0.35,anchor='center')#2
                    L2=tk.Label(upd,text='Whose value is to be updated:',justify='center')
                    L2.place(relx=0.54,rely=0.4,anchor='center')
                    L2['background']='light cyan'#3
                    E2=tk.Entry(upd,justify='center')
                    E2.place(relx=0.54,rely=0.45,anchor='center')#4  
                    B1=tk.Button(upd,text='OK',command=extra,justify='center')
                    B1.place(relx=0.54,rely=0.5,anchor='center')#5
            Choices.destroy()
            upd=tk.Tk()
            var=tk.StringVar()
            upd.geometry('800x400')
            upd['background']='light cyan'
            upd.title('Update')
            M1=tk.Label(upd,text='Kousheya Silk Mills',justify='center',font=('Algerian',20))
            M1.place(relx=0.5,rely=0.1,anchor='center')
            M1['background']='light cyan'
            R1=tk.Radiobutton(upd, text="Vid", variable=var, value='vid',command=sel)
            R1.place(relx=0.2,rely=0.3,anchor='center')
            R2=tk.Radiobutton(upd, text="Vname", variable=var, value='vname',command=sel)
            R2.place(relx=0.2,rely=0.4,anchor='center')
            R3=tk.Radiobutton(upd, text="DOF", variable=var, value='dof',command=sel)
            R3.place(relx=0.2,rely=0.5,anchor='center')
            R4=tk.Radiobutton(upd, text="Nworth", variable=var, value='Nworth',command=sel)
            R4.place(relx=0.2,rely=0.6,anchor='center')
            R5=tk.Radiobutton(upd, text="City", variable=var, value='city',command=sel)
            R5.place(relx=0.2,rely=0.7,anchor='center')
            Bx=tk.Button(upd,text='Back',command=extra2)
            Bx.place(relx=0.1,rely=0.9,anchor='se')
        elif w=='fabric':
            def extra2():
                upd.destroy()
                menu()
            def sel():
                cr=cn.cursor()
                x=var.get()
                if x=='cost' or x=='quantity' or x=='vid':
                    def extra():
                        xx=E1.get()
                        yy=E2.get()
                        q="update fabric set {}={} where Fcode='{}'".format(x,xx,yy)
                        cr.execute(q)
                        cn.commit()
                        upd.destroy()
                        menu()
                    L1=tk.Label(upd,text='New Value:',justify='center')
                    L1.place(relx=0.54,rely=0.3,anchor='center')
                    L1['background']='light cyan'#1
                    E1=tk.Entry(upd,justify='center')
                    E1.place(relx=0.54,rely=0.35,anchor='center')#2
                    L2=tk.Label(upd,text='Whose value is to be updated:',justify='center')
                    L2.place(relx=0.54,rely=0.4,anchor='center')
                    L2['background']='light cyan'#3
                    E2=tk.Entry(upd,justify='center')
                    E2.place(relx=0.54,rely=0.45,anchor='center')#4
                    B1=tk.Button(upd,text='OK',command=extra,justify='center')
                    B1.place(relx=0.54,rely=0.5,anchor='center')#5
                elif x=='fname' or x=='fcode':
                    def extra():
                        xx=E1.get()
                        yy=E2.get()
                        q="update fabric set {}='{}' where Fcode='{}'".format(x,xx,yy)
                        cr.execute(q)
                        cn.commit()
                        upd.destroy()
                        menu()
                    L1=tk.Label(upd,text='New Value:',justify='center')
                    L1.place(relx=0.54,rely=0.3,anchor='center')
                    L1['background']='light cyan'#1
                    E1=tk.Entry(upd,justify='center')
                    E1.place(relx=0.54,rely=0.35,anchor='center')#2
                    L2=tk.Label(upd,text='Whose value is to be updated:',justify='center')
                    L2.place(relx=0.54,rely=0.4,anchor='center')
                    L2['background']='light cyan'#3
                    E2=tk.Entry(upd,justify='center')
                    E2.place(relx=0.54,rely=0.45,anchor='center')#4  
                    B1=tk.Button(upd,text='OK',command=extra,justify='center')
                    B1.place(relx=0.54,rely=0.5,anchor='center')#5
            Choices.destroy()
            upd=tk.Tk()
            var=tk.StringVar()
            upd.geometry('800x400')
            upd['background']='light cyan'
            upd.title('Update')
            M1=tk.Label(upd,text='Kousheya Silk Mills',justify='center',font=('Algerian',20))
            M1.place(relx=0.5,rely=0.1,anchor='center')
            M1['background']='light cyan'
            R1=tk.Radiobutton(upd, text="Fcode", variable=var, value='fcode',command=sel)
            R1.place(relx=0.2,rely=0.3,anchor='center')
            R2=tk.Radiobutton(upd, text="Fname", variable=var, value='fname',command=sel)
            R2.place(relx=0.2,rely=0.4,anchor='center')
            R3=tk.Radiobutton(upd, text="Cost", variable=var, value='cost',command=sel)
            R3.place(relx=0.2,rely=0.5,anchor='center')
            R4=tk.Radiobutton(upd, text="Quantity", variable=var, value='quantity',command=sel)
            R4.place(relx=0.2,rely=0.6,anchor='center')
            R5=tk.Radiobutton(upd, text="Vid", variable=var, value='vid',command=sel)
            R5.place(relx=0.2,rely=0.7,anchor='center')
            Bx=tk.Button(upd,text='Back',command=extra2)
            Bx.place(relx=0.1,rely=0.9,anchor='se')#updating
    var1=tk.StringVar()
    R1=tk.Radiobutton(Choices, text="Vendor", variable=var1, value='vendor',command=func)
    R1.place(relx=0.2,rely=0.4,anchor='center')
    R1['background']='light cyan'
    R2=tk.Radiobutton(Choices, text="Fabric", variable=var1, value='fabric',command=func)
    R2.place(relx=0.8,rely=0.4,anchor='center')
    R2['background']='light cyan'
#-------------------------------------------------------------Search--------------------------------------------------------------
def p_search():
    def func():
        z=var1.get()
        if z=='vendor':
            def extra2():
                sear.destroy()
                menu()
            sear=tk.Tk()
            Choices.destroy()
            sear['background']='light cyan'
            sear.geometry('800x400')
            sear.title('Search')
            M1=tk.Label(sear,text='Kousheya Silk Mills',justify='center',font=('Algerian',20))
            M1.place(relx=0.5,rely=0.1,anchor='center')
            M1['background']='light cyan'
            L1=tk.Label(sear,text='Vid of Vendor:',justify='center')
            L1.place(relx=0.4,rely=0.3,anchor='center')
            L1['background']='light cyan'
            E1=tk.Entry(sear)
            E1.place(relx=0.6,rely=0.3,anchor='center')
            def extra():
                x=E1.get()
                h=p_display1()
                for k in h:
                    if int(x)==k[0]:
                        T=tk.Text(sear, height=6,width =40)                                 #text field
                        T.place(relx=0.5, rely=0.8, anchor='center')
                        T.insert(tk.END,k)
                        break
                else:
                        w=tk.Label(sear,text='Record not present',fg='Red')
                        w.place(relx=0.5, rely=0.6, anchor='center')
                        w['background']='light cyan'
            B1=tk.Button(sear,text='Ok',command=extra)
            B1.place(relx=0.5,rely=0.5,anchor='center')
            Bx=tk.Button(sear,text='Back',command=extra2)
            Bx.place(relx=0.1,rely=0.9,anchor='se')
        elif z=='fabric':
            def extra2():
                sear.destroy()
                menu()
            sear=tk.Tk()                
            Choices.destroy()
            sear['background']='light cyan'
            sear.geometry('800x400')
            sear.title('Search')
            M1=tk.Label(sear,text='Kousheya Silk Mills',justify='center',font=('Algerian',20))
            M1.place(relx=0.5,rely=0.1,anchor='center')
            M1['background']='light cyan'
            L1=tk.Label(sear,text='Fcode of Fabric:',justify='center')
            L1.place(relx=0.4,rely=0.3,anchor='center')
            L1['background']='light cyan'
            E1=tk.Entry(sear)
            E1.place(relx=0.6,rely=0.3,anchor='center')
            def extra():
                x=E1.get()
                h=p_display2()
                for k in h:
                    if x==k[0]:
                        T=tk.Text(sear, height=6,width =40)                                 #text field
                        T.place(relx=0.5, rely=0.8, anchor='center')
                        T.insert(tk.END,k)
                        break
                else:
                        w=tk.Label(sear,text='Record not present',fg='Red')
                        w.place(relx=0.5, rely=0.6, anchor='center')
                        w['background']='light cyan'
            B1=tk.Button(sear,text='Ok',command=extra)
            B1.place(relx=0.5,rely=0.5,anchor='center')
            Bx=tk.Button(sear,text='Back',command=extra2)
            Bx.place(relx=0.1,rely=0.9,anchor='se')
    var1=tk.StringVar()
    R1=tk.Radiobutton(Choices, text="Vendor", variable=var1, value='vendor',command=func)
    R1.place(relx=0.2,rely=0.5,anchor='center')
    R1['background']='light cyan'
    R2=tk.Radiobutton(Choices, text="Fabric", variable=var1, value='fabric',command=func)
    R2.place(relx=0.8,rely=0.5,anchor='center')
    R2['background']='light cyan'
#-------------------------------------------------------------Graph--------------------------------------------------------------
def p_graph():
    def func():
        z=var1.get()
        if z=='vendor':
            Choices.destroy()
            t=p_display1()
            x=[];y=[]
            for k in t:
                x.append(k[1])
                y.append(k[3])
            plt.bar(x,y)
            plt.xlabel('Names')
            plt.ylabel('Nworth')
            plt.show()
            menu()
        elif z=='fabric':
            Choices.destroy()
            t=p_display2()
            x=[];y=[]
            for k in t:
                x.append(k[1])
                y.append(k[2])
            plt.plot(x,y)
            plt.xlabel('Fabric')
            plt.ylabel('Cost')
            plt.show()
            menu()
    var1=tk.StringVar()
    R1=tk.Radiobutton(Choices, text="Vendor", variable=var1, value='vendor',command=func)
    R1.place(relx=0.2,rely=0.7,anchor='center')
    R1['background']='light cyan'
    R2=tk.Radiobutton(Choices, text="Fabric", variable=var1, value='fabric',command=func)
    R2.place(relx=0.8,rely=0.7,anchor='center')
    R2['background']='light cyan'
#-------------------------------------------------------------Exit---------------------------------------------------------------
def p_exit():
    Choices.destroy()
    cn.close()
    print('Thanks')
#-------------------------------------------------------------Menu---------------------------------------------------------------
def menu():
    global Choices
    Choices=tk.Tk()
    Choices.geometry('800x400')
    Choices['background']='light cyan'
    Choices.title('Menu')
    M1=tk.Label(Choices,text='Kousheya Silk Mills Welcomes You!',justify='center',font=('Algerian',20))
    M1.place(relx=0.5,rely=0.1,anchor='center')
    M1['background']='light cyan'
    q1=tk.Button(Choices,text='Display',command=p_display,justify='center')
    q1.place(relx=0.5,rely=0.2,anchor='center')
    q2=tk.Button(Choices,text='Insert',command=p_insert,justify='center')
    q2.place(relx=0.5,rely=0.3,anchor='center')
    q3=tk.Button(Choices,text='Update',command=p_update,justify='center')
    q3.place(relx=0.5, rely=0.4, anchor='center')
    q4=tk.Button(Choices,text='Search',command=p_search,justify='center')
    q4.place(relx=0.5, rely=0.5, anchor='center')
    q5=tk.Button(Choices,text='Delete',command=p_delete,justify='center')
    q5.place(relx=0.5, rely=0.6, anchor='center')
    q6=tk.Button(Choices,text='Graph',command=p_graph,justify='center')
    q6.place(relx=0.5, rely=0.7, anchor='center')
    q7=tk.Button(Choices,text='Exit',command=p_exit,justify='center')
    q7.place(relx=0.5, rely=0.8, anchor='center')
#----------------------------------------------------------Verifiying------------------------------------------------------------
def check():
    ud=E1.get()
    pd=E2.get()
    if ud=='a' and pd=='abc':
        home.destroy()
        menu()
    else:
        w=tk.Label(home,text='Invalid Username or Password',fg='Red')
        w.place(relx=0.5, rely=0.6, anchor='center')
        w['background']='light cyan'
#----------------------------------------------------------Login Form------------------------------------------------------------
home=tk.Tk()
home.geometry("800x400")
home['background']='light cyan'
home.title('Login')
M1=tk.Label(home,text='Kousheya Silk Mills Welcomes You!',justify='center',font=('Algerian',20))
M1.place(relx=0.5,rely=0.1,anchor='center')
M1['background']='light cyan'
M2=tk.Label(home,text='Login Here:',justify='center',font='Bahnschrift')
M2.place(relx=0.5,rely=0.2,anchor='center')
M2['background']='light cyan'
L1=tk.Label(home,text='User ID:',justify='center')
L1.place(relx=0.36,rely=0.345,anchor='center')
L1['background']='light cyan'
E1=tk.Entry(home)
E1.place(relx=0.5,rely=0.345,anchor='center')
L2=tk.Label(home,text='Password:',justify='center')
L2.place(relx=0.36,rely=0.45,anchor='center')
L2['background']='light cyan'
E2=tk.Entry(home,show='*')
E2.place(relx=0.5,rely=0.45,anchor='center')
B1=tk.Button(home,text='OK',command=check,justify='center')
B1.place(relx=0.5, rely=0.55, anchor='center')
L3=tk.Label(home,text='Prepared by Shreyash, Shreyansh, Sumit')
L3.place(x=1,rely=1,anchor='sw')
L3['background']='light cyan'
tk.mainloop()
#----------------------------------------------------------The End-------------------------------------------------------------
