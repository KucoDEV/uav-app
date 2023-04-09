# Fait par "Mathéo PICHOT-MOÏSE" alias "Kuco"
# Version actuelle: 1.8.1
# https://github.com/KucoDEV
# (c) Copyright, KucoDEV 2022-2023

from datetime import datetime
from tkinter import ttk
from tkinter import *
import csv
import os
import requests

def login():
    delete_main_screen()
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
                menufichier.add_command(label="Retour", accelerator="CTRL+R", command=leave)
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
                    confirm.geometry("500x100")
                        
                    boite = Frame(confirm)

                    Label(boite, text="Voulez vous vraiment envoyer les données de vol ?").pack()
                    Button(boite, text="Envoyer", command=envoyer).pack()
                    Button(boite, text="Annuler", command=annuler).pack()

                    boite.pack(expand=YES)
                    confirm.mainloop()

                def envoyer():
                    a = entry_a.get()
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
                menufichier.add_command(label="Retour", accelerator="CTRL+R", command=leave)
                menufichier.bind_all("<Control-r>", lambda x: leave())
                        
                da = Label(framenew, text="Date").grid(row=1, column=0)
                entry_a = Entry(framenew)
                entry_a.grid(row=1, column=1)

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
                entry_c = Entry(framenew)
                entry_c.grid(row=3, column=1)

                dr = Label(framenew, text="Temps de vol").grid(row=4, column=0)
                entry_d = Entry(framenew)
                entry_d.grid(row=4, column=1)

                ba = Label(framenew, text="Numéro de la batterie").grid(row=5, column=0)
                entry_e = Entry(framenew)
                entry_e.grid(row=5, column=1)

                pb = Label(framenew, text="% de batterie restant").grid(row=6, column=0)
                entry_f = Entry(framenew)
                entry_f.grid(row=6, column=1)

                pb = Label(framenew, text="Nombre de cycle").grid(row=7, column=0)
                entry_g = Entry(framenew)
                entry_g.grid(row=7, column=1)

                send = Button(framenew, text="Envoyer", command=confirm)
                send.grid(row=8, column=0, columnspan=2, pady=20)

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
                menufichier.add_command(label="Retour", accelerator="CRTL+R", command=leave)
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
            menufichier.add_command(label="Statistiques", accelerator="CTRL+S", command=load_stats)
            menufichier.add_command(label="Nouveau", accelerator="CTRL+T", command=load_new)
            menufichier.add_separator()
            menufichier.add_command(label="Quitter", accelerator="CTRL+E", command=leave)
            menubar.add_cascade(label="Navigation", menu=menufichier)

            menubar.bind_all("<Control-s>", lambda x: load_stats())
            menubar.bind_all("<Control-t>", lambda x: load_new())
            menubar.bind_all("<Control-e>", lambda x: leave())

            perm = data['perm']

            if perm == "admin":
                menuadm = Menu(menubar,tearoff=0)
                menuadm.add_command(label="Tout les utilisateurs", accelerator="CTRL+A", command=list_users)
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

def delete_main_screen():
    main_screen.destroy()
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("250x150")
    main_screen.resizable(False, False)
    main_screen.overrideredirect(True)
    Label(text="\n\n\n\n\n\n\n\n\n\n\n\n\n")
    Label(text="Bienvenue sur l'application", fg="blue", width="300", font=("Calibri", 13)).pack()
    Label(text="Veuillez choisir votre direction", fg="blue", width="300", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Se connecter", height="2", width="30", command=login).pack()
    Label(text="").pack()
 
    main_screen.mainloop()
 
main_account_screen()