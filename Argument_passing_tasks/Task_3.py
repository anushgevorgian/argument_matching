def print_user_profile(first_name, last_name, *, age, city):
    print(f"{first_name} {last_name} {age} {city}")

print_user_profile("John", "Doe", age=30, city="New York")