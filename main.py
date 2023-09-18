# imports
import pandas as pd
import polars as pl
import matplotlib.pyplot as plt
import plotly.express as px



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

def pie_plot(path, variable):
    df = pd.read_csv(path)
    category_count = df[variable].value_counts()
 #   plt.figure(figsize=(6, 6))
    #explode = (0.1, 0, 0, 0)
    plt.pie(
        category_count,
        labels=category_count.index,
        autopct="%1.1f%%",
        startangle=180,
     #   explode=explode,
    )
    plt.title(
        "Number of job positions with respect to the variable {0} ".format(variable)
    )
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig("{0}.png".format(variable.lower()))


def bar_plot_skills(path):
    df = pd.read_csv(path)
    skills = (
        df[
            [
                "PYTHON",
                "C++",
                "JAVA",
                "HADOOP",
                "SCALA",
                "FLASK",
                "PANDAS",
                "SPARK",
                "NUMPY",
                "PHP",
                "SQL",
                "MYSQL",
                "CSS",
                "MONGODB",
                "NLTK",
                "TENSORFLOW",
                "LINUX",
                "RUBY",
                "JAVASCRIPT",
                "DJANGO",
                "REACT",
                "REACTJS",
                "AI",
                "UI",
                "TABLEAU",
                "NODEJS",
                "EXCEL",
                "POWER BI",
                "SELENIUM",
                "HTML",
                "ML",
            ]
        ]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))
    skills.plot(kind="bar", color="skyblue")

    plt.xlabel("Skills")
    plt.ylabel("Sum")
    plt.title("Most in-demand skills and technologies")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("skills.png")


def hist_plot(path, variable):
    df = pd.read_csv(path)
    plt.hist(
        df[[variable]],
        bins=10,
    )
    plt.xlabel(variable)
    plt.ylabel("frequency")
    plt.title("Histogram of {0} per job posting".format(path, variable))
    plt.savefig("{}.png".format(variable.lower()))


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
    pie_plot("LinkedInTechJobsDataset.csv", "Involvement")
    plt.clf()
    bar_plot_skills("LinkedInTechJobsDataset.csv")
    plt.clf()
    hist_plot("LinkedInTechJobsDataset.csv", "Total_applicants")

