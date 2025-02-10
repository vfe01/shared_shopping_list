class AmbiguousIdentifierException(Exception):
    def __init__(self):
        super().__init__("Couldn't find a single unique tag given the attribute value pairs")