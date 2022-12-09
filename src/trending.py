import index_tools

def cagr(idxlist, periods):
    """
    The idxlist is a 2-item list of [HPI0, HPI1], where HPI0 is the index value of
    the earlier period. The periods is the number (N) of periods (years) between the
    two HPI values in the list

    calling: cagr((80.26, 110.3), 10)
    returns: 3.2304060717629035
    """
    divide = idxlist[1] / idxlist[0]
    x = 1/periods
    return ((divide**x)-1) * 100

def calculate_trends(data, year0, year1):
    """
    The data is a dictionary from region to a list of AnnualHPI. The year0 and year1
    specify the periods of interest. The year0 is the starting year, year1 is the ending
    year, and the pre-condition is year0 < year1

    data: {[region]:[annualHPI]}
    cagr = ((index1/index0)^(1/N) - 1) * 100

    returns:
    [('DC', 9.647635516494146), ('HI', 8.204494647464621),
    ('MD', 6.615176334862793), ('WY', 6.517865881457396), ....]

    annualized data:
    [AnnualHPI( year=1991, index=99.9675 ), AnnualHPI( year=1992, index=101.355)]
    """
    lst = []
    for state in data:
        start_year_index = None
        end_year_index = None
        # print(data) # qhpi(year, qtr, index)
        for value in data[state]:
            # print(value) # returns qhpi(year, qtr, index)
            if int(year0) == int(value.year):
                start_year_index = value.index
            if int(year1) == int(value.year):
                end_year_index = value.index
        if start_year_index != None and end_year_index != None:
            rate = cagr((start_year_index, end_year_index), int(year1)-int(year0))
            lst.append((state, rate))
    return1 = index_tools.Sort_Tuple(lst)
    #print(return1)
    return return1

if __name__ == "__main__":
    """
    prompts user to enter a file 
    if file is a state file, runs it through the state house data, prompts user to enter a start year and a end year, 
        annualizes the data, calculates the trend of the annualized data and returns the ranking in a life 
        
    if file is a zip file, runs it through the zip house data, prompts user to enter a start year and a end year, 
        calculates the trend of the data and returns the ranking in a life 
    
    otherwise, prompts a file not found error 
    """
    file = input("Enter house price index file: ")
    if "state" in file:
        data = index_tools.read_state_house_price_data("data/"+file)
        year0 = int(input("Enter a start year: "))
        year1 = int(input("Enter a end year: "))
        print("\n" + str(year0) + "-" + str(year1), "Compound Annual Growth Rate")
        annualized = index_tools.annualize(data)
        final = calculate_trends(annualized, year0, year1)
        index_tools.print_ranking(final)

    elif "ZIP" in file:
        data = index_tools.read_zip_house_price_data("data/" +file)
        year0 = int(input("Enter a start year: "))
        year1 = int(input("Enter a end year: "))
        print("\n" + str(year0) + "-" + str(year1), "Compound Annual Growth Rate")
        final = calculate_trends(data, year0, year1)
        index_tools.print_ranking(final)
    else:
        raise FileNotFoundError("File is not found")

