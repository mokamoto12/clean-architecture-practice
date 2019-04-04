class ResourceNotFound(Exception):
    def __init__(self, resource: str, message: str) -> None:
        self.resource = resource
        self.message = message
