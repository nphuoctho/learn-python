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


def check_adjacency(adj_matrix: list[list[int]], u: int, i: int):
    """Kiểm tra xem đỉnh u có kề với đỉnh i không."""
    if i in adj_matrix[u]:
        print("TRUE")
    else:
        print("FALSE")


def find_neighbors(adj_matrix: list[list[int]], u: int):
    """Tìm và in ra các đỉnh kề của đỉnh u."""
    neighbors = adj_matrix[u]

    if neighbors:
        print(*sorted(neighbors))
    else:
        print("NONE")


if __name__ == "__main__":
    v, e, n = map(int, input().split())

    adj_matrix = [[] for _ in range(v + 1)]

    edges_read = 0
    while edges_read < e:
        line = input()
        if not line.strip():
            continue

        u, i = map(int, line.split())
        adj_matrix[u].append(i)
        edges_read += 1

    ops_read = 0
    while ops_read < n:
        line = input()
        if not line.strip():
            continue

        parts = list(map(int, line.split()))
        c = parts[0]

        if c == 1 and len(parts) == 3:
            _, u, i = parts

            check_adjacency(adj_matrix, u, i)
        elif c == 2 and len(parts) == 2:
            _, u = parts

            find_neighbors(adj_matrix, u)

        ops_read += 1
