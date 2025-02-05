# Billboard to Spotify Playlist

This project allows you to create a private Spotify playlist based on the Billboard Hot 100 chart for a specific date. The script fetches the top songs from the Billboard chart for the selected year and date, searches for those tracks on Spotify, and then generates a Spotify playlist containing those tracks.

## Requirements

1. **Python 3.x**
2. **Spotify Developer Account**: You will need to create a Spotify Developer account and generate your own client ID and client secret. 
   - [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)
3. **Install Python Libraries**: Install the required Python libraries via `pip`:
    ```bash
    pip install spotipy requests beautifulsoup4
    ```

## Setup

1. **Spotify API Credentials**:
   Replace `client_id` and `client_secret` in the script with your own credentials obtained from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

2. **Billboard Chart**:
   The script will fetch the Billboard Hot 100 chart for the date you specify in the format `YYYY-MM-DD`.

## How to Use

1. Clone the repository or download the script.
2. Run the script:
   ```bash
   python script_name.py
   ```
3. Enter the date in the format `YYYY-MM-DD` when prompted, for example:
   ```
   Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 1990-05-12
   ```
4. The script will fetch the top songs from the Billboard Hot 100 chart for the provided date, search for those songs on Spotify, and create a private playlist on your Spotify account.

5. The script prints the list of song names and their corresponding Spotify track IDs. A new Spotify playlist named `"Billboard of <date>"` will be created, and the songs will be added to the playlist.

## Code Breakdown

1. **Fetching Billboard Chart**: The script uses `requests` and `BeautifulSoup` to scrape the Billboard Hot 100 page for the provided date and extract the song titles.
2. **Spotify Search**: The `spotipy` library is used to search for the extracted songs on Spotify, and the release year is used to filter the search results.
3. **Create Playlist**: The script creates a private playlist on your Spotify account and adds the tracks to it using the Spotify Web API.

## Example Output

```bash
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 1990-05-12
['Nothing Compares 2 U', 'Vogue', 'I Will Always Love You', ...] 
Spotify IDs: ['spotify:track:1a2b3c...', 'spotify:track:4d5e6f...', ...]
Playlist 'Billboard of 1990-05-12' created successfully!
```

## Notes

- The script currently retrieves the top 100 songs (or fewer if there aren't that many) for a specific date.
- Ensure that you have valid Spotify credentials and the necessary permissions (`playlist-modify-private` and `playlist-modify-public`) set in your Spotify Developer Dashboard.
- The script will only add songs released in the specified year or later.

---
