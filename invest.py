### Check the README for additional information ###

# 1. Create a function called number_shares_a() that only accepts an investment amount and returns the number of shares of Fund A which that investment could buy today.
# Then call the function with two different amounts to ensure that it works properly.

def number_shares_a(budget):
    shares = int(budget/5.95)
    return shares
    
print (number_shares_a(17))
print (number_shares_a(23))
    


# 2. Create a more-general function called number_shares() that takes in an investment amount and a fund. It should return the number of shares of that fund which that investment could buy today.
# Then call the function with different amounts and different funds.

def number_shares(amount, fund):
    if fund == 'A':
        return int(amount/5.95)
    elif fund == 'B':
        return int(amount/21.01)
    elif fund == 'C':
        return int(amount/23.01)
    elif fund == 'D':
        return int(amount/1.83)

print (number_shares(140, 'A'))
print (number_shares(130, 'B'))
print (number_shares(93, 'C'))
print (number_shares(34, 'D'))
        
    
    

# 3. Create a more flexible calculator method called history_shares() that takes in an investment amount, fund, and year and returns the number of shares that money could buy in that year.

def history_shares(amount, fund, year):
    if fund == 'A':
        if year == 1980:
            return int(amount/2.5)
        elif year == 1996:
            return int(amount/3.75)
        elif year == 2012:
            return int(amount/4.1)
        elif year == 2016:
            return int(amount/5.1)
        elif year == 2019:
            return int(amount/5.95)
    elif fund == 'B':
        if year == 1980:
            return int(amount/12.02)
        elif year == 1996:
            return int(amount/14.10)
        elif year == 2012:
            return int(amount/15.76)
        elif year == 2016:
            return int(amount/18.08)
        elif year == 2019:
            return int(amount/21.01)
    elif fund == 'C':
        if year == 1980:
            return int(amount/8.65)
        elif year == 1996:
            return int(amount/8.03)
        elif year == 2012:
            return int(amount/11.15)
        elif year == 2016:
            return int(amount/19.82)
        elif year == 2019:
            return int(amount/23.01)

### Advanced Bonus Challenge ###

# 4. What is the change of an investment over time? Create a method calculate_profit() that accepts an initial investment amount, the fund, and the initial investment year, and returns the current profit made on the initial investment. This is an open ended one - there are many ways to do this!



# Bonus: Format the output of the function as USD currency, so instead of 1000, the function should output $1000.00.



### Double Advanced Bonus Challenge ###

# 5. Which investment is the best? Create a method best_choice() that accepts an investment amount and a year, and returns the name of the fund that would have made the most money for the investor.



# Bonus: In addition to the name of the fund, also return how much money the investor would have earned.



### Triple Advanced Bonus Challenge ###

# 6. Consider the current profit difference between making an investment in a fund several years apart. Create a method investment_diff() that accepts an investment amount, a fund, and two year values and returns the current profit difference if the money had been made earlier vs. later.



# Bonus: How can you account for a sloppy investment advisor who puts the years in a different order than you expect?


