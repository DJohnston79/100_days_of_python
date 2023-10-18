prompt = "Hello. I can help you calculate your tip."
prompt += "Please enter the bill total using decimal form, e.g. 123.45.      "
bill = float(input(prompt))
prompt_1 = "what percentage of the bill would you like to leave as a tip?"
prompt_1 += "Enter a number such as 10, 15, or a custom amount."
tip = float(input(prompt_1))
result = (bill * tip/100)

print(f"Your tip should be, {result}.")




