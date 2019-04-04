from datetime import datetime

import pytest

from src.entities.entities import Entities


class TestEntities:
    @pytest.mark.parametrize('eid,offset', [('UTC', 0), ('JST', 9)])
    def test_dance_jst(self, eid: str, offset: int):
        entities = Entities(eid, offset)
        t: datetime = entities.dance()
        assert t.tzname() == eid
        assert t.utcoffset().seconds == offset * 3600
