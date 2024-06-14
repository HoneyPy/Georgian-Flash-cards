import PyPDF2

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text

# Function to parse questions and answers from text
def parse_qa_from_text(text):
    qa_list = []
    lines = text.split("\n")
    question, options, answer = "", [], ""
    for line in lines:
        if "Question" in line:
            if question:
                qa_list.append({"question": question, "options": options, "answer": answer})
            question = line
            options = []
        elif "Correct Answer" in line:
            answer = line
        elif line.strip():
            options.append(line.strip())
    if question:
        qa_list.append({"question": question, "options": options, "answer": answer})
    return qa_list

# Function to format flashcards
def format_flashcards(qa_list):
    flashcards = []
    for qa in qa_list:
        flashcard = f"Question: {qa['question']}\nOptions: {', '.join(qa['options'])}\nAnswer: {qa['answer']}\n\n"
        flashcards.append(flashcard)
    return flashcards

# Paths to the PDF files (update these paths to the correct locations on your machine)
file_paths = [
    r"C:\Users\HP\PycharmProjects\Geo\path\to\ტესტები-საქართველოს-მოქალაქეობის-მოპოვებისათვის-ქართულ-ენაში.pdf",
    r"C:\Users\HP\PycharmProjects\Geo\path\to\ტესტები-საქართველოს-მოქალაქეობის-მოპოვებისათვის-ისტორიაში.pdf",
    r"C:\Users\HP\PycharmProjects\Geo\path\to\ilide.info-pr_454ab731aa14f6346e2dd5284d517942.pdf"
]

# Extract and parse questions and answers from each file
qa_data = []
for file_path in file_paths:
    text = extract_text_from_pdf(file_path)
    qa_data.extend(parse_qa_from_text(text))

# Format flashcards
flashcards = format_flashcards(qa_data)

# Save the flashcards to a file (update the path if needed)
flashcards_file = r"C:\Users\HP\PycharmProjects\Geo\Georgian_Citizenship_Test_Flashcards.txt"
with open(flashcards_file, "w") as file:
    for card in flashcards:
        file.write(card)

print(f"Flashcards have been saved to {flashcards_file}")