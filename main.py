from tkinter import *
import sqlite3
from tkinter import messagebox as ms
import os

nama1 = []
harga1 = []
jumlah1 = []
b = 0
stok1 = 0
# harga1=[]

root = Tk()
root.title("Tubes PBO")
root.geometry('300x420')

# icon = PhotoImage(file = 'book.ico')
root.iconbitmap('book.ico')

with sqlite3.connect('penjualan.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
c.execute('CREATE TABLE IF NOT EXISTS komik (no INTEGER NOT NULL ,nama TEXT NOT NULL , harga INTEGER NOT NULL , stok INTEGER NOT NULL);')
c.execute('CREATE TABLE IF NOT EXISTS novel (no INTEGER NOT NULL ,nama TEXT NOT NULL , harga INTEGER NOT NULL , stok INTEGER NOT NULL);')
db.commit()
db.close()

def Login() :
    HEIGHT = 500
    WIDTH = 450

    root.title("Login")
    loginFrame = Frame(width= 500 , height= 100)
    loginFrame.place(relwidth=1 , relheight=1)

    username = StringVar()
    password = StringVar()

    canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg="#edc7d2")
    canvas.pack()
    label_judul = Label(root, bg="#edc7d2", fg="#271c94", text="SELAMAT DATANG ", font=("Times New Roman", 10))
    label_judul.place(x=80, y=10)
    label_judul = Label(root, bg="#edc7d2", fg="#271c94", text="DI TOKO BUKU CERIA",
                           font=("Times New Roman", 10))
    label_judul.place(x=78, y=25)

    label_judul = Label(root, bg="#edc7d2", fg="#271c94", text="Jl.mustofa dg bunga VIII",
                           font=("Times New Roman", 8))
    label_judul.place(x=85, y=40)

    frame_alas = Frame(root, bd=5, bg="#edc7d2")
    frame_alas.place(x=20, y=70, width=260, height=190)

    frame_input = Frame(frame_alas, bd=1, bg="#f14e74")
    frame_input.place(y=1, x=1, width=250, height=138)

    label_user = Label(frame_input, bg="#ffffff", fg="#271c94", text="Menu Login", font=("Times", 10))
    label_user.place(x=0, y=0, width="248")

    label_user = Label(frame_input, bg="#f14e74", fg="#271c94", text="Username :", font=("Times", 10))
    label_user.place(x=10, y=30)

    entry_user = Entry(frame_input, textvariable=username, font=("Times", 12))
    entry_user.place(x=10, y=50, width=170)

    label_pass = Label(frame_input, bg="#f14e74", fg="#271c94", text="Password :", font=("Times", 10))
    label_pass.place(x=10, y=80)

    entry_pass = Entry(frame_input, textvariable=password, font=("Times", 12), show="*")
    entry_pass.place(x=10, y=100, width=170)

    frame_button = Frame(root, bd=5, bg="#edc7d2")
    frame_button.place(x=50, y=220, width=330, height=70)

    button_login = Button(frame_button, text="Reset", bg="#271c94", fg="#ffffff", font=("Times", 10),
                          command = lambda : reset(username , password))
    button_login.place(x=78, y=30, height=20, width=70)

    button_login = Button(frame_button, text="Sign in", bg="#271c94", fg="#ffffff",
                             font=("Times", 10), command=lambda : login1(username , password) )
    button_login.place(x=150, y=30, height=20, width=70)

def login1(username , password):
    # Establish Connection
        with sqlite3.connect('penjualan.db') as db:
            c = db.cursor()


        # Find user If there is any take proper action

        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user , [(username.get()), (password.get())])
        result = c.fetchall()
        if result:
            Utama()

            ms.showinfo("succes" , "Selamat Datang\n" + username.get())
        else:
            ms.showerror('Salah' , 'Maaf Password Salah')

def reset(username , password) :

    username.set("")
    password.set("")

def Utama() :
    HEIGHT = 500
    WIDTH = 450
    root.title("Utama")
    utamaFrame = Frame(width=300, height=100 , bg="#edc7d2")
    utamaFrame.place(relwidth=1, relheight=1)

    label_judul = Label(root, bg="#edc7d2", fg="#271c94", text="SELAMAT DATANG ", font=("Times New Roman", 10))
    label_judul.place(x=90, y=30)
    label_pilih = Label(root, bg="#edc7d2", fg="#271c94", text="SILAHKAN PILIH", font=("Times New Roman", 10))
    label_pilih.place(x=95, y=50)

    nama1.clear()
    harga1.clear()
    jumlah1.clear()

    button_komik = Button(root, text="Komik", bg="#271c94", fg="#ffffff", font=("Times", 10),
                          command=lambda: Komik())

    button_komik.place(x=60, y=100, height=25, width=200)

    button_novel = Button(root, text="Novel", bg="#271c94", fg="#ffffff", font=("Times", 10) ,
                          command=lambda : Novel())
    button_novel.place(x=60, y=133, height=25, width=200)

    button_cari = Button(root, text="Cari", bg="#271c94", fg="#ffffff", font=("Times", 10),
                          command=lambda: cari())
    button_cari.place(x=60, y=167, height=25, width=200)

