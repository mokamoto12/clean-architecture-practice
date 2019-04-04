from typing import Dict, Optional

import pytest

from src.entities.entities import Entities
from src.usecases.usecases import DataAccessInterface, OutputBoundary, OutputData, InputBoundary, UseCaseInteractor, \
    InputData


class InMemoryDataAccess(DataAccessInterface):
    table: Dict[str, Entities] = {
        'UTC': Entities('UTC', 0),
        'JST': Entities('JST', 9)
    }

    def find(self, eid: str) -> Entities:
        return self.table[eid]


class BufferedOutputBoundary(OutputBoundary):
    buffer: OutputData

    def print(self, output_data: OutputData) -> None:
        self.buffer = output_data


@pytest.fixture(params=['UTC', 'JST'])
def input_data(request) -> InputData:
    return InputData(request.param)


@pytest.fixture()
def data_access_interface() -> InMemoryDataAccess:
    return InMemoryDataAccess()


@pytest.fixture()
def output_boundary() -> BufferedOutputBoundary:
    return BufferedOutputBoundary()


@pytest.fixture()
def input_boundary(data_access_interface, output_boundary) -> InputBoundary:
    return UseCaseInteractor(output_boundary, data_access_interface)
