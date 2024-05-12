import customtkinter
import tkinterDnD
import numpy as np

customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x600")
app.title("Resolver Integración Númerica")

print(type(app), isinstance(app, tkinterDnD.Tk))

def f(x):       # Función a usar
    return 0.5 * np.sin(2*x) + (1/3) * np.cos(3*x) + x**2 + 1

# Regla del trapecio
def trapecio(a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i*h)
    result *= h
    return result

# Simpson 1/3
def simpson_13(a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4 * f(a + i*h)
    for i in range(2, n-1, 2):
        result += 2 * f(a + i*h)
    result *= h / 3
    return result

# Simpson 3/8
def simpson_38(a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            result += 2 * f(a + i*h)
        else:
            result += 3 * f(a + i*h)
    result *= 3*h / 8
    return result


def button_callback():
    a = float(entry_1.get())
    b = float(entry_2.get())
    n = int(entry_3.get())

    integral_trapecio = trapecio(a, b, n)
    integral_simpson13 = simpson_13(a, b, n)
    integral_simpson38 = simpson_38(a, b, n)

    textbox_trapecio.insert("1.0",str(integral_trapecio))
    textbox_simpson13.insert("1.0",str(integral_simpson13))
    textbox_simpson38.insert("1.0", str(integral_simpson38))

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=40, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(text="Función usada: (1/2)sin(2x) + (1/3)cos(3x) + x^2 + 1", master=frame_1, justify=customtkinter.LEFT)
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Límite inferior")
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Límite superior")
entry_2.pack(pady=10, padx=10)

entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Subintervalos")
entry_3.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(text="Calcular", master=frame_1, command=button_callback)
button_1.pack(pady=10, padx=10)

label_2 = customtkinter.CTkLabel(text="Regla Trapecio Simple", master=frame_1, justify=customtkinter.RIGHT)
label_2.pack(pady=10, padx=10)
textbox_trapecio = customtkinter.CTkTextbox(master=frame_1, height=1)
textbox_trapecio.pack(padx=10)

label_3 = customtkinter.CTkLabel(text="Regla Simpson 1/3 Simple", master=frame_1, justify=customtkinter.RIGHT)
label_3.pack(pady=10, padx=10)
textbox_simpson13 = customtkinter.CTkTextbox(master=frame_1, height=1)
textbox_simpson13.pack(padx=10)

label_3 = customtkinter.CTkLabel(text="Regla Simpson 3/8 Simple", master=frame_1, justify=customtkinter.RIGHT)
label_3.pack(pady=10, padx=10)
textbox_simpson38 = customtkinter.CTkTextbox(master=frame_1, height=1)
textbox_simpson38.pack(padx=10)

app.mainloop()
