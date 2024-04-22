from src.widget import format_date, mask_info
from src.processing import filter_by_state_and_date, sort_by_date

masked_info = mask_info(input())
print(masked_info)

date_str = input()
formatted_date = format_date(date_str)
print(formatted_date)

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_data_executed = filter_by_state_and_date(data)
print(filtered_data_executed)

filtered_data_canceled = filter_by_state_and_date(data, state='CANCELED')
print(filtered_data_canceled)

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

sorted_data_descending = sort_by_date(data)
print(sorted_data_descending)
