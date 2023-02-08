import requests
import json
import time

# Replace with your Spotify API access token
access_token = "your_access_token"

# Replace with the name of the song you want to search for
song_name = input("Enter the name of a song: ")

# Set up the API endpoint and header for the request
endpoint = f"https://api.spotify.com/v1/search?q={song_name}&type=track"
header = {
    "Authorization": "Bearer " + access_token
}

# Send a GET request to the Spotify Web API to search for the song
response = requests.get(endpoint, headers=header)

# Parse the JSON response
data = json.loads(response.text)

# Check if any songs were found
if data.get("tracks") and data["tracks"].get("total") > 0:
    # Extract the first song found
    song = data["tracks"]["items"][0]
    song_id = song["id"]
    
    # Set up the API endpoint and header for the request to retrieve information about the song
    endpoint = f"https://api.spotify.com/v1/tracks/{song_id}"
    header = {
        "Authorization": "Bearer " + access_token
    }
    
    # Display a loading animation
    print("Loading", end="")
    for i in range(3):
        time.sleep(0.5)
        print(".", end="")
        
    # Send a GET request to the Spotify Web API to retrieve information about the song
    response = requests.get(endpoint, headers=header)
    
    # Parse the JSON response
    data = json.loads(response.text)
    
    # Extract information about the song
    song_name = data["name"]
    artist = data["artists"][0]["name"]
    album = data["album"]["name"]
    popularity = data["popularity"]
    duration_ms = data["duration_ms"]
    
    # Calculate the average listen time
    average_listen_time = duration_ms / 1000 / 60
    
    # Print the information about the song
    print(f"\nSong Name: {song_name}")
    print(f"Artist: {artist}")
    print(f"Album: {album}")
    print(f"Popularity: {popularity}")
    print(f"Duration (ms): {duration_ms}")
    print(f"Average Listen Time (minutes): {average_listen_time}")
else:
    # No songs were found with the given name
    print("\nNo songs were found with that name.")
    
    # Check if there are any similar songs based on the search results
    if data.get("tracks"):
        # Suggest similar songs based on the search results
        print("\nDid you mean:")
        for song in data["tracks"]["items"]:
            print(f"- {song['name']} by {song['artists'][0]['name']}")
    else:
        # No similar songs were found
        print("\nNo similar songs were found.")
