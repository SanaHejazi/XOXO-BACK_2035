from sqlalchemy.orm.session import Session
from database.db import PlayersInfo_db,get_db,engine
from pydantic import BaseModel
from enum import Enum



class typeStatus(str, Enum):
    Win='Win'
    Lose='Lose'

class UserINFO(BaseModel):
    name: str='Player Name'
    status: typeStatus







def Create_Player(db:Session , Information: UserINFO):
    Player = PlayersInfo_db()
    Player.name=Information.name
    Player.status=Information.status

    db.add(Player)
    db.commit()
    db.refresh(Player)