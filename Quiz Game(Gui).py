# Quiz Game using CustomTkinter
from customtkinter import *
from tkinter import messagebox as m
def title(a):
	l = CTkLabel(a, text="Quiz Game", font=("Arial", 105, "bold"), fg_color="blue", text_color="white", corner_radius=20)
	l.pack(pady=45, side="top")

def clk(x):
	global qn, o, s, q, o1, o2, o3, o4,a
	if not a.winfo_exists():
		return
	if d[qn].get("answer") == o[x]:
		s += 1
	else:
		pass
	if qn < l - 1:
		qn += 1
		q.configure(text=d[qn].get("question"))
		o = list(d[qn].get("options"))
		o1.configure(text=o[0])
		o2.configure(text=o[1])
		o3.configure(text=o[2])
		o4.configure(text=o[3])
	else:
		if s == l:
			m.showinfo(title="Result", message=f'You have scored:-\n\n          {s}/{l}')
			if a.winfo_exists():
				a.destroy()
		else:
			if m.askretrycancel(title="Result", message=f'You have scored:-\n\n          {s}/{l}', icon="info"):
				if a.winfo_exists():
					a.destroy()
					game()
			else:
				if a.winfo_exists():
					a.destroy()

def a_():
	if m.askyesno(title="Exit", message="Are you sure you want to exit?"):
		# If user confirms exit, destroy the main window
		a.destroy()

def ch_th(choice):
	if choice == "light":
		set_appearance_mode("light")
	elif choice == "dark":
		set_appearance_mode("dark")
	thm.set("Theme")

def game():
	global qn, o, s, q, o1, o2, o3, o4, a, thm
	qn = 0
	s = 0
	a = CTk()
	set_appearance_mode("dark")
	set_default_color_theme("blue")

	a.geometry("600x500")
	a.title("Quiz Game")
	a.resizable(False, False)

	title(a)
	# theme button
	thm = CTkOptionMenu(a, values=["light", "dark"], height=40, width=120, font=("Arial", 30, "bold"),dropdown_font=("Arial", 20), fg_color="blue", command=ch_th, anchor="center", corner_radius=40)
	thm.place(relx=0.02, rely=0.0, relheight=0.067, relwidth=0.3)
	thm.set("Theme")
	# exit button
	exit = CTkButton(a, text="Exit", command=a_, fg_color="red", font=('Arial', 20, "bold"), corner_radius=40)
	exit.place(relx=0.8, rely=0.01, relheight=0.067, relwidth=0.18)

	# _________________Question and Options____________________
	q = CTkLabel(a, text=d[qn].get("question"), anchor="center", font=("Arial", 25), fg_color="blue", text_color="white", corner_radius=20)
	q.pack(pady=30)

	o = list(d[qn].get("options"))
	o1 = CTkButton(a, text=o[0], width=200, command=lambda x=0: clk(x), font=("Arial", 20), fg_color="#00ff00", corner_radius=40, text_color="black")
	o1.pack(pady=5)

	o2 = CTkButton(a, text=o[1], width=200, command=lambda x=1: clk(x), font=("Arial", 20), fg_color="#00ff00", corner_radius=40, text_color="black")
	o2.pack(pady=5)

	o3 = CTkButton(a, text=o[2], width=200, command=lambda x=2: clk(x), font=("Arial", 20), fg_color="#00ff00", corner_radius=40, text_color="black")
	o3.pack(pady=5)

	o4 = CTkButton(a, text=o[3], width=200, command=lambda x=3: clk(x), font=("Arial", 20), fg_color="#00ff00", corner_radius=40, text_color="black")
	o4.pack(pady=5)

	a.mainloop()
#______________Main_Code_________________
if __name__ == "__main__":
	d=[{"question":"In which language this game is made?","options":["Python", "Java","c++","Typescript"],"answer":"Python"},
	{"question":"What is full form of NSE?","options":["National Source Executive","National Sony Electronic","National Stock Exchange","National Stock Executive"],"answer":"National Stock Exchange"},
	{"question":"What is the capital city of India?","options":["Chennai","Delhi","Mumbai","Kolkata"],"answer":"Delhi"},
	{"question":"Which planet is known as the 'Evening Star'?","options":["Venus","Mars","Saturn","Jupiter"],"answer":"Venus"},
	{"question":"In what year did World War II begin?","options":["1914","1918","1945","1939"],"answer":"1939"},
	{"question":"How many players are on a basketball team\nat one time?","options":["6","5","8","7"],"answer":"5"},
	{"question":"What is the smallest unit of matter?","options":["Molecule","Protons","Atom","Electron"],"answer":"Atom"}]
	l=len(d)
	game()