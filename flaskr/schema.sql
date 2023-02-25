DROP TABLE IF EXISTS tracks;


CREATE TABLE tracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT UNIQUE NOT NULL,
  artist TEXT NOT NULL,
  genre TEXT NOT NULL,
  length_ INTEGER NOT NULL
);

INSERT INTO tracks (title, artist, genre, length_)
VALUES
    ('Young and beautiful', 'Lana Del Ray', 'Indie-Rock', 220),
    ('Summertime Sadness', 'Lana Del Ray', 'Indie-Rock', 210),
    ('No Time To Die', 'Billie Eillish', 'POP-Music', 235),
    ('Kino', 'MACAN', 'HIP-HOP', 180),
    ('Serpantin', 'MARKUL', 'HIP-HOP', 225),
    ('Starboy', 'Weekend', 'Loft-Music', 190),
    ('TOP', 'DOROFEEVA', 'Ukrainian-POP', 220),
    ('KAFEL', 'DOROFEEVA', 'Ukrainian-POP', 215);
