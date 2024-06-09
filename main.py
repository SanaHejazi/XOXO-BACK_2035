from fastapi import FastAPI, Depends
from database.CreatePlayer import Create_Player,UserINFO
from database.db import get_db
app=FastAPI()
from database import db
from database.db import engine

db.base.metadata.create_all(engine)






@app.get('/')
def Hello():
    return {"HEllo"}

@app.post('/CreateUser')
def CreatUser(UserInfo: UserINFO , db=Depends(get_db)):
  return Create_Player(db,UserInfo)