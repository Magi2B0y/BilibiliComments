import csv

f = "672_ori_3.csv"
neg = open("temp/672_neg.txt", "a+", encoding="utf-8")
pos = open("temp/672_pos.txt", "a+", encoding="utf-8")
sug = open("temp/672_sug.txt", "a+", encoding="utf-8")
neu = open("temp/672_neu.txt", "a+", encoding="utf-8")
c = open("./comments/" + f, "r+", encoding="utf-8")
try:
    print("Now process file: " + f)
    start = int(input("Enter the start point [0,len(file)):"))
    com = [row[2] for row in csv.reader(c)]
    if start != 0:
        start += 1
    while start < len(com):
        print("Now line " + str(start))
        print(com[start])
        command = input("g(neg)/p(pos)/n(neu)/s(sug)/gs/ps/ns: ")
        data = com[start].replace("\n", "")
        if command == "g":
            neg.write(data + "\n")
            start += 1
        elif command == "p":
            pos.write(data + "\n")
            start += 1
        elif command == "n":
            neu.write(data + "\n")
            start += 1
        elif command == "s":
            sug.write(data + "\n")
            start += 1
        elif command == "ps":
            pos.write(data + "\n")
            sug.write(data + "\n")
            start += 1
        elif command == "ns":
            neu.write(data + "\n")
            sug.write(data + "\n")
            start += 1
        elif command == "gs":
            neg.write(data + "\n")
            sug.write(data + "\n")
            start += 1
        else:
            print("Try again.")
    neg.close()
    pos.close()
    neu.close()
    c.close()
except:
    neg.close()
    pos.close()
    neu.close()
    c.close()