def Komik() :
    root.title("Komik")
    utamaFrame = Frame(width=500, height=100 , bg="#edc7d2")
    utamaFrame.place(relwidth=1, relheight=1)

    label_judul = Label(root, bg="#edc7d2", fg="#271c94", text="Jenis Buku Komik ",
                           font=("Times New Roman", 12, "bold"))
    label_judul.place(x=130, y=15)

    label_judul = Label(root, bg="#edc7d2", fg="#271c94", text="Daftar Judul Buku :",
                           font=("Times New Roman", 10, "bold"))
    label_judul.place(x=20, y=40)

    frame_button = Frame(root, bd=5, bg="#f14e74")
    frame_button.place(x=20, y=70, width=262, height=245)

    label_judul = Label(root, bg="#ffffff", fg="#271c94", text="No", font=("Times New Roman", 10))
    label_judul.place(x=21, y=72, height=20, width=20)
    label_judul = Label(root, bg="#ffffff", fg="#271c94", text="Nama Buku ", font=("Times New Roman", 10))
    label_judul.place(x=43, y=72, height=20, width=108)
    label_judul = Label(root, bg="#ffffff", fg="#271c94", text="Harga ", font=("Times New Roman", 10))
    label_judul.place(x=153, y=72, height=20, width=80)



    label_judul = Label(root, bg="#ffffff", fg="#271c94", text=" Stok ", font=("Times New Roman", 10))
    label_judul.place(x=235, y=72, height=20, width=45)

    connt = sqlite3.connect('penjualan.db')
    cursor = connt.cursor()
    cursor.execute('SELECT * FROM komik')
    komik = cursor.fetchall()
    no = []
    nama = []
    harga = []
    stok = []
    y = 2

    for data in komik:
        no.insert(y ,data[0])
        y=y+1
    for data in komik:
        nama.append(data[1])
    for data in komik:
        harga.append(data[2])
    for data in komik:
        stok.append(data[3])

    t = 0
    o = 0
    for i in range(0 , len(nama)):

        label_judul = Label(root, bg="#ffffff", fg="#271c94", text=no[i], font=("Times New Roman", 10))
        label_judul.place(x=21, y=94 + t, height=20, width=20)
        label_judul = Label(root, bg="#ffffff", fg="#271c94", text=nama[i], font=("Times New Roman", 10))
        label_judul.place(x=43, y=94+t, height=20, width=108)
        label_judul = Label(root, bg="#ffffff", fg="#271c94", text=harga[i], font=("Times New Roman", 10))
        label_judul.place(x=153, y=94+t, height=20, width=80)

        label_stok = Label(root, bg="#ffffff", fg="#271c94", text=stok[i], font=("Times New Roman", 10))
        label_stok.place(x=235, y=94+t, height=20, width=45)
        t= t +22
        o=o+1

    frame_buttonn = Frame(root, bd=5, bg="#edc7d2")
    frame_buttonn.place(x=10, y=300, width=390, height=100)

    button_loginn = Button(frame_buttonn, text="Create", bg="#271c94", fg="#ffffff", font=("Times", 10),
                           command = lambda : Create(o+1 , "komik"))
    button_loginn.place(x=5, y=2, height=20, width=45)

    button_login = Button(frame_buttonn, text="Beli", bg="#271c94", fg="#ffffff", font=("Times New Roman", 10),
                          command = lambda : beli())

    button_login.place(x=55, y=2, height=20, width=45)

    button_update = Button(frame_buttonn, text="Update", bg="#271c94", fg="#ffffff", font=("Times New Roman", 10),
                           command=lambda: upd())
    button_update.place(x=105, y=2, height=20, width=45)

    button_update = Button(frame_buttonn, text="Delete", bg="#271c94", fg="#ffffff", font=("Times New Roman", 10),
                           command=lambda: det())
    button_update.place(x=155, y=2, height=20, width=45)

    button_loginn = Button(frame_buttonn, text="Back", bg="#271c94", fg="#ffffff", font=("Times", 10),
                              command=lambda : Utama())
    button_loginn.place(x=205, y=75, height=18, width=60)

    button_loginn = Button(frame_buttonn, text="Exit", bg="#271c94", fg="#ffffff", font=("Times", 10),
                           command=lambda : keluar())
    button_loginn.place(x=143, y=75, height=18, width=60)

    def beli() :
        nomor = StringVar()
        label_no = Label(root, bg="#edc7d2", fg="#000000", text="masukkan nomor komik", font=("Times New Roman", 10))
        label_no.place(x=5, y=350, height=20, width=150)

        entry_no = Entry(root, bg="#ffffff", font=("Times", 12) , textvariable=nomor)
        entry_no.place(x=145, y=350, height=18, width=100)

        button_loginn = Button(root, text="Ok", bg="#271c94", fg="#ffffff", font=("Times", 10),
                               command =  lambda : seleksiStok(nomor))
        button_loginn.place(x=230, y=350, height=17, width=48)

        def seleksiStok(nomor) :
            if (stok[int(nomor.get()) - 1] <= 0):
                ms.showerror("Maaf", "Barang Telah Habis Silahkan Memesan Yang Lain")
            else:
                Transaksi(nama[int(nomor.get()) - 1], harga[int(nomor.get()) - 1], "komik",
                          stok[int(nomor.get()) - 1])

    def det() :
        nomor = StringVar()
        label_no = Label(root, bg="#edc7d2", fg="#000000", text="masukkan nomor komik", font=("Times New Roman", 10))
        label_no.place(x=5, y=350, height=20, width=150)

        entry_no = Entry(root, bg="#ffffff", font=("Times", 12) , textvariable=nomor)
        entry_no.place(x=145, y=350, height=18, width=100)


        button_loginn = Button(root, text="Ok", bg="#271c94", fg="#ffffff", font=("Times", 10),
                               command =  lambda :delete(no[int(nomor.get()) - 1] , "komik"))
        button_loginn.place(x=230, y=350, height=17, width=48)

    def upd() :
        nomor = StringVar()
        label_no = Label(root, bg="#edc7d2", fg="#000000", text="masukkan nomor komik", font=("Times New Roman", 10))
        label_no.place(x=5, y=350, height=20, width=150)

        entry_no = Entry(root, bg="#ffffff", font=("Times", 12) , textvariable=nomor)
        entry_no.place(x=145, y=350, height=18, width=100)


        button_loginn = Button(root, text="Ok", bg="#271c94", fg="#ffffff", font=("Times", 10),
                               command =  lambda :update(no[int(nomor.get()) - 1] , nama[int(nomor.get()) - 1] , harga[int(nomor.get()) - 1]
                                                         ,stok[int(nomor.get()) - 1] , "komik"))
        button_loginn.place(x=230, y=350, height=17, width=48)

