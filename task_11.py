class Dessert:
    def __init__(self, name: str  = "", calories: int | float = 0) -> None:
        self._name = name
        self._calories = calories

    def is_healthy(self) -> bool:
        if not isinstance(self.calories, (int, float)):
            return False
        if self.calories < 200:
            return True
        return False

    def is_delicious(self) -> bool:
        return True

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def calories(self) -> int|float:
        return self._calories

    @calories.setter
    def calories(self, calories: int | float) -> None:
        self._calories = calories
