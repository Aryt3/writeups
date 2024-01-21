# Secret Message 1

## Description
```
We swiped a top-secret file from the vaults of a very secret organization, but all the juicy details are craftily concealed. 
Can you help me uncover them?

Author: SteakEnthusiast
```

## Provided Files
`secret.pdf`

## Writeup

Looking at the `.pdf` I saw a blacked out flag. <br/>
![image](https://github.com/Aryt3/writeups/assets/110562298/603e743c-553d-4432-aed1-632753bee749)

To get the flag I used a python script with the library `PyPDF2` to extract the messages. <br/>
```py
import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            
            text = page.extractText()
            print(f"Page {page_num + 1}:\n{text}\n")

extract_text_from_pdf('secret.pdf')
```

Executing the script I obtained the flag which concludes this writeup. <br/>
```sh
kali@kali python3 solve.py

Page 1:
Confidential Document
TRANSCRIPT: A Very Private Conversation
Person 1: "So, have you reviewed the latest security measures?"
Person 2: "I have. The team's done a thorough job this time."
Person 1: "Especially after the last breach, we couldn't take any chances."
Person 2: "Absolutely. The new encryption protocols should prevent similar incidents."
Person 1: "What about the insider threat? Any measures against that?"
Person 2: "Yes, they've implemented strict access controls and regular audits."
Person 1: "Good to hear. By the way, how's the CTF challenge coming along?"
Person 2: "Oh, it's going great. We've got some tricky puzzles this time."
Person 1: "Just make sure the flag is well-protected. We don't want a repeat of last time."
Person 2: "Definitely not. The flag 'uoftctf{fired_for_leaking_secrets_in_a_pdf}' is securely
embedded."
Person 1: "Great. But remember, that's between us."
Person 2: "Of course. Confidentiality is key in these matters."
Person 1: "Alright, I trust your discretion. Let's keep it under wraps."
Person 2: "Agreed. We'll debrief the team about general security, but specifics stay with us."
Person 1: "Sounds like a plan. Let's meet next week for another update."
Person 2: "Will do. Take care until then."
```


