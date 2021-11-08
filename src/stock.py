import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class stock:
    # HACK: クラス変数使うべきか?
    url = 'http://www.kiraraten.jp/goods_list.html'
    header = ('商品番号', '商品カテゴリ', '商品名', '購入限定数', '在庫状況')


    def __init__(self) -> None:
        self.soup = None
        self.goods = []
        self.updated_time = None

        self.update()
        

    def update(self) -> None:
        self.soup = self._init_soup()

        self.goods = list(self._fetch_table())
        self.updated_time = datetime.strptime(self._fetch_updated_time(), '%Y年%m月%d日 %H:%M')


    def _fetch_table(self) -> iter:
        goods_table = self.soup.find('table', class_='goods_list').find('tbody')
        goods_rows = goods_table.find_all('tr') # HACK: find_all_nextでイテレータを作成する?

        def row_iter(goods_rows) -> iter:
            for row in goods_rows:
                # HACK: ...
                striped_row = [elm.get_text().strip() for elm in row.find_all('th')]
                yield striped_row
        
        return row_iter(goods_rows)


    @classmethod
    def _init_soup(cls) -> BeautifulSoup:
        html = requests.get(cls.url).content
        soup = BeautifulSoup(html, 'html.parser')

        return soup


    def _fetch_updated_time(self) -> str:
        text = self.soup.find(class_='goodslist_exp').find_all('p')[1].find('strong').get_text()
        date_str = re.search(r'[0-9]{4}年.*[0-9]{2}', text)
        
        # xxxx年xx月xx日 xx:xx
        return date_str.group()


        

class _goods_status:
    def __init__(self) -> None:
        pass 