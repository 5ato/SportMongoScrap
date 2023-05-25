from requests import Session

from uuid import uuid4
from typing import Optional
from fake_useragent import UserAgent


class Scraping:
    def __init__(self, url: Optional[str] = None) -> None:
        self.url: str = url
        self.headers: dict = {
            'user-agent': UserAgent().random,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        }
    
    def __get_response(self, url: Optional[str] = None, params: dict = None):
        with Session() as session:
            with session.get(url if url else self.url, headers=self.headers, params=params) as response:
                return response
        
    def get_one_product(self, article: str):
        response = self.__get_response('https://api.uzum.uz/api/v2/product/' + article)
        data = response.json()['payload']['data']
        return {
                    '_id': uuid4(),
                    'title': data['title'],
                    'price': data['skuList'][0]['purchasePrice'],
                    'image': data['photos'][0]['photo']['540']['high'],
                    'rating': data['rating']
                }
            
    def get_default_data(self):
        response = self.__get_response('https://api.uzum.uz/api/v2/product/414876/similar?size=25')
        count = 0
        result = []
        for item in response.json():
            if count == 5:
                yield result
                result, count = [], 0
            else:
                result.append({
                    '_id': uuid4(),
                    'title': item['title'],
                    'price': item['fullPrice'],
                    'image': item['image'],
                    'rating': item['rating']
                })
                count += 1


if __name__ == '__main__':
    s = Scraping(None)
    print(s.get_one_product('115249'))
