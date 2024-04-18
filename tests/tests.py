from src.widget import format_date, mask_info

masked_info = mask_info(input())
print(masked_info)

date_str = input()
formatted_date = format_date(date_str)
print(formatted_date)
