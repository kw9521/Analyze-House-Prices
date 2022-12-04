import index_tools
"""
task 1
"""

def quarter_data(data, year, qtr):
    """
    data: {region: qtrHPI[]}
    returns: tuple(region, qtrHPI.index)[]

    returns a list of state, index pair of the year and qtr the user inputs
    answer["HPI_PO_state.txt 1993 1"] = [('UT', 117.69), ('OR', 116.94)]
    """
    lst = []
    for state, qtrhpis in data.items():
        [tuple] = [(state, qtrhpi.index) for qtrhpi in qtrhpis if qtrhpi.year == year and qtrhpi.qtr == qtr]
        lst.append(tuple)
    sorted_lst = index_tools.Sort_Tuple(lst)
    return sorted_lst

def annual_data(data, year):
    """
    Name: annual_data
    Parameters: data, year
    The data is a dictionary mapping a state or zip code to a list of AnnualHPI
    data: {[state|zipcode]:AnnualHPI[]}
    objects, and the year is the year of interest.
    Returned Result Type:
    A list of (region, HPI) tuples sorted from high value HPI to low value HPI.
    [(state|zipcode, AnnualHPI)]
    """
    region_hpi = []
    for k, v in data.items():
        for ahpi in v:
            if ahpi.year == year:
                region_hpi.append((k, ahpi.index))
    sorted_lst = index_tools.Sort_Tuple(region_hpi)
    return sorted_lst
"""
if __name__ == "__main__":
    file = input("Enter String: ")
    year = input("Enter year of interest for house prices:")


"""
