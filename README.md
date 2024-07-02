# PDFusion

## Overview

PDFusion is a simple and powerful tool for merging multiple PDF files into a single document. This software traverses through a specified directory, collects all PDF files, and merges them into one cohesive file, making it easier to manage and share your PDF documents.

## Features

- Automatically scans and collects PDF files from a specified directory.
- Merges PDFs in alphabetical order.
- Outputs a single merged PDF document.

## Requirements

- Python 3.6 or higher
- PyPDF2

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/PDFusion.git
   cd PDFusion
   ```

2. **Install the required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Create a standalone executable (optional)**:
   If you want to create a standalone executable, you can use PyInstaller:
   ```sh
   pip install pyinstaller
   pyinstaller --onefile PDFusion.py
   ```

## Usage

### Using the Python Script

1. **Run the script**:
   ```sh
   python PDFusion.py <input_directory> <output_file>
   ```
   Replace `<input_directory>` with the path to the directory containing the PDF files you want to merge, and `<output_file>` with the desired name for the merged PDF.

   **Example**:
   ```sh
   python PDFusion.py /path/to/pdf_directory output.pdf
   ```

### Using the Standalone Executable
    Feel free to add the binary file into you `/usr/local/bin` to use it anywhere in terminal.

1. **Navigate to the directory containing the executable**:
   ```sh
   cd dist
   ```

2. **Run the executable**:
   ```sh
   ./PDFusion <input_directory> <output_file>
   ```
   Replace `<input_directory>` with the path to the directory containing the PDF files you want to merge, and `<output_file>` with the desired name for the merged PDF.

   **Example**:
   ```sh
   ./PDFusion /path/to/pdf_directory output.pdf
   ```
## TODO
   1. Scale this tool to merge more file formats
   2. Make it pretty

## Contributing

We welcome contributions! Please fork the repository and submit your pull requests.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact [paulestephan@proton.me](mailto:paulestephan@proton.me).
