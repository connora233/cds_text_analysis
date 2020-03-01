import os
import re
path = '/Users/connoranderson/desktop/1618filings/2018/QTR1'
# Read in files
for filename in os.listdir(path):
    # Check if 10-K file
    if "10-K" in filename and "866609" in filename:
        text = ""
        p = "/Users/connoranderson/desktop/1618filings/2018/QTR1/" + filename
        # Open file and parse lines
        with open(p, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                sline = line.strip()
                if len(sline) != 0:
                    # Remove tabs from lines
                    if "\t" in sline:
                        sline = sline.replace("\t", " ")
                    text += sline + " "
# Finding company name
front = text.find("COMPANY CONFORMED NAME:")
back = text.find("CENTRAL INDEX KEY:")
name = text[front:back]
n = name.split(" ")[3:]
company_name = ""
for w in n:
    if w != "":
        company_name = company_name + w + " "
print(company_name)

# Reading in MD&A section of text
text = text.lower()
text = text.replace("  ", " ")
text = text.replace("   ", " ")
text = text.replace("    ", " ")
first = re.search("7. management|7 management", text).start()
front = re.search("7. management|7 management", text[first+1:]).start()
first = re.search("7a. quant|7a quant", text).start()
back = re.search("7a. quant|7a quant", text[first+1:]).start()
# front = text.find(
#     "7. management", text.find(
#         "7. management") + 1)
# back = text.find("item 7a.", text.find(
#     "item 7a.") + 1)
print(front)
print(back)
if front != -1 and back != -1:
    print(text[front:back])
