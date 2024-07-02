import os
import argparse
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_dir, output_file):
    # Store PDF files here 
    pdfFiles = []

    for root, dirs, filenames in os.walk(input_dir):
        for filename in filenames:
            # for every file that ends with '.pdf' add their full path to the pdfFiles array
            if filename.lower().endswith('.pdf'):
                pdfFiles.append(os.path.join(root, filename))

    # Sort files alphabetically
    pdfFiles.sort(key=str.lower)

    # Assign PdfWriter to variable
    pw = PdfWriter()

    print("Oh yeah, It's a fuuusiiooooonnn!!!!!")

    for filename in pdfFiles:
        print(f"Processing file: {filename}")
        with open(filename, 'rb') as pdfFileObj:
            pdfReader = PdfReader(pdfFileObj)
            for pageNum in range(len(pdfReader.pages)):
                print(f"Adding page {pageNum + 1} of {filename}")
                pageObj = pdfReader.pages[pageNum]
                pw.add_page(pageObj)

    # Write the merged PDF to an output file
    with open(output_file, 'wb') as pdfOutput:
        pw.write(pdfOutput)

    print(f"PDFs have been successfully merged into {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge All PDF files from inside the selected directory into one PDF file.")
    parser.add_argument("input_dir", help="The directory containing the PDF files to merge.")
    parser.add_argument("output_file", help="The output PDF file name.")
    
    args = parser.parse_args()
    
    merge_pdfs(args.input_dir, args.output_file)

