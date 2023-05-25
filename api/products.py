from fastapi import APIRouter

from models.products import ProductView, ProductUpdate, ProductCreate
from services.products import ProductService

from typing import Optional
from uuid import UUID
from utils.specification import ProductUUIDSpecification


router = APIRouter(
    prefix='/products'
)


@router.get(
    path='/products-list',
    response_model=list[ProductView],
    description='List all the available persons'
)
def list_products(params: Optional[str] = None) -> list[ProductView]:
    return ProductService.list(params)


@router.get(
    path='/product',
    response_model=ProductView,
    description='Get one product by uuid'
)
def get_product(parametrs: UUID) -> ProductView:
    return ProductService.get(ProductUUIDSpecification(parametrs))


@router.patch(
    path='/product-update',
    response_model=ProductView,
    description='Update product',
)
def update_product(uuid: UUID, params: ProductUpdate) -> ProductView:
    return ProductService.update(uuid, params)


@router.post(
    path='create-product-by-article',
    response_model=ProductView,
    description='Inserts data into the database through the article'
)
def create_product(article: int) -> ProductView:
    return ProductService.create_by_url_product(str(article))


@router.post(
    path='create-product',
    response_model=ProductView,
    description='Create product',
)
def create_product(params: ProductCreate) -> ProductView:
    return ProductService.create(params)


@router.delete(
    path='/delete-product',
    description='Delete product'
)
def delete_product(uuid: UUID) -> None:
    return ProductService.delete(uuid)
