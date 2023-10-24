# James Alan Bush | SU200619706
# CIS261 - Object-Oriented Computer Programming I
# Week 3 | Create and Call Functions with Parameters
# https://github.com/JamesBushStrayer/Create-and-Call-Functions-With-Parameters


# Create a function that will input and return the employee's name and
# is called inside the loop.

def employee_name():
  name = input("Enter employee's name (or 'End' to finish): ")
  return name


# Create a function that will input and return total hours and
# is called inside the loop.

def total_hours():
  hours = input("Enter total hours (or 'End' to finish): ")
  return hours


# Create a function that will input and return the hourly rate and
# is called inside the loop.

def hourly_rate():
  rate = input("Enter hourly rate (or 'End' to finish): ")
  return rate


# Create a function that will input and return the income tax rate and 
# is called inside the loop.

def income_tax_rate():
  tax_rate = input("Enter the income tax rate (or 'End' to finish): ")
  return tax_rate


# Create a function that will take total hours, hourly rate, and
# tax rate as parameters and calculate and return the gross pay, income tax, and 
# net pay and is called inside the loop.

def calculate_pay(hours, rate, tax_rate):
  gross_pay = hours * rate
  income_tax = gross_pay * tax_rate / 100
  net_pay = gross_pay - income_tax
  return gross_pay, income_tax, net_pay


# Create a function that will display employee name, total hours, hourly rate, 
# gross pay, income tax rate, income tax, and net pay, and is called inside the loop.

def display_pay_details(name, hours, rate, gross_pay, tax_rate, income_tax,
                        net_pay):
  print(f"\nEmployee Name: {name}")
  print(f"Total Hours: {hours}")
  print(f"Hourly Rate: {rate}")
  print(f"Gross Pay: {gross_pay}")
  print(f"Income Tax Rate: {tax_rate}")
  print(f"Income Tax: {income_tax}")
  print(f"Net Pay: {net_pay}")


# Create a function that will display total number of employees, total hours, 
# total gross pay, total tax, and total net pay.

def display_total_summary(num_employees, total_hours, total_gross_pay,
                          total_tax, total_net_pay):
  print(f"\n** Total Summary **")
  print(f"Total Number of Employees: {num_employees}")
  print(f"Total Hours: {total_hours}")
  print(f"Total Gross Pay: {total_gross_pay}")
  print(f"Total Tax: {total_tax}")
  print(f"Total Net Pay: {total_net_pay}")


# Create a loop that will get user input by calling various functions until 
# terminated by the user typing “End.”

def main():
  employees = []
  hours_list = []
  rate_list = []
  tax_rate_list = []

  while True:
    name = employee_name()
    if name.lower() == 'end':
      break
    employees.append(name)

    hours = total_hours()
    if hours.lower() == 'end':
      break
    hours_list.append(hours)

    rate = hourly_rate()
    if rate.lower() == 'end':
      break
    rate_list.append(rate)

    tax_rate = income_tax_rate()
    if tax_rate.lower() == 'end':
      break
    tax_rate_list.append(tax_rate)

  total_pay = 0
  total_hours_main = 0
  total_gross_pay = 0
  total_tax = 0
  total_net_pay = 0

  for i in range(len(employees)):
    gross_pay, income_tax, net_pay = calculate_pay(int(hours_list[i]),
                                                   float(rate_list[i]),
                                                   float(tax_rate_list[i]))

    total_pay += net_pay
    total_hours_main += int(hours_list[i])
    total_gross_pay += gross_pay
    total_tax += income_tax
    total_net_pay += net_pay

    display_pay_details(employees[i], hours_list[i], rate_list[i], gross_pay,
                        tax_rate_list[i], income_tax, net_pay)

  display_total_summary(len(employees), total_hours_main, total_gross_pay,
                        total_tax, total_net_pay)


if __name__ == '__main__':
  main()
