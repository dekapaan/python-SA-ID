""" Task that intakes and evaluates SA ID and outputs year born, month born, date of birth, gender,
citizen/noncitizen. This SA ID program only works for years 1922 - 2021(a century) """
_id = 'global'
year = 'global'


# function asks user for ID and checks to see if ID given is valid. If not, it repeats itself until valid ID is given
def valid_id():
    global _id
    global year
    while True:
        try:
            _id = input("Enter your ID: ")
            int(_id)  # makes sure value isn't string
            if type(_id) == float:
                raise ValueError
            list31 = ["01", "03", "05", "07", "08", "10", "12"]  # Represents all months with 31 days
            list30 = ["04", "06", "09", "11"]  # Represents all months with 30 days
            if 22 <= int(_id[0:2]) <= 99:
                year = 1900 + int(_id[0:2])
                if len(_id) != 13 or (12 < int(_id[2: 4]) < 1):
                    raise ValueError
                if (_id[2:4]) in list31:
                    if int(_id[4:6]) not in range(1, 32):
                        raise ValueError
                elif (_id[2:4]) in list30:
                    if int(_id[4:6]) not in range(1, 31):
                        raise ValueError
                elif (_id[2:4]) == "02":  # if month is february, checks if it is leap year
                    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                        if int(_id[4:6]) not in range(1, 30):
                            raise ValueError
                    else:
                        if int(_id[4:6]) not in range(1, 29):
                            raise ValueError
                elif int(_id[6:10]) not in range(10000):
                    raise ValueError
                elif _id[10] != "0" or _id[10] != "1":
                    raise ValueError
                break
            else:
                if 00 <= int(_id[0:2]) <= 21:
                    year = 2000 + int(_id[0:2])
                    if len(_id) != 13 or (12 < int(_id[2: 4]) < 1):
                        raise ValueError
                    if (_id[2:4]) in list31:
                        if int(_id[4:6]) not in range(1, 32):
                            raise ValueError
                    elif (_id[2:4]) in list30:
                        if int(_id[4:6]) not in range(1, 31):
                            raise ValueError
                    elif (_id[2:4]) == "02":  # if month is february, checks if it is leap year
                        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                            if int(_id[4:6]) not in range(1, 30):
                                raise ValueError
                        else:
                            if int(_id[4:6]) not in range(1, 29):
                                raise ValueError
                    elif int(_id[6:10]) not in range(10000):
                        raise ValueError
                    elif _id[10] != "0" or _id[10] != "1":
                        raise ValueError
                    break
        except ValueError:
            print("Invalid entry")
            print("")
    return None


valid_id()
months = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June",
          "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
print("")
print("Year born: {}".format(year))
print("Month born: {}".format(months[_id[2:4]]))
print("Date of birth(dd/mm/yyyy): {}/{}/{}".format(_id[4:6], _id[2:4], year))
if 0 <= int(_id[6:10]) <= 4999:
    print("Gender: Female")
else:
    print("Gender: Male")
if _id[10] == "0":
    print("Citizenship: SA citizen")
else:
    print("Citizenship: Permanents resident")
