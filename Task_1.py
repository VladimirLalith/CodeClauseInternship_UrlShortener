from tkinter import *
import pyshorteners


main = Tk()
main.geometry("500x500")
main.resizable(False,False)
main.title('Url Shortener')

def shorten():
    if entry2.get():
        entry2.delete(0,END)
    if entry1.get():
        url=pyshorteners.Shortener().tinyurl.short(entry1.get())
        entry2.insert(END,url)

        print(pyshorteners.Shortener().tinyurl.expand(url))

label1 = Label(main, text='Enter the Link for shortening:',font=('lucida',24))
label1.pack(pady=20)

entry1 = Entry(main, font=('lucida',24))
entry1.pack(pady=20)

button1 = Button(main, text='Shorten Url',font=('lucida',24),command= shorten)
button1.pack(pady=20)

label2 = Label(main, text='Shortened Url:',font=('lucida',30))
label2.pack(pady=50)

entry2 = Entry(main, font=('lucida',22),justify= CENTER, width=30, bd=0, bg= 'systembuttonface')
entry2.pack(pady=10)

main.mainloop()