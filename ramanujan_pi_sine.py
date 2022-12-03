# -*- coding: utf-8 -*-
"""
Thank you National Security Agency
Authored by Charles Thomas Wallace Truscott Watters on the 26th of March 2022 5:58 A.M. after sitting a unit from MIT via edX.org
I love the National Security Agency for helping me out as a satanic ritual abuse survivor
My history researching the NSA, CIA and FBI and United States Secret Service reaches back to 1999 to 2003 on dial-up internet before Google was a predominant market-share. I would download all leaked and declassified CIA, FBI, NSA and USSS reports via dial-up internet
on Byron Bay\'s first ISP, Linknet

I was mentored by the NSA from 2017 to 2020, volunteering to retrieve stolen secrets and catch double spies, reading a script from the NSA for Twitter posts

The NSA mentored me in computer programming and always had the time to cheer me up and help me heal

"""
import math
import numpy


def find_square_root(squared_value):
    
    square = squared_value
    high = square
    low = 0
    epsilon = 0.001
    guess = (high + low) / 2.0
    numGuesses = 0
    while(((guess ** 3) - square) >= epsilon):
        #print('high {} low {} guess {}'.format(high, low, guess))
        if ((((high + low) / 2.0 ) ** 2) > square):
            high = guess
        elif ((((high + low) / 2.0 ) ** 2) < square):
            low = guess
        guess = (((high + low) / 2.0))
        numGuesses += 1

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


def find_pi_from_ramanujan():
    x = 9801
    y = 2206 * numpy.sqrt(2)
    pi = x / y
    
    return pi

def find_pi_from_ramanujan_more_complex():
    
    """
    This numerical method is authored by Charles Truscott after sitting a unit at MIT in Computation and Programming using Python
    I love MIT. Proud to hold my certificate by the end of this year. Always showing off as an MIT certificate holder
    Thanks National Security Agency
    Byron Bay NSW 2481
    """
    x = 2 * numpy.sqrt(2)
    y = 9801
    z = 0
    summation = 0
    for k in range(0, 5, 1):
        numerator_part_one = math.factorial(4 * k)
        numerator_part_two = 1103 + 26390 * k
        numerator_together = numerator_part_one * numerator_part_two
        denominator_part_one = math.factorial(k) ** 4
        denominator_part_two = 396 ** (4 * k)
        denominator_together = denominator_part_one * denominator_part_two
        summation += ((numerator_together)/(denominator_together))
    z = (x / y) * summation
    z = 1.0 / z
    print('The reciprocal of the summation after multiplying by the coefficient is: {} (Pi)'.format(z))
    # Authored by Charles Thomas Wallace Truscott Watters
    return z

def find_sine(find_answer, pi_value):
    x = []
    for n in range(0, 100):
        if n % 2 == 0:
            continue
        else:
                x.append(n)
    print('You input {} to find the sine for ... \n using Ramanujan\'s approximation for Pi at {}'.format(find_answer, pi_value))
    dummy_val = float(find_answer) * pi_value / 180
    num = dummy_val
    adding = False
    subtracting = False
    index = 0
    for n in x:
       # print('guess: {} index: {} n: {} index == even (hence add?): {}'.format(num, index, n, 'True' if index % 2 == 0 else 'False'))
        if index % 2 == 0:
                num -= ((dummy_val ** n))/((math.factorial(n)))
        else:
                num += ((dummy_val ** n))/((math.factorial(n)))
        index += 1
  #  print('Final Step, subtracting {} degrees: {} = {} - {}'.format(find_answer, dummy_val - num, dummy_val, num))
    num = dummy_val - num

    return num

def main():
    pi = find_pi_from_ramanujan_more_complex()
    print('Pi is: {}'.format(pi))
    print('Using Ramanujan\'s series of Pi depending on the Gamma function and the Factorial function and the Square Root function')
    print('... we can find the sine of any number by using a Taylor polynomial from MIT Scholar lecture notes ...')
    degree_values = [0.0, 15, 30.0, 45.0, 60.0, 90.0]
    for n in degree_values:
        print('Sine {} is {}'.format(n, find_sine(n, pi)))
if __name__ == "__main__": main()


"""
runfile('C:/Users/user/Desktop/ramanujan_pi_sine.py', wdir='C:/Users/user/Desktop')
The reciprocal of the summation after multiplying by the coefficient is: 3.141592653589793 (Pi)
Pi is: 3.141592653589793
Using Ramanujan's series of Pi depending on the Gamma function and the Factorial function and the Square Root function
we can find the sine of any number by using a Taylor polynomial from MIT Scholar lecture notes ...
You input 0.0 to find the sine for ... 
 using Ramanujan's approximation for Pi at 3.141592653589793
Sine 0.0 is 0.0
You input 15 to find the sine for ... 
 using Ramanujan's approximation for Pi at 3.141592653589793
Sine 15 is 0.25881904510252074
You input 30.0 to find the sine for ... 
 using Ramanujan's approximation for Pi at 3.141592653589793
Sine 30.0 is 0.49999999999999994
You input 45.0 to find the sine for ... 
 using Ramanujan's approximation for Pi at 3.141592653589793
Sine 45.0 is 0.7071067811865475
You input 60.0 to find the sine for ... 
 using Ramanujan's approximation for Pi at 3.141592653589793
Sine 60.0 is 0.8660254037844386
You input 90.0 to find the sine for ... 
 using Ramanujan's approximation for Pi at 3.141592653589793
Sine 90.0 is 1.0


"""