def Novel() :
    root.title("Novel")
    utamaFrame = Frame(width=500, height=100, bg="#edc7d2")
    utamaFrame.place(relwidth=1, relheight=1)

    label_judul = Label(root, bg="#edc7d2", fg="#271c94", text="Jenis Buku Novel ",
                        font=("Times New Roman", 12, "bold"))
    label_judul.place(x=130, y=15)

    label_judul = Label(root, bg="#edc7d2", fg="#271c94", text="Daftar Judul Buku :",
                        font=("Times New Roman", 10, "bold"))
    label_judul.place(x=20, y=40)

    frame_button = Frame(root, bd=5, bg="#f14e74")
    frame_button.place(x=20, y=70, width=262, height=245)

    label_judul = Label(root, bg="#ffffff", fg="#271c94", text="No", font=("Times New Roman", 10))
    label_judul.place(x=21, y=72, height=20, width=20)
    label_judul = Label(root, bg="#ffffff", fg="#271c94", text="Nama Buku ", font=("Times New Roman", 10))
    label_judul.place(x=43, y=72, height=20, width=108)
    label_judul = Label(root, bg="#ffffff", fg="#271c94", text="Harga ", font=("Times New Roman", 10))
    label_judul.place(x=153, y=72, height=20, width=80)

    label_judul = Label(root, bg="#ffffff", fg="#271c94", text=" Stok ", font=("Times New Roman", 10))
    label_judul.place(x=235, y=72, height=20, width=45)

    connt = sqlite3.connect('penjualan.db')
    cursor = connt.cursor()
    cursor.execute('SELECT * FROM novel')
    komik = cursor.fetchall()
    no = []
    nama = []
    harga = []
    stok = []
    y = 2

    for data in komik:
        no.insert(y, data[0])
        y = y + 1
    for data in komik:
        nama.append(data[1])
    for data in komik:
        harga.append(data[2])
    for data in komik:
        stok.append(data[3])

    t = 0
    o = 0
    for i in range(0, len(nama)):
        label_judul = Label(root, bg="#ffffff", fg="#271c94", text=no[i], font=("Times New Roman", 10))
        label_judul.place(x=21, y=94 + t, height=20, width=20)
        label_judul = Label(root, bg="#ffffff", fg="#271c94", text=nama[i], font=("Times New Roman", 10))
        label_judul.place(x=43, y=94 + t, height=20, width=108)
        label_judul = Label(root, bg="#ffffff", fg="#271c94", text=harga[i], font=("Times New Roman", 10))
        label_judul.place(x=153, y=94 + t, height=20, width=80)

        label_stok = Label(root, bg="#ffffff", fg="#271c94", text=stok[i], font=("Times New Roman", 10))
        label_stok.place(x=235, y=94 + t, height=20, width=45)
        t = t + 22
        o = o + 1

    frame_buttonn = Frame(root, bd=5, bg="#edc7d2")
    frame_buttonn.place(x=10, y=300, width=390, height=100)

    button_loginn = Button(frame_buttonn, text="Create", bg="#271c94", fg="#ffffff", font=("Times", 10),
                           command=lambda: Create(o + 1 , "novel"))
    button_loginn.place(x=5, y=10, height=20, width=45)

    button_login = Button(frame_buttonn, text="Beli", bg="#271c94", fg="#ffffff", font=("Times New Roman", 10),
                          command=lambda: beli())
    button_login.place(x=55, y=10, height=20, width=45)

    button_update = Button(frame_buttonn, text="Update", bg="#271c94", fg="#ffffff", font=("Times New Roman", 10),
                           command=lambda: upd())
    button_update.place(x=105, y=10, height=20, width=45)

    button_update = Button(frame_buttonn, text="Delete", bg="#271c94", fg="#ffffff", font=("Times New Roman", 10),
                           command=lambda: det())
    button_update.place(x=155, y=10, height=20, width=45)

    button_loginn = Button(frame_buttonn, text="Back", bg="#271c94", fg="#ffffff", font=("Times", 10),
                           command=lambda: Utama())
    button_loginn.place(x=215, y=70, height=20, width=50)

    button_loginn = Button(frame_buttonn, text="Exit", bg="#271c94", fg="#ffffff", font=("Times", 10),
                           command=lambda: keluar())
    button_loginn.place(x=160, y=70, height=20, width=50)

    def beli():
        nomor = StringVar()
        label_no = Label(root, bg="#edc7d2", fg="#000000", text="masukkan nomor komik", font=("Times New Roman", 10))
        label_no.place(x=5, y=350, height=20, width=150)

        entry_no = Entry(root, bg="#ffffff", font=("Times", 12), textvariable=nomor)
        entry_no.place(x=145, y=350, height=18, width=100)

        button_loginn = Button(root, text="Ok", bg="#271c94", fg="#ffffff", font=("Times", 10),
                               command=lambda: seleksiStok(nomor))
        button_loginn.place(x=230, y=350, height=17, width=48)

        def seleksiStok(nomor):
            if (stok[int(nomor.get()) - 1] <= 0):
                ms.showerror("Maaf", "Barang Telah Habis Silahkan Memesan Yang Lain")
            else:
                Transaksi(nama[int(nomor.get()) - 1], harga[int(nomor.get()) - 1], "novel",
                          stok[int(nomor.get()) - 1])

    def det():
        nomor = StringVar()
        label_no = Label(root, bg="#edc7d2", fg="#000000", text="masukkan nomor komik", font=("Times New Roman", 10))
        label_no.place(x=5, y=350, height=20, width=150)

        entry_no = Entry(root, bg="#ffffff", font=("Times", 12), textvariable=nomor)
        entry_no.place(x=145, y=350, height=18, width=100)

        button_loginn = Button(root, text="Ok", bg="#271c94", fg="#ffffff", font=("Times", 10),
                               command=lambda: delete(no[int(nomor.get()) - 1] , "novel"))
        button_loginn.place(x=230, y=350, height=17, width=48)

    def upd():
        nomor = StringVar()
        label_no = Label(root, bg="#edc7d2", fg="#000000", text="masukkan nomor komik", font=("Times New Roman", 10))
        label_no.place(x=5, y=350, height=20, width=150)

        entry_no = Entry(root, bg="#ffffff", font=("Times", 12), textvariable=nomor)
        entry_no.place(x=145, y=350, height=18, width=100)

        button_loginn = Button(root, text="Ok", bg="#271c94", fg="#ffffff", font=("Times", 10),
                               command=lambda: update(no[int(nomor.get()) - 1], nama[int(nomor.get()) - 1],
                                                      harga[int(nomor.get()) - 1], stok[int(nomor.get()) - 1] , "novel"))
        button_loginn.place(x=230, y=350, height=17, width=48)

