


import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import time

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CONVERTER TOOL")
        self.root.geometry("360x640")
        self.root.resizable(False, False)
        
        # কালার স্কিম - Modern UI
        self.colors = {
            "primary": "#3498db",
            "secondary": "#2ecc71",
            "accent": "#e74c3c",
            "background": "#ecf0f1",
            "text_dark": "#2c3e50",
            "card": "#ffffff"
        }
        
        # ফন্ট সেটআপ
        self.title_font = tkFont.Font(family="Arial", size=24, weight="bold")
        self.button_font = tkFont.Font(family="Arial", size=16, weight="bold")
        self.text_font = tkFont.Font(family="Arial", size=12)
        
        self.current_frame = None
        self.show_splash_screen()

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root, bg=self.colors["background"])
        self.current_frame.pack(fill="both", expand=True)

    def show_splash_screen(self):
        self.clear_frame()
        splash = self.current_frame
        splash.configure(bg=self.colors["primary"])
        
        # App Logo/Title
        title = tk.Label(splash, text="CONVERTER TOOL", font=self.title_font, 
                        fg="white", bg=self.colors["primary"])
        title.place(relx=0.5, rely=0.4, anchor="center")
        
        # Loading Animation
        loading = tk.Label(splash, text="Loading...", font=self.text_font, 
                          fg="white", bg=self.colors["primary"])
        loading.place(relx=0.5, rely=0.6, anchor="center")
        
        # Animate dots
        self.dots = 0
        def animate():
            text = "Loading" + "." * (self.dots % 4)
            loading.config(text=text)
            self.dots += 1
            if splash.winfo_exists():
                splash.after(500, animate)
        
        animate()
        self.root.after(5000, self.show_home_page)

    def show_home_page(self):
        self.clear_frame()
        home = self.current_frame
        
        # App Title
        title = tk.Label(home, text="CONVERTER TOOL", font=self.title_font,
                        fg=self.colors["text_dark"], bg=self.colors["background"])
        title.pack(pady=20)
        
        # Input Section
        input_frame = tk.Frame(home, bg=self.colors["card"], padx=10, pady=10,
                              relief="groove", bd=0, highlightthickness=0)
        input_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(input_frame, text="Enter Text/Number:", font=self.text_font,
                fg=self.colors["text_dark"], bg=self.colors["card"]).pack(anchor="w")
        
        self.input_entry = tk.Entry(input_frame, font=self.text_font, bd=2,
                                   relief="groove", highlightthickness=0)
        self.input_entry.pack(fill="x", pady=5)
        
        # Conversion Buttons
        button_frame = tk.Frame(home, bg=self.colors["background"])
        button_frame.pack(pady=20)
        
        buttons = [
            {"text": "BIN", "name": "Binary", "command": self.convert_to_binary},
            {"text": "OCT", "name": "Octal", "command": self.convert_to_octal},
            {"text": "DEC", "name": "Decimal", "command": self.convert_to_decimal},
            {"text": "HEX", "name": "Hexadecimal", "command": self.convert_to_hex}
        ]
        
        for i, btn in enumerate(buttons):
            frame = tk.Frame(button_frame, bg=self.colors["background"])
            frame.grid(row=i//2, column=i%2, padx=15, pady=10)
            
            btn_widget = tk.Label(frame, text=btn["text"], font=("Arial", 24, "bold"),
                                 width=4, height=2, bg=self.colors["primary"], fg="white")
            btn_widget.pack()
            btn_widget.bind("<Button-1>", lambda e, cmd=btn["command"]: cmd())
            
            # Hover effects
            btn_widget.bind("<Enter>", lambda e, w=btn_widget: 
                           w.config(bg="#2980b9"))
            btn_widget.bind("<Leave>", lambda e, w=btn_widget: 
                           w.config(bg=self.colors["primary"]))
            
            tk.Label(frame, text=btn["name"], font=self.text_font,
                    fg=self.colors["text_dark"], bg=self.colors["background"]).pack(pady=5)
        
        # Instructions
        help_frame = tk.Frame(home, bg=self.colors["card"], padx=15, pady=15)
        help_frame.pack(pady=20, padx=20, fill="x")
        
        tk.Label(help_frame, text="How to Use:", font=self.text_font,
                fg=self.colors["text_dark"], bg=self.colors["card"], anchor="w").pack(fill="x")
        
        instructions = [
            "1. Enter English text/numbers in input box",
            "2. Select conversion type (BIN/OCT/DEC/HEX)",
            "3. See converted result on next screen",
            "4. Press 'Back Home' to return"
        ]
        
        for step in instructions:
            tk.Label(help_frame, text=step, font=self.text_font,
                    fg=self.colors["text_dark"], bg=self.colors["card"], anchor="w").pack(fill="x", pady=2)
        
        # Exit Button
        exit_btn = tk.Button(home, text="Exit", font=self.text_font, command=self.root.destroy,
                            bg=self.colors["accent"], fg="white", bd=0, padx=20, pady=5)
        exit_btn.pack(pady=10)

    def convert_to_binary(self):
        self.perform_conversion("binary")
    
    def convert_to_octal(self):
        self.perform_conversion("octal")
    
    def convert_to_decimal(self):
        self.perform_conversion("decimal")
    
    def convert_to_hex(self):
        self.perform_conversion("hexadecimal")

    def perform_conversion(self, conv_type):
        text = self.input_entry.get()
        if not text:
            messagebox.showerror("Input Error", "Please enter text or numbers!")
            return
            
        result = []
        for char in text:
            ascii_val = ord(char)
            if conv_type == "binary":
                result.append(bin(ascii_val)[2:])
            elif conv_type == "octal":
                result.append(oct(ascii_val)[2:])
            elif conv_type == "decimal":
                result.append(str(ascii_val))
            elif conv_type == "hexadecimal":
                result.append(hex(ascii_val)[2:].upper())
        
        self.show_result_page(text, conv_type.capitalize(), " ".join(result))

    def show_result_page(self, original, conv_type, result):
        self.clear_frame()
        result_frame = self.current_frame
        
        # Result Header
        tk.Label(result_frame, text="CONVERSION RESULT", font=self.title_font,
                fg=self.colors["text_dark"], bg=self.colors["background"]).pack(pady=20)
        
        # Original Input
        input_card = tk.Frame(result_frame, bg=self.colors["card"], padx=15, pady=10)
        input_card.pack(pady=10, padx=20, fill="x")
        
        tk.Label(input_card, text="Original Input:", font=self.text_font,
                fg=self.colors["text_dark"], bg=self.colors["card"], anchor="w").pack(fill="x")
        
        tk.Label(input_card, text=original, font=("Arial", 14),
                fg=self.colors["primary"], bg=self.colors["card"], anchor="w", wraplength=300).pack(fill="x", pady=5)
        
        # Converted Result
        result_card = tk.Frame(result_frame, bg=self.colors["card"], padx=15, pady=10)
        result_card.pack(pady=10, padx=20, fill="x")
        
        tk.Label(result_card, text=f"Converted to {conv_type}:", font=self.text_font,
                fg=self.colors["text_dark"], bg=self.colors["card"], anchor="w").pack(fill="x")
        
        tk.Label(result_card, text=result, font=("Arial", 14),
                fg=self.colors["secondary"], bg=self.colors["card"], anchor="w", wraplength=300).pack(fill="x", pady=5)
        
        # Back Button
        back_btn = tk.Button(result_frame, text="Back Home", font=self.button_font,
                            command=self.show_home_page, bg=self.colors["primary"], fg="white", 
                            padx=20, pady=10, bd=0)
        back_btn.pack(pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()