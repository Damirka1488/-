def filter_by_state_and_date(list_of_dicts, state="EXECUTED", date=None):
    """Фильтрует список словарей по состоянию и дате."""

    filtered_list = []
    for d in list_of_dicts:
        if d.get('state') == state:
            if date:
                if d.get('date')[:10] == date[:10]:
                    filtered_list.append(d)
            else:
                filtered_list.append(d)
    return filtered_list


def sort_by_date(data, reverse=True):
    """Сортирует список словарей по убыванию даты."""
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
