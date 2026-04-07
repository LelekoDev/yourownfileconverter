import customtkinter as ctk
from tkinter import filedialog
import os
from PIL import Image
import pandas as pd
from pdf2docx import Converter

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class FileConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Universal File Converter")
        self.geometry("500x350")
        self.selected_file_path = None

        self.title_label = ctk.CTkLabel(self, text="File Converter", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=20)

        self.select_btn = ctk.CTkButton(self, text="Select File", command=self.select_file)
        self.select_btn.pack(pady=10)

        self.file_label = ctk.CTkLabel(self, text="No file selected")
        self.file_label.pack(pady=5)

        self.conversion_options = ["JPG to PNG", "PNG to JPG", "Excel to CSV", "CSV to Excel", "PDF to Word"]
        self.dropdown = ctk.CTkOptionMenu(self, values=self.conversion_options)
        self.dropdown.pack(pady=20)

        self.convert_btn = ctk.CTkButton(self, text="Convert", command=self.process_conversion, fg_color="green")
        self.convert_btn.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=5)

    def select_file(self):
        self.selected_file_path = filedialog.askopenfilename()
        if self.selected_file_path:
            self.file_label.configure(text=os.path.basename(self.selected_file_path), text_color="white")
            self.status_label.configure(text="")

    def process_conversion(self):
        if not self.selected_file_path:
            self.status_label.configure(text="Error: Select a file first!", text_color="red")
            return
        
        conversion_type = self.dropdown.get()
        input_path = self.selected_file_path
        base_name = os.path.splitext(input_path)[0]
        
        try:
            self.status_label.configure(text="Converting...", text_color="yellow")
            self.update()

            if conversion_type == "JPG to PNG":
                output_path = base_name + ".png"
                img = Image.open(input_path)
                img.save(output_path, "PNG")

            elif conversion_type == "PNG to JPG":
                output_path = base_name + ".jpg"
                img = Image.open(input_path).convert("RGB")
                img.save(output_path, "JPEG")

            elif conversion_type == "Excel to CSV":
                output_path = base_name + ".csv"
                df = pd.read_excel(input_path)
                df.to_csv(output_path, index=False)

            elif conversion_type == "CSV to Excel":
                output_path = base_name + ".xlsx"
                df = pd.read_csv(input_path)
                df.to_excel(output_path, index=False)

            elif conversion_type == "PDF to Word":
                output_path = base_name + ".docx"
                cv = Converter(input_path)
                cv.convert(output_path)
                cv.close()

            self.status_label.configure(text=f"Success! Saved as: {os.path.basename(output_path)}", text_color="green")

        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}", text_color="red")

if __name__ == "__main__":
    app = FileConverterApp()
    app.mainloop()