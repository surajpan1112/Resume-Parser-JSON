import fitz  
import json

def extract_resume_text(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

def parse_resume_text(text):
  
    resume_json = {
        "Contact Information": {
            "Name": "John Doe",
            "Email": "john.doe@example.com",
            "Phone": "123-456-7890",
            "LinkedIn": "https://www.linkedin.com/in/johndoe",
            "GitHub": "https://github.com/johndoe"
        },
        "Summary": "Experienced software developer with a strong background in Python and web development.",
        "Skills": [
            "Python",
            "JavaScript",
            "HTML/CSS"
        ],
        "Experience": [
            {
                "Job Title": "Software Developer",
                "Company": "Tech Solutions Inc.",
                "Location": "New York, NY",
                "Dates": "Jan 2020 - Present",
                "Responsibilities": [
                    "Developed web applications using Django.",
                    "Collaborated with the front-end team on UI/UX improvements."
                ]
            }
        ],
        "Education": [
            {
                "Degree": "Bachelor of Science in Computer Science",
                "Institution": "University of Tech",
                "Location": "Los Angeles, CA",
                "Dates": "Sep 2015 - Jun 2019"
            }
        ]
    }
    return resume_json

def main():
    pdf_path = 'resume.pdf'
    resume_text = extract_resume_text(pdf_path)
    resume_json = parse_resume_text(resume_text)
    with open('resume.json', 'w') as json_file:
        json.dump(resume_json, json_file, indent=4)

if __name__ == "__main__":
    main()
