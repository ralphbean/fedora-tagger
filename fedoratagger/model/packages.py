# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
from sqlalchemy.orm import relation, backref

from fedoratagger.model import DeclarativeBase, metadata, DBSession


def tag_sorter(tag1, tag2):
    """ The tag list for each package should be sorted in descending order by
    the total score, ties are broken by the number of votes cast and if there is
    still a tie, alphabetically by the tag.
    """
    for attr in ['label', 'votes', 'total']:
        result = cmp(getattr(tag1, attr), getattr(tag2, attr))
        if result:
            return result
    return result


class Package(DeclarativeBase):
    __tablename__ = 'package'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    tags = relation('Tag', backref=('package'))

    def __repr__(self):
        """ JSON.. kinda. """
        return {
            self.name: [repr(tag) for tag in sorted(self.tags, tag_sorter)]
        }

class Tag(DeclarativeBase):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    package_id = Column(Integer, ForeignKey('package.id'))
    label = Column(Unicode(255), nullable=False)
    like = Column(Integer, default=1)
    dislike = Column(Integer, default=0)

    @property
    def total(self):
        return self.like - self.dislike

    @property
    def magnitude(self):
        return self.like + self.dislike

    def __repr__(self):
        return {
            'tag': self.label,
            'like': self.like,
            'dislike': self.dislike,
            'total': self.total,
            'votes': self.votes,
        }