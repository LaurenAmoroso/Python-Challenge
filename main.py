import os
import csv

election_data_path =os.path.join('..','Pypoll','election_data.csv')

with open(election_data_path) as election_data:
    reader = csv.reader(election_data, delimiter= ',')
    next(reader)
    data = list(reader)
    count = len(data)

    candidatelist = list()
    total = list()

    for i in range (0, count):
        candidate = data[i][2]
        total.append(candidate)
        if candidate not in candidatelist:
            candidatelist.append(candidate)
    candidatecount = len(candidatelist)

    votes = list()
    percentage = list()
    for j in range (0,candidatecount):
        name= candidatelist[j]
        votes.append(total.count(name))
        percent = votes[j]/count

    winner = votes.index(max(votes)) 

print ("Election Results")
print(f"Toal Votes: {count:,}")

print(f"Winner: {candidatelist[winner]}")

print("Election Results", file=open("PyPoll.txt", "a"))
print(f"Toal Votes: {count:,}", file=open("PyPoll.txt", "a"))
print(f"Winner: {candidatelist[winner]}", file=open("PyPoll.txt", "a"))