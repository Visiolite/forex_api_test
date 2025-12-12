#--------------------------------------------------------------------------------- location
# webapi/service/service.py

#--------------------------------------------------------------------------------- Description
# service

#--------------------------------------------------------------------------------- Import
from myLib.model import model_output
from myLib.utils import config, debug, sort
from myLib.data_orm import Data_Orm as Logic

#--------------------------------------------------------------------------------- Variable
database = config.get("general", {}).get("database_management", {})

#--------------------------------------------------------------------------------- service
class Service:
    #-------------------------- [Init]
    def __init__(self, model) : 
        self.model = model
        self.logic = Logic(database=database)

    #-------------------------- [Add]
    def add(self, item) -> model_output:
        item = item.dict()
        if 'id' in item : del item['id']
        if 'date' in item : del item['date']
        item = self.model(**item)
        output:model_output = self.logic.add(model=self.model, item=item)
        return output

    #-------------------------- [Items]
    def items(self, **filters) -> model_output:
        output:model_output = self.logic.items(model=self.model, **filters)
        if output.status : 
            data = []
            for item in output.data : data.append(item.toDict())
            output.data = data
        return output
    
    #-------------------------- [Update]
    def update(self, item) -> model_output:
        return self.logic.update(model=self.model, item=self.model(**item.dict()))

    #-------------------------- [Delete]
    def delete(self, id:int) -> model_output:
        return self.logic.delete(model=self.model, id=id)

    #-------------------------- [Enable]
    def enable(self, id:int) -> model_output:
        return self.logic.enable(model=self.model, id=id)

    #-------------------------- [Disable]
    def disable(self, id:int) -> model_output:
        return self.logic.disable(model=self.model, id=id)

    #-------------------------- [Status]
    def status(self, id:int) -> model_output:
        return self.logic.status(model=self.model, id=id)
    
    #-------------------------- [Dead]
    def dead(self, id:int) -> model_output:
        return self.logic.dead(model=self.model, id=id)