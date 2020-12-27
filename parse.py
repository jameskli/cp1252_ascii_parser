#!/usr/bin/env/python
# -*- coding: utf-8 -*-
import codecs

FILE_NAME = "enter_filename.csv"
OUTPUT_FILE_NAME = "parsed_{}".format(FILE_NAME)


def main():
    """ Run main parsing function"""

    error_count = 0
    with codecs.open(FILE_NAME, 'r', 'cp1252') as read_file:
    # with codecs.open(FILE_NAME, "r", "utf-8") as read_file:
        lines = read_file.readlines()
    with open(OUTPUT_FILE_NAME, "w") as write_file:
        for line in lines:
            new_str = line.encode("utf-8").decode("utf-8")
            undecoded_str = unidecode(new_str)
            if undecoded_str != new_str:
                print undecoded_str
                error_count += 1
            write_file.write(unidecode(new_str))
    print "Rows corrected,", error_count


main()
