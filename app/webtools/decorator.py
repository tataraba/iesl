import logging
from datetime import datetime
from functools import wraps
from typing import Annotated, Type

from fastapi import Form, Request

# from app import models
from app.models.league_data.season import SeasonCreate

logger = logging.getLogger(__name__)
season = SeasonCreate(
    name="test",
    description="test",
    start_date=datetime.now(),
    end_date=datetime.now(),
)


def form_it(model: SeasonCreate):

    def inner(func):

        model_fields = model.dict().keys()
        params = [f"{f}=Annotated[str, Form()]" for f in model_fields]
        print(params)
        @wraps(func)
        def add_model_to_function_args(*args, **kwargs):
            print("inside the add model function")
            return(func(*args, *params, **kwargs, ))
        return add_model_to_function_args
    return inner





if __name__ == "__main__":

    @form_it({"model": "season"})
    def hello(name: str, **kwargs):
        print(f"hello {name} and {kwargs}")

    hello(name="Mario")



