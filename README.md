# Universal File Converter

A lightweight, standalone desktop application designed to convert common everyday files directly on your local machine. Built with a modern Python GUI, this tool eliminates the need for online converters, ensuring data privacy and offline accessibility.

## 🚀 Features

* **Data File Processing:** Instantly convert between **Excel (.xlsx)** and **CSV** for rapid data manipulation and reporting.
* **Image Conversion:** Swap formats between **JPG** and **PNG** without quality loss.
* **Document Parsing:** Extract text from **PDF** files and convert them to editable **Word (.docx)** documents.
* **Modern GUI:** Clean, user-friendly interface powered by `CustomTkinter`.
* **Standalone Executable:** Fully packaged into a `.exe` file—no Python installation required for the end-user.

## 🛠️ Tech Stack

* **Backend:** Python 3.13
* **Frontend:** CustomTkinter
* **Data Processing:** Pandas, Openpyxl
* **Image Processing:** Pillow (PIL)
* **Document Processing:** pdf2docx
* **Packaging:** PyInstaller

## ⚙️ How to Run from Source

1. Clone this repository:
   ```bash
   git clone [https://github.com/LelekoDev/yourownfileconverter.git](https://github.com/LelekoDev/yourownfileconverter.git)
   cd yourownfileconverter
   ```

2. Create and activate a virtual environment:

   ```Bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
3. Install dependencies:

   ```Bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```Bash
   python main.py
   ```
   
📦 How to Build the Executable
To generate your own .exe file for Windows:
   ```Bash
pyinstaller --noconsole --onefile main.py
   ```
The compiled executable will be located in the dist/ folder.

📄 License
MIT License. Feel free to use and modify.
