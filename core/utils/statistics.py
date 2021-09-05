from typing import Any


def get_max_temperature(forecast_list: list) -> float:
    """
    An alternative function to this is the max()
    function which is part of the python standard library
    """
    max_temp_list = [forecast.get("maxtemp_c") for forecast in forecast_list]
    max_temp_list.sort(reverse=True)
    return round(max_temp_list[0], 2)


def get_min_temperature(forecast_list: list) -> float:
    """
    An alternative function to this is the min()
    function which is part of the python standard library
    """
    min_temp_list = [forecast.get("mintemp_c") for forecast in forecast_list]
    min_temp_list.sort()
    return round(min_temp_list[0], 2)


def get_average_temperature(forecast_list: list) -> float:
    average_temperature_list = [forecast.get("avgtemp_c") for forecast in forecast_list]
    total_average_temperature = sum(average_temperature_list)
    average_temperature_list = round(
        total_average_temperature / len(average_temperature_list), 2
    )
    return average_temperature_list


def get_median_temperature(forecast_list: list) -> Any:
    average_temperature_list = [forecast.get("avgtemp_c") for forecast in forecast_list]
    average_temperature_list.sort()
    temp_len = len(average_temperature_list)

    if temp_len == 0:
        return None
    elif temp_len % 2 == 0:
        sum_of_two_mid_values = (
            average_temperature_list[(temp_len - 1) // 2]
            + average_temperature_list[(temp_len + 1) // 2]
        )
        median_temperature = sum_of_two_mid_values / 2
        return round(median_temperature, 2)
    else:
        # explicityly converting the value to int as an alternative to
        # the floor division used above. just an alternative way to do the same thing
        median_index = int((temp_len - 1) / 2)
        median_temperature = average_temperature_list[median_index]
        return round(median_temperature, 2)
