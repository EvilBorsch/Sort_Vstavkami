import random  # чтобы можно было рандомит

arr = []  # объявил массив


def index_min(i, arr):  # функция которая находит индекс минимального элемента
    index = i
    for i in range(i, arr.__len__()):  # веду поиск от i-того элемента, до конца массива
        if arr[i] < arr[index]:
            index = i
    return index


for i in range(0, 10):  # заполняю массив случайными числами(чтобы удобней было)
    arr.append(random.randint(1, 100))

print("Массив заполненный рандомной хуйней: ", arr)
for i in range(0, arr.__len__()):
    min_index = index_min(i,arr)  # нахожу индекс минимального элемента в промежутке от i того элемента до конца массива
    arr[i], arr[min_index] = arr[min_index], arr[i]  # меняю местами i-тый элемент и минимальный элемент
print(f"Готово,лол,кек,чебурек: ", arr)