def cari() :
    root.title("Komik")
    nama = StringVar()
    utamaFrame = Frame(width=500, height=100, bg="#edc7d2")
    utamaFrame.place(relwidth=1, relheight=1)

    label_judul = Label(root, bg="#edc7d2", fg="#271c94", text="Nama Buku : ", font=("Times New Roman", 10))
    label_judul.place(x=10, y=10, height=20, width=108)

    entry_nama = Entry(root, bg="#ffffff", font=("Times", 12), textvariable=nama)
    entry_nama.place(x=125, y=10, height=18, width=150)

    button_cari = Button(root, text="Cari", bg="#271c94", fg="#ffffff", font=("Times New Roman", 10),
                         command = lambda : search(nama.get()))
    button_cari.place(x=110, y=60, height=18, width=85)

    button_cancel = Button(root, text="Cancel", bg="#271c94", fg="#ffffff", font=("Times New Roman", 10),
                         command=lambda: Utama())
    button_cancel.place(x=110, y=85, height=18, width=85)

    def search(nama) :
        tabel = ""
        print(nama)
        connt = sqlite3.connect('penjualan.db')
        cursor = connt.cursor()
        cursor1 = connt.cursor()

        cursor.execute('SELECT * FROM komik')
        cursor1.execute('SELECT * FROM novel')
        dataku = cursor.fetchall()
        dataku1 = cursor1.fetchall()
        t = 0
        for i in dataku :
            if (nama == dataku[t][1]) :
                tabel = "komik"
            t = t +1
        j = 0
        for i in dataku1 :
            if (nama == dataku1[j][1]) :
                tabel = "novel"
            j = j + 1

        cursor.execute("SELECT * FROM " + tabel + " WHERE nama = (?)", (nama,))
        data1 = cursor.fetchall()

        nama = []
        harga = []
        stok = []
        for i in data1:
            nama.append(data1[0][1])
        for i in data1:
            harga.append(data1[0][2])

        for i in data1:
            stok.append(data1[0][3])

        t = 0
        o = 0
        for i in range(0, len(nama)):
            o = o + 1;
            label_judul = Label(root, bg="#ffffff", fg="#271c94", text=o, font=("Times New Roman", 10))
            label_judul.place(x=20, y=120 + t, height=20, width=20)
            label_judul = Label(root, bg="#ffffff", fg="#271c94", text=nama[i], font=("Times New Roman", 10))
            label_judul.place(x=42, y=120 + t, height=20, width=108)
            label_judul = Label(root, bg="#ffffff", fg="#271c94", text=harga[i], font=("Times New Roman", 10))
            label_judul.place(x=152, y=120 + t, height=20, width=70)
            label_stok = Label(root, bg="#ffffff", fg="#271c94", text=stok[i], font=("Times New Roman", 10))
            label_stok.place(x=224, y=120 + t, height=20, width=25)

            button_login = Button(root, text="Beli", bg="#271c94", fg="#ffffff", font=("Times New Roman", 10),
                                  command=lambda: seleksiStok())

            button_login.place(x=250, y=120 + t, height=19, width=45)

            t = t + 22

            def seleksiStok():
                if (stok[i] <= 0):
                    ms.showerror("Maaf", "Barang Telah Habis Silahkan Memesan Yang Lain")
                else:
                    Transaksi(nama[i] , harga[i] , "cari" , stok[i])


