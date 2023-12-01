#!/bin/python3
def calculate_cashback(total_deposit, total_withdrawal, bonus_received_deposit):
    try:
        total_deposit = float(total_deposit)
        total_withdrawal = float(total_withdrawal)
        bonus_received_deposit = float(bonus_received_deposit)

        total_deposit_excluding_bonus = total_deposit - bonus_received_deposit
        difference = total_deposit_excluding_bonus - total_withdrawal
        result = difference / 5

        if difference < 750:
            return "You are not eligible."
        else:
            return result
    except ValueError:
        return "Invalid input. Please enter numerical values."

total_deposit = input("Enter total deposit amount: ")
total_withdrawal = input("Enter total withdrawal amount: ")
bonus_received_deposit = input("Enter the deposit amount where the player received a bonus: ")

cashback_result = calculate_cashback(total_deposit, total_withdrawal, bonus_received_deposit)

print(f"cashback Result: {cashback_result}")

