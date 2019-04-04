from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from src.entities.entities import Entities


class DataAccessInterface(ABC):
    @abstractmethod
    def find(self, eid: str) -> Entities:
        pass


@dataclass
class InputData:
    id: str


class InputBoundary(ABC):
    @abstractmethod
    def run(self, input_data: InputData) -> None:
        pass


@dataclass
class OutputData:
    id: str
    date: datetime


class OutputBoundary(ABC):
    @abstractmethod
    def print(self, output_data: OutputData) -> None:
        pass


class UseCaseInteractor(InputBoundary):
    def __init__(self, output_boundary: OutputBoundary,
                 data_access: DataAccessInterface) -> None:
        self.output_boundary = output_boundary
        self.data_access = data_access

    def run(self, input_data: InputData) -> None:
        e: Entities = self.data_access.find(input_data.id)

        output_data = OutputData(e.id, e.dance())

        self.output_boundary.print(output_data)
