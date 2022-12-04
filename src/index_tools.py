from dataclasses import dataclass

@dataclass
class QuarterHPI:
    year: int
    qtr: int
    index: float

@dataclass
class AnnualHPI:
    year: int
    index: float

def read_state_house_price_data(filepath):
    """
    d is an empty dictionary
    opens file and strips each line and splits by a tab
    if the first line's first index is "state", skips over that line
    if line[0] isnt found in dictionary, creates a new list and appends the values in line to dictionary
    otherwise, just append
    if no data is there, prints data unavailable and the line
    returns d
    """
    d = {}
    with open(filepath) as f:
        for line in f:
            line = line.strip().split("\t")
            if line[0] != "state":
                try:
                    if line[0] not in d.keys():
                        d[line[0]] = []
                        d[line[0]].append(QuarterHPI(int(line[1]), int(line[2]), float(line[3])))
                    else:
                        d[line[0]].append(QuarterHPI(int(line[1]), int(line[2]), float(line[3])))
                except:
                    print("data unavailable: ")
                    print(str(line[0] + " "+ line[1] + " "+ line[2]+" "+line[3] +" "+ line[4]) + " " +line[5])
    return d

def read_zip_house_price_data(filepath):
    """
    d = empty dictionary
    counter and missing_counter just counts oe # of lines that are used or not accounted for
    opens file, strips and splits on tab
    skips first line if index of 0 says "Five-Digit Zip Code"
    adds 1 to counter if index 3 of line is "."
    otherwise, checks if zipcode is in dictionary, if yes, appends to d and adds 1 to counter
    if zipcode is not in dictionary, creates a new list and adds 1 to counter
    prints count: ... uncounted: ... if uncounted is >0, otherwise skips over this part
    returns d
    """
    d = {}
    counter = 0
    missing_counter = 0
    with open(filepath) as f:
        for line in f:
            line = line.strip().split("\t")
            if line[0] != "Five-Digit ZIP Code":
                if (line[3] == "."):
                    missing_counter += 1
                else:
                    if line[0] in d:
                        d[line[0]].append(AnnualHPI(int(line[1]), float(line[3])))
                        counter += 1
                    else:
                        d[line[0]] = [AnnualHPI(int(line[1]), float(line[3]))]
                        counter+=1
        if missing_counter != "0":
            print("count: "+str(counter) +" uncounted:"+str(missing_counter))
    return d

def index_range(data,region):
    """
    data: list of annual hpi or quarter hpi objects
    region: state
    returns a tuple of objects that are the highest index values of the dataset

    basically looks like this at the end:
    (QuarterHPI( year=1995, qtr=1, index=98.04 ), QuarterHPI( year=2007, qtr=3,index=220.74 ))
    """
    min = -1
    max = -1
    for line in data[region]:
        if min == -1:
            min = line
            max = line
        else:
            if min.index > line.index:
                min = line
            if max.index < line.index:
                max = line
    return (min, max)

def print_range(data, region):
    Min_Max = index_range(data, region)
    print("Region: "+region)
    print("Low: year/quarter/index:",Min_Max[0].year,"/",Min_Max[0].qtr,"/",Min_Max[0].index)
    print("High: year/quarter/index:",Min_Max[1].year,"/",Min_Max[1].qtr,"/",Min_Max[1].index)

def Sort_Tuple(tup):
    """
    sorts the list of tuples by second item
    returns [('UT', 182.3), ('CO', 166.24),
    ('OR', 165.86), ('MT', 163.95), ('WY', 152.27),
     ('NE', 147.24), ('SD', 145.55), ('MI', 145.16),
      ('WI', 143.14), ('ID', 142.68), ('LA', 142.64), .......]
    """
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if (tup[j][1] < tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup

def print_ranking (data, heading="Ranking"):
    """
    data: a list of ("state", index_nsa)
    [('AK', 100.0), ('AK', 102.24), ('AK', 104.92),
    ('AK', 110.87), ('AK', 114.63), ('AK', 120.6),
    ('AK', 123.15), ('AK', 125.52), ('AK', 129.25),
    ('AK', 129.97), ('AK', 130.68), ...............]
    """
    # print("original data")
    # print(data)
    # print()
    #
    # print("sorted data:")
    sorted_data = Sort_Tuple(data)
    # print(sorted_data)
    # print()

    print(heading)
    print("The Top 10: ")
    for i in range(0, 10):
        print(str(i+1) + " : " + str(sorted_data[i]))
    print("The Bottom 10: ")
    for i in range(-9, 1):
        print(str(len(sorted_data)+i) + " : " + str(sorted_data[i-1]))

def sum_index(list_qtr):
    """
    pre-condition: there is only 4 qtrs per year
    returns the avg of index all 4 indexes in each year
    """
    if (len(list_qtr)!=4):
        raise IndexError("there is not enough data")
    return (list_qtr[0].index+list_qtr[1].index+list_qtr[2].index+list_qtr[3].index)/4

def annualize(data):
    """
    returns the annual avg index for first wtv annual[][x] years, x = # ofy ears
    uses this format: list[int:int:int] to loop through the list of items

    returns a dictionary mapping regions to lists of AnnualHPI objects. Note: This function
    operates only on a dictionary whose value type is list of QuarterHPI objects. It
    averages those objects to create the lists of AnnualHPI objects. Since some quarterly
    data may be unavailable, it averages whatever ones actually exist, whether
    that be one, two, three or four items per year.

    data: {region[]: QuarterHPI[]}
    returns:
        {region[]: AnnualHPI[]}
    """
    fin = {}
    for k, v in data.items():
        # list = [4*i for i in list]
        # range(int(len(v)/4))
        # AnnualHPI(v[4*i].year, sum_index(v[4*i:4*(i+1)]))
        fin[k] = [AnnualHPI(v[4*i].year, sum_index(v[4*i:4*(i+1)])) for i in range(int(len(v)/4))]
    return fin

if __name__ == "__main__":
    print("hi")
    # file = input("Enter house price index file: ")
    # if file == "HPI_AT_state.txt":
    #     data = read_state_house_price_data("data/HPI_AT_state.txt")
    # elif file == "HPI_PO_state.txt":
    #     data = read_zip_house_price_data("data/HPI_PO_state.txt")
    # else:
    #     raise FileNotFoundError(">:(")
    # region = input("Enter region of interest (Hit enter to stop): ")
    # if region is not None:
    #
    # else:
    #     break
    #     data = read_state_house_price_data("../data/HPI_AT_state.txt")
    # else:
    #     data = read_zip_house_price_data("../data/HPI_PO_state.txt")
    # while region != "":
    #     print("====================================================")
    #     print("Region: " + str(region))
    #     print(print_range(data, region))
    # file = "./HPI_AT_state.txt"
    # print(data["14610"][:3])
    # print("")
    # print(data["14706"][-3:])
    # data = read_state_house_price_data("../data/HPI_PO_state.txt")
    # annual = annualize(data)
    # year = 1998
    # qtr = 1
    # print_ranking(period_ranking.quarter_data(data, year, qtr), str(year) + "/Q" + str(qtr) + " Quarterly Ranking" )

    # HPI_PO_state.txt
    # print(index_range(data, "NY"))
    # print("")
    # data = read_state_house_price_data("../data/HPI_PO_state.txt")
    # print(data)
    # print(annualize_helper(data))
    # annual = annualize(data)
    # print()
    # print(annual["NY"][:3])


