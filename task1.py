# TODO Напишите функцию для поиска индекса товара
from typing import List, Optional
def find_idx(item: str, items: List[str]) -> Optional[int]:
    for i, value in enumerate(items):
        if item == value:
            return i
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_idx(find_item, items_list)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
