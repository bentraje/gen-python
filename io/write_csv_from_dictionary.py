import pandas as pd
from csv import DictWriter

data_to_write = []

data_to_write.append(
        {
        "title": "aaa",
        "year": "aaa",
        "network": "aaa",
        "duration_in_minutes": "aaa",
        "director": "aaa",
        "screenwriter": "aaa",
        "episodes": "aaa",
        "ratings": "aaa",
        "totnum_ratings": "aaa",
        "totnum_watchers": "aaa",
        "totnum_reviews": "aaa",
        "genres": "aaa",
        "tags": "aaa",
        "url": "aaa",
        }
    )

genres = ['Mystery', 'Drama', 'Sci-Fi', 'Fantasy', 'Melodrama']
write_me = ''.join(str(e) + "," for e in genres)

data_to_write.append(
        {
        "title": "bbb",
        "year": "bbb",
        "network": "bbb",
        "duration_in_minutes": "bbb",
        "director": "bbb",
        "screenwriter": "bbb",
        "episodes": "bbb",
        "ratings": "bbb",
        "totnum_ratings": "bbb",
        "totnum_watchers": "bbb",
        "totnum_reviews": "bbb",
        "genres": write_me,
        "tags": "bbb",
        "url": "bbb",
        }
    )

field_names = [
        "title",
        "year",
        "network",
        "duration_in_minutes",
        "director",
        "screenwriter",
        "episodes",
        "ratings",
        "totnum_ratings",
        "totnum_watchers",
        "totnum_reviews",
        "genres",
        "tags",
        "url"]

file = open("write_csv_from_dict.csv", "a", newline='')
dictwriter_object = DictWriter(file, fieldnames=field_names)

for data in data_to_write:
    dictwriter_object.writerow(data)
file.close()