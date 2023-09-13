from tkinter import * 
from tkinter import ttk 
import tkinter as tk
import webbrowser

NABTA = Tk() 

NABTA.geometry("555x555")

NABTA.title (" Nabtah - نبتة") 

NABTA.minsize(500,500)  

NABTA.iconbitmap('C:\\Users\\amina\\Downloads\\nabta Amina.ico')
#C:\Users\amina\Downloads>nabtaAmina22.jpg
#C:\Users\amina\Downloads>nabtaAmina23.png

NABTA.configure(bg="#FFFCEC") 

def open_link_brbeer():
    url = "https://www.instagram.com/explore/tags/itallgrows_purslane?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(url)

def open_link_n3n3():
    ur2 = "https://www.instagram.com/explore/tags/itallgrows_mint?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur2)

def open_link_shams():
    ur3 = "https://www.instagram.com/p/Ch_35QZsU7n/?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur3)

def open_link_khss():
    ur4 = "https://www.instagram.com/explore/tags/itallgrows_lettuce?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur4)

def open_link_jzr():
    ur5 = "https://www.instagram.com/reel/CjNuLaAgjFu/?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur5)

def open_link_grgeer():
    ur6 = "https://www.instagram.com/explore/tags/itallgrows_rocca?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur6)

def open_link_ryhan():
    ur7 = "https://www.instagram.com/explore/tags/itallgrows_basil?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur7)

def open_link_khyar():
    ur8 = "https://youtu.be/UFKY-mrvFh8?si=otR--0VePcdBolbK"  
    webbrowser.open(ur8)

def open_link_qr3():
    ur9 = "https://www.instagram.com/explore/tags/itallgrows_pumpkin?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur9)

def open_link_mlokheya():
    ur10 = "https://www.instagram.com/explore/tags/itallgrows_molokhia?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur10)

def open_link_smsm():
    ur11 = "https://www.instagram.com/reel/CsRN9rXAaHc/?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur11)

def open_link_frawla():
    ur12 = "https://youtu.be/7DsUqnk5L-g?si=GvrywU6DQHZdf94T"  
    webbrowser.open(ur12)

def open_link_cotton():
    ur13 = "https://www.instagram.com/reel/CtTryu5gQTE/?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur13)

def open_link_watermelon():
    ur14 = "https://www.instagram.com/explore/tags/itallgrows_melon?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur14)

def open_link_zhra():
    ur15 = "https://youtu.be/CDsmYo_Z_sE?si=SWNcolHDM1xrJrEV"  
    webbrowser.open(ur15)

def open_link_kosa():
    ur16 = "https://www.instagram.com/explore/tags/itallgrows_zucchini?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur16)

def open_link_bamya():
    ur17 = "https://youtu.be/3mEXySbeC_Q?si=qcOwmTnOqLf1DAfK"  
    webbrowser.open(ur17)

def open_link_fool():
    ur18 = "https://www.instagram.com/explore/tags/itallgrows_peanut?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur18)

def open_link_spanekh():
    ur19 = "https://www.instagram.com/explore/tags/itallgrows_newzealand?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur19)

def open_link_btata():
    ur20 = "https://www.instagram.com/explore/tags/itallgrows_sweetpotato?igshid=MzRlODBiNWFlZA=="  
    webbrowser.open(ur20)

def new_page9():
    sep= Tk()
    sep.geometry("555x555")
    sep.title ("September")
    sep.minsize(500,500)
    sep.iconbitmap('C:\\Users\\amina\\Downloads\\nabta Amina.ico')
    sep.configure(bg="#FFFCEC")
    
    label_may = Label(sep, text="هذه هي المحاصيل التي يمكنك زراعتها في شهر سبتمبر",bg="#FFFCEC",font =("Courier New",20),pady=30)
    label_may.pack()

    khyar = Button(sep, text="خيار",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_khyar) 
    khyar.config(activebackground="#FFFCEC")
    khyar.pack(side=LEFT, padx=10, ipady=20)
    
    qr3 = Button(sep, text=" قرع",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_qr3) 
    qr3.config(activebackground="#FFFCEC")
    qr3.pack(side=LEFT, padx=10, ipady=20)
    
    shams = Button(sep, text="دوار شمس",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_shams) 
    shams.config(activebackground="#FFFCEC")
    shams.pack(side=LEFT, padx=10, ipady=20)
    
    kosa= Button(sep, text="كوسا",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_kosa) 
    kosa.config(activebackground="#FFFCEC")
    kosa.pack(side=LEFT, padx=10, ipady=20)
    
    ryhan = Button(sep, text=" ريحان",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_ryhan) 
    ryhan.config(activebackground="#FFFCEC")
    ryhan.pack(side=LEFT, padx=10, ipady=20)
    
    grgeer= Button(sep, text=" جرجير",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_grgeer) 
    grgeer.config(activebackground="#FFFCEC")
    grgeer.pack(side=LEFT, padx=10, ipady=20)
    
    jzr= Button(sep, text=" جزر",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_jzr) 
    jzr.config(activebackground="#FFFCEC")
    jzr.pack(side=LEFT, padx=10, ipady=20)

    sep.mainloop()

