import numpy.ma as ma
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import copy
import index_tools
import trending


def build_plottable_array(xyears, regiondata):
    pass

def filter_years(data, year0, year1):
    """
    DATA IS A LIST OF APHI
    data = [ahpi(year, index), ahpi(), ahpi(), ...]
    returns: [aphi(year, annualized_index), aphi(), ...]

    return looks like:
    [AnnualHPI(year=1998, index=105.5825),
    AnnualHPI(year=1999, index=113.875),
    AnnualHPI(year=2000, index=124.655), ...]
    """
    lst = []
    for idx in data:    # idx are a bunch of ahpis
        if idx.year >= year0 and idx.year <= year1: # checks aphi's years
            lst.append(idx)
    return lst

if __name__ == "__main__":
    file = index_tools.read_state_house_price_data("data/HPI_PO_state.txt")
    annual = index_tools.annualize(file)
    print(filter_years(annual["NY"], 1998, 2004))

def plot_HPI(data, regionList):
    pass

def plot_whiskers(data, regionList):
    pass
