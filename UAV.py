# Fait par "Mathéo PICHOT-MOÏSE" alias "Kuco"
# Version actuelle: 1.8.6
# https://github.com/KucoDEV
# (c) Copyright, KucoDEV 2022-2023
# Required PIP packages: requests, tkcalendar

from tkinter import ttk
from tkinter import *
from tkcalendar import *
import csv
import requests

def login():
    def connect():
        global login_screen
        login_screen = Tk()
        login_screen.overrideredirect(True)
        login_screen.geometry("300x250")
        login_screen.resizable(False, False)
        Label(text="\n\n\n\n\n\n\n\n\n\n\n\n\n")
        Label(login_screen, text="Mettre les informations de votre compte").pack()
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

    def login_verify():        
        def uav():
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

                ent = Label(framestats, text="Vol d'entainement").grid(row=1, column=1)
                ope = Label(framestats, text="Vol d'opération").grid(row=2, column=1)

                framestats.pack(expand=YES)
                        
                stats.mainloop()

            def load_new():
                def confirm():
                    def annuler():
                        confirm.destroy()
                    
                    confirm = Tk()
                    confirm.overrideredirect(True)
                    w, h = new.winfo_screenwidth(), new.winfo_screenheight()
                    confirm.geometry("%dx%d" % (w, h))
                        
                    boite = Frame(confirm)

                    Label(boite, text="Voulez vous vraiment envoyer les données de vol ?").pack()
                    Button(boite, text="Envoyer", command=envoyer).pack()
                    Button(boite, text="Annuler", command=annuler).pack()

                    boite.pack(expand=YES)
                    confirm.mainloop()

                def envoyer():
                    confirm.destroy()
                    a = cal.get_date()
                    b = entry_bb.get()
                    c = entry_c.get()
                    d = entry_d.get()
                    e = entry_e.get()
                    f = entry_f.get()
                    g = entry_g.get()

                    nom_colonnes =['Date','Drone','Type','Temps','Batterie','%Batterie','Cycle']
                    fichier = open('données.csv', 'a', newline='\n', encoding='utf-8')
                    try:
                        with fichier:    
                            file = csv.DictWriter(fichier, fieldnames=nom_colonnes)
                            file.writerow({'Date': f'{a}','Drone': f'{b}', 'Type': f'{c}','Temps': f'{d}', 'Batterie': f'{e}','%Batterie': f'{f}%','Cycle': f'{g}'})
                            oui = Label(framenew, text="Les données ont bien été envoyer !", fg="green")
                            oui.grid(row=9, column=1, columnspan=2)
                    except:
                        non = Label(framenew, text="Je n'ai pas réussie à envoyer les données !", fg="red")
                        non.grid(row=9, column=1, columnspan=2)
                        
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
                cal = Calendar(framenew, selectmode="day", year=2023, month=4, day=9)
                cal.grid(row=1, column=1)

                dr = Label(framenew, text="Numéro de drone").grid(row=2, column=0)
                entry_b = StringVar()
                entry_bb = ttk.Combobox(framenew, textvariable=entry_b)
                entry_bb['values'] = ("Drône 1", 
                            "Drône 2")
                entry_bb['state'] = 'readonly'
                entry_bb.current(0) 
                entry_bb.bind('<<ComboboxSelected>>')
                entry_bb.grid(row=2, column=1)

                dr = Label(framenew, text="Type de vol").grid(row=3, column=0)
                entry_d = StringVar()
                entry_dd = ttk.Combobox(framenew, textvariable=entry_d)
                entry_dd['values'] = ("Entraînement", 
                            "Opération",
                            "Autres")
                entry_dd['state'] = 'readonly'
                entry_dd.current(0) 
                entry_dd.bind('<<ComboboxSelected>>')
                entry_dd.grid(row=3, column=1)

                dr = Label(framenew, text="Sous-type de vol").grid(row=4, column=0)
                entry_d = StringVar()
                entry_dd = ttk.Combobox(framenew, textvariable=entry_d)
                entry_dd['values'] = ("Ordre publique", 
                            "Anti-Crim")
                entry_dd['state'] = 'readonly'
                entry_dd.current(0) 
                entry_dd.bind('<<ComboboxSelected>>')
                entry_dd.grid(row=4, column=1)

                dr = Label(framenew, text="Temps de vol").grid(row=5, column=0)
                entry_c1 = StringVar()
                entry_heure = ttk.Combobox(framenew, textvariable=entry_c1)
                entry_heure['values'] = ("1h", 
                            "2h",
                            "3h",
                            "4h",
                            "5h",
                            "6h",
                            "7h",
                            "8h",
                            "9h",
                            "10h",
                            "11h",
                            "12h",
                            "13h",
                            "14h",
                            "15h",
                            "16h",
                            "17h",
                            "18h",
                            "19h",
                            "20h",
                            "21h",
                            "22h",
                            "23h",
                            "24h")
                entry_heure['state'] = 'readonly'
                entry_heure.current(0) 
                entry_heure.bind('<<ComboboxSelected>>')
                entry_heure.grid(row=5, column=1)
                entry_c2 = StringVar()
                entr_minute = ttk.Combobox(framenew, textvariable=entry_c2)
                entr_minute['values'] = ("1m", 
                            "2m",
                            "3m",
                            "4m",
                            "5m",
                            "6m",
                            "7m",
                            "8m",
                            "9m",
                            "10m",
                            "11m",
                            "12m",
                            "13m",
                            "14m",
                            "15m",
                            "16m",
                            "17m",
                            "18m",
                            "19m",
                            "20m",
                            "21m",
                            "22m",
                            "23m",
                            "24m",
                            "25m",
                            "26m",
                            "27m",
                            "28m",
                            "29m",
                            "30m",
                            "31m",
                            "32m",
                            "33m",
                            "34m",
                            "35m",
                            "36m",
                            "37m",
                            "38m",
                            "39m",
                            "40m",
                            "41m",
                            "42m",
                            "43m",
                            "44m",
                            "45m",
                            "46m",
                            "47m",
                            "48m",
                            "49m",
                            "50m",
                            "51m",
                            "52m",
                            "53m",
                            "54m",
                            "55m",
                            "56m",
                            "57m",
                            "58m",
                            "59m")
                entr_minute['state'] = 'readonly'
                entr_minute.current(0) 
                entr_minute.bind('<<ComboboxSelected>>')
                entr_minute.grid(row=5, column=2)
                entry_c3 = StringVar()
                entry_sec = ttk.Combobox(framenew, textvariable=entry_c3)
                entry_sec['values'] = ("1s", 
                            "2s",
                            "3s",
                            "4s",
                            "5s",
                            "6s",
                            "7s",
                            "8s",
                            "9s",
                            "10s",
                            "11s",
                            "12s",
                            "13s",
                            "14s",
                            "15s",
                            "16s",
                            "17s",
                            "18s",
                            "19s",
                            "20s",
                            "21s",
                            "22s",
                            "23s",
                            "24s",
                            "25s",
                            "26s",
                            "27s",
                            "28s",
                            "29s",
                            "30s",
                            "31s",
                            "32s",
                            "33s",
                            "34s",
                            "35s",
                            "36s",
                            "37s",
                            "38s",
                            "39s",
                            "40s",
                            "41s",
                            "42s",
                            "43s",
                            "44s",
                            "45s",
                            "46s",
                            "47s",
                            "48s",
                            "49s",
                            "50s",
                            "51s",
                            "52s",
                            "53s",
                            "54s",
                            "55s",
                            "56s",
                            "57s",
                            "58s",
                            "59s")
                entry_sec['state'] = 'readonly'
                entry_sec.current(0) 
                entry_sec.bind('<<ComboboxSelected>>')
                entry_sec.grid(row=5, column=3)

                ba = Label(framenew, text="Numéro de la batterie").grid(row=6, column=0)
                entry_e = Entry(framenew)
                entry_e.grid(row=6, column=1)

                pb = Label(framenew, text="% de batterie restant").grid(row=7, column=0)
                entry_f = Entry(framenew)
                entry_f.grid(row=7, column=1)

                pb = Label(framenew, text="Nombre de cycle").grid(row=8, column=0)
                entry_g = Entry(framenew)
                entry_g.grid(row=8, column=1)

                send = Button(framenew, text="Envoyer", command=confirm)
                send.grid(row=9, column=0, columnspan=2, pady=20)

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

                nb_user = 2
                Label(framelist, text=f"J'ai trouver {nb_user} utilisateurs\ndans mes base de données.\n\n", fg="blue").pack()
                Label(framelist, text="\n\n\n")
                
                menubar = Menu(list)
                list.config(menu=menubar)
                menufichier = Menu(menubar,tearoff=0)
                menubar.add_cascade(label="Navigation", menu=menufichier)
                menufichier.add_command(label="Retour", command=leave)
                menufichier.bind_all("<Control-r>", lambda x: leave())

                clent = StringVar()
                lnent = StringVar()
                gbent = StringVar()

                Label(framelist, text="Clermont-Ferrand:").pack()
                clrmfd = ttk.Combobox(framelist, textvariable=clent)
                clrmfd['values'] = ("Utilisateur", 
                   "mpichotmoise", 
                   "ppichotmoise")
                clrmfd['state'] = 'readonly'
                clrmfd.current(0) 
                clrmfd.bind('<<ComboboxSelected>>') 
                clrmfd.pack()
                
                Label(framelist, text="Lyon:").pack()
                lyon = ttk.Combobox(framelist, textvariable=lnent)
                lyon['values'] = ("Utilisateur",
                   "none")
                lyon['state'] = 'readonly'
                lyon.current(0) 
                lyon.bind('<<ComboboxSelected>>') 
                lyon.pack()
                
                Label(framelist, text="Grenoble:").pack()
                grnb = ttk.Combobox(framelist, textvariable=gbent)
                grnb['values'] = ("Utilisateur",
                   "none")
                grnb['state'] = 'readonly'
                grnb.current(0) 
                grnb.bind('<<ComboboxSelected>>') 
                grnb.pack() 

                framelist.pack(expand=YES)

                list.mainloop()
            
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
            menufichier.add_command(label="Déconnexion", command=leave)
            menufichier.add_command(label="Quitter", command=leave)
            menubar.add_cascade(label="Navigation", menu=menufichier)

            menubar.bind_all("<Control-s>", lambda x: load_stats())
            menubar.bind_all("<Control-t>", lambda x: load_new())
            menubar.bind_all("<Control-e>", lambda x: leave())

            perm = data['perm']

            if perm == "admin":
                menuadm = Menu(menubar,tearoff=0)
                menuadm.add_command(label="Tout les utilisateurs", command=list_users)
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
 
login()