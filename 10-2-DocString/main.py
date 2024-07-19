# def function_name(parameters)
#     """Docstring"""

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    #use the title() function to convert to title case
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    #return formated strings
    return f"{formated_f_name} {formated_l_name}"
    
#now we can call the function and pass arguments to it
formated_string = format_name("MiSTer", "sEveN")
print(formated_string)