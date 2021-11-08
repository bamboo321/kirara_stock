import stock
import writer


def main():
    s = stock.stock()

    w = writer.create_writer(s)
    csv_w = w.create(writer.csv_writer)

    csv_w.write()


if __name__ == '__main__':
    main()
