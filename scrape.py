import os
import re
import pickle
p = '/Users/connoranderson/desktop/1618filings/2018/QTR1'
filings = {}


def scrape(path, year):
    test = 0
    # Read in files
    for filename in os.listdir(path):
        # Check if 10-K file
        if "10-K" in filename:
            text = ""
            p = path + "/" + filename
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
            # print(company_name)

            # Reading in MD&A section of text
            text = text.lower()
            text = text.replace("  ", " ")
            text = text.replace("   ", " ")
            text = text.replace("    ", " ")
            flag = False
            if re.search("7. management|7 management", text) != None:
                first = re.search("7. management|7 management", text).start()
            else:
                flag = True
            if re.search("7. management|7 management", text[first+1:]) != None:
                front = re.search("7. management|7 management",
                                  text[first+1:]).start()
            else:
                flag = True
            if re.search("7a. quant|7a quant", text) != None:
                sec = re.search("7a. quant|7a quant", text).start()
            else:
                flag = True
            if re.search("7a. quant|7a quant", text[sec+1:]) != None:
                back = re.search("7a. quant|7a quant", text[sec+1:]).start()
            else:
                flag = True
            # front = text.find(
            #     "7. management", text.find(
            #         "7. management") + 1)
            # back = text.find("item 7a.", text.find(
            #     "item 7a.") + 1)
            if not flag:
                if(len(text[front+first:back+sec]) > 50):
                    company_name = company_name.lower()
                    if company_name in filings:
                        filings[company_name] = filings[company_name] + \
                            [year+text[front+first:back+sec]]
                    else:
                        filings[company_name] = [
                            year+text[front+first:back+sec]]
                    # print(text[front+first:back+sec])


scrape(p, "2018")
print("Finished 2018")
p = '/Users/connoranderson/desktop/1618filings/2017/QTR1'
scrape(p, "2017")
print("Finished 2017")
p = '/Users/connoranderson/desktop/1618filings/2016/QTR1'
scrape(p, "2016")
print("Finished 2016")
count = 0
output = {}
for key in filings:
    if len(filings[key]) > 2:
        count += 1
        output[key] = filings[key]
with open('filings.txt', 'wb') as handle:
    pickle.dump(output, handle)
