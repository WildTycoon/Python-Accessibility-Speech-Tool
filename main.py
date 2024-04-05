import tkinter as tk
from tkinter import filedialog
import pyttsx3
from PyPDF2 import PdfReader

class PDFToAudioConverter:
    def __init__(self, master):
        self.master = master
        master.title("PDF Reader & Audio Converter")
        master.geometry("600x400")

        self.intro_label = tk.Label(master, text="Welcome to PDF Reader & Audio Converter", font=("Helvetica", 16), pady=20)
        self.intro_label.pack()

        self.label = tk.Label(master, text="Select PDF file:", font=("Helvetica", 12))
        self.label.pack()

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_pdf, font=("Helvetica", 12))
        self.browse_button.pack()

        self.status_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.status_label.pack()

        self.pdf_path = ""
        self.speaker = None

    def browse_pdf(self):
        self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.pdf_path:
            self.status_label.config(text=f"Selected PDF: {self.pdf_path}")
            self.read_pdf()

    def read_pdf(self):
        self.speaker = pyttsx3.init()
        self.speaker.setProperty('rate', 150)  # You can adjust the speaking rate (words per minute)

        with open(self.pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page in pdf_reader.pages:
                text = page.extract_text()
                self.speaker.say(text)

        self.speaker.runAndWait()
        self.status_label.config(text="Reading completed.")

def main():
    root = tk.Tk()
    app = PDFToAudioConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
