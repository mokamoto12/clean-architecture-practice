from src.frameworks.db.database import DataAccess, DataBase
from src.frameworks.ui.view import ViewImpl
from src.interfaceadapters.controllers.controller import Controller
from src.interfaceadapters.presenters.presenter import Presenter, View
from src.usecases.usecases import (DataAccessInterface, InputBoundary,
                                   OutputBoundary, UseCaseInteractor)


def data_access_interface() -> DataAccessInterface:
    return DataAccess(DataBase())


def controller() -> [Controller, View]:
    view = ViewImpl()
    output_boundary: OutputBoundary = Presenter(view)
    input_boundary: InputBoundary = UseCaseInteractor(output_boundary,
                                                      data_access_interface())
    return Controller(input_boundary), view
