
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

cents_per_kwh = float(input('Which Tariff do you want to use? 11 or 31?'))
daily_use = float(input('Enter daily use kWh:' ))
billing_days = float(input('Enter number of billing days kWh:'))

if ( cents_per_kwh == 11 ) : cents_per_kwh = TARIFF_11

if ( cents_per_kwh == 31 ) : cents_per_kwh = TARIFF_31



estimated_bill = (cents_per_kwh * daily_use) * billing_days

print('Estimated Bill $', estimated_bill)

