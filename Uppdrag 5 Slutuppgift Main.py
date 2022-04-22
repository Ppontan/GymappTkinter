from tkinter import *


window = Tk()  #definera window
window.title("Gym")   #meny namnet ( längst upp till vänster)
window.geometry("1280x720") #storleket på rutan när den startas
window.config(bg = "#343436") #bakgrundsfärgen på fönstret, siffrorna är en färgkod som jag fick fram genom discord, man kan ha bakgrundfärg på sin profil där och där används färgkoder
#så det fanns en meny där man kan dra en prick runtom på ett färgfält så får man en färgkod till den färgen.

my_menu = Menu(window)  #meny med flera alternativ med flera funktioner
window.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="Alternativ", menu=file_menu)
file_menu.add_command(label="Avsluta", command=window.quit) #avsluta


def update():
    my_label.config(text="Hoppas att du har en bra dag")
my_label = Label(window, text="Kör hårt", font="rubik 15", bg="#343436", fg="white")
my_label.pack(pady=20)
my_label.after(5000, update) #uppdateringsfrekvens


#här defineras alla "click" till alla buttons (alternativen)
#Detta är newwindow, så varje gång man klickar på alternativ kommer en ny ruta för respektive alternativ,
def click1(): # def click1 är definera knappen (alternativet) i startmenyn medans def click01 är knappen ( alternativ ) i nya rutan som man kommer till efter startmenyn
    newWindow = Toplevel(window, bg="#343436") #ny ruta, bakgrundsfärg
    newWindow.title("Gymkort") #namnet på rutan (längst upp till vänster)
    newWindow.geometry("800x600") #storleken på rutan när den öppnas
    Label(newWindow, text="Gymkort 2022", bg="#343436", fg="white", font="rubik 25").pack() #text högst upp, bakgrundsfärg, font färg, font och storlek på texten.
    Label(newWindow, text="Alternativ", bg="#343436", fg="white", font="rubik 20").pack()
    Label(newWindow, text="1 månad 199kr", bg="#343436", fg="white", font="rubik 15").pack()
    button7 = Button(newWindow, text="Köp", width=15, bg="#807e7e", fg="white", font="rubik 10", command=click01)
    button7.pack()
def click01(): #command för button7 i click1, en ny ruta öppnas med tack för köp och information
    newWindow = Toplevel(window, bg="#343436")
    newWindow.title("Köp") #title för window är vad rutan heter ( längst upp till vänster )
    newWindow.geometry("600x300") #storlek på rutan när den öppnas
    Label(newWindow, text="Tack för ditt köp hos oss på Gym360", bg="#343436", fg="white", font="rubik 20").pack() #bg= bakgrundsfärg, fg är fontfärgen, font är vilken sorts font man vill ha som t.ex times new roman eller rubik och siffran är storleken
    Label(newWindow, text="Kontakt: 070 111 222 33, gym360@gmail.com", bg="#343436", fg="white", font="rubik 15").pack() #pack är packetet
    Label(newWindow, text="199 kr kommer dras inom 10 dagar", bg="#343436", fg="white", font="rubik 15").pack()

def click2():
    newWindow = Toplevel(window, bg="#343436")
    newWindow.title("Kläder")
    newWindow.geometry("800x600")
    Label(newWindow, text="Kläder i lager, 1-3 leveransdagar", bg="#343436", fg="white", font="rubik 25").pack()
    Label(newWindow, text="hoodie", bg="#343436", fg="white", font="rubik 15").pack()
    button8 = Button(newWindow, text="Köp hoodie", bg="#343436", fg="white", font="rubik 20", command=click02)
    button8.pack()
def click02():
    newWindow = Toplevel(window, bg="#343436")
    newWindow.title("klädköp")
    newWindow.geometry("500x300")
    Label(newWindow, text="Tack för ditt köp hos oss på gym 360", bg="#343436", fg="white", font="rubik 20").pack()

def click3():
    newWindow = Toplevel(window, bg="#343436")
    newWindow.title("Kontakt")
    newWindow.geometry("800x600")
    Label(newWindow, text="Kontaktuppgifter Gym360", bg="#343436", fg="white", font="rubik 25").pack()
    Label(newWindow, text="telefon: 070 111 222 53     mail: Gym360@gmail.com", bg="#343436", fg="white", font="rubik 20").pack()

def click4():
    newWindow = Toplevel(window, bg="#343436")
    newWindow.title("Regler och villkor")
    newWindow.geometry("1200x400")
    Label(newWindow, text="Regler och villkor hos oss på gym360", bg="#343436", fg="white", font="rubik 25").pack()
    Label(newWindow, text="Inga uteskor, släng skräp i papperskorgar, gör rent redskap före och efter användning", bg="#343436", fg="white", font="rubik 20").pack()
    Label(newWindow, text="Mvh Personalen på Gym360", bg="#343436", fg="white", font="rubik 20").pack()

l = Label(window, text="välkommen till gym360 :)", bg="#343436", fg="white", font="Rubik 20")
l.pack()
#alla knapparna i startmenyn med titlat, bredd, bakgrundsfärg, fontfärg och textfont och storlek med länkad till sina respektive commandon
button1 = Button(window, text="Gymkort", width=15, bg="#807e7e", fg="white", font="rubik 20",command=click1) #command=click)
button1.pack()

button2 = Button(window, text="Kläder", width=15, bg="#807e7e", fg="white", font="rubik 20", command=click2)
button2.pack()

button3 = Button(window, text="Kontakt", width=15, bg="#807e7e", fg="white", font="rubik 20", command=click3)
button3.pack()

button4 = Button(window, text="Regler och villkor", width=15, bg="#807e7e", fg="white", font="rubik 20", command=click4)
button4.pack()

def buttonfunction():#avsluta I startmeny
    exit()
button6 = Button(window, text="Avsluta", width=15, bg="#807e7e", fg="white", font="rubik 20", command=buttonfunction)
button6.pack()

window.mainloop()