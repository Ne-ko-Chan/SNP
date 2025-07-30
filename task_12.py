from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(
        self, name: str = "", calories: int | float = 0, flavor: str = ""
    ) -> None:
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self) -> str:
        return self._flavor

    @flavor.setter
    def flavor(self, flavor: str) -> None:
        self._flavor = flavor

    def is_delicious(self) -> bool:
        return False if self.flavor == "black licorice" else True
