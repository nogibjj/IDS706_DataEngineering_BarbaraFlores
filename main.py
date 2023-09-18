# imports
import polars as pl
import matplotlib.pyplot as plt


# Read Dataset and exploring
def exploring_data(path):
    df = pl.read_csv(path)
    return(df.head(5))

def mean_variable(path, variable):
    df = pl.read_csv(path)
    return df[variable].mean()

def median_variable(path, variable):
    df = pl.read_csv(path)
    return df[variable].median()

def count_variable(path, variable):
    df = pl.read_csv(path)
    return df[variable].sum() / df[variable].mean() 

def hist_plot(path, variable):
    df = pl.read_csv(path)
    plt.hist(
        df[[variable]],
        bins=10,
    )
    plt.xlabel(variable)
    plt.ylabel("frequency")
    plt.title(f"Histogram of {variable} per job posting in {path}")
    plt.savefig("{}.png".format(variable.lower()))
    return "done!"


if __name__ == "__main__":
    print(exploring_data("LinkedInTechJobsDataset.csv"))
    print()
    for i in ["Total_applicants", "Employee_count", "LinkedIn_Followers"]:
        print(f"The mean of variable {i} is {round(mean_variable('LinkedInTechJobsDataset.csv', i))}.")
    print()
    for i in ["Total_applicants", "Employee_count", "LinkedIn_Followers"]:
        print(f"The median of variable {i} is {round(median_variable('LinkedInTechJobsDataset.csv', i))}.")
    print()
    for i in ["Total_applicants", "Employee_count", "LinkedIn_Followers"]:
        print(f"The count of variable {i} is {round(count_variable('LinkedInTechJobsDataset.csv', i))}.")
    plt.clf()
    hist_plot("LinkedInTechJobsDataset.csv", "Total_applicants")

