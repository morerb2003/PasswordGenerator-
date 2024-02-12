import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to Password Generator")

    while True:
        length = int(input("Enter the desired length of the password: "))

        if length <= 0:
            print("Invalid length. Please enter a positive number.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)

        choice = input("Do you want to generate another password? (yes/no): ")
        if choice.lower() != 'yes':
            print("Exiting Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
