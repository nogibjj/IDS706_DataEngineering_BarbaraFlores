# imports
import pandas as pd
import matplotlib.pyplot as plt

# Read Dataset and exploring
def exploring_data(path):
    df = pd.read_csv(path)
    print(df.head(5),"/n")
    print(df.info(),"/n")
    print(df.describe(),"/n")

if __name__ == "__main__":
    exploring_data("LinkedInTechJobsDataset.csv")
