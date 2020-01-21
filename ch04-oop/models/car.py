import abc

class Car(abc.ABC):

    def __init__(self, model_name: str, engine_type: str, cylinders: int, base_price: float):
        self.model_name: str = model_name
        self.engine_type: str = engine_type
        self.cylinders: int = cylinders
        self.base_price: float = base_price

    def drive(self) -> None:
        print(f"Car: the {self.model_name} goes vroom!")

    @abc.abstractmethod
    def refuel(self) -> None:
        pass

    @property
    def is_electric(self) -> bool:
        return self.engine_type == 'electric'