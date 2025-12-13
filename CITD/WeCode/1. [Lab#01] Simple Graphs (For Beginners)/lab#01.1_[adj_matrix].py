"""Cài đặt một số thao tác cơ bản trên một đồ thị hữu hướng.

INPUT:

- Dòng đầu tiên chứa 03 số v, e và n, đây lần lượt là số đỉnh, số cạnh của đồ thị cùng với số thao tác xử lý.
- e dòng tiếp theo, mỗi dòng chứa 02 số u và i, thể hiện việc có một cạnh nối từ đỉnh thứ u sang đỉnh thứ i trong đồ thị (thứ tự các đỉnh được đánh số từ 1...v)
- n dòng tiếp theo, mỗi dòng tương ứng với một thao tác xử lý các thao tác có cú pháp như sau:
-- Thao tác kiểm tra tính kề của 02 đỉnh, dòng này bắt đầu bằng số 1, theo sau là 02 số u và i.
-- Thao tác tìm kiếm đỉnh lân cận của 01 đỉnh, dòng này bắt đầu bằng số 2, theo sau là số u.

OUTPUT:

- Ứng với thao tác kiểm tra tính kề của 02 đỉnh, xuất ra màn hình chuỗi "TRUE" nếu đỉnh thứ u kề với đỉnh thứ i. Nếu đỉnh thứ u không kề với đỉnh thứ i xuất ra chuỗi "FALSE".
- Ứng với thao tác tìm kiếm đỉnh lân cận của 01 đỉnh, xuất ra màn hình trên cùng một dòng thứ tự của các đỉnh kề với đỉnh thứ u, các đỉnh xuất theo thứ tự tăng dần, cách nhau bởi khoảng trắng.

Nếu không có đỉnh nào kề với đỉnh thứ u xuất ra chuỗi "NONE".
"""

import sys
from bisect import bisect_left


def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    iterator = iter(input_data)

    try:
        v = int(next(iterator))
        e = int(next(iterator))
        n = int(next(iterator))
    except StopIteration:
        return

    adj_matrix: dict[int, list[int]] = {}

    for _ in range(e):
        u = int(next(iterator))
        i = int(next(iterator))

        if u not in adj_matrix:
            adj_matrix[u] = []
        adj_matrix[u].append(i)

    for u in adj_matrix:
        adj_matrix[u] = sorted(list(set(adj_matrix[u])))

    output = []

    for _ in range(n):
        type_op = int(next(iterator))

        if type_op == 1:
            u = int(next(iterator))
            i = int(next(iterator))

            if u in adj_matrix:
                neighbors = adj_matrix[u]
                index = bisect_left(neighbors, i)

                if index < len(neighbors) and neighbors[index] == i:
                    output.append("TRUE")
                else:
                    output.append("FALSE")
            else:
                output.append("FALSE")

        elif type_op == 2:
            u = int(next(iterator))

            if u in adj_matrix and adj_matrix[u]:
                output.append(" ".join(map(str, adj_matrix[u])))
            else:
                output.append("NONE")

    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
