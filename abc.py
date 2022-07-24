def valid_expression(strex):
    """
    Evaluate if strex is a valid mathematical expression.
    """
    for i in range(len(strex)):
        # If the first char is invalid.
        if i==0:
            if strex[i] in ['+', '-', '*', '/', '%', ')']:
                return False

        # If the last char is also invalid.
        if i == len(strex) - 1:
            if strex[i] in ['+', '-', '*', '/', '%', '(']:
                return False

        # Validate char if it is a number, operators or parenthesis.
        if (strex[i] >= '0' and strex[i] <= '9') or strex[i] in ['+', '-', '*', '/', '%', '(', ')']:
            continue  # continue with the next character
        else:
            return False
    
    return True  # We cannot find invalid chars.

    
def main():
    st.title(' ofir Calculator')

    # The input value from the user will be saved in user_expr.
    user_expr = st.text_input('Please enter a mathematical expression')

    if not valid_expression(user_expr):
        st.error("Invalid Expression")
    else:
        st.success("Valid Expression")

        # Get the value of the expression.
        value = get_value(user_expr)
        st.write(f'The answer is {value}.')  # ref.: https://docs.python.org/3/tutorial/inputoutput.html


# Entry point
main()
