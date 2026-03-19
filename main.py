"""
A simple program to retrieve and display the top 5 posts from a specified subreddit.
This module uses the Reddit API (via requests) to fetch posts from any subreddit.
Users can interactively enter subreddit names to view their top posts, including
the post title, score, and URL. The program continues until the user enters 'exit'.
Functions:
    get_subreddit(subreddit): Fetches the top 5 posts from a given subreddit.
Main:
    Runs an interactive loop that prompts the user for subreddit input and
    displays the top 5 posts with their titles, scores, and URLs.
"""

import requests

def get_subreddit(subreddit):
    try:
        response = requests.get(f"https://www.reddit.com/r/{subreddit}/top.json?limit=5", headers={"User-Agent": "my-app/1.0"})
    except requests.RequestException as e:
        raise ConnectionError(f"Network error: {e}")

    data = response.json()
    posts = data["data"]["children"]
    if not posts:
        raise ValueError(f"Subreddit '{subreddit}' does not exist.")
    return posts


print("This is a simple program to return the top 5 posts in a subreddit.\n")

while True:
    subreddit = input("Enter a subreddit to see its top posts (or 'exit' to quit): ")

    if subreddit.lower() == "exit":
        print("Goodbye!")
        break

    try:
        posts = get_subreddit(subreddit)
    except (ValueError, ConnectionError) as e:
        print(f"Error: {e}")
        continue

    for post in posts:
        p = post["data"]
        print(f"\n-- {p['title']}, {p['score']}, {p['url']}\n")
    