def new_page10():
    oct= Tk()
    oct.geometry("555x555")
    oct.title ("October")
    oct.minsize(500,500)
    oct.iconbitmap('C:\\Users\\amina\\Downloads\\nabta Amina.ico')
    oct.configure(bg="#FFFCEC")
    
    label_may = Label(oct, text="هذه هي المحاصيل التي يمكنك زراعتها في شهر أكتوبر",bg="#FFFCEC",font =("Courier New",20),pady=30)
    label_may.pack()

    shams = Button(oct, text="دوار شمس",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_shams) 
    shams.config(activebackground="#FFFCEC")
    shams.pack(side=LEFT, padx=10, ipady=20)
    
    khyar = Button(oct, text="خيار",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_khyar) 
    khyar.config(activebackground="#FFFCEC")
    khyar.pack(side=LEFT, padx=10, ipady=20)
    
    ryhan = Button(oct, text=" ريحان",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_ryhan) 
    ryhan.config(activebackground="#FFFCEC")
    ryhan.pack(side=LEFT, padx=10, ipady=20)
    
    qr3 = Button(oct, text=" قرع",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_qr3) 
    qr3.config(activebackground="#FFFCEC")
    qr3.pack(side=LEFT, padx=10, ipady=20)
    
    grgeer= Button(oct, text=" جرجير",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_grgeer) 
    grgeer.config(activebackground="#FFFCEC")
    grgeer.pack(side=LEFT, padx=10, ipady=20)
    
    n3n3= Button(oct, text="نعناع",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_n3n3) 
    n3n3.config(activebackground="#FFFCEC")
    n3n3.pack(side=LEFT, padx=10, ipady=20)

    oct.mainloop()

def new_page11():
    nov= Tk()
    nov.geometry("555x555")
    nov.title ("November")
    nov.minsize(500,500)
    nov.iconbitmap('C:\\Users\\amina\\Downloads\\nabta Amina.ico')
    nov.configure(bg="#FFFCEC")
    
    label_may = Label(nov, text="هذه هي المحاصيل التي يمكنك زراعتها في شهر نوفمبر",bg="#FFFCEC",font =("Courier New",20),pady=30)
    label_may.pack()

    kosa= Button(nov, text="كوسا",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_kosa) 
    kosa.config(activebackground="#FFFCEC")
    kosa.pack(side=LEFT, padx=10, ipady=20)
    
    ryhan = Button(nov, text=" ريحان",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_ryhan) 
    ryhan.config(activebackground="#FFFCEC")
    ryhan.pack(side=LEFT, padx=10, ipady=20)
    
    grgeer= Button(nov, text=" جرجير",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_grgeer) 
    grgeer.config(activebackground="#FFFCEC")
    grgeer.pack(side=LEFT, padx=10, ipady=20)

    n3n3= Button(nov, text="نعناع",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_n3n3) 
    n3n3.config(activebackground="#FFFCEC")
    n3n3.pack(side=LEFT, padx=10, ipady=20)



    nov.mainloop()

