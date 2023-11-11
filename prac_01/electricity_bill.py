TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
price_per_kWh_in_cents = float
tariff = int(input("which tariff? 11 or 31: "))
while tariff != 11 and tariff != 31:
    print("Invalid tariff input")
    tariff = input("which tariff? 11 or 31: ")
if tariff == 11:
    price_per_kWh_in_cents = TARIFF_11
elif tariff == 31:
    price_per_kWh_in_cents = TARIFF_31
daily_use_in_kWh = float(input("Enter daily use in kWh: "))
number_of_days_in_billing_period = float(input("Enter number of days in billing period: "))
Estimated_bill = price_per_kWh_in_cents * daily_use_in_kWh * number_of_days_in_billing_period
print(f"Estimated bill: ${Estimated_bill:.2f}")