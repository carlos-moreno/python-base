#!/usr/bin/env python3


def welcome():
    print("Welcome to the test.")
    input("When you are ready press enter.")


def ask_questions(ask_color=False):
    name = input("Name: ")
    print(f"It is nice to meet you {name}")

    if ask_color:
        color = input("Quat is your favorite color? ")
        print(f"{color} is a great color.")

    input("Describe yourself: ")
    print("admirable!")


def goodbye():
    print("Goofbye.")


welcome()
ask_questions(ask_color=True)
goodbye()
