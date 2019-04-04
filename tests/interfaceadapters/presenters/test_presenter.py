from datetime import datetime
from unittest.mock import MagicMock

import pytest

from src.interfaceadapters.presenters.presenter import View, Presenter, ViewModel
from src.usecases.usecases import OutputData


@pytest.fixture()
def view() -> View:
    return MagicMock()


class TestPresenter:
    @pytest.mark.parametrize(('eid', 'date'), [('UTC', datetime.now())])
    def test_print(self, eid: str, date: datetime, view: MagicMock):
        p = Presenter(view)
        p.print(OutputData(eid, date))

        view.print.assert_called_once_with(ViewModel(eid, date.isoformat()))
