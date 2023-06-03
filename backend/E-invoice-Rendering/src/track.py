'''this module tracks server activity and logs it'''
from datetime import datetime

def log(route, start_time, status):
    '''
    Given a route name, start time, status code, log the end point call to log_file.txt

    Arguments:
        route: str
        start_time: date object

    Return value:
        None
    '''
    end_time = datetime.now()
    time_took = end_time - start_time
    log_file = open("log_file.txt", "a")
    log_file.write("ROUTE: [" + route + "] TIME: " + " [" + str(end_time) + "] " + "TIME TAKEN: [" + str(time_took) + "] STATUS: [" + str(status) + "]\n")
