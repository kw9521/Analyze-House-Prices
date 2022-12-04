"""
Demonstrate sorting lists of dataclass structures and list comprehensions.

File: sort_structs.py
Author: bksteele
"""

import copy
from dataclasses import dataclass
from random import *        # shuffle function

@dataclass(frozen=True)
class ColorWave:
    """
    ColorWave represents a color's wavelength band from low to high.
    color is the color of interest.
    lo_wave and hi_wave are the color low and high wavelengths in nanometers.
    """
    color: str
    lo_wave: int
    hi_wave: int


def init_colorwaves():
    """
    initialize the demo list.
    @return list of ColorWave objects
    """
    waves = []
    data = [ ('violet', 380, 430) \
           , ('blue', 430, 500) \
           , ('cyan', 500, 520) \
           , ('green', 520, 565) \
           , ('yellow', 565, 590) \
           , ('orange', 590, 625) \
           , ('red', 625, 740) \
           ]
    for (col, lo, hi) in data:
        waves.append( ColorWave( col, lo, hi))
    return waves

def print_wavelist( lst):
    """
    Pretty print the list of ColorWave elements, one per line.
    """
    print( "Color Wavelengths (nm):")
    for item in lst:
        print_color_wave( item)

def print_color_wave( color):
    """
    Pretty print one ColorWave element labeling its slots.
    """
    print( "color:", color.color, "\tlo:", color.lo_wave, "hi:", color.hi_wave)

def main():
    """
    run the demonstration of copying, sorting using list.sort() and sorted(),
    and constructing a list using a list comprehension.
    """
    waves = init_colorwaves()
    print(waves)
    print()
    print_wavelist( waves)
    namelist = copy.deepcopy( waves)
    # a lambda function has one argument, shown here as C, and
    # this lambda function's purpose is to extract a slot value
    # by which to sort the list; the sort criterion is the color name.
    print( "\nSorted by color name:")
    namelist.sort( key=lambda C: C.color)
    print_wavelist( namelist)

    # use a 'list comprehension' to make a sublist
    print( "\nFiltered to get lo wavelength:")
    sublist = [item for item in waves if item.lo_wave < 500]
    print_wavelist( sublist)

    print( "\nSort by hi wavelength in reverse:")
    waves.sort( key=lambda C: C.hi_wave, reverse=True)
    print_wavelist( waves)

    print( "\nSorted using sorted() to get new list by lo wavelength:")
    newwaves = sorted( waves, key=lambda C: C.lo_wave)
    print_wavelist( newwaves)

if __name__ == "__main__":
    main()