def Transaksi(nama , harga , tabel , stok) :
    nama1.append(nama)
    harga1.append(harga)

    if (tabel == "cari") :
        connt = sqlite3.connect('penjualan.db')
        cursor = connt.cursor()
        cursor1 = connt.cursor()

        cursor.execute('SELECT * FROM komik')
        cursor1.execute('SELECT * FROM novel')
        dataku = cursor.fetchall()
        dataku1 = cursor1.fetchall()

        t = 0
        for i in dataku:
            if (nama == dataku[t][1]):
                tabelku = "komik"
            t = t + 1
        j = 0

        for i in dataku1:
            if (nama == dataku1[j][1]):
                tabelku = "novel"
            j = j + 1
    elif tabel == "komik" :
        tabelku = "komik"
    elif tabel == "novel" :
        tabelku = "novel"

    root.title("Penjualan")
    utamaFrame = Frame(width=500, height=100, bg="#edc7d2")
    utamaFrame.place(relwidth=1, relheight=1)

    label_judul = Label(root, bg="#edc7d2", fg="#271c94", text="Menu Pembelian", font=("Times New Roman", 10))
    label_judul.place(x=15, y=10)

    frame_alas = Frame(root, bd=5, bg="#edc7d2")
    frame_alas.place(x=10, y=30, width=270, height=400)

    frame_input = Frame(frame_alas, bd=1, bg="#f14e74")
    frame_input.place(y=1, x=1, width=360, height=300)

    frame_button = Frame(root, bd=5, bg="#f14e74")
    frame_button.place(x=70, y=140, width=200, height=170)

    label_user = Label(frame_input, bg="#f14e74", fg="#271c94", text="Nama Buku :", font=("Times", 10))
    label_user.place(x=5, y=15)

    entry_user = Label(frame_input, bg="#f14e74", fg="#271c94" , font=("Times", 12) , text=nama)
    entry_user.place(x=80, y=15, height=18, width=167)

    label_pass = Label(frame_input, bg="#f14e74", fg="#271c94", text="Harga Buku :", font=("Times", 10))
    label_pass.place(x=5, y=40)

    entry_pass = Label(frame_input, bg="#f14e74", fg="#271c94" , font=("Times", 12) , text=harga)
    entry_pass.place(x=80, y=40, height=18, width=167)

    label_pass = Label(frame_input, bg="#f14e74", fg="#271c94", text="Jumlah Beli  :", font=("Times", 10))
    label_pass.place(x=5, y=66)

    entry_pass = Entry(frame_input, bg="#f14e74" , fg="#271c94" , font=("Times", 12))
    entry_pass.place(x=80, y=66, height=18, width=167)

    print(len(entry_pass.get()))

    button_login = Button(frame_button, text="Beli Buku", bg="#271c94", fg="#ffffff", font=("Times New Roman", 10) ,
                          command= lambda : seleksi())
    button_login.place(x=1, y=5, height=30, width=150)

    button_login = Button(frame_button, text="Tambah Buku lain", bg="#271c94", fg="#ffffff",
                             font=("Times New Roman", 10) , command = lambda : seleksi1())
    button_login.place(x=1, y=45, height=30, width=150)

    if (tabel == "komik") :
        button_login = Button(frame_button, text="cancel", bg="#271c94", fg="#ffffff", font=("Times", 10),
                              command = lambda : Komik() )
        button_login.place(x=130, y=120, height=20, width=50)

    elif (tabel == "novel") :
        button_login = Button(frame_button, text="cancel", bg="#271c94", fg="#ffffff", font=("Times", 10),
                              command=lambda: Novel())
        button_login.place(x=130, y=120, height=20, width=50)

    elif (tabel == "cari") :
        button_login = Button(frame_button, text="cancel", bg="#271c94", fg="#ffffff", font=("Times", 10),
                              command=lambda: cari())
        button_login.place(x=130, y=120, height=20, width=50)

    button_login = Button(frame_button, text="Exit", bg="#271c94", fg="#ffffff", font=("Times", 10), )
    button_login.place(x=79, y=120, height=20, width=50)

    def seleksi():
        a =(len(entry_pass.get()))

        if (a == 0):
            ms.showwarning('Warning', 'Form Tidak Boleh Kosong')
        else:
            b = int(entry_pass.get())
            jumlah1.append(b)

            if (b > stok) :
                ms.showerror('Maaf', 'Melebihi Batas Maksimum Barang')
            else:
                stok1 = stok - b
                conn = sqlite3.connect('penjualan.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE " + tabelku + " SET stok = ? WHERE nama = ?",
                               (stok1, nama))
                conn.commit()
                Tr(nama1 , sum(harga1) * sum(jumlah1))

    def seleksi1():
        a =(len(entry_pass.get()))
        if (a == 0):
            ms.showwarning('Warning', 'Form Tidak Boleh Kosong')
        else:
            b = int(entry_pass.get())
            jumlah1.append(b)

            if (b > stok) :
                ms.showerror('Maaf', 'Melebihi Batas Maksimum Barang')
            else:
                stok1 = stok - b
                conn = sqlite3.connect('penjualan.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE " + tabelku + " SET stok = ? WHERE nama = ?",
                               (stok1, nama))
                conn.commit()
                if (tabel == "komik") :
                    Komik()
                elif(tabel == "novel") :
                    Novel()
                elif (tabel == "cari"):
                    cari()


