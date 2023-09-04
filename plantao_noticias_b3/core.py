import datetime
import requests

from .utils import format_datestr_to_url


class NewsB3API:
    MAIN_URL = 'https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/'

    @staticmethod
    def get_url(start: str = '', end: str = '') -> str:
        start = format_datestr_to_url(start)
        end = format_datestr_to_url(end)

        return NewsB3API.MAIN_URL + (
            f'ListarTitulosNoticias?agencia=18&palavra=&dataInicial={start}&dataFinal={end}'
        )
    
    @staticmethod
    def request_url(start: str = '', end: str = '') -> requests.Response:
        url = NewsB3API.get_url(start, end)
        return requests.get(url)

    @staticmethod
    def get_all_news(start: str = '', end: str = '') -> list:
        response = NewsB3API.request_url(start, end)
        if response.status_code == 200:
            return [new['NwsMsg'] for new in response.json()]
        else:
            return response.json()
        

class ProventosReader:
    ...
    
        
def proventos(start: str = '', end: str = '') -> list:
    news = NewsB3API.get_all_news(start, end)
    return [new for new in news if 'PROVENTOS DOS EMISSORES COTADOS NA FORMA "EX"' in new['headline']]