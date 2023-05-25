from database import coll

from models.products import ProductView, ProductUpdate, ProductCreate

from uuid import UUID, uuid4
from typing import Optional
from utils.specification import Specification
from utils.products import Scraping


class ProductService:
    @staticmethod
    def list(params: Optional[str] = None) -> list[ProductView]:
        if params is None:
            return [ProductView(**document) for document in coll.find()]
        return [ProductView(**document) for document in coll.find({'title': {'$regex': params}})]

    @staticmethod
    def get(params: Specification) -> ProductView:
        return ProductView(**coll.find_one(params.is_satisfied()))
    
    @staticmethod
    def update(uuid: UUID, params: ProductUpdate) -> ProductView:
        params = params.dict()
        result = coll.find_one_and_update({'_id': uuid}, {'$set': params})
        return result
    
    @staticmethod
    def create_by_url_product(article: str) -> ProductView:
        result = Scraping()
        result = result.get_one_product(article)
        coll.insert_one(result)
        return ProductView(**result)

    @staticmethod
    def create(params: ProductCreate) -> ProductView:
        params = params.dict()
        params['_id'] = uuid4()
        coll.insert_one(params)
        return coll.find_one({'_id': params['_id']})

    @staticmethod
    def delete(uuid: UUID) -> None:
        coll.delete_one({'_id': uuid})
