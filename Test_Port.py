import tkinter as tk

def retrieve_input():
    inputValue=textbox.get("1.0","end-1c")
    print(inputValue)
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
root.title("JARVIS")
root.geometry("235x100")
root.config(background='blue')
textbox = tk.Text(root, height=5, width=29)
textbox.pack()
recordBootton = tk.Button(frame, height=1, width=10, text="Commit", command=lambda: retrieve_input())
recordBootton.pack(side=tk.LEFT)
callButton = tk.Button(frame,height=1, width=10, text="Commit", command=lambda: retrieve_input())
callButton.pack(side=tk.RIGHT)
exitButton = tk.Button(frame,height=1, width=10, text="Commit")
exitButton.pack(side=tk.RIGHT)
root.mainloop()

