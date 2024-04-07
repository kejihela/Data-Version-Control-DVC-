import pandas as pd


Data = [

    {"name": "keji adebayo", "number":"07066231665", "course":"computer science"},
    {"name": "Zainab shittu", "number":"09135511951", "course":"Nurse"},
     {"name": "Taofiq gegele", "number":"098253426", "course":"Lawyer"},
      {"name": "Shamba kazeem", "number":"0987654321", "course":"Elect/elect"}
]
data = pd.DataFrame(Data)
data.to_csv("data/data.csv", index=False)
