# imports
import pandas as pd
import matplotlib.pyplot as plt

# Read Dataset and exploring
def exploring_data(path):
    df = pd.read_csv(path)
    print(df.head(5),"/n")
    print(df.info(),"/n")
    print(df.describe(),"/n")

def pie_plot(path, variable):
    df = pd.read_csv(path)
    category_count = df[variable].value_counts()
    plt.figure(figsize=(6, 6))   
    explode = (0.1, 0, 0, 0)  
    plt.pie(category_count, labels=category_count.index, autopct='%1.1f%%', startangle=180, explode=explode)
    plt.title("Number of job positions with respect to the variable {0} ".format(variable))
    plt.axis('equal')  
    plt.tight_layout()
    plt.savefig("{0}.png".format(variable))
  

if __name__ == "__main__":
    exploring_data("LinkedInTechJobsDataset.csv")
    pie_plot("LinkedInTechJobsDataset.csv",
             "Involvement")
