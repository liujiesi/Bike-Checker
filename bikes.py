""" CSC108 Assignment 2 Starter code """

from typing import List, TextIO

# A set of constants, each representing a list index for station information.
ID = 0
NAME = 1
LATITUDE = 2
LONGITUDE = 3
CAPACITY = 4
BIKES_AVAILABLE = 5
DOCKS_AVAILABLE = 6
IS_RENTING = 7
IS_RETURNING = 8

####### BEGIN HELPER FUNCTIONS ####################

def is_number(value: str) -> bool:
    """Return True if and only if value represents a decimal number.

    >>> is_number('csc108')
    False
    >>> is_number('  108 ')
    True
    >>> is_number('+3.14159')
    True
    """

    return value.strip().lstrip('-+').replace('.', '', 1).isnumeric()


def csv_to_list(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on data to be input.
    """

    # Read and discard header.
    csv_file.readline()

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data


####### END HELPER FUNCTIONS ####################

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####

SAMPLE_STATIONS = [
    [7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False]]

HANDOUT_STATIONS = [
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11, True, True],
    [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,
     15, 5, 10, True, True]]

#########################################

def clean_data(data: List[list]) -> None:
    """Convert each string in data to an int if and only if it represents a
    whole number, a float if and only if it represents a number that is not a
    whole number, True if and only if it is 'True', False if and only if it is
    'False', and None if and only if it is either 'null' or the empty string.

    >>> d = [['abc', '123', '45.6', 'True', 'False']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, True, False]]
    >>> d = [['ab2'], ['-123'], ['False', '3.2']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], [False, 3.2]]
    """

    for sublist in data:        
        for i in range(len(sublist)):
            if sublist[i] == 'True':
                sublist[i] = bool(True)
            elif sublist[i] == 'False':
                sublist[i] = bool(False)
            elif '.' in sublist[i]:
                if sublist[i][:sublist[i].find('.')].isdigit():
                    sublist[i] = float(sublist[i])
                elif sublist[i][0] == '-':
                    sublist[i] = float(sublist[i])
                else:
                    sublist[i] = sublist[i]
            elif sublist[i].isdigit():
                sublist[i] = int(sublist[i])
            elif '-' in sublist[i] and sublist[i][1:].isdigit():
                sublist[i] = int(sublist[i])
            elif sublist[i] == 'null':
                sublist[i] = None
            elif sublist[i] == '':
                sublist[i] = None
            
    return None
                

def get_station_info(station_id: int, stations: List[list]) -> list:
    """Return a list containing the following information from stations
    about the station with id number station_id:
        - station name
        - number of bikes available
        - number of docks available
    (in this order)

    Precondition: station_id will appear in stations.

    >>> get_station_info(7087, SAMPLE_STATIONS)
    ['Danforth/Aldridge', 9, 14]
    >>> get_station_info(7088, SAMPLE_STATIONS) 
    ['Danforth/Coxwell', 13, 2]
    """
    
    station_info = []
    used_station = []
    for sublist in range(len(stations)):
        if station_id in stations[sublist]:
            used_station.append(stations[sublist])
            station_info.append(used_station[0][NAME])
            station_info.append(used_station[0][BIKES_AVAILABLE])
            station_info.append(used_station[0][DOCKS_AVAILABLE])
            
    return station_info


def get_total(index: int, stations: List[list]) -> int:
    """Return the sum of the column in stations given by index.

    Precondition: the items in stations at the position
                  that index refers to are ints.

    >>> get_total(BIKES_AVAILABLE, SAMPLE_STATIONS)
    22
    >>> get_total(DOCKS_AVAILABLE, SAMPLE_STATIONS)
    16
    """

    total = 0
    for sublist in range(len(stations)):
        total = total + stations[sublist][index]
        
    return total
    
    
def get_station_with_max_bikes(stations: List[list]) -> int:
    """Return the station ID of the station that has the most bikes available.
    If there is a tie for the most available, return the station ID that appears
    first in stations.

    Precondition: len(stations) > 0

    >>> get_station_with_max_bikes(SAMPLE_STATIONS)
    7088
    """
    
    bikes_available_list = []
    stationID_list = []
    for sublist in range(len(stations)):
        bikes_available_list.append(stations[sublist][BIKES_AVAILABLE])
        stationID_list.append(stations[sublist][ID])
        
    return stationID_list[bikes_available_list.index(max(bikes_available_list))]
        

def get_stations_with_n_docks(n: int, stations: List[list]) -> List[int]:
    """Return a list containing the station IDs for the stations in stations
    that have at least n docks available, in the same order as they appear
    in stations.

    Precondition: n >= 0

    >>> get_stations_with_n_docks(2, SAMPLE_STATIONS)
    [7087, 7088]
    >>> get_stations_with_n_docks(5, SAMPLE_STATIONS)
    [7087]
    """
    
    stations_with_docks = []
    for sublist in range(len(stations)):
        if stations[sublist][DOCKS_AVAILABLE] >= n:
            stations_with_docks.append(stations[sublist][ID])
    
    return stations_with_docks


def get_direction(start_id: int, end_id: int, stations: List[list]) -> str:
    """ Return a string that contains the direction to travel to get from
    station start_id to station end_id according to data in stations.

    Precondition: start_id and end_id will appear in stations.

    >>> get_direction(7087, 7088, SAMPLE_STATIONS)
    'SOUTHWEST'
    """

    direction = None
    starting_point = []
    ending_point =  []
    for sublist in range(len(stations)):
        if start_id in stations[sublist]:
            starting_point = stations[sublist]
        elif end_id in stations[sublist]:
            ending_point = stations[sublist]
    if starting_point[LONGITUDE] > ending_point[LONGITUDE]:
        if starting_point[LATITUDE] > ending_point[LATITUDE]:
            direction = 'SOUTHWEST'
        elif starting_point[LATITUDE] < ending_point[LATITUDE]:
            direction = 'SOUTHEAST'
    elif starting_point[LONGITUDE] < ending_point[LONGITUDE]:
        if starting_point[LATITUDE] > ending_point[LATITUDE]:
            direction = 'NORTHWEST'
        elif starting_point[LATITUDE] < ending_point[LATITUDE]:
            direction = 'NORTHEAST'        
    elif starting_point[LONGITUDE] == ending_point[LONGITUDE]:
        if starting_point[LATITUDE] > ending_point[LATITUDE]:
            direction = 'WEST'
        elif starting_point[LATITUDE] < ending_point[LATITUDE]:
            direction = 'EAST' 
    elif starting_point[LATITUDE] == ending_point[LATITUDE]:
        if starting_point[LONGITUDE] > ending_point[LONGITUDE]:
            direction = 'SOUTH'
        elif starting_point[LONGITUDE] < ending_point[LONGITUDE]:
            direction = 'NORTH' 
            
    return direction


def rent_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for the station in stations with id station_id as if a single bike was
    removed, leaving an additional dock available. Return True if and only
    if the rental was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available - 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available + 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """
    used_station = []
    for sublist in range(len(stations)):
        if station_id in stations[sublist]:
            used_station = stations[sublist]
            if (used_station[BIKES_AVAILABLE] >= 1 and used_station[IS_RENTING] 
                == True):
                used_station[BIKES_AVAILABLE] = (used_station[BIKES_AVAILABLE] 
                                                 - 1)
                used_station[DOCKS_AVAILABLE] = (used_station[DOCKS_AVAILABLE] 
                                                 + 1)
                return True            
        elif not station_id in stations[sublist]:
            return False
        
    return False
        

