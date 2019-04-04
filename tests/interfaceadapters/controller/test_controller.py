from unittest.mock import MagicMock

import pytest

from src.interfaceadapters.controllers.controller import Controller
from src.usecases.usecases import InputBoundary, InputData


@pytest.fixture()
def input_boundary() -> InputBoundary:
    return MagicMock()


class TestController:
    @pytest.mark.parametrize('input_param', ['UTC', 'JST'])
    def test_show(self, input_param: str, input_boundary: MagicMock):
        c = Controller(input_boundary)
        c.show(input_param)

        input_boundary.run.assert_called_once_with(InputData(input_param))
