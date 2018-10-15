from sqlalchemy import (
    Boolean,
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    Table
)
from sqlalchemy.orm import relationship

from database import Base

title_to_name_table = Table(
    'title_to_name', Base.metadata,
    Column('titles_id', String, ForeignKey('titles.tconst')),
    Column('names_id', String, ForeignKey('names.nconst'))
)


class Title(Base):
    __tablename__ = 'titles'
    tconst = Column(String, primary_key=True)
    titleType = Column(String)
    primaryTitle = Column(String)
    originalTitle = Column(String)
    isAdult = Column(Boolean)
    startYear = Column(Integer)
    endYear = Column(Integer)
    runtimeMinutes = Column(Integer)
    genres = Column(String)
    knownPeople = relationship(
        "Name",
        secondary=title_to_name_table,
        back_populates='knownForTitles'
    )

    def to_dict(self):
        return {
            'tconst': self.tconst,
            'titleType': self.titleType,
            'primaryTitle': self.primaryTitle,
            'originalTitle': self.originalTitle,
            'isAdult': self.isAdult,
            'startYear': self.startYear,
            'endYear': self.endYear,
            'runtimeMinutes': self.runtimeMinutes,
            'genres': self.genres.split(',') if self.genres else [],
            'knownPeople': [name.to_dict() for name in self.knownPeople]
        }


class Name(Base):
    __tablename__ = 'names'
    nconst = Column(String, primary_key=True)
    primaryName = Column(String)
    birthYear = Column(Integer)
    deathYear = Column(Integer)
    primaryProfession = Column(String)
    knownForTitles = relationship(
        "Title",
        secondary=title_to_name_table,
        back_populates='knownPeople'
    )

    def to_dict(self):
        return {
            'nconst': self.nconst,
            'primaryName': self.primaryName,
            'birthYear': self.birthYear,
            'deathYear': self.deathYear,
            'primaryProfession': self.primaryProfession.split(',') if self.primaryProfession else []
        }
