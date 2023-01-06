playlist = {
    "title": "like song",
    "author": "asib",
    "songs": [
        {"title": "let me down", "artist": ["mc", "pitbull"], "duration": 2.5},
        {"title": "paper cut", "artist": ["linkin park"], "duration": 5.5},
        {"title": "alone", "artist": ["masmello"], "duration": 4},
    ],
}

total_duration = 0
print(playlist["songs"])
print(playlist["title"])
for song in playlist["songs"]:
    total_duration += song["duration"]
print(total_duration)
