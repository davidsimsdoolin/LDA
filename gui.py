#gui.py

import tkinter as tk
from time import sleep
import modelCreation as mc
import topicAllocation as ta
import topicGraph as tg
import os
import traceback


def loading(app, document, task):
    dropDown.pack_forget()
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    var.set(task + " running on " + document + " . \n This may take some time. \n ...")
    app.after(2000)
    app.update()


def AllocateTopics(app,document):
    loading(app, document,"Topic Allocation")
    try:
        ta.topic_allocation(document)
    except Exception as err:
        print("An Exception Occurred")
        traceback.print_tb(err.__traceback__)
        print(err)

    var.set("Enter file name which lda will be done on:")
    dropDown.pack()
    button1.pack()
    button2.pack()
    button3.pack()


def GraphTopics(app, document):
    loading(app, document, "Topic Graphing")
    try:
        tg.topic_graph(document)
    except Exception as err:
        print("An Exception Occurred")
        traceback.print_tb(err.__traceback__)
        print(err)

    var.set("Enter file name which lda will be done on:")
    dropDown.pack()
    button1.pack()
    button2.pack()
    button3.pack()


def CreateModel(app,document):
    loading(app, document,"Model Creation")
    try:
        mc.model_creation(document)
    except Exception as err:
        print("An Exception Occurred")
        traceback.print_tb(err.__traceback__)
        print(err)

    var.set("Enter file name which lda will be done on:")
    dropDown.pack()
    button1.pack()
    button2.pack()
    button3.pack()


app = tk.Tk()
app.title("LDA")
app.geometry("300x170")
app.resizable(0,0)
app.pack_propagate(0)

var = tk.StringVar()
label = tk.Label(app, bd = 5, textvariable = var, justify=tk.CENTER)
var.set("Enter file name which lda will be done on:")
label.pack()

files = [f for f in os.listdir(os.getcwd() + "\\Src Files") if os.path.isfile(os.path.join(os.getcwd() + "\\Src Files", f))]
selection = tk.StringVar(app)
selection.set(files[0])
dropDown = tk.OptionMenu(app, selection, *files)
dropDown.pack()

CreateModelCommand = lambda: CreateModel(app,selection.get()[0:-4])
button1 = tk.Button(app, bd = 5, justify=tk.CENTER, text= "Create Model", command = CreateModelCommand)
button1.pack()
AllocateTopicCommand = lambda: AllocateTopics(app,selection.get()[0:-4])
button2 = tk.Button(app, bd = 5, justify=tk.CENTER, text= "Allocate Topics", command = AllocateTopicCommand)
button2.pack()

GraphCommand = lambda: GraphTopics(app,selection.get()[0:-4])
button3 = tk.Button(app, bd = 5, justify=tk.CENTER, text= "Graph Topics", command = GraphCommand)
button3.pack()

app.mainloop()
