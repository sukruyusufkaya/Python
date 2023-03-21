from tkinter import * 
import socket
from tkinter import filedialog
from tkinter import messagebox
import os


root = Tk()
root.title("Dosya Paylaş")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)


def dosya_gonder():
    window = Toplevel(root)
    window.title("Dosya Gönder")
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)

    def dosya_sec():
        global dosya_adi
        dosya_adi = filedialog.askopenfilename(initialdir=os.getcwd(), title='Dosya Seç',filetype= (('Klasörler','*.txt'),('Tüm Dosyalar','*.*')))
    
    def dosya_gonderici():
        s = socket.socket()
        host = socket.gethostname()
        port = 8080 
        s.bind((host,port))
        s.listen(1)
        print(host)
        print("Bağlantı Bekleniyor") 
        conn,adrr = s.accept()
        file = open(dosya_adi,'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print("Dosya Transferi Başarılı")   
    
    #icon
    image_icon1 = PhotoImage(file="C:/Users/sukrukaya/Documents/python/my_projects/data_transfer/send.png")
    window.iconphoto(False,image_icon1)

    gonder_background = PhotoImage(file="C:/Users/sukrukaya/Documents/python/my_projects/data_transfer/sender.png")
    Label(window,image=gonder_background).place(x=-2,y=0)

    gonder_id_background = PhotoImage(file="C:/Users/sukrukaya/Documents/python/my_projects/data_transfer/id.png")
    Label(window,image=gonder_id_background,bg="#f4fdfe").place(x=100,y=260)    

    host = socket.gethostname()
    Label(window,text=f'ID: {host}', bg='white',fg='black').place(x=140,y=290)
    
    Button(window,text = "Dosya Seç",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=dosya_sec).place(x=160,y=150)
    Button(window,text="Gönder",width=8,height=1,font='arial 14 bold',bg='#000',fg='#fff',command=dosya_gonderici).place(x=300,y=150)
    window.mainloop()


def dosya_al():
    main = Toplevel(root)
    main.title("Dosya Al")
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)

    def gonderen():
        ID = gonderici_ID.get()
        dosya_adi1 = gelen_dosya.get()

        s = socket.socket()
        port = 8080 
        s.connect((ID,port))
        dosya = open(dosya_adi1,'wb')
        file_data = s.recv(1024)
        dosya.write(file_data)
        dosya.close()
        print("Dosya Alindi.")

    #icon
    image_icon1 = PhotoImage(file="C:/Users/sukrukaya/Documents/python/my_projects/data_transfer/receive.png")
    main.iconphoto(False,image_icon1)

    Hbackground = PhotoImage(file="C:/Users/sukrukaya/Documents/python/my_projects/data_transfer/receiver.png")
    Label(main,image=Hbackground).place(x=-2,y=0)

    logo = PhotoImage(file="C:/Users/sukrukaya/Documents/python/my_projects/data_transfer/profile.png")
    Label(main,image=logo,bg="#f4fdfe").place(x=10,y=250)

    Label(main,text="Dosya Al",font=('arial',20),bg="#f4fdfe").place(x=100,y=280)
    
    Label(main,text="Gönderen ID ",font=('arial',10,'bold'),bg='#f4fdfe').place(x=20,y=340)
    gonderici_ID = Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    gonderici_ID.place(x=20,y=370)
    gonderici_ID.focus()

    Label(main,text="Gelen Dosya Adı ",font=('arial',10,'bold'),bg='#f4fdfe').place(x=20,y=420)
    gelen_dosya = Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    gelen_dosya.place(x=20,y=450)
    
    imageicon = PhotoImage(file="C:/Users/sukrukaya/Documents/python/my_projects/data_transfer/arrow.png")
    rr = Button(main,text="Gelen",compound=LEFT,image=imageicon,width=130,bg="#39c790",font='arial 14 bold',command=gonderen)
    rr.place(x=20,y=500)


    main.mainloop()


#icon
image_icon = PhotoImage(file="C:/Users/sukrukaya/Documents/python/my_projects/data_transfer/icon.png")
root.iconphoto(False,image_icon)


Label(root,text="Dosya Transferi",font=('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)

Frame(root,width=400,height=2,bg="#f4f5f6").place()

gonder_dosya = PhotoImage(file="C:/Users/sukrukaya/Documents/python/my_projects/data_transfer/Image/send.png")
gonder = Button(root,image=gonder_dosya,bg="#f4fdfe",bd=0,command=dosya_gonder)
gonder.place(x=50,y=100)

al_dosya = PhotoImage(file="C:/Users/sukrukaya/Documents/python/my_projects/data_transfer/Image/receive.png")
al = Button(root,image=al_dosya,bg="#f4fdfe",bd=0,command=dosya_al)
al.place(x=300,y=100)


#label

Label(root,text="Dosya Gönder",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=15,y=200)
Label(root,text="Dosya Al",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=300,y=200)

background = PhotoImage(file="C:/Users/sukrukaya/Documents/python/my_projects/data_transfer/Image/background.png")
Label(root,image=background).place(x=-2,y=323)
root.mainloop()
