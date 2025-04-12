#https://www.kdnuggets.com/lesser-known-python-functions-that-are-super-useful
from operator import attrgetter
from datetime import datetime

# Let's create a simple class to demonstrate an article in a blog
class Article:
    def __init__(self, title, author, views, date):
        self.title = title
        self.author = author
        # create Nested attribute stats.views by dynamically creating a class called Stats
        self.stats = type('Stats', (), {'views': views})
        self.date = date

    #same as toString() in Java
    def __repr__(self):
        return f"{self.title} by {self.author}"

# Create some sample articles
articles = [
	Article("Python Tips", "Alice", 1500, datetime(2025, 1, 15)),
	Article("Data Science", "Bob", 500, datetime(2025, 1, 20)),
	Article("Web Dev", "Alice", 1800, datetime(2025, 1, 10))
]

# Sort articles by author and within author by views
get_author_views = attrgetter('author', 'stats.views')

# Sort articles by views
#get_views = attrgetter("stats.views")

# Sort by given key
sorted_articles = sorted(articles, key=get_author_views)
for article in sorted_articles:
    print(f"{article.author}: {article.title} ({article.stats.views} views)")

# You can also use it to extract specific attributes
#map takes a function and iterable. Calls the function with each element in iterable
#and returns an iterable.
#list takes an iterable and converts it into a list
dates = list(map(attrgetter('date'), articles))
print("\nArticle dates:", dates)