"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    # name_data == {name: {year: rank}}
    if name in name_data:  # same name on name_date list
        if year in name_data[name]:  # year already exist
            higher_rank = [int(name_data[name][year]), int(rank)]
            name_data[name][year] = min(higher_rank)
        else:  # new year
            name_data[name][year] = rank
    else:  # new data new name
        name_data[name] = {year: rank}




def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r') as f:
        for line in f:
            lst = line.split(',')
            if len(lst[0]) == 4:
                year = lst[0]
            else:
                rank = lst[0].strip()
                name_m = lst[1].strip()
                name_f = lst[2].strip()
                add_data_for_name(name_data, year, rank, name_f)
                add_data_for_name(name_data, year, rank, name_m)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.f

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for filename in filenames:
        with open(filename, 'r') as f:
            for line in f:
                lst = line.split(',')
                if len(lst[0]) > 2:
                    year = lst[0].strip()
                else:
                    rank = lst[0].strip()
                    name_m = lst[1].strip()
                    name_f = lst[2].strip()
                    if name_m in name_data:
                        if year in name_data[name_m]:
                            name_data[name_m][year] = min(name_data[name_m][year], rank)
                        else:
                            name_data[name_m][year] = rank
                    else:
                        name_data[name_m] = {year: rank}  # new name
                    if name_f in name_data:
                        if year in name_data[name_f]:
                            name_data[name_f][year] = min(name_data[name_f][year], rank)
                        else:
                            name_data[name_f][year] = rank
                    else:
                        name_data[name_f] = {year: rank}  # new name
    return name_data





def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    matching_names = []
    lower_target = target.lower()
    for name in name_data:
        lower_name = name.lower()
        if lower_target in lower_name:
            matching_names.append(name)
    return matching_names








def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
