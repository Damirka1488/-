from typing import Dict, List, Optional


def filter_by_state_and_date(
    list_of_dicts: List[Dict], state: str = "EXECUTED", date: Optional[str] = None
) -> (List[Dict]):
    """Фильтрует список словарей по состоянию и дате."""
    filtered_list = []
    for d in list_of_dicts:
        if d.get("state") == state:
            if date:
                if d.get("date")[:10] == date[:10]:
                    filtered_list.append(d)
            else:
                filtered_list.append(d)
    return filtered_list


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словарей по убыванию даты."""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
