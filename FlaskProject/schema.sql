CREATE TABLE ariana_grande (
  track int,
  title text,
  album text,
  album_edition text,
  album_id int,
  release_date date,
  duration interval,
  genre text,
  PRIMARY KEY (track, album_id)
);

select *
from ariana_grande;

DROP TABLE ariana_grande;