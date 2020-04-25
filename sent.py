import pickle

with open('filings.txt', 'rb') as handle:
    filings = pickle.loads(handle.read())
count = 0
tokenized_filings = {}
for key in filings:
    for reports in filings[key]:
        t = reports.lower()
        temp = t.split(" ")
        if key not in tokenized_filings:
            tokenized_filings[key] = [temp]
        else:
            tokenized_filings[key] = tokenized_filings[key] + [temp]
for key in tokenized_filings:
    for lst in tokenized_filings[key]:
        for word in lst:
            if word == "ceo" or word == "cfo":
                count += 1
# Check unique number of filings that mention these strings, add "Chief
# Executive Officer" and "Chief Financial Officer."
#
# Start comparing different years
print(count)