def Tr(nama , harga) :
    root.title("Transaksi")
    utamaFrame = Frame(width=500, height=100, bg="#edc7d2")
    utamaFrame.place(relwidth=1, relheight=1)

    frame_alas = Frame(root, bd=5, bg="#edc7d2")
    frame_alas.place(x=10, y=10, width=280, height=385)

    frame_input = Frame(frame_alas, bd=1, bg="#f14e74")
    frame_input.place(y=1, x=1, width=415, height=385)

    label_user = Label(frame_input, bg="#f14e74", fg="#271c94", text="Buku Yang Di Beli   :", font=("Times", 10))
    label_user.place(x=5, y=7)

    t = 0

    for i in range(len(nama)) :
        print(nama[i])
        label_pass = Label(root, bg="#f14e74", fg="#271c94", text=nama[i], font=("Times", 10))
        label_pass.place(x=140, y=24 + t)
        t = t + 20

    label_pass = Label(frame_input, bg="#f14e74", fg="#271c94", text="Harga Total    :", font=("Times", 10))
    label_pass.place(x=5, y=90)

    entry_pass = Label(frame_input, bg="#f14e74", fg="#271c94" , font=("Times", 11) , text=harga)
    entry_pass.place(x=100, y=90)

    label_pass = Label(frame_input, bg="#f14e74", fg="#271c94", text="Harga Bayar   :", font=("Times", 10))
    label_pass.place(x=5, y=130)

    entry_pass = Entry(frame_input, bg="#f14e74", fg="#271c94" , font=("Times", 12))
    entry_pass.place(x=95, y=130, height=18, width=100)

    frame_button = Frame(root, bd=5, bg="#f14e74")
    frame_button.place(x=95, y=188, width=150, height=95)

    button_login = Button(frame_button, text="Bayar", bg="#271c94", fg="#ffffff", font=("Times", 10),
                          command = lambda : Struk(nama , harga ,  int(entry_pass.get())))
    button_login.place(x=5, y=10, height=25, width=100)

    button_login = Button(frame_button, text="Cancel", bg="#271c94", fg="#ffffff", font=("Times", 10), )
    button_login.place(x=5, y=45, height=25, width=100)

