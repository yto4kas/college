from src.database.models import BaseModelModify
from src.database.db_manager import db

class Resolver:

    def __init__(self, model: type[BaseModelModify]):
        self.model: type[BaseModelModify] = model
        self.model_name = self.model.__name__

    def get(self, object_id: int) -> BaseModelModify:
        res = db.execute(
            query=f'select * from {self.model_name} where id=(?)',
            args=(object_id,)
        )
        return None if not res else self._get_model(res)

    def create(self, model: BaseModelModify) -> None:
        dump = model.model_dump()
        if dump.__contains__("id"):
            dump.pop("id")
        fields = len(dump)

        db.execute(
            query=f"insert into {self.model_name}({array_to_str(dump.keys())}) values({get_values_str(fields)})",
            args=(tuple(dump.values()))
        )

    def update(self, object_id: int, new_data: BaseModelModify) -> None:
        dump = new_data.model_dump()
        if dump.__contains__("id"):
            dump.pop("id")
        fields = len(dump)

        args = list(dump.values())
        args.append(object_id)
        return db.execute(
            query=f'update {self.model_name} set ({array_to_str(dump.keys())}) = ({get_values_str(fields)}) where id=(?)',
            args=(tuple(args)))

    def get_all(self) -> list[BaseModelModify]:
        res_list = db.execute(query=f"select * from {self.model_name}", many=True)
        models = []
        if res_list:
            for res in res_list:
                models.append(self._get_model(res))

        return models

    def remove(self, object_id: int) -> None:
        return db.execute(f'delete from {self.model_name} where id=(?)', args=(object_id,))

    def _get_model(self, res: tuple):
        fields = tuple(self.model.model_fields.keys())
        args = {}
        for i in range(0, len(res)):
            args[fields[i]] = res[i]

        return self.model(**args)

def get_values_str(amount: int) -> str:
    values: str = "?"
    for i in range(1, amount):
        values += ", ?"
    return values

def array_to_str(array) -> str:
    return ','.join(map(str, array))
