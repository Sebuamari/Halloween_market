from helpers import create_city

try:
    city = create_city()
except Exception as e:
    print(f"An unexpected error occurred: {e}")