import tkinter.messagebox
import tkinter as tk
import random

n= int(random.randint(10000,100000))

root= tk.Tk()
root.geometry("230x100")
root.title("Číslo")

ncislo_label = tk.Label(root, text=n, font=('calibre',55, 'bold'))    
ncislo_label.grid(row=0,column=1)
root.after(1500,lambda:root.destroy())

a= int(input("Aké bolo moje číslo? "))

if a == n:
    super = "SUPER"
    tk.messagebox.showinfo("Správa", super)

elif a != n:
    zle ="Nesprávne číslo, tvoje číslo je " + str(n)
    tk.messagebox.showinfo("Správa", zle)

else:
    print("Chyba")


root.mainloop()