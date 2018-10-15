import csv

from database import db_session, init_db
from models import Name, Title


def map_null(value: str):
    return value if value != '\\N' else None


def insert_names_into_db(batch_size: int = 10000, limit: int = 50000):
    with open('name.basics.tsv') as names_tsv:
        names_tsv.readline()
        reader = csv.reader(names_tsv, delimiter='\t')
        counter = 0

        names = []
        number_in_batch = 0
        for row in reader:
            if number_in_batch > batch_size:
                number_in_batch = 0
                db_session.add_all(names)
                db_session.commit()
                names = []
                counter += batch_size
                print(f'added {counter} names')
                if limit and counter >= limit:
                    return
            row = list(map(map_null, row))
            name = Name(
                nconst=row[0],
                primaryName=row[1],
                birthYear=row[2],
                deathYear=row[3],
                primaryProfession=row[4],
            )
            if row[5]:
                titles = Title.query.filter(Title.tconst.in_(row[5].split(',')))
            name.knownForTitles = list(titles)
            names.append(name)
            number_in_batch += 1
        db_session.commit()


def insert_titles_into_db(batch_size: int = 10000, limit: int = 50000):
    with open('title.basics.tsv') as titles_tsv:
        titles_tsv.readline()
        reader = csv.reader(titles_tsv, delimiter='\t')
        counter = 0

        titles = []
        number_in_batch = 0
        for row in reader:
            if number_in_batch > batch_size:
                number_in_batch = 0
                db_session.add_all(titles)
                db_session.commit()
                titles = []
                counter += batch_size
                print(f'added {counter} titles')
                if limit and counter >= limit:
                    return
            row = list(map(map_null, row))
            title = Title(
                tconst=row[0],
                titleType=row[1],
                primaryTitle=row[2],
                originalTitle=row[3],
                isAdult=bool(row[4]),
                startYear=row[5],
                endYear=row[6],
                runtimeMinutes=row[7],
                genres=row[8]
            )
            titles.append(title)
            number_in_batch += 1
        db_session.commit()


if __name__ == '__main__':
    init_db()
    insert_titles_into_db()
    insert_names_into_db()
