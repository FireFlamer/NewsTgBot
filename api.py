import requests as req
from constants import API_KEY

class NewsAPI:
    def __init__(self):
        self._api_key = API_KEY
        self._base_url = 'https://newsapi.org/v2/everything'

    def get_news_with_category(self, category: str) -> str:
        response = req.get(url=self._base_url, params={'apiKey': self._api_key, 'q': category, 'language': 'ru', 'pageSize': 7})

        if response.status_code == 200:
            news = response.json()       
        else:
            response.raise_for_status()

        if news['articles']:
            return self._news_processing(news) 
        else:
            return 'Ничего не найдено по вашему запросу'



    @staticmethod
    def _news_processing(news_data: dict) -> str:
        news_info = news_data['articles']
        news_str = 'Вот что мне удалось найти по вашему запросу:\n\n'

        for news in news_info:
            news_str += f"Автор: {news['author']}\n{news['title']}:\n{'—' * 35}\nОписание: {news['description']}\n{'—' * 35}\nСсылка: {news['url']}\n\n\n"
        
        return news_str
    
news = NewsAPI()


        