from src.widget import get_date, mask_account_card

account_card: str = input()
start_date: str = input()
print(mask_account_card(account_card))
print(get_date(start_date))
