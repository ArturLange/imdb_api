from flask import Flask, jsonify, request

from database import init_db
from models import Base, Name, Title

app = Flask(__name__)


@app.route('/year/<int:startYear>/titles', methods=['GET'])
def get_titles_from_year(startYear):
    titles = Title.query.filter(Title.startYear == int(startYear)).order_by(Title.primaryTitle)
    genre = request.args.get('genre')
    if genre:
        titles = titles.filter(Title.genres.ilike(f'%{genre}%'))
    return jsonify(
        [
            title.to_dict() for title in titles
        ]
    )


@app.route('/titles', methods=['GET'])
def get_titles():
    titles = Title.query.all()
    return jsonify(
        [
            title.to_dict() for title in titles
        ]
    )


@app.route('/names', methods=['GET'])
def get_names():
    names = Name.query.all()
    return jsonify(
        [
            name.to_dict() for name in names
        ]
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host='0.0.0.0')
