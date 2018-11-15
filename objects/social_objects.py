from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from db import db


# Races in Play
# Governor | Senate | House | Proposals

class ballots(db.Model):
    __tablename__ = 'ballots'
    uid = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    election_date = Column(DateTime)
    election_type = Column(Integer, db.ForeignKey('elections.uid')) # ADD THIS Look UP table
    sections = Column(Text) # THIS SHOULD BE A JSON STRING -- Possibly Re-Think This


    @property
    def __repr__(self):
        return '<Ballot %r>' % self.name

class candidates(db.Model):
    __tablename__ = 'candidates'
    cid = Column(Integer, primary_key=True)
    ballot_id = Column(Integer, db.ForeignKey('ballot.uid'))
    # party_id = Column(Integer, db.ForeignKey('parties.uid')) # Add this
    status = Column(Boolean) # Does this need more?
    desc = Column(Text)
    candidate_name = Column(String(100), nullable=False)
    bio = Column(Text, nullable=False)
    policies = Column(Text, nullable=False)

    @property
    def __repr__(self):
        return '<Candidate %r>' % self.candidate_name

class measures(db.Model): #analogous to candidates
    __tablename__ = 'measures'
    mid = Column(Integer, primary_key=True)
    desc = Column(Text)

class races(db.Model): 
    __tablename__ = 'races'
    rid = Column(Integer, primary_key=True)
    desc = Column(Text) # governor, senator, etc.
    duties = Column(Text) # what the governor does (duties/responsibilities)
    cid = Column(Integer, db.ForeignKey('candidates.cid'))
    bid = Column(Integer, db.ForeignKey('ballots.uid'))

class ballot_measures(db.Model): # analagous to races
    bmid = Column(Integer, primary_key=True)
    desc = Column(Text) # Prop 1, Prop 2
    colloq_name = Column(String(150))
    mid = Column(Integer, db.ForeignKey('measures.mid'))
    bid = Column(Integer, db.ForeignKey('ballots.uid'))