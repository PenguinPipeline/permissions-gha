import os
# import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    # my_input = os.environ["INPUT_MYINPUT"]

    result = f"Permissions File: {os.environ['permissions_file_path']}\n Reference File: {os.environ['restrictions_file_path']}"

    print(f"::set-output name=result::{result}")


if __name__ == "__main__":
    main()