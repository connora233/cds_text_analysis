import pickle

with open('filings.txt', 'rb') as handle:
    filings = pickle.loads(handle.read())
count = 0
num_filings = 0
added_filings = []
tokenized_filings = {}
change_words = ["hire", "appoint", "elect", "new",
                "search", "fire", "resign", "resignation"]
job_titles = ["ceo", "cfo", "chief executive officer",
              "chief financial officer"]
years = ["2016", "2017", "2018"]
for key in filings:
    for reports in filings[key]:
        t = reports.lower()
        temp = t.split(" ")
        if key not in tokenized_filings:
            tokenized_filings[key] = [temp]
        else:
            tokenized_filings[key] = tokenized_filings[key] + [temp]
for key in tokenized_filings:
    yr = 0
    for lst in tokenized_filings[key]:
        num_filings += 1
        yr += 1
        c = -15
        b = -15
        w = 0
        for word in lst:
            if word in job_titles:
                c = w
                if w - b < 10:
                    print(key)
                    print(yr)
                    if key not in added_filings:
                        count += 1
                        added_filings += [key]
            if word in change_words:
                b = w
                if w - c < 10:
                    print(key)
                    print(yr)
                    if key not in added_filings:
                        count += 1
                        added_filings += [key]
            w += 1

# Check unique number of filings that mention these strings, add "Chief
# Executive Officer" and "Chief Financial Officer."
#
# Start comparing different years
print(count)
print(num_filings)
print(count/num_filings)
