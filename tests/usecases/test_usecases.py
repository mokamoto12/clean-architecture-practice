from src.usecases.usecases import DataAccessInterface, UseCaseInteractor, InputData, OutputData
from tests.usecases.conftest import BufferedOutputBoundary


class TestUseCaseInteractor:
    def test_run(self, input_data: InputData, output_boundary: BufferedOutputBoundary, data_access_interface: DataAccessInterface):
        u = UseCaseInteractor(output_boundary, data_access_interface)
        u.run(input_data)

        assert isinstance(output_boundary.buffer, OutputData)
        assert output_boundary.buffer.id == input_data.id
