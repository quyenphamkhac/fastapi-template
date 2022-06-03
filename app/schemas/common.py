from email import message
from typing import Optional, TypeVar, Generic
from numpy import number
from pydantic.generics import GenericModel

from pydantic import BaseModel

T = TypeVar('T')


class ResponseBaseModel(BaseModel):
    code: int = 500
    message: str = ''

    def return_with_code(self, code: int, message: str):
        self.code = code
        self.message = message
        return self

    def return_success(self, message: str):
        self.code = 200
        self.message = message
        return self


class ResponseModel(ResponseBaseModel):
    data: Optional[T] = None

    def return_with_code(self, code: int, message: str, data: T):
        self.code = code
        self.message = message
        self.data = data
        return self

    def return_success(self, data: T):
        self.code = 200
        self.message = 'Success'
        self.data = data
        return self
