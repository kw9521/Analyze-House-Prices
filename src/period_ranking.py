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

"""
def main():
    data=index_tools.read_state_house_price_data("data/HPI_PO_state.txt")
    qd = quarter_data( data, 1998, 2)
    print(qd[:2])
main()
"""

def annual_data(data, year):
    """
    Name: annual_data
    Parameters: data, year
    The data is a dictionary mapping a state or zip code to a list of AnnualHPI
    data: {[state|zipcode]:AnnualHPI[]}
    objects, and the year is the year of interest.
    Returned Result Type:
    A list of (region, HPI) tuples sorted from high value HPI to low value HPI.
    [(state/zipcode, AnnualHPI)]

    returns [(state: annualized index values),(), ()]
    like:
    [('CO', 243.845), ('MN', 219.41750000000002),
    ('MT', 217.6625), ('OR', 215.73), ('MA', 215.5),
    ('DC', 209.41750000000002), ...]
    """
    region_hpi = []
    for k, v in data.items():
        for ahpi in v:
            if ahpi.year == year:
                region_hpi.append((k, ahpi.index))
    sorted_lst = index_tools.Sort_Tuple(region_hpi)
    return sorted_lst

"""
def main():
    data = index_tools.read_state_house_price_data( "data/HPI_PO_state.txt")
    annual = index_tools.annualize( data )
    print(annual_data(annual, 2003)) 
    # returns [(state: annualized index values),(), ()]
main()
"""


if __name__ == "__main__":
    """
    prompts user to enter a file name
    if file is a state file, opens file w/ the state price data prompts user to enter year of interest, annualizes the data and returns the rankings of that year
    if file is a zip file opens file w/ the zip price data, prompts user to enter year of interest and returns the ranking of that year
    otherwise, raises a file not found error
    """
    file = input("Enter region-based house price index filename: ")
    if "state" in file:
        data = index_tools.read_state_house_price_data("data/"+file)
        year = int(input("Enter year of interest for house prices: "))
        print(year, "Annual Ranking\n")
        annual = index_tools.annualize(data)
        x = annual_data(annual, year)  # [(state:  ), (), ()]
        index_tools.print_ranking(x)

    elif "ZIP" in file:
        data = index_tools.read_zip_house_price_data("data/"+file)
        year = int(input("Enter year of interest for house prices: "))
        print(year, "Annual Ranking\n")
        # annual = index_tools.annualize(data)
        # print(annual)     # annual is {"state: [aphi(year, index), aphi()]}
        x = annual_data(data, year)  # [(state:  ), (), ()]
        index_tools.print_ranking(x)
    else:
        raise FileNotFoundError("File is not found")




