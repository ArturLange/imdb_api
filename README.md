# IMDB API

## How to run

### Using Pipenv

#### Prerequisites

- pipenv
- docker

#### Instructions

- `pipenv install` - to install dependencies
- `pipenv run start_db` - to start postgres in docker
- `pipenv run app` - to start application

### No Pipenv

#### Prerequisites

- make sure postgres is running on `localhost:5432` or change accordingly in `database.py`

#### Instructions

- install dependencies from `requirements.txt`
- Run `python flask_app.py`

## Endpoints

Both endpoints get optional parameters `maxResults` and `page`. These are used for pagination.
Please note that if no pagination parameters are set, there is no constraints and response might be resource heavy.

- `/year/<year>/titles` - Returns titles with `startYear` equal to `<year>`.

  Titles are returned in alphabetical order.
  Optional request param `genre` filters by genre (only one genre is supported).

  E.g. request to `/year/2012/titles?genre=Comedy&maxResults=20` returns 20 (or less) comedies from 2012.

- `/names` - returns names matching given params. For each name which has any titles, returns them in field `knownForTitles`

  E.g. request to `/names?primaryName=Fred&birthYear=1899&deathYear=1987` should return Fred Astaire and his movies.
