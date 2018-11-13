from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from db import db
from objects.social_interactions import comments, comment_votes, candidate_votes, candidate_comments, measure_votes
from objects.social_objects import *


class users(db.Model):
    '''Requires username, email, & zip code'''
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    zipcode = Column(String(5), nullable=False)
    is_active = 1
    is_authenticated = 1

    def get_id(self):
        return self.id

    def user_comments(username):
        '''Return a list of all of a users comments -- Provide a type'''
        comments_list = social_interactions.comments.query()
    
    def __repr__(self):
        return '<User %r>' % self.username