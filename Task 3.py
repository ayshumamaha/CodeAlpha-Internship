import re

input_file = "Sample.txt"

output_file = "emails.txt"

try:

    file = open(input_file, "r")

    content = file.read()

    file.close()

    emails = re.findall(r'\S+@\S+', content)

    output = open(output_file, "w")

    for email in emails:
        output.write(email + "\n")

    output.close()

    print("Email addresses extracted successfully.")

except FileNotFoundError:
    print("Input file not found.")
    
    
