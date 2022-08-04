from tkinter import *
from tkinter import messagebox


def escriure():
    if len(Subtitol.get()) > 0 and len(Titol.get()) > 0 and len(imatge.get()) > 0 and len(text.get("1.0", "end")) > 0:
        titol = "C:/PycharmProjects/Notícies/Noticies/"+str(Titol.get())+".txt"
        noticia = [titol, str(Subtitol.get()), str(text.get("1.0", "end")), str(imatge.get())]
        full = open(titol, "w")
        full.write(noticia[0] + "\n" + noticia[1] + "\n" + noticia[2] + "\n" + noticia[3])
        messagebox.showinfo("Operació realitzada", "La noticia s'ha guardat correctament")
    else:
        messagebox.showerror("Error", "Suisplau, empleni tots els camps per continuar")


root = Tk()
root.title("Afegir noticies")
root.iconbitmap("Imatges/+.ico")
root.geometry("1000x600")
root.config(bg="White")
Titol = StringVar()
Subtitol = StringVar()
imatge = StringVar()
Label(root, text="", bg="white", font="ARIAL 16").grid(row=0, column=0)
Label(root, text="Títol:", bg="white", font="Arial 16 bold").grid(row=1, column=0)
Entry(root, textvariable=Titol, bg="white", font="Arial 16", width=40).grid(row=1, column=1)
Label(root, text="Subtítol:", bg="white", font="Arial 16 bold").grid(row=2, column=0, padx=20, pady=20)
Entry(root, textvariable=Subtitol, bg="white", font="Arial 14", width=44).grid(row=2, column=1)
Label(root, text="Text:", bg="white", font="Arial 16 bold").grid(row=3, column=0)
text = Text(root, height=20, width=80, bg="white", font="Arial 12")
text.place(x=130, y=130)
Label(root, text="Nombre de la imagen:", bg="white", font="Arial 16 bold").place(x=20, y=530)
Entry(root, textvariable=imatge, bg="white", font="Arial 12", width=20).place(x=260, y=535)
img = PhotoImage(file="Imatges/+.png")
Button(root, image=img, command=escriure, bg="white", relief=FLAT).place(x=940, y=540)
root.mainloop()
