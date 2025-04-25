from github import Github
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
from datetime import date

# Load environment variables from .env file
load_dotenv(override=True)

# Authenticate with your GitHub token
# Use your personal access token fetched from .env file
ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')

print("Initialising git Object")

# Initialize Github object
g = Github(ACCESS_TOKEN)

# Input the repository you are interested in
repo_name = input("Enter the GitHub repository name (e.g., username/repo_name): ")

print(f"Getting repository object for {repo_name}")
repo = g.get_repo(repo_name)

print("fetching commits")

# Fetch all commits
commits = repo.get_commits()

# Create a dictionary to hold commit counts per author
print("Creating commit counts")

commit_counts = {}
for commit in commits:
    author = commit.author.login if commit.author else 'Unknown'
    if author in commit_counts:
        commit_counts[author] += 1
    else:
        commit_counts[author] = 1

#calculate total commits and percentage of commits per author
total_commits = sum(commit_counts.values())
commit_percentages = {author: (count / total_commits) * 100 for author, count in commit_counts.items()}

print(f"Total commits: {total_commits}")
print(f"Commit percentages: {commit_percentages}")

print("Generating pie chart")

# Prepare data for the pie chart
labels = commit_percentages.keys()
sizes = commit_percentages.values()

today = date.today().strftime("%d-%b-%Y")

# Plot
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title(f"Reporting Date:{today}\nrepository: {repo_name}\nContribution Percentage by Commits\n")

plt.show()