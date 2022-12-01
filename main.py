import tkinter as tk
root=tk.Tk()
root.geometry("400x200")
name_var=tk.StringVar()
date_var=tk.StringVar()

def submit():

	name=name_var.get()
	date=date_var.get()
	
	print("Hello " + name + "!")


	print("You were born in " + date)
	
	name_var.set("")
date_var.set("")
	
	

name_label = tk.Label(root, text = 'Name', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))


passw_label = tk.Label(root, text = 'Birthyear', font = ('calibre',10,'bold'))


passw_entry=tk.Entry(root, textvariable = date_var, font = ('calibre',10,'normal'))


sub_btn=tk.Button(root,text = 'Submit', command = submit)



name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)


root.mainloop()
