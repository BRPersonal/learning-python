class Greeting:
    def __init__(self, name: str) -> None:
        self.name = name

    def __call__(self, greeting: str) -> str:
        return f"{greeting}, {self.name}"
