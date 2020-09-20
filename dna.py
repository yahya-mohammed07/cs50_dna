import sys
import csv


def main():
    if len(sys.argv) != 3:
        print("usage python dna.py data.csv sequence.txt")
        sys.exit(1)
    # loading text file into string
    with open(sys.argv[2], "r") as sequence:
        seq = sequence.read()
    # loading csv database into a list and taking the first row
    dataList = []
    with open(sys.argv[1], "r") as data:
        read = csv.DictReader(data)
        for row in read:
            dataList.append(row)
    # just a lis to store the keys
    keys = list(dataList[0].keys())
    # a dict to store keys and values and will be updated with STRs
    counts = {}
    for k in keys:
        counts[k] = ""
    # updating the STRs
    for k in keys:
        if k != "name":
            count = 0
            for i in range(len(seq)):
                for j in range(i + len(str(k)), len(seq), len(str(k))):
                    sub_len = len(seq[i:j]) // len(str(k))
                    subStr = str(str(k) * sub_len)
                    if seq[i:j] == subStr and sub_len > count:
                        count = sub_len
                    counts[k] = count
    # finding a match
    counts["name"] = "no match"
    match = 0
    for p in dataList:
        for k in keys:
            if k != "name" and (int(counts[k]) == int(p[k])):
                match += 1
            else:
                match = 0
        if match == len(keys) - 1:
            counts["name"] = p["name"]

    print(counts["name"])


main()