def new_page12():
    dec= Tk()
    dec.geometry("555x555")
    dec.title ("December")
    dec.minsize(500,500)
    dec.iconbitmap('C:\\Users\\amina\\Downloads\\nabta Amina.ico')
    dec.configure(bg="#FFFCEC")
    
    label_may = Label(dec, text="هذه هي المحاصيل التي يمكنك زراعتها في شهر ديسمبر",bg="#FFFCEC",font =("Courier New",20),pady=30)
    label_may.pack()

    grgeer= Button(dec, text=" جرجير",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_grgeer) 
    grgeer.config(activebackground="#FFFCEC")
    grgeer.pack(side=LEFT, padx=10, ipady=20)
    
    n3n3= Button(dec, text="نعناع",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_n3n3) 
    n3n3.config(activebackground="#FFFCEC")
    n3n3.pack(side=LEFT, padx=10, ipady=20)

    spanekh= Button(dec, text="سبانخ",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_spanekh) 
    spanekh.config(activebackground="#FFFCEC")
    spanekh.pack(side=LEFT, padx=10, ipady=20)

    khss= Button(dec, text="خس",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_khss) 
    khss.config(activebackground="#FFFCEC")
    khss.pack(side=LEFT, padx=10, ipady=20)

    dec.mainloop()

def new_page1():
    jan= Tk()
    jan.geometry("555x555")
    jan.title ("January")
    jan.minsize(500,500)
    jan.iconbitmap('C:\\Users\\amina\\Downloads\\nabta Amina.ico')
    jan.configure(bg="#FFFCEC")
    
    label_may = Label(jan, text="هذه هي المحاصيل التي يمكنك زراعتها في شهر يناير",bg="#FFFCEC",font =("Courier New",20),pady=30)
    label_may.pack()

    grgeer= Button(jan, text=" جرجير",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_grgeer) 
    grgeer.config(activebackground="#FFFCEC")
    grgeer.pack(side=LEFT, padx=10, ipady=20)

    khss= Button(jan, text="خس",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_khss) 
    khss.config(activebackground="#FFFCEC")
    khss.pack(side=LEFT, padx=10, ipady=20)

    spanekh= Button(jan, text="سبانخ",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_spanekh) 
    spanekh.config(activebackground="#FFFCEC")
    spanekh.pack(side=LEFT, padx=10, ipady=20)

    zhra= Button(jan, text="زهرة",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_zhra) 
    zhra.config(activebackground="#FFFCEC")
    zhra.pack(side=LEFT, padx=10, ipady=20)

    frawla= Button(jan, text="فراولة",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_frawla) 
    frawla.config(activebackground="#FFFCEC")
    frawla.pack(side=LEFT, padx=10, ipady=20)

    jan.mainloop()

def new_page2():
    feb= Tk()
    feb.geometry("555x555")
    feb.title ("Februay")
    feb.minsize(500,500)
    feb.iconbitmap('C:\\Users\\amina\\Downloads\\nabta Amina.ico')
    feb.configure(bg="#FFFCEC")
    
    label_may = Label(feb, text="هذه هي المحاصيل التي يمكنك زراعتها في شهر فبراير",bg="#FFFCEC",font =("Courier New",20),pady=30)
    label_may.pack()

    kosa= Button(feb, text="كوسا",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_kosa) 
    kosa.config(activebackground="#FFFCEC")
    kosa.pack(side=LEFT, padx=10, ipady=20)
    
    bamya = Button(feb, text="بامية",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_bamya) 
    bamya.config(activebackground="#FFFCEC")
    bamya.pack(side=LEFT, padx=10, ipady=20)
    
    
    khyar = Button(feb, text="خيار",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_khyar) 
    khyar.config(activebackground="#FFFCEC")
    khyar.pack(side=LEFT, padx=10, ipady=20)
    
    shams = Button(feb, text="دوار شمس",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_shams) 
    shams.config(activebackground="#FFFCEC")
    shams.pack(side=LEFT, padx=10, ipady=20)
    
    ryhan = Button(feb, text=" ريحان",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_ryhan) 
    ryhan.config(activebackground="#FFFCEC")
    ryhan.pack(side=LEFT, padx=10, ipady=20)
    
    feb.mainloop()

