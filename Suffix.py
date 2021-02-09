import re

class Suffix:

    suffix_name = ''
    suffix_types = []
    irregularity = None

    check_before = False    # If this is true, check the previous part, if it does not match with irregularity, do not do deletion
    delete_before = False

    def __init__(self, suffix_name, suffix_types, irregularity, check_before, delete_before):
        self.suffix_name = suffix_name
        self.suffix_types = suffix_types
        self.irregularity = irregularity
        self.check_before = check_before
        self.delete_before = delete_before

    def get_name(self):
        return self.suffix_name

    def get_types(self):
        return self.suffix_types

    def get_irregularities(self):
        return self.irregularity

