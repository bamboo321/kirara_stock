import csv
from stock import stock


# FIXME: stockクラスを引数にとるようにする?
def create_writer(writertype: str = "csv") -> object:
    type = {
        'csv': csv_writer,
        # 'influxdb': influxdbwriter,
    }

    return type[writertype](stock)


class csv_writer:
    def __init__(self, stock: stock) -> None:
        self.stock = stock
        self.dict = '../data/'
        self.filename = stock.updated_time.strftime('%Y%m%d_%H:%M:%S') + '.csv'


    def write(self):
        with open(self.dict + self.filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.stock.header)
            writer.writerows(self.stock.goods)