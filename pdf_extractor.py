import pdfplumber

# Specify the path to your PDF file
pdf_file_path = '/Users/adiyen/myFiles/Learning/notes/educative/Educative-PromptEngineering.pdf'
# Specify the page number you want to extract text from (1-based index)
page_number = 2

# Open the PDF file
with pdfplumber.open(pdf_file_path) as pdf:
    # Check if the specified page number is valid
    if page_number <= len(pdf.pages):
        # Get the specific page
        page = pdf.pages[page_number - 1]  # Adjust for 0-based index
        # Extract text
        text = page.extract_text()

        # Print the extracted text
        print(text)
    else:
        print(f"Page {page_number} does not exist in this PDF.")

