def solution(season, dayCount, initialPhase):
    # input: string, int, string
    # output: string
    
    # season is the MONTH
    # dayCount is the day in that month
    # initial phase is considered from the beginning of the year
    # use .get() to get the value of the dict
    # use .index() to get the index of the dict
    
    lunar_phases = ["NewMoon", "Crescent", "Quarter", "Gibbous", "Full", "Waning", "Eclipse", "Twilight"]
    seasons = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

    months = list(seasons.keys())
    total = 0
    
    for month in months:
        if month == season:
            break
        total += seasons[month]
        
    total += dayCount - 1

    index = lunar_phases.index(initialPhase)
    curr_index = (index + total) % len(lunar_phases)
    
    return lunar_phases[curr_index]