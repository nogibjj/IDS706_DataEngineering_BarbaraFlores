# imports
import pandas as pd
import matplotlib.pyplot as plt

def print_head_data(path):
    df = pd.read_csv(path)
    print(df.head(5))


if __name__ == "__main__":
    print_head_data("LinkedInTechJobsDataset.csv")
