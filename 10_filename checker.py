from datetime import date
import re


# if filename is blank, returns default name
# otherwise checks filename and either returns
# an error or returns the filename (with .txt extension)
def filename_maker(filename):

    # creates default filename
    # (YYYY_MM_DD_temperature_calculations)
    if filename == "":

        # set filename_ to "" so we can see
        # default name for testing purposes
        filename_ok = ""
        date_part = get_date()
        filename = "{}_temperature_calculations".format(date_part)

    # checks filename has only a-z ? A-Z / underscores
    else:
        filename_ok = check_filename(filename)

    if filename_ok == "":
        filename += ".txt"

    else:
        filename = filename_ok

    return filename


# retrieves date and creates YYYY_MM_DD string
def get_date():