def new_page3():
    mar= Tk()
    mar.geometry("555x555")
    mar.title ("March")
    mar.minsize(500,500)
    mar.iconbitmap('C:\\Users\\amina\\Downloads\\nabta Amina.ico')
    mar.configure(bg="#FFFCEC")
    
    label_may = Label(mar, text="هذه هي المحاصيل التي يمكنك زراعتها في شهر مارس",bg="#FFFCEC",font =("Courier New",20),pady=30)
    label_may.pack()

    mlokheya= Button(mar, text="ملوخية",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_mlokheya) 
    mlokheya.config(activebackground="#FFFCEC")
    mlokheya.pack(side=LEFT, padx=10, ipady=20)
    
    watermelon= Button(mar, text=" شمام\ بطيخ",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_watermelon) 
    watermelon.config(activebackground="#FFFCEC")
    watermelon.pack(side=LEFT, padx=10, ipady=20)
    
    cotton= Button(mar, text="قطن",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_cotton) 
    cotton.config(activebackground="#FFFCEC")
    cotton.pack(side=LEFT, padx=10, ipady=20)
    
    kosa= Button(mar, text="كوسا",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_kosa) 
    kosa.config(activebackground="#FFFCEC")
    kosa.pack(side=LEFT, padx=10, ipady=20)
    
    bamya = Button(mar, text="بامية",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_bamya) 
    bamya.config(activebackground="#FFFCEC")
    bamya.pack(side=LEFT, padx=10, ipady=20)
    
    khyar = Button(mar, text="خيار",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_khyar) 
    khyar.config(activebackground="#FFFCEC")
    khyar.pack(side=LEFT, padx=10, ipady=20)
    
    mar.mainloop()

def new_page4():
    apr= Tk()
    apr.geometry("555x555")
    apr.title ("April")
    apr.minsize(500,500)
    apr.iconbitmap('C:\\Users\\amina\\Downloads\\nabta Amina.ico')
    apr.configure(bg="#FFFCEC")
    
    label_may = Label(apr, text="هذه هي المحاصيل التي يمكنك زراعتها في شهر إبريل",bg="#FFFCEC",font =("Courier New",20),pady=30)
    label_may.pack()

    cotton= Button(apr, text="قطن",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_cotton) 
    cotton.config(activebackground="#FFFCEC")
    cotton.pack(side=LEFT, padx=10, ipady=20)
    
    mlokheya= Button(apr, text="ملوخية",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_mlokheya) 
    mlokheya.config(activebackground="#FFFCEC")
    mlokheya.pack(side=LEFT, padx=10, ipady=20)
    
    brbeer= Button(apr, text="رجلة\ بربير",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_brbeer) 
    brbeer.config(activebackground="#FFFCEC")
    brbeer.pack(side=LEFT, padx=10, ipady=20)
    
    smsm= Button(apr, text="سمسم",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_smsm) 
    smsm.config(activebackground="#FFFCEC")
    smsm.pack(side=LEFT, padx=10, ipady=20)
    
    watermelon= Button(apr, text=" شمام\ بطيخ",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_watermelon) 
    watermelon.config(activebackground="#FFFCEC")
    watermelon.pack(side=LEFT, padx=10, ipady=20)
    
    fool= Button(apr, text="فول سوداني",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_fool) 
    fool.config(activebackground="#FFFCEC")
    fool.pack(side=LEFT, padx=10, ipady=20)

    apr.mainloop()

def new_page5():
    from PIL import Image, ImageTk
    from tkinter import ttk 
    import tkinter as tk

    may= Tk()
    may.geometry("555x555")
    may.title ("May")
    may.minsize(500,500)
    may.iconbitmap('C:\\Users\\amina\\Downloads\\nabta Amina.ico')
    may.configure(bg="#FFFCEC")
    
    label_may = Label(may, text="هذه هي المحاصيل التي يمكنك زراعتها في شهر مايو",bg="#FFFCEC",font =("Courier New",20),pady=30)
    label_may.pack()

#C:\\Users\\amina\\Downloads\\nabtaAmina22.jpg

    smsm= Button(may, text="سمسم",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_smsm) 
    smsm.config(activebackground="#FFFCEC")
    smsm.pack(side=LEFT, padx=10, ipady=20)
    
    brbeer= Button(may, text="رجلة\ بربير",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_brbeer) 
    brbeer.config(activebackground="#FFFCEC")
    brbeer.pack(side=LEFT, padx=10, ipady=20)
    
    mlokheya= Button(may, text="ملوخية",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_mlokheya) 
    mlokheya.config(activebackground="#FFFCEC")
    mlokheya.pack(side=LEFT, padx=10, ipady=20)
    
    cotton= Button(may, text="قطن",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_cotton) 
    cotton.config(activebackground="#FFFCEC")
    cotton.pack(side=LEFT, padx=10, ipady=20)
    
    sweatpotato= Button(may, text="بطاطا حلوة",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_btata) 
    sweatpotato.config(activebackground="#FFFCEC")
    sweatpotato.pack(side=LEFT, padx=10, ipady=20)
    
    fool= Button(may, text="فول سوداني",fg="black",bg="#FFCEC8",width=20, height=2,font =("Courier New",10),pady=5,relief="flat", command=open_link_fool) 
    fool.config(activebackground="#FFFCEC")
    fool.pack(side=LEFT, padx=10, ipady=20)
    
    may.mainloop()

