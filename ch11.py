"""Review of Chapter 11: Nested Data.

Author: Chris Mayfield
Version: 12/02/2024
"""

from statistics import mean, median


def print_stats(label, strings):
    """Print statistics about the lengths of the strings.

    Output format:
    >>> print_stats("Letters:", {"A", "BB", "CCC", "DDD"})
    Letters: min = 1.0, median = 2.5, mean = 2.2, min = 3.0

    Args:
        label (str): The first line to print above the stats.
        strings (set): The strings to calculate the stats.
    """
    lens = [len(s) for s in strings]
    print(label,
          f"min = {min(lens):.1f}, "
          f"median = {median(lens):.1f}, "
          f"mean = {mean(lens):.1f}, "
          f"max = {max(lens):.1f}")


def track_stats(tracks):
    """Analyze track names, artist names, and album titles.

    Args:
        tracks (list): Top 50 tracks from the last.fm API.
    """
    track_names = set()
    artist_names = set()
    album_titles = set()
    for track in tracks:
        track_names.add(track["name"])
        artist_names.add(track["artist"]["name"])
        if "album" in track:
            album_titles.add(track["album"]["title"])
    print_stats("Track names:", track_names)
    print_stats("Artist names:", artist_names)
    print_stats("Album titles:", album_titles)
