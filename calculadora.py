from tkinter import *
from tkinter import ttk

#cores 
cor1 = "#000000" #Black
cor2 = "#030166" #Navy blue
cor3 = "#F7F7FD" #Ghost white
cor4 = "#76767B" #Gray
cor5 = "#EF8008" #Tangerine

janela = Tk()
janela.title("Calculadora")
janela.geometry("240x310")
janela.config(bg=cor1)

frame_janela = Frame(janela, width=240, height= 50, bg=cor2)
frame_janela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=240, height=270)
frame_corpo.grid(row=1, column=0 )

todos_valores = ""
valor_texto = StringVar()

def entrar_valor(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    

    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))
    

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

    

app_label = Label(frame_janela, textvariable= valor_texto, width=16, height=2, padx=7, relief= FLAT, anchor="e", justify=RIGHT , fg=cor3, font=('Ivy 18'), bg=cor2 )
app_label.place(x=0, y=0)

botao1 = Button(frame_corpo, command= limpar_tela ,text="C", width=11, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao1.place(x=0, y=0)

botao2 = Button(frame_corpo, command= lambda: entrar_valor('%'), text="%", width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao2.place(x=118, y=0)

botao3 = Button(frame_corpo, command= lambda: entrar_valor('/'), text="/", width=5, height=2, bg=cor5, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao3.place(x = 179, y=0)

botao4 = Button(frame_corpo, command= lambda: entrar_valor('7'), text="7", width=5, height=2, bg=cor4, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao4.place(x=0, y=52)

botao5 = Button(frame_corpo, command= lambda: entrar_valor('8'), text="8", width=5, height=2, bg=cor4, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao5.place(x=59, y=52)

botao6 = Button(frame_corpo, command= lambda: entrar_valor('9'), text="9", width=5, height=2, bg=cor4, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao6.place(x=118, y=52)

botao7 = Button(frame_corpo, command= lambda: entrar_valor('*'), text="*", width=5, height=2, bg=cor5, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao7.place(x=179, y=52)

botao7 = Button(frame_corpo, command= lambda: entrar_valor('4'), text="4", width=5, height=2, bg=cor4, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao7.place(x=0, y=104)

botao8 = Button(frame_corpo, command= lambda: entrar_valor('5'), text="5", width=5, height=2, bg=cor4, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao8.place(x=60, y=104)

botao9 = Button(frame_corpo, command= lambda: entrar_valor('6'), text="6", width=5, height=2, bg=cor4, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao9.place(x=118, y=104)

botao10 = Button(frame_corpo, command= lambda: entrar_valor('-'), text="-", width=5, height=2, bg=cor5, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao10.place(x = 179, y=104)

botao11 = Button(frame_corpo, command= lambda: entrar_valor('1'), text="1", width=5, height=2, bg=cor4, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao11.place(x=0, y=155)

botao12 = Button(frame_corpo, command= lambda: entrar_valor('2'), text="2", width=5, height=2, bg=cor4, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao12.place(x=60, y=155)

botao13= Button(frame_corpo, command= lambda: entrar_valor('3'), text="3", width=5, height=2, bg=cor4, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao13.place(x=118, y=155)


botao14= Button(frame_corpo, command= lambda: entrar_valor('+'), text="+", width=5, height=2, bg=cor5, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao14.place(x=179, y=155)

botao15 = Button(frame_corpo, command= lambda: entrar_valor('0'), text="0", width=11, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao15.place(x=0, y=206)

botao16= Button(frame_corpo, command= lambda: entrar_valor('.'), text=".", width=5, height=2, bg=cor4, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao16.place(x=118, y=206)

botao17= Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor5, fg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
botao17.place(x=179, y=206)



janela.mainloop()
