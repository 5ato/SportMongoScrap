from pydantic import Field

from uuid import uuid4


class ProductField:
    title = Field(
        title='Product Name',
        min_length=1
    )

    price = Field(
        title='Price Product',
        description='Uzbek currency is used',
        ge=0
    )

    image = Field(
        title='Produce Image',
        description='Url link image',
        example='https://images.uzum.uz/cdkvcurb3ho5lmurjg80/original.jpg'
    )

    rating = Field(
        title='Product rating',
        default=0,
        ge=0, le=5
    )
