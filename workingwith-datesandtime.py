import datetime

r"""   
This script creates an empty file.
"""

filename=datetime.datetime.now()

#Create empty file
def create_file():
    """This script creates an empty file."""
    with open(filename.strftime("%Y-%m-%d-%H, %M"), "w") as file:
        file.write("")  #Writing empty string
        
create_file()