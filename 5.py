import tkinter as tk

def change_text():
    if button["text"] == "�������� ����":
        button["text"] = "����� ������!"
    else:
        button["text"] = "�������� ����"

def show_entries():

    print("������� �������:", entry_lastname.get())
    print("�������� ���� ����������:", entry_result.get())

def copy_lastname():
    lastname = entry_lastname.get()
    entry_result.delete(0, tk.END)  # �������� ���� ������
    entry_result.insert(0, lastname)

def on_closing():
    print("good bye")
    root.destroy()

def selected_gender():
    print("������ �����:", gender.get())

root = tk.Tk()
root.title("���������� � �������, ������ �������� �� Radiobutton")

root.iconbitmap('image-x-ico_36116.ico')  

label_lastname = tk.Label(root, text="�������:")
label_lastname.pack(pady=5)

entry_lastname = tk.Entry(root)
entry_lastname.pack(pady=5)

label_result = tk.Label(root, text="������� �������:")
label_result.pack(pady=5)

entry_result = tk.Entry(root)
entry_result.pack(pady=5)

button_copy = tk.Button(root, text="���������", command=copy_lastname)
button_copy.pack(pady=5)

button = tk.Button(root, text="�������� ����", command=change_text)
button.pack(pady=5)

show_entries_button = tk.Button(root, text="�������� ��������", command=show_entries)
show_entries_button.pack(pady=5)


root.resizable(False, False)


root.protocol("WM_DELETE_WINDOW", on_closing)


gender = tk.StringVar()  # ����� ��� ���������� �������� ��������
male_radio = tk.Radiobutton(root, text="������", variable=gender, value="male", command=selected_gender)
male_radio.pack(pady=5)
female_radio = tk.Radiobutton(root, text="Ƴ���", variable=gender, value="female", command=selected_gender)
female_radio.pack(pady=5)

root.mainloop()

˳����� ����:  2 
import tkinter as tk
from tkinter import messagebox

def show_selected():
    selected_fruit_index = listbox.curselection()
    if selected_fruit_index:
        selected_fruit = fruits[selected_fruit_index[0]]
        messagebox.showinfo("����", f"�������� �����: {selected_fruit}")
    else:
        messagebox.showwarning("������������", "���� �����, ������� �����!")


root = tk.Tk()
root.title("���� ������")


fruits = ["������", "�����", "��������", "�����"]
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
for fruit in fruits:
    listbox.insert(tk.END, fruit)
listbox.pack(pady=10)


tk.Button(root, text="�������� ����", command=show_selected).pack(pady=10)

root.mainloop()

