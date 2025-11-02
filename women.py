import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import random
from plyer import notification

# Simulated SOS function
def send_sos():
    notification.notify(
        title="Emergency SOS Alert",
        message="Call to emergency contact activated!",
        timeout=10
    )

    with open("sos_log.txt", "a") as file:
        file.write(f"SOS triggered at {time.ctime()}\n")

    messagebox.showinfo("SOS Activated", "Emergency call sent.\nLog saved.")

# Fake Call Generator
def fake_call():
    name = simpledialog.askstring("Fake Call", "Enter fake caller name (e.g., Mom, Boss, Police):")
    delay = simpledialog.askinteger("Delay", "Enter delay in seconds before the fake call:", minvalue=1, maxvalue=30)

    if not name or not delay:
        messagebox.showwarning("Input Error", "Please enter valid name and delay.")
        return

    messagebox.showinfo("Fake Call", f"Incoming fake call from {name} in {delay} seconds...")
    time.sleep(delay)

    call_screen = tk.Toplevel(app)
    call_screen.title("Fake Call Incoming")
    call_screen.geometry("350x250")
    call_screen.configure(bg="#1a1a1a")

    tk.Label(call_screen, text=f"{name} is calling...", font=("Helvetica", 16), fg="#00ff99", bg="#1a1a1a").pack(pady=30)
    tk.Button(call_screen, text="Answer", width=15, bg="#33cc33", fg="white", font=("Arial", 12), command=lambda: answer_call(call_screen)).pack(side="left", padx=30, pady=20)
    tk.Button(call_screen, text="Reject", width=15, bg="#ff3333", fg="white", font=("Arial", 12), command=call_screen.destroy).pack(side="right", padx=30, pady=20)

def answer_call(screen):
    messagebox.showinfo("Call Answered", "You answered the fake call. Stay safe!")
    screen.destroy()

# Secret Code Trigger
def secret_code_check():
    secret_code = "i forgot my homework"
    user_input = simpledialog.askstring("Secret Code", "Say something:")

    if user_input and user_input.lower() == secret_code:
        send_sos()
    else:
        messagebox.showinfo("Safe", "No SOS triggered.")

# Guardian Mode Simulation
def guardian_mode():
    route = [(12.91, 77.60), (12.92, 77.61), (12.93, 77.62)]
    messagebox.showinfo("Guardian Mode", "Simulation started...")

    for step in route:
        print(f"Current location: {step}")
        time.sleep(1)

        if random.choice([True, False]):
            messagebox.showwarning("Deviation Detected", f"Deviation at {step}! Triggering SOS.")
            send_sos()
            return

    messagebox.showinfo("Guardian Mode", "Route completed safely.")

# Quick Law & Rights Guide
def law_guide():
    info = (
        "Workplace Harassment:\n"
        "Illegal to harass at workplace. Helpline: 181\n\n"
        "Police Rights:\n"
        "Right to dignity when stopped by police.\n\n"
        "Women's Helpline:\n"
        "National Helpline: 1091 or 181"
    )
    messagebox.showinfo("Law & Rights Guide", info)

# ------------------------
# Build Polished GUI
# ------------------------
app = tk.Tk()
app.title("Women Safety App Simulation")
app.geometry("450x600")
app.configure(bg="#222831")

header = tk.Label(app, text="Women Safety App", font=("Helvetica", 24, "bold"), fg="#00adb5", bg="#222831")
header.pack(pady=30)

btn_style = {
    "font": ("Arial", 14),
    "width": 30,
    "bd": 0,
    "relief": "ridge",
    "pady": 10
}

tk.Button(app, text="Trigger SOS", bg="#ff4d4d", fg="white", command=send_sos, **btn_style).pack(pady=10)
tk.Button(app, text="Fake Call Generator", bg="#4da6ff", fg="white", command=fake_call, **btn_style).pack(pady=10)
tk.Button(app, text="Secret Code Test", bg="#00b894", fg="white", command=secret_code_check, **btn_style).pack(pady=10)
tk.Button(app, text="Guardian Mode Simulation", bg="#fdcb6e", fg="#222831", command=guardian_mode, **btn_style).pack(pady=10)
tk.Button(app, text="Law & Rights Guide", bg="#6c5ce7", fg="white", command=law_guide, **btn_style).pack(pady=10)
tk.Button(app, text="Exit App", bg="#a6a6a6", fg="white", command=app.quit, **btn_style).pack(pady=30)

app.mainloop()
