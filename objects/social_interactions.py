from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from db import db
from objects.social_objects import ballots, candidates, measures
from objects.users import users

# Need to:
#   - create Races
#   - see slides for object model

class comments(db.Model):
    ''' M:M to capture user comments on candidates or measures'''
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    uid = Column(Integer, db.ForeignKey("users.uid"))
    comment_type = Column(Boolean) # 0 == Candidate | 1 == Measure
    comment_position = Column(Boolean) # 0 == Pro | 1 == Con
    cid = Column(Integer, db.ForeignKey('candidates.cid'))
    mid = Column(Integer, db.ForeignKey('measures.cid'))
    comment_text = Column(Text)


    # Should this be a static method? A function in the controller file? Confused!
    def retrieve_top_comments(type):
        top_ten_ids = comment_votes().top_ten_comments
        payload = comments.query.filter_by(comments.comments_id.in_(top_ten_ids)).all()
        return payload


class comment_votes(db.Model):
    '''Captures the comment up votes'''
    __tablename__ = 'comment_votes'
    comment_id = Column(Integer, db.ForeignKey('comments.comment_id'))
    uid = Column(Integer, db.ForeignKey('users.uid'))
    vote = Column(Boolean) # 0 == No vote | 1 == upvote # Default == 0
    type = relationship("comments", foreign_keys='comment_vote.comment_id') # .comment_type

    # Should this be a static method? A function in the controller file? Confused!
    def vote_on_comment(uid, comment_id):
        '''Upvote a comment, or take back an upvote'''
        cv = comment_votes.query.filter_by(uid=uid, cid=comment_id) # Should just be 1 record
        if cv.vote == 1:
            cv.vote = 0
        else:
            cv.vote = 1
        db.Session.commit()

    def top_ten_comments(type):
        all = comment_votes.query(comment_votes.comment_id, func.sum(comment_votes.vote)
                                  .label('total_votes')
                                  .group_by(comment_votes.comment_id)
                                  .order_by('total_votes')
                                  .limit(10)
        return all

class candidate_votes(db.Model):
    __tablename__ = 'candidate_votes'
    candidate_id = Column(Integer, db.ForeignKey('candidates.cid'))
    user_id = Column(Integer, db.ForeignKey('users.uid'))
    votes = Column(Boolean)

    def vote_on(candidate_id, user_id):
        '''Upvote a comment, or take back an upvote'''
        cv = candidate_votes.query.filter_by(candidate_id=candidate_id, user_id=user_id)
        if cv.votes == 1:
            cv.votes = 0
        else:
            cv.votes = 1
        db.Session.commit()

class measure_votes(db.Model):
    __tablename__ = 'measure_votes'
    measure_id = Column(Integer, db.ForeignKey('measures.mid'))
    user_id = Column(Integer, db.ForeignKey('users.uid'))
    votes = Column(Boolean)

    def vote(candidate_id, user_id):
        '''Upvote a comment, or take back an upvote'''
        mv = measure_votes.query.filter_by(candidate_id=candidate_id, user_id=user_id)
        if mv.votes == 1:
            mv.votes = 0
        else:
            mv.votes = 1
        db.Session.commit()

class candidate_comments(db.Model):
    __tablename__ = 'candidate_comments'
    candidate_id = Column(Integer, db.ForeignKey('candidates.cid'))
    user_id = Column(Integer, db.ForeignKey('users.uid'))
    votes = Column(Boolean)

    def vote(self, candidate_id, user_id):
        if self.votes == 1:
            self.votes = 0
        else:
            self.votes = 1
        db.Session.commit()