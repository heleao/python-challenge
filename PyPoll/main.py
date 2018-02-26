'''
You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). Each dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

    The total number of votes cast

    A complete list of candidates who received votes

    The percentage of votes each candidate won

    The total number of votes each candidate won

    The winner of the election based on popular vote.

As an example, your analysis should look similar to the one below:
'''

import pandas as pd

data_file = "raw_data/election_data_1.csv"
voteData_df= pd.read_csv(data_file, sep=',')
votesCast = len(voteData_df)
candidate = voteData_df.Candidate.value_counts()
candidateVotes_df = pd.DataFrame(candidate)

percentOfVotes = (candidateVotes_df["Candidate"]/int(votesCast)) *100
candidateVotes_df["Percent of Votes"] = percentOfVotes.astype('float')
winner = candidateVotes_df["Candidate"].max()
winningCandidate = winner
organizedCandidate_df = candidateVotes_df[["Candidate","Percent of Votes"]]

print("Election Results")
print("-----------------------------------------------")
print("Total Votes: "+ str(votesCast))
print("-----------------------------------------------")
print(organizedCandidate_df)
print("-----------------------------------------------")
print("Winner: " + str(winningCandidate))
print("-----------------------------------------------")

organizedCandidate_df.to_csv("Output/fileOne.csv", index=False, header=True)



data_file = "raw_data/election_data_2.csv"
voteData_df= pd.read_csv(data_file, sep=',')
votesCast = len(voteData_df)
candidate = voteData_df.Candidate.value_counts()
candidateVotes_df = pd.DataFrame(candidate)

percentOfVotes = (candidateVotes_df["Candidate"]/int(votesCast)) *100
candidateVotes_df["Percent of Votes"] = percentOfVotes.astype('float')
winner = candidateVotes_df["Candidate"].max()
winningCandidate = winner
organizedCandidate_df = candidateVotes_df[["Candidate","Percent of Votes"]]

print("Election Results")
print("-----------------------------------------------")
print("Total Votes: "+ str(votesCast))
print("-----------------------------------------------")
print(organizedCandidate_df)
print("-----------------------------------------------")
print("Winner: " + str(winningCandidate))
print("-----------------------------------------------")

organizedCandidate_df.to_csv("Output/fileTwo.csv", index=False, header=True)