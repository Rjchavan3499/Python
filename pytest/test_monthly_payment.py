import  pytest

def weeklyPaid():
	hours_worked = 50
	wage = 100
	pay = 40 * wage + (hours_worked - 40) * wage * 1.5
	return pay



def test_monthly(pay):
	assert pay == 5500.00