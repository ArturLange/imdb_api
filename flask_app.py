from flask import Flask, jsonify, request

from database import init_db
from models import Base, Name, Title

app = Flask(__name__)


@app.route('/year/<int:startYear>/titles', methods=['GET'])
def get_titles_from_year(startYear):
    titles = Title.query.filter(Title.startYear == int(
        startYear)).order_by(Title.primaryTitle)
    genre = request.args.get('genre')
    maxResults = request.args.get('maxResults')
    page = request.args.get('page')
    if genre:
        titles = titles.filter(Title.genres.ilike(f'%{genre}%'))
    if maxResults:
        titles = titles.limit(maxResults)
        if page:
            titles = titles.offset((int(page)-1) * int(maxResults))
    return jsonify(
        [
            title.to_dict() for title in titles
        ]
    )


@app.route('/names', methods=["GET"])
def get_people_and_their_titles():
    names = Name.query

    primaryName = request.args.get('primaryName')
    birthYear = request.args.get('birthYear')
    deathYear = request.args.get('deathYear')
    primaryProfession = request.args.get('primaryProfession')

    if primaryName:
        names = names.filter(Name.primaryName.ilike(f'%{primaryName}%'))
    if birthYear:
        names = names.filter(Name.birthYear == birthYear)
    if deathYear:
        names = names.filter(Name.deathYear == deathYear)
    if primaryProfession:
        names = names.filter(
            Name.primaryProfession.ilike(f'%{primaryProfession}%'))

    maxResults = request.args.get('maxResults')
    page = request.args.get('page')

    if maxResults:
        names = names.limit(maxResults)
        if page:
            names = names.offset((int(page)-1) * int(maxResults))

    return jsonify(
        [
            name.to_dict() for name in names.order_by(Name.primaryName)
        ]
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host='0.0.0.0')
