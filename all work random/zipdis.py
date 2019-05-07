import csv

D = dict()
with open('directory.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        dis = row[4]
        zip = row[2][-5:]
        D[zip] = dis

#print(L[0])
#print(L[1])
del D['dress']
#print(D)

with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in D.items():
       writer.writerow([key, value])

print(D)
with open('allzipsmetronyc.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        #print(row[0])
        if str(row[0]) in D.keys():
            pass
        else:
            print(str(row[0]))
        #print(D[(str(row[0]))])

if str(11221) in D.keys():
    print('YES IT IS')

with open('profs.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        pass
        #print(row)
