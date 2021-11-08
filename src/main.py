import csv

import stock
import writer


def main():
    s = stock.stock()
    # output_csv(s)

    # w = writer.create_writer('csv')
    w = writer.csv_writer(s)
    w.write()


def output_csv(stock) -> None:
    with open('../data/' + stock.updated_time.strftime('%Y%m%d_%H:%M:%S') + '.csv', 'w') as f:
    # with open('a', 'w') as f:
        header = ('商品番号', '商品カテゴリ', '商品名', '購入限定数', '在庫状況')
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(stock.goods)


if __name__ == '__main__':
    main()