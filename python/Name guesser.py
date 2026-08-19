male_names = {"Shivansh", "Dhruv", "Kabir", "Vedant", "Kiaan", "Aarav", "Arjun", "Viraj", "Krishna", "Avyan", "Ram", "Mohammed", "Santosh", "Sanjay", "Sunil", "Rajesh", "Ramesh", "Ashok", "Manoj", "Anil"}
female_names = {"Aarohi", "Ananya", "Aadhya", "Ishita", "Saanvi", "Myra", "Diya", "Aaradhya", "Anika", "Riya", "Priya", "Sneha", "Pooja", "Kavya", "Shreya", "Nisha", "Meera", "Aditi", "Rashmi", "Sakshi"}

x = input("Enter your names first letter: ")
gender = input("Enter your gender (male/female): ")

if gender == "male":
    for x in male_names:
        name = x
        if x in male_names:
            print(name)


if gender == "female":
    for y in female_names:
        name = y
        if y in female_names:
            print(name)


