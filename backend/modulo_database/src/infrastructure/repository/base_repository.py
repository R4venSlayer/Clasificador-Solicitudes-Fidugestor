
class BaseRepository:
    model = None

    def create(self, **data):
        return self.model.objects.create(**data)

    def bulk_create(self, objs: list):
        self.model.objects.bulk_create(objs)

    def get(self, **filters):
        return self.model.objects.get(**filters)

    def filter(self, **filters):
        return self.model.objects.filter(**filters)

    def update_by_filters(self, filters: dict, data: dict) -> int:
        return self.model.objects.filter(**filters).update(**data)

    def exists(self, **filters) -> bool:
        return self.model.objects.filter(**filters).exists()
