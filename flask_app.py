from flask import Flask, jsonify
from models import Base, Title
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# bind SQLAlchemy
engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)


@app.route('/titles', methods=['GET'])
def get_titles():
    return jsonify(Title.query.all())


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host='0.0.0.0')
