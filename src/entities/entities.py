from datetime import datetime, timedelta, timezone


class Entities:
    __eid: str
    __offset: int

    def __init__(self, eid: str, offset: int) -> None:
        self.__eid = eid
        self.__offset = offset

    @property
    def id(self) -> str:
        return self.__eid

    def dance(self) -> datetime:
        return datetime.now(
            timezone(timedelta(hours=self.__offset), self.__eid))
