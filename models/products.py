from pydantic import BaseModel, validator

from typing import Optional

from .fields.products import ProductField


class BaseProduct(BaseModel):
    title: str = ProductField.title
    price: int = ProductField.price
    image: str = ProductField.image
    rating: int = ProductField.rating

    @validator('image')
    def image_url_validate(cls, value: str):
        temp = value.split('/')
        if len(temp) != 5:
            raise ValueError('Incorrect parameters for the image')
        if 'jpg' not in temp[-1].split('.'):
            raise ValueError('Wrong format in link')
        return value


class ProductView(BaseProduct):
    ...


class ProductUpdate(BaseProduct):
    title: Optional[str] = ProductField.title
    price: Optional[int] = ProductField.price
    image: Optional[str] = ProductField.image
    rating: Optional[int] = ProductField.rating


class ProductCreate(BaseProduct):
    pass
    