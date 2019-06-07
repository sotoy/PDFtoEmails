from tika import parser
import re
import os

emails = []

directory = r'Path/to/folder/'


for dirpath, dirnames, filenames in os.walk(directory): #it searches through the subfolders as well.
    for filename in [f for f in filenames if f.endswith(".pdf")]:
        filepath = os.path.join(directory, dirpath, filename)
        print("File "+filepath+" readed!")
        raw = parser.from_file(filepath)
        content = str(raw['content'].strip().encode('utf-8', errors='ignore'))
        
        #this regular expression matches all standard emails format plus {name1, name2, ...namen}@something.egg format.
        match = re.findall(r'[\w\.-]+@[\w\.-]+\.[\w\.-]+|{[\w\., -]+}@[\w\.-]+\.[\w\.-]+', content) #[\w\.-]+@[\w\.-]+    #[\w\.-]+@[\w\.-]+|{[\w\., -]+}@[\w\.-]+
        print(match)
        emails.extend(match)
        
print(emails)

emails_corrected = []
false_emails = []
for email in emails:
    if '{' in email and '}' in email:
        names = email.split('}')[0].replace('{', '').split(',')
        at = email.split('}')[1]
        for name in names:
            emails_corrected.append(name.strip()+at)
            print(name.strip()+at)
        false_emails.append(email)

for false in false_emails:
    emails.remove(false)

emails.extend(emails_corrected)
        
            
print(emails)

with open("emails.txt", "a") as myfile:
    for email in emails:
        myfile.write('\n'+email)
