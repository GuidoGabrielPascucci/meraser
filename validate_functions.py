import os

def validate_args(args):
    return len(args) == 2

def validate_dir(directory):
    return os.path.isdir(directory)