first_label = Label(NABTA, text="أهلا بك في نبته!",bg="#FFFCEC",font =("Courier New",20),pady=30)
first_label.pack()

from PIL import Image, ImageTk

image = Image.open("C:\\Users\\amina\\Downloads\\nabtaAmina22.jpg") 
new_width = 300  
new_height = 300
image = image.resize((new_width, new_height))
photo = ImageTk.PhotoImage(image)
label = tk.Label(NABTA, image=photo)
label.image = photo  
label.pack()

second_label = Label(NABTA, text=(":اختر أيًّا من هذه الشهور لتظهر لك قائمة بالمحاصيل والنباتات التي تتم زراعتها في هذا الشهر،"),bg="#FFFCEC",font =("Courier New",15))
second_label.pack()

ZR9 = Button(NABTA, text="Sep 9",fg="black",bg="#FFCDC7",width=14, height=2,font =("Courier New",10),pady=5,command=new_page9,relief="flat") 
ZR9.config(activebackground="#FFFCEC")
ZR9.pack(side=LEFT, padx=10, ipady=20)

ZR10 = Button(NABTA, text="Oct 10",fg="black",bg="#C89F9A",width=14, height=2,font =("Courier New",10),pady=5,command=new_page10,relief="flat") 
ZR10.config(activebackground="#FFFCEC")
ZR10.pack(side=LEFT, padx=10, ipady=20)

ZR11 = Button(NABTA, text="Nov 11",fg="black",bg="#FFCDC7",width=14, height=2,font =("Courier New",10),pady=5,command=new_page11,relief="flat") 
ZR11.config(activebackground="#FFFCEC")
ZR11.pack(side=LEFT, padx=10, ipady=20)

ZR12 = Button(NABTA, text="Dec 12",fg="black",bg="#C89F9A",width=14, height=2,font =("Courier New",10),pady=5,command=new_page12,relief="flat") 
ZR12.config(activebackground="#FFFCEC")
ZR12.pack(side=LEFT, padx=10, ipady=20)

ZR1 = Button(NABTA, text="Jan 1",fg="black",bg="#FFCDC7",width=14, height=2,font =("Courier New",10),pady=5,command=new_page1,relief="flat") 
ZR1.config(activebackground="#FFFCEC")
ZR1.pack(side=LEFT, padx=10, ipady=20)

ZR2 = Button(NABTA, text="Feb 2",fg="black",bg="#C89F9A",width=14, height=2,font =("Courier New",10),pady=5,command=new_page2,relief="flat") 
ZR2.config(activebackground="#FFFCEC")
ZR2.pack(side=LEFT, padx=10, ipady=20)

ZR3 = Button(NABTA, text="Mar 3",fg="black",bg="#FFCDC7",width=14, height=2,font =("Courier New",10),pady=5,command=new_page3,relief="flat") 
ZR3.config(activebackground="#FFFCEC")
ZR3.pack(side=LEFT, padx=10, ipady=20)

ZR4 = Button(NABTA, text="Apr 4",fg="black",bg="#C89F9A",width=14, height=2,font =("Courier New",10),pady=5,command=new_page4,relief="flat") 
ZR4.config(activebackground="#FFFCEC")
ZR4.pack(side=LEFT, padx=10, ipady=20)

ZR5 = Button(NABTA, text="May 5",fg="black",bg="#FFCDC7",width=14, height=2,font =("Courier New",10),pady=5,command=new_page5,relief="flat") 
ZR5.config(activebackground="#FFFCEC")
ZR5.pack(side=LEFT, padx=10, ipady=20)

NABTA.mainloop()