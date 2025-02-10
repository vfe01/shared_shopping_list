class NoTagFoundException(Exception):
    def __init__(self):
        super().__init__("Couldn't find any tags.")