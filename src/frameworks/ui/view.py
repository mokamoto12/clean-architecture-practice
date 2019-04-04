import json
from dataclasses import asdict
from typing import Callable, Optional

from src.interfaceadapters.presenters.presenter import View, ViewModel


class ViewImpl(View):
    buffer: Optional[Callable[[], str]]

    def __init__(self) -> None:
        pass

    def print(self, view_model: ViewModel) -> None:
        self.buffer = lambda: json.dumps(asdict(view_model))
