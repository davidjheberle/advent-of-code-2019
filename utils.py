import getopt
import sys

def read_input():
    full_cmd_args = sys.argv
    arg_list = full_cmd_args[1:]
    unix_options = "f:"
    gnu_options = "file="

    try:
        args, _ = getopt.getopt(arg_list, unix_options, gnu_options)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)

    file_name = None
    for arg, value in args:
        if arg in ("-f", "--file"):
            file_name = value
            print("Reading %s" % file_name)

    file = open(file_name)
    raw_input = file.read()
    file.close()
    return raw_input