def Struk(nama , harga , bayar) :
    root.title("Struk")
    utamaFrame = Frame(width=500, height=100, bg="#edc7d2")
    utamaFrame.place(relwidth=1, relheight=1)

    frame_alas = Frame(root, bd=5, bg="#edc7d2")
    frame_alas.place(x=10, y=10, width=278, height=385)

    frame_input = Frame(frame_alas, bd=1, bg="#f14e74")
    frame_input.place(y=1, x=1, width=415, height=380)

    label_judul = Label(root, bg="#f14e74", fg="#271c94", text=" TOKO BUKU CERIA", font=("Times New Roman", 10))
    label_judul.place(x=80, y=25)

    label_judul = Label(root, bg="#f14e74", fg="#271c94", text="Jl.mustofa dg bunga VIII",
                           font=("Times New Roman", 8))
    label_judul.place(x=80, y=40)

    # label_user = Label(frame_input, bg="#f14e74", fg="#271c94", text="Pembelian :", font=("Times", 10))
    # label_user.place(x=5, y=50)

    # frame_button = tk.Frame(root, bd=5, bg="#f14e74")
    # frame_button.place(x=70, y=140,width=190, height=140)
    t = 0
    label_user = Label(frame_input, bg="#f14e74", fg="#271c94", text="Buku Yang Di Beli   :", font=("Times", 10))
    label_user.place(x=5, y=58)
    for i in range(len(nama)):
        print(nama[i])
        label_pass = Label(root, bg="#f14e74", fg="#271c94", text=nama[i], font=("Times", 10))
        label_pass.place(x=150, y=74+t)
        t = t + 20


    label_pass = Label(frame_input, bg="#f14e74", fg="#271c94", text="Harga Bayar    :", font=("Times", 10))
    label_pass.place(x=5, y=150)

    label_harga = Label(frame_input, bg="#f14e74", fg="#271c94", text=harga, font=("Times", 10))
    label_harga.place(x=90, y=150)

    kembalian = bayar - harga

    label_pass = Label(frame_input, bg="#f14e74", fg="#271c94", text="Kembalian      :", font=("Times", 10))
    label_pass.place(x=5, y=180)

    label_kembalian = Label(frame_input, bg="#f14e74", fg="#271c94", text=kembalian, font=("Times", 10))
    label_kembalian.place(x=90, y=180)

    label_judul = Label(root, bg="#f14e74", fg="#271c94", text=" TERIMA KASIH TELAH BERBELANJA",
                           font=("Times New Roman", 10))
    label_judul.place(x=30, y=290)

    label_judul = Label(root, bg="#f14e74", fg="#271c94", text="DI TOKO KAMI", font=("Times New Roman", 8))
    label_judul.place(x=100, y=310)

    button_kembali = Button(root, text="Kembali Ke Menu Utama", bg="#271c94", fg="#ffffff", font=("Times", 10),
                          command=lambda: Utama())
    button_kembali.place(x=70, y=360, height=30, width=150)

def Create(no , tabel) :
    root.title("Create")
    utamaFrame = Frame(width=500, height=100, bg="#edc7d2")
    utamaFrame.place(relwidth=1, relheight=1)

    print(no)

    frame_alas = Frame(root, bd=5, bg="#f14e74")
    frame_alas.place(x=0, y=0, width=270, height=230)

    frame_input = Frame(frame_alas, bd=1, bg="#f14e74")
    frame_input.place(y=1, x=1, width=250, height=200)

    label_user = Label(frame_input, bg="#f14e74", fg="#271c94", text="nama buku  :", font=("Times", 10))
    label_user.place(x=5, y=15)

    entry_nama = Entry(frame_input, bg="#f14e74", font=("Times", 12))
    entry_nama.place(x=80, y=15, height=18, width=140)

    label_user = Label(frame_input, bg="#f14e74", fg="#271c94", text="harga           :", font=("Times", 10))
    label_user.place(x=5, y=40)

    entry_harga = Entry(frame_input, bg="#f14e74", font=("Times", 12))
    entry_harga.place(x=80, y=40, height=18, width=140)

    label_user = Label(frame_input, bg="#f14e74", fg="#271c94", text="stok             :", font=("Times", 10))
    label_user.place(x=5, y=65)

    entry_stok = Entry(frame_input, bg="#f14e74", font=("Times", 12))
    entry_stok.place(x=80, y=65, height=18, width=140)

    frame_button = Frame(root, bd=5, bg="#f14e74")
    frame_button.place(x=90, y=110, width=165, height=95)

    button_login = Button(frame_button, text="Create", bg="#271c94", fg="#ffffff", font=("Times", 10),
                          command = lambda :Tambah(tabel))
    button_login.place(x=5, y=10, height=20, width=100)

    if (tabel == "komik") :
        button_login = Button(frame_button, text="Cancel", bg="#271c94", fg="#ffffff", font=("Times", 10),
                          command= lambda : Komik())
        button_login.place(x=90, y=65, height=20, width=50)
    elif (tabel == "novel") :
        button_login = Button(frame_button, text="Cancel", bg="#271c94", fg="#ffffff", font=("Times", 10),
                              command=lambda: Novel())
        button_login.place(x=90, y=65, height=20, width=50)


    def Tambah(tabel) :
        nama = entry_nama.get()
        harga = entry_harga.get()
        stok = entry_stok.get()

        if(len(nama) == 0 or len(harga) == 0 or len(stok) == 0) :
            ms.showwarning("Warning" , "Form Tidak Boleh Kosong")
        else :
            conn = sqlite3.connect('penjualan.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO ' + tabel + ' (no ,nama, harga , stok) VALUES(?,?,?,?)', (no ,nama, harga,stok))
                ms.showinfo('Berhasil', 'Data Berhasil Di tambahkan')
                db.close()
                entry_nama.delete(0, END)
                entry_harga.delete(0, END)
                entry_stok.delete(0, END)

            if (tabel == "komik"):
                Komik()
            elif (tabel == "novel"):
                Novel()


