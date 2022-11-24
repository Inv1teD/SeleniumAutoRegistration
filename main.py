from src.isaps_filler import fill_Isaps_with_data
from src.user_prop import User, make_test_user


def script():
    client = User
    client.create(client)
    # client = make_test_user()
    fill_Isaps_with_data(client)

def main():
    script()


if __name__ == '__main__':
    main()