def return_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for station in stations with id station_id as if a single bike was added,
    making an additional dock unavailable. Return True if and only if the
    return was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available + 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available - 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """
    
    used_station = []
    for sublist in range(len(stations)):
        if station_id in stations[sublist]:
            used_station = stations[sublist]
            if (used_station[DOCKS_AVAILABLE] >= 1 and 
                used_station[IS_RETURNING] == True):
                used_station[DOCKS_AVAILABLE] = (used_station[DOCKS_AVAILABLE] 
                                                 - 1)
                used_station[BIKES_AVAILABLE] = (used_station[BIKES_AVAILABLE] 
                                                 + 1)
                return True            
        elif not station_id in stations[sublist]:
            return False
        
    return False

def balance_all_bikes(stations: List[list]) -> int:
    """Calculate the percentage of bikes available across all stations
    and evenly distribute the bikes so that each station has as close to the
    overall percentage of bikes available as possible. Remove bikes from a
    station if and only if the station is renting and there is a bike
    available to rent, and return a bike if and only if the station is
    allowing returns and there is a dock available. Return the difference
    between the number of bikes rented and the number of bikes returned.

    >>> balance_all_bikes(HANDOUT_STATIONS)
    0
    >>> HANDOUT_STATIONS == [\
     [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 17, 14, True, True], \
     [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, \
     15, 8, 7, True, True]]
    True
    """
    
    bikes_numerator = 0
    capacity_denom = 0
    overall_percentage = 0
    station_percentage = 0
    bikes_rented = 0
    bikes_returned = 0
    for sublist in range(len(stations)):
        bikes_numerator = bikes_numerator + stations[sublist][BIKES_AVAILABLE]
        capacity_denom = capacity_denom + stations[sublist][CAPACITY]
        
    overall_percentage = round(bikes_numerator / capacity_denom, 2)
            
    for sublist in range(len(stations)):
        station_percentage = round(stations[sublist][BIKES_AVAILABLE] / 
                                   stations[sublist][CAPACITY], 2)
        while not -0.03 <= round(station_percentage - overall_percentage, 
                                 2) <= 0.03:
            if (stations[sublist][IS_RENTING] == True and station_percentage > 
                overall_percentage):
                bikes_rented = bikes_rented + 1
                stations[sublist][BIKES_AVAILABLE] = stations[
                    sublist][BIKES_AVAILABLE] - 1
                stations[sublist][DOCKS_AVAILABLE] = stations[
                    sublist][DOCKS_AVAILABLE] + 1
                station_percentage = round(stations[sublist][BIKES_AVAILABLE]
                                           / stations[sublist][CAPACITY], 2)
            elif (stations[sublist][IS_RETURNING] == True and station_percentage
                  < overall_percentage):
                bikes_returned = bikes_returned + 1
                stations[sublist][BIKES_AVAILABLE] = stations[
                    sublist][BIKES_AVAILABLE] + 1
                stations[sublist][DOCKS_AVAILABLE] = stations[sublist][
                    DOCKS_AVAILABLE] - 1
                station_percentage = round(stations[sublist][BIKES_AVAILABLE] / 
                                           stations[sublist][CAPACITY], 2)

    return bikes_rented - bikes_returned

if __name__ == '__main__':
    pass  

    # # To test your code with larger lists, you can uncomment the code below to
    # # read data from the provided CSV file.
    # stations_file = open('stations.csv')
    # bike_stations = csv_to_list(stations_file)
    # clean_data(bike_stations)

    # # For example,
    # print('Testing get_station_with_max_bikes: ', \
    #     get_station_with_max_bikes(bike_stations) == 7033)
