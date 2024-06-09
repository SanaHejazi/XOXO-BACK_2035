from  sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String
import main
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///MyDatabase.db")
base = declarative_base()
sessionlocal =sessionmaker(engine)


def get_db():
  session = sessionlocal()
  try:
      yield session
  finally:
      session.close()





class PlayersInfo_db(base):
    __tablename__='PlayersInfo_db'

    _id=Column('id',Integer,unique=True ,primary_key=True)
    name = Column('name', String)
    status =Column('status',String)


#player1 = PlayersInfo_db()
#player1.name="sana"
#player1.status="Win"



#with Session(engine) as session:

#Add
    #session.add(player1)
#Delete
    #query = session.query(PlayersInfo_db).filter(PlayersInfo_db.name=='sana').all()
    #session.delete(query)
#Update
    #session.query(PlayersInfo_db).filter(PlayersInfo_db.name=="Ali").update({'name':"REZA"})
    #session.commit()


