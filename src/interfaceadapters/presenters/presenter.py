from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.usecases.usecases import OutputBoundary, OutputData


@dataclass
class ViewModel:
    id: str
    date: str


class View(ABC):
    @abstractmethod
    def buffer(self) -> str:
        pass

    @abstractmethod
    def print(self, view_model: ViewModel) -> None:
        pass


class Presenter(OutputBoundary):
    def __init__(self, view: View) -> None:
        self.view = view

    def print(self, output_data: OutputData) -> None:
        self.view.print(
            ViewModel(output_data.id, output_data.date.isoformat()))
