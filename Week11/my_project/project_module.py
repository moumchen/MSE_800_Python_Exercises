
from typing import List


def rolling_average(values: List, period:int)-> List:
    # defined a variable to store the rolling averages
    rolling_averages = []

    # this is a loop that calculates the rolling average
    # first, the loop is from the period to the length of the values list
    # and then, every loop will calculate the average of the values from i-period t
    # for example, the list is [1,2,3,4,5,6] and the period is 3
    # the first loop will calculate [1,2,3] and the average is 2.0
    # the second loop will calculate [2,3,4] and the average is 3.0
    # .... the result will be [2.0, 3.0, 4.0, 5.0]
    for i in range(period, len(values)+1):
        average = sum(values[i-period:i]) / period
        rolling_averages.append(average)

    return rolling_averages