from datetime import date

# vacation = input("Skriv inn hvilken dag ferien starter (dd/mm/yyyy): ")
vacation = input("Enter what day the holiday starts: (dd/mm/yyyy): ")
vacation = vacation.split("/")
vacation = date(int(vacation[2]), int(vacation[1]), int(vacation[0]))

this_day = date.today()

print(f"{vacation - this_day}")
