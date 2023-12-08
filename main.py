
year = int(input("yil:"))


def find_century(century):
    if century > 1801 and century < 1900:
        print("19th century")

    elif century > 1901 and century < 2000:
         print("20th century")


    elif century > 2001 and century < 2024:
         print("21st century")




find_century(year)


