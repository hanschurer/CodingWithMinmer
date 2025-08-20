# You are given two arrays departures and returns where departures [i] and returns [i] are ticket prices for departing and returning flights on the ith day, respectively.
# You want to minimize your cost by choosing a single day to buy a departure flight and choosing a different day in the future to buy a returning flight.
# Return the minimum cost you can achieve from a single round-trip flight.

# 不可以直接用「出发数组的全局最小值」来计算，因为这可能违反「出发日必须早于返程日」的约束。
def find_cheapest_tickets(departures, returns):
    min_departure_cost = departures[0]
    min_cost = float('inf')
    
    for i in range(1, len(returns)):
        min_departure_cost = min(min_departure_cost, departures[i])
        min_cost = min(min_cost, min_departure_cost + returns[i])
 
    return min_cost

if __name__ == "__main__":
    departures = [8, 3, 6, 10]
    returns = [10, 9, 5, 8]
    assert find_cheapest_tickets(departures, returns) == 8

    departures = [10, 3, 10, 9, 3]
    returns = [4, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 9

    departures = [1, 3, 10, 9, 3]
    returns = [1, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [1, 3, 10, 9, 3]
    returns = [1, 1, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 2

    departures = [1, 3, 10, 9, 3]
    returns = [10, 9, 8, 7, 6]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [12, 33, 44, 9, 23]
    returns = [100, 90, 80, 70, 15]
    assert find_cheapest_tickets(departures, returns) == 24

    departures = [4, 3, 5, 11, 2]
    returns = [1, 6, 10, 2, 9]
    assert find_cheapest_tickets(departures, returns) == 5