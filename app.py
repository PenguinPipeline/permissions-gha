#!/usr/bin/env python
import os
# import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    # my_input = os.environ["INPUT_MYINPUT"]

    # result = f"Permissions File: {os.environ['permissions_file_path']}--Reference File: {os.environ['restrictions_file_path']}"

    line = ""
    with open("/github/workspace/" + os.environ['permissions_file_path']) as f:
        line = f.readline()
    
    print(f"::set-output name=result::{line}")


if __name__ == "__main__":
    main()