# ============================================================
# QUESTION:
# Implement any one Expert System.
#
# Selected Topic:
# Help Desk Management Expert System
# ============================================================


# ============================================================
# THEORY:
#
# An Expert System is an Artificial Intelligence program that
# tries to behave like a human expert.
#
# It takes a problem from the user and gives a suitable solution
# based on stored knowledge.
#
# Example:
# Human expert:
# User says: "Printer not working"
# Expert says: "Check printer power and connection"
#
# Expert system:
# User enters: "printer not working"
# System gives: "Check printer power cable and connection"
#
# So, an expert system is mainly used for decision making.
# ============================================================


# ============================================================
# MAIN PARTS OF EXPERT SYSTEM:
#
# 1. Knowledge Base:
#    It stores facts, rules, problems, and solutions.
#
# 2. Inference Engine:
#    It checks the user's problem and searches for the correct
#    solution from the knowledge base.
#
# 3. User Interface:
#    It allows the user to enter the problem and see the answer.
#
# In this program:
#
# Knowledge Base  -> problem_dict
# Inference Engine -> handle_request() function
# User Interface -> input() and print()
# ============================================================


# ============================================================
# KNOWLEDGE BASE:
#
# This dictionary stores help desk problems and their solutions.
#
# Dictionary format:
# "problem" : "solution"
#
# The left side is the user's problem.
# The right side is the solution given by the expert system.
#
# Example:
# "printer not working" : "Check printer power cable and connection."
#
# Here, if user enters "printer not working",
# system will return "Check printer power cable and connection."
# ============================================================

problem_dict = {
    "printer not working": "Check printer power cable and connection.",
    "can't log in": "Check username and password.",
    "software not installing": "Check system requirements and storage space.",
    "internet connection not working": "Restart modem/router and check Wi-Fi.",
    "email not sending": "Check internet connection and email settings."
}


# ============================================================
# FUNCTION: show_problems()
#
# Purpose:
# This function displays all available problems to the user.
#
# Why needed?
# If user does not know exactly what to type,
# this list helps the user select/enter a valid problem.
#
# for problem in problem_dict:
# This loop goes through every key/problem in the dictionary.
# ============================================================

def show_problems():
    print("\nAvailable Problems:")

    for problem in problem_dict:
        print("-", problem)


# ============================================================
# FUNCTION: handle_request(user_input)
#
# Purpose:
# This function works like the Inference Engine.
#
# Inference Engine means:
# It takes user input, checks the knowledge base,
# and gives the correct answer.
#
# Steps:
# 1. Convert user input to lowercase.
# 2. Check if user entered "exit".
# 3. If problem exists in dictionary, return solution.
# 4. If problem does not exist, show default message.
# ============================================================

def handle_request(user_input):

    # Convert input to lowercase.
    # This helps to match input easily.
    #
    # Example:
    # "Printer Not Working" becomes "printer not working"
    user_input = user_input.lower()

    # If user wants to stop the program
    if user_input == "exit":
        return "Goodbye!"

    # Check whether user's problem is present in knowledge base
    elif user_input in problem_dict:

        # If problem is found, return its solution
        return problem_dict[user_input]

    # If problem is not found in knowledge base
    else:
        return "Problem not found. Please contact technical support."


# ============================================================
# PROGRAM STARTS FROM HERE
# ============================================================

print("===================================")
print(" Help Desk Management Expert System")
print("===================================")


# ============================================================
# while True:
#
# This loop keeps the expert system running again and again
# until user enters "exit".
#
# Why loop is used?
# Because help desk system should solve multiple problems,
# not only one problem.
# ============================================================

while True:

    # Show all available problems to the user
    show_problems()

    # Take problem from user
    user_input = input("\nEnter your problem or type exit: ")

    # Send user's problem to inference engine
    response = handle_request(user_input)

    # Display solution returned by expert system
    print("Solution:", response)

    # If user enters exit, stop the loop
    if user_input.lower() == "exit":
        break


# ============================================================
# CONCLUSION:
#
# This program is a simple Help Desk Management Expert System.
#
# It stores common technical problems and their solutions in a
# knowledge base. When the user enters a problem, the system
# checks the knowledge base and gives the suitable solution.
#
# If the problem is not available, it asks the user to contact
# technical support.
# ============================================================