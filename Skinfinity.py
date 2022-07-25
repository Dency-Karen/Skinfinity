from tkinter import *
from tkinter import ttk
#from turtle import left
import mysql.connector as myconn

global skin_type,skintype_id,skincon_id,myresd12,myresd22,user_id



    
    #def __init__(self, user_name,user_age):
        #self.user_name=user_name
        #self.user_age=user_age
def final_disp():
    global skintype_id
    global skincon_id
    global user_id
    #master=Tk(className="Skincare Routine")
    master=Toplevel(top)
    master.title("Skincare Routine")
    master.geometry("600x400")
    txt1=Text(master,height=5,width=52)
    txt2=Text(master,height=10,width=60)
    l6=Label(master,text="AM Routine")
    l6.config(font=("Courier",14))
    l7=Label(master,text="PM Routine")
    l7.config(font=("Courier",14))
    str=""
    str2=""
    z=""
    print("skin_typeid is",skintype_id)
    print("skincon_id is",skincon_id)
    print("Use in the morning")
    c=0
    list1=["Cleanser","Toner","Moisturizer","Sunscreen"]
    for x in myresd12:
                for y in x:
                    if(c<4):
                        
                        str=str +list1[c]+":"
                        str=str+y+"\n"
                        print(y,end=", ")
                        c=c+1
    str2=myresd22[0][1].split(",")
    print(type(str2))
    for x in str2:
        z=z+x+"\n"

            
                        


    print("\n Use at night")
    print(myresd22[0][1])
    txt1.insert(END,str)
    txt2.insert(END,z)
    l6.grid(row=0,column=1)
    txt1.grid(row=1,column=1)
    l7.grid(row=2,column=1)
    txt2.grid(row=3,column=1)
    b1_exit=Button(master,text="Exit",command=top.destroy)
    b1_exit.grid(row=4,column=1)
    master.mainloop()
    cursor=conn.cursor(buffered=True)
    cursor.execute("UPDATE user SET skin_type_id=%s ,skin_concern_id=%s WHERE user_id=%s",(skintype_id,skincon_id,user_id,))
            
    conn.commit()


def display2(choice):
        global skincon_id,myresd22
        choice=drop2.get()
        cursor=conn.cursor(buffered=True)
        query="SELECT skin_concern_id FROM skin_concern WHERE issues=%s"
        
            
        cursor.execute(query,(choice, ))
        myres=cursor.fetchall()
    
        myres1=list(myres)
        for x in myres1:
            for y in x:
                skincon_id=y
                print(y)
        print("skin con is is",skincon_id)
        query="SELECT * FROM pm_routine WHERE skin_concern_id=%s"
        cursor.execute(query,(skincon_id,))
        myresd22=cursor.fetchall()
        myresd22=list(myresd22)
        for x in myresd22:
            for y in x:
                
                print(y)
        
def skin_concern():
        global drop2,mas2
        #mas2=Tk(className="Skin Concern")
        mas2=Toplevel(top)
        mas2.title("Skin Concern")
        mas2.geometry("700x400")
        l4=Label(mas2,text="Skin Condition")
        l4.grid(row=0,column=0)
        options2 = ["None","Wrinkles","Dullness","Dullness,Wrinkles","Acne","Acne,Wrinkles","Acne,Dullness","Acne,Dullness,Wrinkles","Pigmentation","Pigmentation,Wrinkles","Pigmentation,Dullness","Pigmentation,Dullness,Wrinkles","Pigementation,Acne","Pigmentation,Acne,Wrinkles","Pigmentation,Acne,Dullness","Pigmentation,Acne,Dullness,Wrinkles"
        
                        ]
        clicked2 = StringVar()
        clicked2.set( "None" )
        drop2=ttk.Combobox(mas2,textvariable=clicked2,width=75)
        drop2['values']=options2
        drop2.grid(row=0,column=1)
        b3=Button(mas2,text="Next",command=lambda:final_disp())  
        b3.grid(row=4,column=1)
        
        
        drop2.bind('<<ComboboxSelected>>',display2)


def display1(event):
        global drop1,conn,myresd12,skintype_id

        choice=drop1.get()
            
            
        cursor=conn.cursor(buffered=True)
        query="SELECT skin_type_id FROM skin_type WHERE type_skin = %s"
        
            
        cursor.execute(query,(choice,))
        myres=cursor.fetchall()
    
        myres1=list(myres)
        for x in myres1:
                for y in x:
                    skintype_id=y
                    print(y)
        print("skin_type_id is",skintype_id)
        query1="SELECT * FROM am_routine WHERE skin_type_id = %s"
        cursor.execute(query1,(skintype_id,))
        myresd12=cursor.fetchall()
        myresd12=list(myresd12)
        for x in myresd12:
                for y in x:
                    
                    print(y)

def skin_type()  :      
        global drop1,mas

        #mas=Tk(className="skin_Type")
        mas=Toplevel(top)
        mas.title("Skin Type")
        mas.geometry("600x400")
        l3=Label(mas,text="Skin Type")
        l3.grid(row=0,column=0)
        options1 = [
            "Normal",
            "Dry",
            "Oily",
            "Combination"
                        ]
        clicked1 = StringVar()
        clicked1.set( "Normal" )
        drop1=ttk.Combobox(mas,textvariable=clicked1)
        drop1['values']=options1


        drop1.grid(row=0,column=1)
        b2=Button(mas,text="Next",command=lambda:skin_concern())   
        b2.grid(row=3,column=1)
        drop1.bind('<<ComboboxSelected>>',display1)
        
def add_data():
    global conn
    global cursor
    global e1,e2
    global skin_type,user_id
    user_name=e1.get()
    user_age=e2.get()
    f_v=True   
    if len(user_name) >20 :
        f_v=False
    try :
        val=int(user_age)
    except :
        f_v=False
    if(f_v ==True) :
        conn = myconn.MySQLConnection(user='sqluser',password='password',host='127.0.0.1',database='project1')
        cursor=conn.cursor(buffered=True)
        cursor.execute("")
        cursor.execute("INSERT INTO user(name,age)VALUES(%s,%s)",(user_name, user_age))
        conn.commit()
        query="SELECT * FROM USER ORDER BY user_id DESC LIMIT 1"
        cursor.execute(query)
        res=cursor.fetchall()
        user_id=int(res[0][2])
        print("user id is",user_id)


            
        conn.commit()
            
        skin_type()
        
    else :
        l5.config(fg='red')   # foreground color
        l5.config(bg='yellow') # background color
        my_str.set("check inputs.")
        

     
    

            
   
       
        

      
    
    
    

choice=""
skintype_id=0
top = Tk(className="Skincare")
top.geometry("600x400")
    
l1 = Label(top, text="User Name")
l2=Label(top, text="Age")

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)



e1=Entry(top)
e2=Entry(top)



  



e1.grid(row=0,column=1)
e2.grid(row=1,column=1)


b1=Button(top,text="Submit",command=lambda:add_data())
b1.grid(row=5,column=1)

my_str = StringVar()
l5 = Label(top,  textvariable=my_str, width=10 )  
l5.grid(row=1,column=3) 
my_str.set("Output")
top.mainloop()
   








