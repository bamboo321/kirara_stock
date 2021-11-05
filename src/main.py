import csv

import stock


def main():
    s = stock.stock()
    output_csv(s.updated_time, s.goods)


def output_csv(updated_time, goods):
    with open('../data/' + updated_time.strftime('%Y%m%d_%H:%M:%S') + '.csv', 'w') as f:
    # with open('a', 'w') as f:
        header = ['商品番号', '商品カテゴリ', '商品名', '購入限定数', '在庫状況']
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(goods)


if __name__ == '__main__':
    main()