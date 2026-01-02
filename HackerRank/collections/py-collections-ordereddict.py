from collections import OrderedDict

if __name__ == "__main__":
    N = int(input())
    ordered_dic = OrderedDict()
    for _ in range(N):
        s = input()
        item_name, net_price = s.rsplit(" ", 1)
        net_price = int(net_price)

        if item_name in ordered_dic.keys():
            ordered_dic[item_name] += net_price
        else:
            ordered_dic[item_name] = net_price

    for key, value in ordered_dic.items():
        print(f"{key} {value}")
