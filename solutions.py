import pandas as pd 

df = pd.read_csv("election_data.csv")

votes_tally_df = df.groupby("Candidate").count()["Voter ID"]

print(votes_tally_df)