from flask import Flask, jsonify

from database import init_db
from models import Base, Name, Title

app = Flask(__name__)



@app.route('/titles', methods=['GET'])
def get_titles():
    titles = Title.query.all()
    return jsonify(
        [
            {
                'tconst': title.tconst,
                'titleType': title.titleType,
                'primaryTitle': title.primaryTitle,
                'originalTitle': title.originalTitle,
                'isAdult': title.isAdult,
                'startYear': title.startYear,
                'endYear': title.endYear,
                'runtimeMinutes': title.runtimeMinutes,
                'genres': title.genres.split(','),
            } for title in titles
        ]
    )


@app.route('/names', methods=['GET'])
def get_names():
    names = Name.query.all()
    return jsonify(
        [
            {
                'nconst': name.nconst,
                'primaryName': name.primaryName,
                'birthYear': name.birthYear,
                'deathYear': name.deathYear,
                'primaryProfession': name.primaryProfession.split(',')
            } for name in names
        ]
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host='0.0.0.0')
