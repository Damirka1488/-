from src.masks import mask_info, format_date

masked_info = mask_info(input())
print(masked_info)

date_str = "2018-07-11T02:26:18.671407"
formatted_date = format_date(date_str)
print(formatted_date)