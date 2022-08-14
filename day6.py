
def user_name(email):
    poop, poopy = email.split("@")
    return poop


def main():
    email = input("Email: ")
    print(user_name(email))


if __name__ == "__main__":
    main()