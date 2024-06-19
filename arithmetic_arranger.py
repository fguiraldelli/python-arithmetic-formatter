def arithmetic_arranger(problems, show_result=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    # Initialize variables
    arranged_problems = ""
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    # Loop through each problem
    for problem in problems:
        # Split the problem into operands and operator
        operands = problem.split()
        operand1 = operands[0]
        operator = operands[1]
        operand2 = operands[2]
        # Check if the operator is valid
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        # Check if the operands are valid
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        # Check if the operands have more than 4 digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        # Calculate the result
        if operator == "+":
            result = str(int(operand1) + int(operand2))
        else:
            result = str(int(operand1) - int(operand2))
        # Determine the maximum length of the operands and result
        if (int(result) < 0 or int(operand2) < int(operand1)):
            max_length = max(len(operand1), len(operand2), len(result) - 1)
        else:
            max_length = max(len(operand1), len(operand2), len(result))
        # Add the operands and result to the arranged problems
        first_line += operand1.rjust(max_length + 2) + "    "
        second_line += operator + " " + operand2.rjust(max_length) + "    "
        third_line += "-" * (max_length + 2) + "    "
        fourth_line += result.rjust(max_length + 2) + "    "
    # Remove the extra spaces at the end of each line
    if (show_result):
        arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip(
        ) + "\n" + third_line.rstrip() + "\n" + fourth_line.rstrip()
    else:
        arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip(
        ) + "\n" + third_line.rstrip()

    return arranged_problems
