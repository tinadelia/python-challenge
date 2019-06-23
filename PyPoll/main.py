import os
import csv

pypoll_csv = os.path.join('Resources', 'election_data.csv')
voter_id = []
county = []
candidate = []
k_votes = []
c_votes = []
l_votes = []
o_votes = []



with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)


    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        candidates = (candidate)


    for c in candidates:
        if c == "Khan":
            k_votes.append(candidate)
        elif c == "Correy":
            c_votes.append(candidate)
        elif c == "Li":
            l_votes.append(candidate)
        elif c == "O'Tooley":
            o_votes.append(candidate)


k_percent = round((len(k_votes) / len(candidates)) * 100, 4)
c_percent = round((len(c_votes) / len(candidates)) * 100, 4)
l_percent = round((len(l_votes) / len(candidates)) * 100, 4)
o_percent = round((len(o_votes) / len(candidates)) * 100, 4)


max_candidate = set(candidates)
winner = max(set(candidates),key=candidates.count)


print("Election Results")
print("--------------------------------")
print(f"Total Votes: {len(voter_id)}")
print("--------------------------------")
print(f"Khan: {k_percent}%  ({(len(k_votes))})")
print(f"Correy: {c_percent}%  ({(len(c_votes))})")
print(f"Li: {l_percent}%  ({(len(l_votes))})")
print(f"O'Tooley: {o_percent}%  ({(len(o_votes))})")
print("--------------------------------")
print(f"Winner: {(winner)}")
print("--------------------------------")

output_file = os.path.join('Resources', 'output_folder', 'output.txt')

with open(output_file, 'w') as txt_file:

    txt_file.write("Election Results\n")
    txt_file.write("--------------------------------\n")
    txt_file.write(f"Total Votes: {len(voter_id)}\n")
    txt_file.write("--------------------------------\n")
    txt_file.write(f"Khan: {k_percent}%  ({(len(k_votes))})\n")
    txt_file.write(f"Correy: {c_percent}%  ({(len(c_votes))})\n")
    txt_file.write(f"Li: {l_percent}%  ({(len(l_votes))})\n")
    txt_file.write(f"O'Tooley: {o_percent}%  ({(len(o_votes))})\n")
    txt_file.write("--------------------------------\n")
    txt_file.write(f"Winner: {(winner)}\n")
    txt_file.write("--------------------------------\n")