# Digital Inker (MVP)

This is the Minimum Viable Product (MVP) of the Digital Inker application. It allows a user to select a single PNG file containing handwritten Japanese/English text and convert it into machine-readable text using OCR.

## Prerequisites

This application requires the Tesseract OCR engine to be installed on your system.

### For Ubuntu Linux

Open a terminal and run the following commands to install Tesseract and its Japanese language pack:

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr tesseract-ocr-jpn
```

### For Windows

1.  **Download the Tesseract Installer**:
    *   Download the official Tesseract installer for Windows from the [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) page. It is recommended to download the latest stable version.

2.  **Run the Installer**:
    *   Run the downloaded `.exe` file.
    *   During installation, make sure to select the "Japanese" language data component to include support for Japanese OCR.

3.  **Add Tesseract to your PATH**:
    *   After installation, you must add the Tesseract installation folder (e.g., `C:\Program Files\Tesseract-OCR`) to your system's `PATH` environment variable. This allows the application to find the Tesseract executable.
    *   You can find instructions on how to add a directory to your PATH by searching online for "how to edit environment variables in Windows".

## Installation

Once the prerequisites are met, follow these steps to set up the application.

1.  **Clone the Repository (or download the files)**:
    *   Get the project files onto your local machine.

2.  **Create a Virtual Environment (Recommended)**:
    *   It is highly recommended to use a Python virtual environment to avoid conflicts with other projects.
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    *   Install all required Python libraries using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, execute the `main.py` script from your terminal:

```bash
python main.py
```

This will launch the GUI. From there, you can:
1.  Click "Select PNG File" to choose an image.
2.  Click "Start Conversion" to perform the OCR.
3.  The results will appear in the text area and will also be saved as a `_output.txt` file in the same directory as your image.
4.  Click "Copy to Clipboard" to copy the results.
