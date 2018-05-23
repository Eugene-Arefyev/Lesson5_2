
Для списка длиной в 10 элементов потребуется сделать 9 действий для того, чтобы поменять порядок.

например

1->2->3->4->5->6->7->8->9->10->null
10->1->2->3->4->5->6->7->8->9->null
10->9->1->2->3->4->5->6->7->8->null
....
10->9->8->7->6->5->4->3->2->1->null

Сложность алгоритма N-1, где N - это кол-во элементов

В случае с массивом получится быстрее, потому что надо поменять только значения внутри ячеек

Алгоритм следующий. Надо менять симметричные пары значений. (первый/последний, второй/предпоследний и тд)

1 2 3 4 5 6 7 8 9 10
10 2 3 4 5 6 7 8 9 1
10 9 3 4 5 6 7 8 2 1
...
10 9 8 7 6 5 4 3 2 1

Сложность тут N/2. Явно лучше
