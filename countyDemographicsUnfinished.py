import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(high_income_counties(counties))
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(lowest_median_income(counties))
    print(state_with_most_counties(counties))

def high_income_counties(counties):
    """Return a LIST of the counties with a median household income over $90,000."""
    list; high_income_counties
    for data in county_demographics
        return counties median_houseold_income > $90,000;
        add county to high_income_counties
    return list high_income_counties
    

def lowest_median_income(counties):
    """Return a name of a county with the lowest median household income"""
    
    if median_houseold_income < 
    list; lowest_median_income
    for data in county_demographics
        return 
        

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    #Hint: you can use < to compare strings in Python. ex) "cat" < "dog" gives the value True

    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""    
    if percent_most_under_18 < 

def county_most_under_18(counties):
    """Return the name a county with the highest percent of under 18 year olds."""
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #1. Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    
    #2. Find the state in the dictionary with the most counties
    
    #3. Return the state with the most counties
    
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""

if __name__ == '__main__':
    main()

    #make an empty list
    #for each county in the list of counties:
    #   If the county's median household income is >$90,000:
    #       append the county's name to the list
    #return the list
