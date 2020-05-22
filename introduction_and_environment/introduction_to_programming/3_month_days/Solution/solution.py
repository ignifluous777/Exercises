print("Enter a month in lower case to determine how many days it has: ")
month = input()
month_dict = {"january": 31,
              "february": 28,
              "march": 31,
              "april": 30,
              "may": 31,
              "june": 30,
              "july": 31,
              "august": 31,
              "september": 30,
              "october": 31,
              "november": 30,
              "december": 31
              }

data = month_dict[month]

print(data)
