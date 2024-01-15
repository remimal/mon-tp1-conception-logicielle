if __name__=="__main__":
    from datetime import datetime
    import pytz

    # Get the timezone object for Reunion
    tz_Reunion = pytz.timezone('Indian/Reunion') 

    # Get the current time in Reunion
    datetime_Reunion = datetime.now(tz_Reunion)

    # Format the time as a string and print it
    print("Reunion time:", datetime_Reunion.strftime("%H:%M:%S"))

    # Get the timezone object for Paris
    tz_Paris = pytz.timezone('Europe/Paris')

    # Get the current time in Paris
    datetime_Paris = datetime.now(tz_Paris)

    # Format the time as a string and print it
    print("Paris time:", datetime_Paris.strftime("%H:%M:%S"))