def delete(nomor , tabel):
    no = []
    connnt = sqlite3.connect('penjualan.db')
    cursor = connnt.cursor()
    cursor.execute("DELETE FROM " + tabel + " WHERE no = ?", (nomor,))
    cursor.execute('SELECT * FROM ' + tabel)
    komik = cursor.fetchall()

    print(nomor)
    f = nomor
    print(tabel)

    for i in komik :
        no.append(i[0])

    for j in range(nomor-1 , len(no)) :
        cursor.execute("UPDATE " + tabel + " SET no = ? WHERE no = ?", (f, no[j]))
        f= f +1


    connnt.commit()
    if (tabel == "komik") :
        Komik()
    elif (tabel == "novel") :
        Novel()

def update(nomor , nama , harga , stok , tabel) :
    root.title("Create")
    utamaFrame = Frame(width=500, height=100, bg="#edc7d2")
    utamaFrame.place(relwidth=1, relheight=1)

    print(nama)

    frame_alas = Frame(root, bd=5, bg="#f14e74")
    frame_alas.place(x=0, y=0, width=270, height=230)

    frame_input = Frame(frame_alas, bd=1, bg="#f14e74")
    frame_input.place(y=1, x=1, width=250, height=200)

    label_user = Label(frame_input, bg="#f14e74", fg="#271c94", text="nama buku  :", font=("Times", 10))
    label_user.place(x=5, y=15)

    entry_nama = Entry(frame_input, bg="#f14e74", font=("Times", 12) , )
    entry_nama.place(x=80, y=15, height=18, width=140)

    entry_nama.insert(0 , nama)

    label_user = Label(frame_input, bg="#f14e74", fg="#271c94", text="harga           :", font=("Times", 10))
    label_user.place(x=5, y=40)

    entry_harga = Entry(frame_input, bg="#f14e74", font=("Times", 12))
    entry_harga.place(x=80, y=40, height=18, width=140)

    entry_harga.insert(0 , harga)

    label_user = Label(frame_input, bg="#f14e74", fg="#271c94", text="stok             :", font=("Times", 10))
    label_user.place(x=5, y=65)

    entry_stok = Entry(frame_input, bg="#f14e74", font=("Times", 12))
    entry_stok.place(x=80, y=65, height=18, width=140)

    entry_stok.insert(0 , stok)

    frame_button = Frame(root, bd=5, bg="#f14e74")
    frame_button.place(x=90, y=110, width=165, height=95)

    button_login = Button(frame_button, text="Update", bg="#271c94", fg="#ffffff", font=("Times", 10),
                          command=lambda: edit())
    button_login.place(x=5, y=10, height=20, width=100)

    if (tabel == "komik") :
        button_login = Button(frame_button, text="Cancel", bg="#271c94", fg="#ffffff", font=("Times", 10),
                              command=lambda: Komik())
        button_login.place(x=90, y=65, height=20, width=50)
    elif (tabel == "novel") :
        button_login = Button(frame_button, text="Cancel", bg="#271c94", fg="#ffffff", font=("Times", 10),
                              command=lambda: Novel())
        button_login.place(x=90, y=65, height=20, width=50)

    def edit():
        nama = entry_nama.get()
        harga = entry_harga.get()
        stok = entry_stok.get()
        conn = sqlite3.connect('penjualan.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE " + tabel + " SET nama = ? , harga = ? , stok = ? WHERE no = ?", (nama , harga , stok , nomor))
        conn.commit()
        entry_nama.delete(0, END)
        entry_harga.delete(0, END)
        entry_stok.delete(0, END)

def keluar():
    global root
    root.quit()

Login()

root.mainloop()
