from tika import parser
import re
import os

emails = []

directory = r'C:/Users/Sotiris/Downloads/'


for dirpath, dirnames, filenames in os.walk(directory):
    for filename in [f for f in filenames if f.endswith(".pdf")]:
        filepath = os.path.join(directory, dirpath, filename)
        print("dfgdfg")
        raw = parser.from_file(filepath)
        content = str(raw['content'].strip().encode('utf-8', errors='ignore'))
        match = re.findall(r'[\w\.-]+@[\w\.-]+|{[\w\., -]+}@[\w\.-]+', content) #[\w\.-]+@[\w\.-]+
        emails.extend(match)

#emails = ['asdfas@adpsfo.ger','asdf@ga.hot','{afdas,asdfas,df}@agg.egg','{malakas, orestis}@mamama.fs']
print(emails)

emails_corrected = []
false_emails = []
for email in emails:
    if '{' in email and '}' in email:
        names = email.split('}')[0].replace('{', '').split(',')
        at = email.split('}')[1]
        for name in names:
            emails_corrected.append(name.strip()+at)
        false_emails.append(email)

for false in false_emails:
    emails.remove(false)

emails.extend(emails_corrected)
        
            
print(emails)

with open("emails.txt", "a") as myfile:
    for email in emails:
        myfile.write('\n'+email)
