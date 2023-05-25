from abc import abstractmethod
from dataclasses import dataclass
from uuid import UUID


class Specification:
    @abstractmethod
    def is_satisfied(self) -> bool:
        pass

    def __and__(self, other: 'Specification') -> 'AndSpecification':
        return AndSpecification(self, other)
    
    def __or__(self, other: 'Specification') -> 'OrSpecification':
        return OrSpecification(self, other)
    
    def __invert__(self) -> 'NotSpecification':
        return NotSpecification(self)
    

@dataclass(frozen=True)
class AndSpecification(Specification):
    first: Specification
    second: Specification

    def is_satisfied(self) -> bool:
        return self.first.is_satisfied() and self.second.is_satisfied()
    

@dataclass(frozen=True)
class OrSpecification(Specification):
    first: Specification
    second: Specification

    def is_satisfied(self) -> bool:
        return self.first.is_satisfied() or self.second.is_satisfied()
    

@dataclass(frozen=True)
class NotSpecification(Specification):
    spec: Specification

    def is_satisfied(self) -> bool:
        return not self.spec.is_satisfied()


class ProductUUIDSpecification(Specification):
    def __init__(self, uuid: UUID):
        self.uuid: UUID = uuid

    def is_satisfied(self) -> dict:
        return {'_id': self.uuid}


class ProductNameSpecification(Specification):
    def __init__(self, name: str):
        self.name: str = name

    def is_satisfied(self) -> bool:
        return {'title': '/' + self.name + '/'}
