GitHub User Activity CLI
A command line interface (CLI) tool that fetches and displays the recent activity of any GitHub user directly in your terminal.
Features

Fetch recent activity for any GitHub user
Display events such as pushes, pull requests, issues, and more
Lightweight with no external dependencies — uses the GitHub public API

Usage
bashpython main.py <github-username>
Example:
bashpython main.py torvalds
Output:
- Pushed 3 commits to torvalds/linux
- Opened an issue in torvalds/linux
- Starred torvalds/subsurface-for-dirk
How It Works

Calls the GitHub Events API
Parses the JSON response
Formats and prints each event to the terminal

What I Learned

Working with REST APIs in Python
Parsing and handling JSON data
Building a simple CLI application
