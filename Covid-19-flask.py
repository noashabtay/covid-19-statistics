from flask import abort, Flask, request
import requests
import collections
import operator
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


app = Flask(__name__)


@app.route('/status/', methods=['GET'])
def status():
    """
    endpoint #4: return a value of success / fail to contact the backend API
    :return: JSON format
    """
    print("in stat")
    return {
        "status": "success"
    }


def create_the_dict(country, option):
    """
    This function creates a dictionary {"date" : cases_number} in the last 31 days
    using the response from the External API
    from a given country name and an option
    :param country:
    :param option: newCasesPeak, recoveredPeak , deathsPeak
    :return: dictionary {"date" : cases_number}
    """
    if country == None:
        return {}
    request_url = 'https://disease.sh/v3/covid-19/historical/' + country + '?lastdays=31'
    api_response = requests.get(request_url).json()
    if 'timeline' in api_response:
        dictionary = api_response['timeline'][option]
        return dictionary
    abort(404)


def dictionary_with_sub_values(dictionary):
    """
    This function creates ordered dictionary,
    ordered by date, with value of the cases in each date
    :param dictionary:
    :return: dictionary
    """
    ordered_dict = collections.OrderedDict()
    for key, value in dictionary.items():
        print(key, value)
        ordered_dict[key] = value
    ordered_dict_items = list(ordered_dict.items())
    items_pairs_after_sub = {
        ordered_dict_items[i + 1][0]:
            int(ordered_dict_items[i + 1][1]) - int(ordered_dict_items[i][1])
        for i in range(len(ordered_dict_items) - 1)
    }
    return items_pairs_after_sub


def get_peak(dictionary):
    """
    This function returns the highest value and his date from a given dictionary
    :param dictionary:
    :return:
    """
    items_pairs_after_sub = dictionary_with_sub_values(dictionary)
    peak_pair = max(items_pairs_after_sub.items(), key=operator.itemgetter(1))
    print(peak_pair)
    max_date_keeper = peak_pair[0]
    max_subvalue_keeper = peak_pair[1]
    print(items_pairs_after_sub)
    print(max_subvalue_keeper)
    print(max_date_keeper)
    return max_date_keeper, max_subvalue_keeper


def peak_in_30_days(country, option, method):
    """
    this function returns a JSON response of the Peak in the last 30 days
    from a given country name, option and method name
    :param country: given country
    :param option: newCasesPeak, recoveredPeak , deathsPeak
    :param method: method name
    :return: JSON format
    """
    dictionary = create_the_dict(country, option)
    print(dictionary)
    max_date_keeper, max_subvalue_keeper = get_peak(dictionary)
    return {
        "country": str(country),
        "method": method,
        "date": max_date_keeper,
        "value": str(max_subvalue_keeper)
    }


@app.route('/recoveredPeak/', methods=['GET'])
def recovered_peak():
    """
    endpoint #3: return the date and values of highest peak of recovered Covid-19 cases
     in the last 30 days for a required country.
    :return: JSON format
    """
    country = request.args.get('country')
    return peak_in_30_days(country, 'recovered', 'recoveredPeak'), 200


@app.route('/deathsPeak/', methods=['GET'])
def deaths_peak():
    """
    endpoint #2: return the date and values of highest peak of death Covid-19 cases
     in the last 30 days for a required country.
    :return: JSON format
    """
    country = request.args.get('country')
    return peak_in_30_days(country, 'deaths', 'deathsPeak'), 200


@app.route('/newCasesPeak/', methods=['GET'])
def new_cases_peak():
    """
    endpoint #1: return the date and values of highest peak of new Covid-19 cases
     in the last 30 days for a required country.
    :return: JSON format
    """
    country = request.args.get('country')
    return peak_in_30_days(country, 'cases', 'newCasesPeak'), 200


@app.errorhandler(404)
def page_not_found(e):
    return {}, 404


if __name__ == '__main__':
    app.run(debug=False)
