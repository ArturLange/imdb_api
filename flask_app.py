from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from database import init_db
from models import Base, Name, Title

app = Flask(__name__)



@app.route('/titles', methods=['GET'])
def get_titles():
    return jsonify(Title.query.all())


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
