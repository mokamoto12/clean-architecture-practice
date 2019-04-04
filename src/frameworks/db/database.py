from typing import Dict, Optional

from src.entities.entities import Entities
from src.usecases.exceptions import ResourceNotFound
from src.usecases.usecases import DataAccessInterface


class DataBase:
    data: Dict[str, Dict[str, str]] = {
        'UTC': {
            'id': 'UTC',
            'offset': '0'
        },
        'JST': {
            'id': 'JST',
            'offset': '9'
        }
    }

    def query(self, query: str) -> Optional[Dict[str, str]]:
        if query not in self.data:
            return None
        return self.data[query]


class DataAccess(DataAccessInterface):
    __data_base: DataBase

    def __init__(self, data_base: DataBase) -> None:
        self.__data_base = data_base

    def find(self, eid: str) -> Entities:
        d = self.__data_base.query(eid)
        if d is None:
            raise ResourceNotFound(eid, '{} not found.'.format(eid))
        return Entities(d['id'], int(d['offset']))
