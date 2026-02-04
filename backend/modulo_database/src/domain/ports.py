# application/contracts/repository_contracts.py
from typing import Protocol, Any, Iterable


class CreateRepository(Protocol):
    def create(self, **data: Any):
        ...


class BulkCreateRepository(Protocol):
    def bulk_create(self, objs: Iterable[Any]):
        ...


class QueryRepository(Protocol):
    def get(self, **filters):
        ...

    def filter(self, **filters):
        ...

    def exists(self, **filters) -> bool:
        ...


class UpdateRepository(Protocol):
    def update_by_filters(self, filters: dict, data: dict) -> int:
        ...
