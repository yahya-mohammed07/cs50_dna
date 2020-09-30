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
        counts[k] = 1
    # updating the STRs by iteratign through the keys
    for k in keys:
        # ingore name
        if k != "name":
            lenK = len(k)
            temp = 0
            count = 0
            i = 0
            while i < len(seq) - lenK:
                if seq[i : lenK + i] == k:
                    temp += 1
                    i += lenK
                else:
                    temp = 0
                    i += 1
                if temp > count:
                    count = temp
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
            break

    print(counts["name"])


main()