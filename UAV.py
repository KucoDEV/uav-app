# Fait par "Mathéo PICHOT-MOÏSE" alias "Kuco"
# https://github.com/KucoDEV
# (c) Copyright, KucoDEV 2022-2023
# Required PIP packages: requests, tkcalendar

try:
    import subprocess
    subprocess.call(["pip", "install", "requests"])
    subprocess.call(["pip", "install", "tkcalendar"])
except:
    pass

version = "1.12"

from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkcalendar import *
import csv
import requests
import webbrowser

def login():
    def connect():
        ddd()
        global login_screen
        login_screen = Tk()
        login_screen.overrideredirect(True)
        login_screen.geometry("300x250")
        login_screen.resizable(False, False)
        Label(text=f"\nVersion: {version}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n\n\n\n\n\n\n\n\n\n\n").pack()
        Label(login_screen, text="Veuillez renseigner les informations de votre compte").pack()
        Label(login_screen, text="").pack()
 
        global username_verify
        global password_verify
 
        username_verify = StringVar()
        password_verify = StringVar()
 
        global username_login_entry
        global password_login_entry
 
        Label(login_screen, text="Identifiant").pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Mot de passe").pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(login_screen, text="").pack() 
        Button(login_screen, text="Se connecter", width=10, height=1, command = login_verify).pack()

        login_screen.mainloop()

    def ddd():
        try:
            root.destroy()
        except:
            pass

    def login_verify():        
        def uav():
            global root
            login_screen.destroy()
            def load_stats():
                def leave():
                    stats.destroy()
                        
                stats = Tk()
                stats.overrideredirect(True)
                w, h = stats.winfo_screenwidth(), stats.winfo_screenheight()
                stats.geometry("%dx%d" % (w, h))
                stats.resizable(False, False)

                framestats = Frame(stats)
                        
                menubar = Menu(stats)
                stats.config(menu=menubar)
                menufichier = Menu(menubar,tearoff=0)
                menubar.add_cascade(label="Navigation", menu=menufichier)
                menufichier.add_command(label="Retour", command=leave)
                menufichier.bind_all("<Control-r>", lambda x: leave())

                t1 = Treeview(framestats, columns=('date', 'numdrone', 'type', 'stype', 'temps', 'numbat', 'pourcent', 'cycle'))

                t1.heading('date', text='Date (M/J/A)')

                t1.heading('numdrone', text='Drone')

                t1.heading('type', text='Type de vol')

                t1.heading('stype', text='Sous-type de vol')

                t1.heading('temps', text='Temps de vol')

                t1.heading('numbat', text='Batterie')

                t1.heading('pourcent', text='Batterie restant')

                t1.heading('cycle', text='Nombre de cycle')

                t1['show'] = 'headings'

                e = requests.get(f"https://db.beinguzeless.repl.co/v1/get?user={username1}")
                codee = e.json()

                final = codee['code']
                final.strip('\n')

                a = open(f"{username1}.csv", "w")
                a.write(final)
                a.close()

                with open(f'{username1}.csv') as f:
                    reader = csv.DictReader(f, delimiter=',')
                    for column in reader:
                        date = column['Date']
                        numdrone = column['Drone']
                        type = column['Type de vol']
                        stype = column['Sous-type de vol']
                        temps = column['Temps de vol']
                        numbat = column['Batterie']
                        pourcent = column['% de batterie restant']
                        cycle = column['Nombre de cycle']
                        t1.insert("", 0, values=(date, numdrone, type, stype, temps, numbat, pourcent, cycle))

                t1.grid(row=2, column=0)

                framestats.pack(expand=YES)
                        
                stats.mainloop()

            def load_new():
                def confirm():
                    global confirme
                    def annuler():
                        confirm.destroy()
                    
                    confirme = Tk()
                    confirme.overrideredirect(True)
                    w, h = new.winfo_screenwidth(), new.winfo_screenheight()
                    confirme.geometry("%dx%d" % (w, h))
                        
                    boite = Frame(confirme)

                    Label(boite, text="Voulez vous vraiment envoyer les données de vol ?").pack()
                    Button(boite, text="Envoyer", command=envoyer).pack()
                    Button(boite, text="Annuler", command=annuler).pack()

                    boite.pack(expand=YES)
                    confirme.mainloop()

                def envoyer():
                    confirme.destroy()
                    a = cal.get_date()# date
                    b = entry_bb.get()#num drone
                    c = entry_dd.get()#type
                    d = entry_cc.get()#sous-type
                    y = entry_y.get()#temps
                    e = entry_e.get()#num batterie
                    f = entry_f.get()#%
                    g = entry_g.get()#cycle

                    try:
                        r = requests.get(f"https://db.beinguzeless.repl.co/v1/{username1}?code={a},{b},{c},{d},{y},{e},{f},{g}")
                        oui = Label(framenew, text="Les données ont bien été envoyer !", fg="green")
                        oui.grid(row=11, column=1, columnspan=2)
                    except:
                        non = Label(framenew, text="Je n'ai pas réussie à envoyer les données !", fg="red")
                        non.grid(row=11, column=1, columnspan=2)
                        
                def leave():
                    new.destroy()

                new = Tk()
                new.overrideredirect(True)
                w, h = new.winfo_screenwidth(), new.winfo_screenheight()
                new.geometry("%dx%d" % (w, h))
                new.resizable(False, False)

                framenew = Frame(new)
                        
                menubar = Menu(new)
                new.config(menu=menubar)
                menufichier = Menu(menubar,tearoff=0)
                menubar.add_cascade(label="Navigation", menu=menufichier)
                menufichier.add_command(label="Retour", command=leave)
                menufichier.bind_all("<Control-r>", lambda x: leave())

                da = Label(framenew, text="Date").grid(row=1, column=0)
                cal = Calendar(framenew, selectmode="day", year=2023, month=4, day=1)
                cal.grid(row=1, column=1)

                ffff = Label(framenew, text=" ").grid(row=2, column=0)

                dr = Label(framenew, text="Numéro de drone").grid(row=3, column=0)
                entry_b = StringVar()
                entry_bb = ttk.Combobox(framenew, textvariable=entry_b)
                entry_bb['values'] = ("Drone 1", 
                            "Drone 2")
                entry_bb['state'] = 'readonly'
                entry_bb.current(0) 
                entry_bb.bind('<<ComboboxSelected>>')
                entry_bb.grid(row=3, column=1)

                dr = Label(framenew, text="Type de vol").grid(row=4, column=0)
                entry_d = StringVar()
                entry_dd = ttk.Combobox(framenew, textvariable=entry_d)
                entry_dd['values'] = ("Entrainement", 
                            "Operation",
                            "Autres")
                entry_dd['state'] = 'readonly'
                entry_dd.current(0) 
                entry_dd.bind('<<ComboboxSelected>>')
                entry_dd.grid(row=4, column=1)

                dr = Label(framenew, text="Sous-type de vol").grid(row=5, column=0)
                entry_c = StringVar()
                entry_cc = ttk.Combobox(framenew, textvariable=entry_c)
                entry_cc['values'] = ("Ordre publique", 
                            "Anti-Crim")
                entry_cc['state'] = 'readonly'
                entry_cc.current(0) 
                entry_cc.bind('<<ComboboxSelected>>')
                entry_cc.grid(row=5, column=1)

                dr = Label(framenew, text="Temps de vol").grid(row=6, column=0)
                entry_y = Entry(framenew)
                entry_y.grid(row=6, column=1)
                drr = Label(framenew, text="Format: heures:minutes:secondes").grid(row=6, column=2)

                ba = Label(framenew, text="Numéro de la batterie").grid(row=7, column=0)
                entry_e = Entry(framenew)
                entry_e.grid(row=7, column=1)

                pb = Label(framenew, text="% de batterie restant").grid(row=8, column=0)
                entry_f = Entry(framenew)
                entry_f.grid(row=8, column=1)
                drr = Label(framenew, text="Ne pas indiquer le signe %").grid(row=8, column=2)

                pb = Label(framenew, text="Nombre de cycle").grid(row=9, column=0)
                entry_g = Entry(framenew)
                entry_g.grid(row=9, column=1)

                send = Button(framenew, text="Envoyer", command=confirm)
                send.grid(row=10, column=0, columnspan=2, pady=20)

                framenew.pack(expand=YES)

                new.mainloop()

            def list_users():
                def leave():
                    list.destroy()
                    
                list = Tk()
                list.overrideredirect(True)
                w, h = list.winfo_screenwidth(), list.winfo_screenheight()
                list.geometry("%dx%d" % (w, h))
                list.resizable(False, False)

                framelist = Frame(list)

                r = requests.get(f"https://db.beinguzeless.repl.co/v1/list")
                data = r.json()
                total = data['total']
                Label(framelist, text=f"Il y a un total de {total} utilisateurs\nSur 3 villes différentes\n\n", fg="blue").pack()
                Label(framelist, text="\n\n\n")
                
                menubar = Menu(list)
                list.config(menu=menubar)
                menufichier = Menu(menubar,tearoff=0)
                menubar.add_cascade(label="Navigation", menu=menufichier)
                menufichier.add_command(label="Retour", command=leave)
                menufichier.bind_all("<Control-r>", lambda x: leave())

                sadm = StringVar()
                clent = StringVar()
                lnent = StringVar()
                gbent = StringVar()

                Label(framelist, text="Super utilisateurs:").pack()
                clrmfd = ttk.Combobox(framelist, textvariable=sadm)
                clrmfd['values'] = data['s-users']
                clrmfd['state'] = 'readonly'
                clrmfd.current(0) 
                clrmfd.bind('<<ComboboxSelected>>') 
                clrmfd.pack()

                Label(framelist, text="\nClermont-Ferrand:").pack()
                clrmfd = ttk.Combobox(framelist, textvariable=clent)
                clrmfd['values'] = data['clermont-users']
                clrmfd['state'] = 'readonly'
                clrmfd.current(0) 
                clrmfd.bind('<<ComboboxSelected>>') 
                clrmfd.pack()
                
                Label(framelist, text="\nLyon:").pack()
                lyon = ttk.Combobox(framelist, textvariable=lnent)
                lyon['values'] = data['lyon-users']
                lyon['state'] = 'readonly'
                lyon.current(0) 
                lyon.bind('<<ComboboxSelected>>') 
                lyon.pack()
                
                Label(framelist, text="\nGrenoble:").pack()
                grnb = ttk.Combobox(framelist, textvariable=gbent)
                grnb['values'] = data['grenoble-users']
                grnb['state'] = 'readonly'
                grnb.current(0) 
                grnb.bind('<<ComboboxSelected>>') 
                grnb.pack() 

                framelist.pack(expand=YES)

                list.mainloop()
            
            def add_users():
                def send():
                    a = entry_a.get()
                    try:
                        b = requests.get(f"https://db.beinguzeless.repl.co/v1/add?user={a}")
                        oui = Label(frameadd, text=f"Une demande a été envoyer pour créer l'utilisateur '{a}' !", fg="green")
                        oui.grid(row=3, column=1, columnspan=2)
                    except:
                        non = Label(frameadd, text="Je n'ai pas réussie à faire une demande !", fg="red")
                        non.grid(row=3, column=1, columnspan=2)
                    

                add = Tk()
                add.overrideredirect(True)
                w, h = add.winfo_screenwidth(), add.winfo_screenheight()
                add.geometry("%dx%d" % (w, h))
                add.resizable(False, False)

                def quit():
                    add.destroy()

                menubar = Menu(add)
                add.config(menu=menubar)
                menufichier = Menu(menubar,tearoff=0)
                menubar.add_cascade(label="Navigation", menu=menufichier)
                menufichier.add_command(label="Retour", command=quit)
                menufichier.bind_all("<Control-r>", lambda x: quit())
                
                frameadd = Frame(add)

                user = Label(frameadd, text="Nom d'utilisateur")
                user.grid(row=1, column=0)
                entry_a = Entry(frameadd)
                entry_a.grid(row=1, column=1)

                btn = Button(frameadd, text="Envoyer", command=send)
                btn.grid(row=2, column=0, columnspan=2, pady=20)

                frameadd.pack(expand=YES)

                add.mainloop()

            def download():
                def envoyer():
                    try:
                        b = requests.get(f"https://db.beinguzeless.repl.co/v1/download")
                        stat = b.json()
                        oui = Label(framedll, text=f"Téléchargement terminé !\nRegardez dans votre dossier téléchargement de votre appareil\npour trouver votre fichier.", fg="green")
                        oui.grid(row=4, column=0)
                        f = open("données_de_vol.csv", "w")
                        f.write(stat['code'])
                    except:
                        non = Label(framedll, text="Je n'ai pas réussie à télécharger !", fg="red")
                        non.grid(row=4, column=1)                    

                dll = Tk()
                dll.overrideredirect(True)
                w, h = dll.winfo_screenwidth(), dll.winfo_screenheight()
                dll.geometry("%dx%d" % (w, h))
                dll.resizable(False, False)

                def out():
                    dll.destroy()

                menubar = Menu(dll)
                dll.config(menu=menubar)
                menufichier = Menu(menubar,tearoff=0)
                menubar.add_cascade(label="Navigation", menu=menufichier)
                menufichier.add_command(label="Retour", command=out)
                menufichier.bind_all("<Control-r>", lambda x: out())

                framedll = Frame(dll)
                
                Label(framedll, text="Voulez-vous télécharger les données ?").grid(row=1, column=0)

                Button(framedll, text="Télécharger", command=envoyer).grid(row=2, column=0)

                framedll.pack(expand=YES)

                dll.mainloop()

            def leave():
                root.destroy()

            root = Tk()
            root.overrideredirect(True)
            w, h = root.winfo_screenwidth(), root.winfo_screenheight()
            root.geometry("%dx%d" % (w, h))
            root.resizable(False, False)
                
            frameapp = Frame(root)

            menubar = Menu(root)

            menufichier = Menu(menubar,tearoff=0)
            menufichier.add_command(label="Statistiques", command=load_stats)
            menufichier.add_command(label="Nouveau", command=load_new)
            menufichier.add_separator()
            menufichier.add_command(label="Déconnexion", command=connect)
            menufichier.add_command(label="Quitter", command=leave)
            menubar.add_cascade(label="Navigation", menu=menufichier)

            menubar.bind_all("<Control-s>", lambda x: load_stats())
            menubar.bind_all("<Control-t>", lambda x: load_new())
            menubar.bind_all("<Control-e>", lambda x: leave())

            perm = data['perm']

            if perm == "admin":
                menuadm = Menu(menubar,tearoff=0)
                menuadm.add_command(label="Tout les utilisateurs", command=list_users)
                menuadm.add_separator()
                menuadm.add_command(label="Nouvelle utilisateur", command=add_users)
                menuadm.add_separator()
                menuadm.add_command(label="Télécharger les données", command=download)
                menubar.bind_all("<Control-a>", lambda x: list_users())
                menubar.add_cascade(label="Administration", menu=menuadm)

            root.config(menu=menubar)
            
            name = data['nom']

            bvn = Label(frameapp, text=f"Bienvenue {name} sur votre compte !")
            bvn.grid(row=2, column=1)
            nav1 = Label(frameapp, text="Allez dans le menu de navigation pour inscrire ")
            nav1.grid(row=3, column=1)
            nav2 = Label(frameapp, text="vos différentes données ou les étudier")
            nav2.grid(row=4, column=1)


            frameapp.pack(expand=YES)

        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)

        r = requests.get(f"https://db.beinguzeless.repl.co/v1/db?user={username1}")
        data = r.json()
        if password1 == data['password']:
            uav()
        else:
            password_not_recognised()
    
    connect()

 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Tk()
    password_not_recog_screen.overrideredirect(True)
    password_not_recog_screen.geometry("150x100")
    password_not_recog_screen.resizable(False, False)
    Label(password_not_recog_screen, text="Mauvais mot de passe ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Tk()
    user_not_found_screen.overrideredirect(True)
    user_not_found_screen.geometry("150x100")
    user_not_found_screen.resizable(False, False)
    Label(user_not_found_screen, text="Identifiant non trouver").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def update():
    webbrowser.open("https://github.com/KucoDEV/uav-app")

r = requests.get(f"https://db.beinguzeless.repl.co/v1/version?version")
data = r.json()
if version == data['version']:
    login()
else:
    update()
