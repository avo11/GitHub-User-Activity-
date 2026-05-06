import sys
import urllib.request
import json

def main():

    username = input("Username: ")
    url = f"https://api.github.com/users/{username}/events"
    
    with urllib.request.urlopen(url) as response:
        body = response.read()
    
    json_string = json.loads(body)
    
    for event in json_string:
        if event["type"] == "PushEvent":
            print(f"- Pushed to {event['repo']['name']}")
        elif event["type"] == "CreateEvent":
            print(f"- Created {event['repo']['name']}")
        else:
            print(f"- {event['type']} in {event['repo']['name']}")

main()

    
