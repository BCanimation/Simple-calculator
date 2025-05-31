import tkinter as tk
swastika = '''
⠀⠄⠀⣨⣮⠀⠀⠀⠀
⠀⠀⣾⣟⠁⣠⣦⡀⢀
⢰⣤⠈⣻⣿⡏⠙⢿⠆
⠀⠙⠿⠋⢈⣿⡆⠀⠀
⠀⠀⠀⠀⡿⠋⠀⠐⠀'''
def show_conev_calculator():
    btn_start_conev.pack_forget()
    start_label.pack_forget()
    instruction_label.pack_forget()
    btn_start_cylinder.pack_forget()
    label_title_for_all.pack()
    label_conev_r.pack()
    entry_conev_r.pack()
    label_conev_h.pack()
    entry_conev_h.pack()
    btn_conev_calc.pack(pady=10)
    label_conev_result.pack()

def show_cylinder_calculator():
    btn_start_cylinder.pack_forget()
    start_label.pack_forget()
    instruction_label.pack_forget()
    btn_start_conev.pack_forget()
    label_title_for_all.pack()
    label_cylinderv_r.pack()
    entry_cylinderv_r.pack()
    label_cylinderv_h.pack()
    entry_cylinderv_h.pack()
    btn_cylinderv_calc.pack(pady=10)
    label_cylinderv_result.pack()

def calculate_cone_volume():
    try:
        r = float(entry_conev_r.get())
        h = float(entry_conev_h.get())
        result = r**2 * 3.14 * h / 3
        label_conev_result.config(text=f"Volume of cone is: {result:.3f}")
    except ValueError:
        label_conev_result.config(text="Please enter valid numbers.", font=("UnifontExMono", 10))
        label_swastika = tk.Label(root, text=swastika, font=("UnifontExMono", 10))
        label_swastika.pack()
        root.geometry("300x250")
def calculate_cylinder_volume():
    try:
        r = float(entry_cylinderv_r.get())
        h = float(entry_cylinderv_h.get())
        result = r**2 * 3.14 * h
        label_cylinderv_result.config(text=f"Volume of cylinder is: {result:.2f}")
    except ValueError:
        label_cylinderv_result.config(text="Please enter valid numbers.", font=("UnifontExMono", 10))
        label_swastika = tk.Label(root, text=swastika, font=("UnifontExMono", 10))
        label_swastika.pack()
        root.geometry("300x250")
root = tk.Tk()
root.title("Cone Volume Calculator")
root.geometry("300x200")

start_label = tk.Label(root, text="Welcome to the Stuff Calculator", font=("UnifontExMono", 13))
instruction_label = tk.Label(root, text="Please choose what you want to calculate", font=("UnifontExMono", 10))
btn_start_conev = tk.Button(root, text="Cone Volume Calculate", command=show_conev_calculator, font=("UnifontExMono", 10))
btn_start_cylinder = tk.Button(root, text="Cylinder Volume Calculate", command=show_cylinder_calculator, font=("UnifontExMono", 10))
start_label.pack()
instruction_label.pack()
btn_start_conev.pack(pady=10)
btn_start_cylinder.pack(pady=10)

label_title_for_all = tk.Label(root, text="Please enter the values", font=("UnifontExMono", 12))
label_conev_r = tk.Label(root, text="Cone Radius (r):", font=("UnifontExMono", 10))
entry_conev_r = tk.Entry(root)
label_conev_h = tk.Label(root, text="Cone Height (h):", font=("UnifontExMono", 10))
entry_conev_h = tk.Entry(root)
btn_conev_calc = tk.Button(root, text="Calculate Cone Volume", command=calculate_cone_volume, font=("UnifontExMono", 10))
label_conev_result = tk.Label(root, text="")
label_cylinderv_r = tk.Label(root, text="Cylinder Radius (r):", font=("UnifontExMono", 10))
entry_cylinderv_r = tk.Entry(root)
label_cylinderv_h = tk.Label(root, text="Cylinder Height (h):", font=("UnifontExMono", 10))
entry_cylinderv_h = tk.Entry(root)
btn_cylinderv_calc = tk.Button(root, text="Calculate Cylinder Volume", command=calculate_cylinder_volume, font=("UnifontExMono", 10))
label_cylinderv_result = tk.Label(root, text="", font=("UnifontExMono", 10))
root.mainloop()