from src.usecases.usecases import InputBoundary, InputData


class Controller:
    def __init__(self, input_boundary: InputBoundary) -> None:
        self.input_boundary = input_boundary

    def show(self, id: str) -> None:
        input_data = InputData(id)
        self.input_boundary.run(input_data)
