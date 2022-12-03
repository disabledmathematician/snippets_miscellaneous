# -*- coding: utf-8 -*-
import math
import sys
import numpy

"""
I LOVE MIT

INFINITE SERIES FOR THE SINE, COSINE, AND TANGENT

CHARLES THOMAS WALLACE TRUSCOTT

BYRON BAY NSW 2481

"""


def ramanujans_pi():
    
    """
    This numerical method is authored by Charles Truscott after sitting a unit at MIT in Computation and Programming using Python
    I love MIT. Proud to hold my certificate by the end of this year. Always showing off as an MIT certificate holder
    Thanks National Security Agency
    Byron Bay NSW 2481
    """
    x = 2 * numpy.sqrt(2)
    y = 9801
    pi = 0
    summation = 0
    for k in range(0, 5, 1):
        numerator = ((math.factorial(4 * k)) * ((1103 + (26390 * k))))
        denominator = ((math.factorial(k) ** 4) * ((396 ** (4 * k))))
        summation += numerator / denominator
    pi = (x / y) * summation
    pi = 1.0 / pi
    print('The reciprocal of the summation after multiplying by the coefficient is: {} (Pi)'.format(pi))
    # Authored by Charles Thomas Wallace Truscott Watters
    return pi

def sine_taylor(find_answer, pi_value):
    odd_numbers = []
    for n in range(0, 100):
        if n % 2 == 0:
            continue
        else:
                odd_numbers.append(n)
#    print('You input {} to find the sine for ... \n using Ramanujan\'s approximation for Pi at {}'.format(find_answer, pi_value))
    dummy_val = float(find_answer) * pi_value / 180
    num = dummy_val
    index = 0
    for n in odd_numbers:
#        print('approximation of sine is currently: {} -/+{}!? {}'.format(num, n, 'Subtract x ^ n / n!' if index % 2 == 0 else 'Add x ^ n / n!'))
        if index % 2 == 0:
                num -= ((dummy_val ** n))/((math.factorial(n)))
        else:
                num += ((dummy_val ** n))/((math.factorial(n)))
        index += 1
#    print(pi)
#    print('Subtracting x: {}'.format(num))
    num = dummy_val - num
#    print('{}'.format(num))
#    print('Sine of {} is {}'.format(find_answer, num))
    # Authored by Charles Thomas Wallace Truscott Watters
    return num


def cosine_taylor(find_answer, pi_value):
    if find_answer == 90.0:
        return 0
    elif find_answer == 0.0:
        return 1
    even_numbers = []
    for n in range(0, 100):
        if n % 2 == 0:
            even_numbers.append(n)
        else:
            continue
#    print('You input {} to find the cosine for ... \n using Ramanujan\'s approximation for Pi at {}'.format(find_answer, pi_value))
    dummy_val = float(find_answer) * pi_value / 180
    num = 1
    index = 0
    for n in even_numbers:
#      print('approximation of cosine is currently: {} -/+{}!? {}'.format(num, n, 'Add x ^ n / n!' if index % 2 == 0 else 'Subtract n ^ x / n!'))
      if index % 2 == 0:
          num += ((dummy_val ** n))/((math.factorial(n)))
      else:
          num -= ((dummy_val ** n))/((math.factorial(n)))
      index += 1
#    print('Subtracting 1 from {}'.format(num))
    num = 1 - num
#    print('{}')
#    print('Cosine of {} is {}'.format(find_answer, num))
    return abs(num)
    
def find_tangent(sine_value, cosine_value):
    if sine_value == 0 or cosine_value == 0:
        return 0
    else:
        return sine_value / cosine_value


def main():
    pi = ramanujans_pi()
    print('Authored by Charles T.W. Truscott Watters for 6.0001 extra-curricular (sitting via edX.org)')
    fractions = []
#    even_numbers_up_to_10 = []
#    odd_numbers_up_to_10 = []
#    for x in range(1, 10, 1):
#        if x % 2 == 0:
#            even_numbers_up_to_10.append(x)
#        elif x % 2 == 1:
#            odd_numbers_up_to_10.append(x)
        
#    for x in even_numbers_up_to_10:
#        for y in odd_numbers_up_to_10:
#            fractions.append(x/y)
    
    for x in range(1, 10, 1):
        fractions.append(1/x)
        fractions.append(2/x)
        fractions.append(3/x)
        fractions.append(4/x)

    fractions_copy = []
    for x in fractions:
        if float(x) < float(1.0):
            fractions_copy.append(x)

 #   print(fractions_copy)
    
    degrees = [0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0]
    degrees_copy = []
    for degree in degrees:
        for fraction in fractions_copy:
            degrees_copy.append(float(degree) + float(fraction))
#    print(degrees_copy)
    for degree in degrees_copy:
        sine_of_degree = sine_taylor(degree, pi)
        cosine_of_degree = cosine_taylor(degree, pi)
        tangent_of_degree = find_tangent(sine_of_degree, cosine_of_degree)
        print('Sine {} is {}\t\tCosine {} is {}\t\tTangent {} is {}'.format(numpy.round(degree, 4), numpy.round(sine_of_degree, 4), numpy.round(degree, 4), numpy.round(cosine_of_degree, 4), numpy.round(degree, 4), numpy.round(tangent_of_degree, 4)))
        
if __name__ == "__main__": main()



"""
runfile('C:/Users/user/Desktop/INFINITE_SERIES_CHARLES_TRUSCOTT.py', wdir='C:/Users/user/Desktop')
The reciprocal of the summation after multiplying by the coefficient is: 3.141592653589793 (Pi)
Authored by Charles T.W. Truscott Watters for 6.0001 extra-curricular (sitting via edX.org)
Sine 0.5 is 0.0087		Cosine 0.5 is 1.0		Tangent 0.5 is 0.0087
Sine 0.33 is 0.0058		Cosine 0.33 is 1.0		Tangent 0.33 is 0.0058
Sine 0.67 is 0.0116		Cosine 0.67 is 0.9999		Tangent 0.67 is 0.0116
Sine 0.25 is 0.0044		Cosine 0.25 is 1.0		Tangent 0.25 is 0.0044
Sine 0.5 is 0.0087		Cosine 0.5 is 1.0		Tangent 0.5 is 0.0087
Sine 0.75 is 0.0131		Cosine 0.75 is 0.9999		Tangent 0.75 is 0.0131
Sine 0.2 is 0.0035		Cosine 0.2 is 1.0		Tangent 0.2 is 0.0035
Sine 0.4 is 0.007		Cosine 0.4 is 1.0		Tangent 0.4 is 0.007
Sine 0.6 is 0.0105		Cosine 0.6 is 0.9999		Tangent 0.6 is 0.0105
Sine 0.8 is 0.014		Cosine 0.8 is 0.9999		Tangent 0.8 is 0.014
Sine 0.17 is 0.0029		Cosine 0.17 is 1.0		Tangent 0.17 is 0.0029
Sine 0.33 is 0.0058		Cosine 0.33 is 1.0		Tangent 0.33 is 0.0058
Sine 0.5 is 0.0087		Cosine 0.5 is 1.0		Tangent 0.5 is 0.0087
Sine 0.67 is 0.0116		Cosine 0.67 is 0.9999		Tangent 0.67 is 0.0116
Sine 0.14 is 0.0025		Cosine 0.14 is 1.0		Tangent 0.14 is 0.0025
Sine 0.29 is 0.005		Cosine 0.29 is 1.0		Tangent 0.29 is 0.005
Sine 0.43 is 0.0075		Cosine 0.43 is 1.0		Tangent 0.43 is 0.0075
Sine 0.57 is 0.01		Cosine 0.57 is 1.0		Tangent 0.57 is 0.01
Sine 0.12 is 0.0022		Cosine 0.12 is 1.0		Tangent 0.12 is 0.0022
Sine 0.25 is 0.0044		Cosine 0.25 is 1.0		Tangent 0.25 is 0.0044
Sine 0.38 is 0.0065		Cosine 0.38 is 1.0		Tangent 0.38 is 0.0065
Sine 0.5 is 0.0087		Cosine 0.5 is 1.0		Tangent 0.5 is 0.0087
Sine 0.11 is 0.0019		Cosine 0.11 is 1.0		Tangent 0.11 is 0.0019
Sine 0.22 is 0.0039		Cosine 0.22 is 1.0		Tangent 0.22 is 0.0039
Sine 0.33 is 0.0058		Cosine 0.33 is 1.0		Tangent 0.33 is 0.0058
Sine 0.44 is 0.0078		Cosine 0.44 is 1.0		Tangent 0.44 is 0.0078
Sine 15.5 is 0.2672		Cosine 15.5 is 0.9636		Tangent 15.5 is 0.2773
Sine 15.33 is 0.2644		Cosine 15.33 is 0.9644		Tangent 15.33 is 0.2742
Sine 15.67 is 0.27		Cosine 15.67 is 0.9628		Tangent 15.67 is 0.2805
Sine 15.25 is 0.263		Cosine 15.25 is 0.9648		Tangent 15.25 is 0.2726
Sine 15.5 is 0.2672		Cosine 15.5 is 0.9636		Tangent 15.5 is 0.2773
Sine 15.75 is 0.2714		Cosine 15.75 is 0.9625		Tangent 15.75 is 0.282
Sine 15.2 is 0.2622		Cosine 15.2 is 0.965		Tangent 15.2 is 0.2717
Sine 15.4 is 0.2656		Cosine 15.4 is 0.9641		Tangent 15.4 is 0.2754
Sine 15.6 is 0.2689		Cosine 15.6 is 0.9632		Tangent 15.6 is 0.2792
Sine 15.8 is 0.2723		Cosine 15.8 is 0.9622		Tangent 15.8 is 0.283
Sine 15.17 is 0.2616		Cosine 15.17 is 0.9652		Tangent 15.17 is 0.2711
Sine 15.33 is 0.2644		Cosine 15.33 is 0.9644		Tangent 15.33 is 0.2742
Sine 15.5 is 0.2672		Cosine 15.5 is 0.9636		Tangent 15.5 is 0.2773
Sine 15.67 is 0.27		Cosine 15.67 is 0.9628		Tangent 15.67 is 0.2805
Sine 15.14 is 0.2612		Cosine 15.14 is 0.9653		Tangent 15.14 is 0.2706
Sine 15.29 is 0.2636		Cosine 15.29 is 0.9646		Tangent 15.29 is 0.2733
Sine 15.43 is 0.266		Cosine 15.43 is 0.964		Tangent 15.43 is 0.276
Sine 15.57 is 0.2684		Cosine 15.57 is 0.9633		Tangent 15.57 is 0.2787
Sine 15.12 is 0.2609		Cosine 15.12 is 0.9654		Tangent 15.12 is 0.2703
Sine 15.25 is 0.263		Cosine 15.25 is 0.9648		Tangent 15.25 is 0.2726
Sine 15.38 is 0.2651		Cosine 15.38 is 0.9642		Tangent 15.38 is 0.275
Sine 15.5 is 0.2672		Cosine 15.5 is 0.9636		Tangent 15.5 is 0.2773
Sine 15.11 is 0.2607		Cosine 15.11 is 0.9654		Tangent 15.11 is 0.27
Sine 15.22 is 0.2626		Cosine 15.22 is 0.9649		Tangent 15.22 is 0.2721
Sine 15.33 is 0.2644		Cosine 15.33 is 0.9644		Tangent 15.33 is 0.2742
Sine 15.44 is 0.2663		Cosine 15.44 is 0.9639		Tangent 15.44 is 0.2763
Sine 30.5 is 0.5075		Cosine 30.5 is 0.8616		Tangent 30.5 is 0.589
Sine 30.33 is 0.505		Cosine 30.33 is 0.8631		Tangent 30.33 is 0.5851
Sine 30.67 is 0.51		Cosine 30.67 is 0.8601		Tangent 30.67 is 0.593
Sine 30.25 is 0.5038		Cosine 30.25 is 0.8638		Tangent 30.25 is 0.5832
Sine 30.5 is 0.5075		Cosine 30.5 is 0.8616		Tangent 30.5 is 0.589
Sine 30.75 is 0.5113		Cosine 30.75 is 0.8594		Tangent 30.75 is 0.5949
Sine 30.2 is 0.503		Cosine 30.2 is 0.8643		Tangent 30.2 is 0.582
Sine 30.4 is 0.506		Cosine 30.4 is 0.8625		Tangent 30.4 is 0.5867
Sine 30.6 is 0.509		Cosine 30.6 is 0.8607		Tangent 30.6 is 0.5914
Sine 30.8 is 0.512		Cosine 30.8 is 0.859		Tangent 30.8 is 0.5961
Sine 30.17 is 0.5025		Cosine 30.17 is 0.8646		Tangent 30.17 is 0.5812
Sine 30.33 is 0.505		Cosine 30.33 is 0.8631		Tangent 30.33 is 0.5851
Sine 30.5 is 0.5075		Cosine 30.5 is 0.8616		Tangent 30.5 is 0.589
Sine 30.67 is 0.51		Cosine 30.67 is 0.8601		Tangent 30.67 is 0.593
Sine 30.14 is 0.5022		Cosine 30.14 is 0.8648		Tangent 30.14 is 0.5807
Sine 30.29 is 0.5043		Cosine 30.29 is 0.8635		Tangent 30.29 is 0.584
Sine 30.43 is 0.5065		Cosine 30.43 is 0.8623		Tangent 30.43 is 0.5874
Sine 30.57 is 0.5086		Cosine 30.57 is 0.861		Tangent 30.57 is 0.5907
Sine 30.12 is 0.5019		Cosine 30.12 is 0.8649		Tangent 30.12 is 0.5803
Sine 30.25 is 0.5038		Cosine 30.25 is 0.8638		Tangent 30.25 is 0.5832
Sine 30.38 is 0.5057		Cosine 30.38 is 0.8627		Tangent 30.38 is 0.5861
Sine 30.5 is 0.5075		Cosine 30.5 is 0.8616		Tangent 30.5 is 0.589
Sine 30.11 is 0.5017		Cosine 30.11 is 0.8651		Tangent 30.11 is 0.5799
Sine 30.22 is 0.5034		Cosine 30.22 is 0.8641		Tangent 30.22 is 0.5825
Sine 30.33 is 0.505		Cosine 30.33 is 0.8631		Tangent 30.33 is 0.5851
Sine 30.44 is 0.5067		Cosine 30.44 is 0.8621		Tangent 30.44 is 0.5877
Sine 45.5 is 0.7133		Cosine 45.5 is 0.7009		Tangent 45.5 is 1.0176
Sine 45.33 is 0.7112		Cosine 45.33 is 0.703		Tangent 45.33 is 1.0117
Sine 45.67 is 0.7153		Cosine 45.67 is 0.6988		Tangent 45.67 is 1.0235
Sine 45.25 is 0.7102		Cosine 45.25 is 0.704		Tangent 45.25 is 1.0088
Sine 45.5 is 0.7133		Cosine 45.5 is 0.7009		Tangent 45.5 is 1.0176
Sine 45.75 is 0.7163		Cosine 45.75 is 0.6978		Tangent 45.75 is 1.0265
Sine 45.2 is 0.7096		Cosine 45.2 is 0.7046		Tangent 45.2 is 1.007
Sine 45.4 is 0.712		Cosine 45.4 is 0.7022		Tangent 45.4 is 1.0141
Sine 45.6 is 0.7145		Cosine 45.6 is 0.6997		Tangent 45.6 is 1.0212
Sine 45.8 is 0.7169		Cosine 45.8 is 0.6972		Tangent 45.8 is 1.0283
Sine 45.17 is 0.7092		Cosine 45.17 is 0.705		Tangent 45.17 is 1.0058
Sine 45.33 is 0.7112		Cosine 45.33 is 0.703		Tangent 45.33 is 1.0117
Sine 45.5 is 0.7133		Cosine 45.5 is 0.7009		Tangent 45.5 is 1.0176
Sine 45.67 is 0.7153		Cosine 45.67 is 0.6988		Tangent 45.67 is 1.0235
Sine 45.14 is 0.7089		Cosine 45.14 is 0.7053		Tangent 45.14 is 1.005
Sine 45.29 is 0.7106		Cosine 45.29 is 0.7036		Tangent 45.29 is 1.01
Sine 45.43 is 0.7124		Cosine 45.43 is 0.7018		Tangent 45.43 is 1.0151
Sine 45.57 is 0.7141		Cosine 45.57 is 0.7		Tangent 45.57 is 1.0201
Sine 45.12 is 0.7086		Cosine 45.12 is 0.7056		Tangent 45.12 is 1.0044
Sine 45.25 is 0.7102		Cosine 45.25 is 0.704		Tangent 45.25 is 1.0088
Sine 45.38 is 0.7117		Cosine 45.38 is 0.7025		Tangent 45.38 is 1.0132
Sine 45.5 is 0.7133		Cosine 45.5 is 0.7009		Tangent 45.5 is 1.0176
Sine 45.11 is 0.7085		Cosine 45.11 is 0.7057		Tangent 45.11 is 1.0039
Sine 45.22 is 0.7098		Cosine 45.22 is 0.7044		Tangent 45.22 is 1.0078
Sine 45.33 is 0.7112		Cosine 45.33 is 0.703		Tangent 45.33 is 1.0117
Sine 45.44 is 0.7126		Cosine 45.44 is 0.7016		Tangent 45.44 is 1.0156
Sine 60.5 is 0.8704		Cosine 60.5 is 0.4924		Tangent 60.5 is 1.7675
Sine 60.33 is 0.8689		Cosine 60.33 is 0.495		Tangent 60.33 is 1.7556
Sine 60.67 is 0.8718		Cosine 60.67 is 0.4899		Tangent 60.67 is 1.7796
Sine 60.25 is 0.8682		Cosine 60.25 is 0.4962		Tangent 60.25 is 1.7496
Sine 60.5 is 0.8704		Cosine 60.5 is 0.4924		Tangent 60.5 is 1.7675
Sine 60.75 is 0.8725		Cosine 60.75 is 0.4886		Tangent 60.75 is 1.7856
Sine 60.2 is 0.8678		Cosine 60.2 is 0.497		Tangent 60.2 is 1.7461
Sine 60.4 is 0.8695		Cosine 60.4 is 0.4939		Tangent 60.4 is 1.7603
Sine 60.6 is 0.8712		Cosine 60.6 is 0.4909		Tangent 60.6 is 1.7747
Sine 60.8 is 0.8729		Cosine 60.8 is 0.4879		Tangent 60.8 is 1.7893
Sine 60.17 is 0.8675		Cosine 60.17 is 0.4975		Tangent 60.17 is 1.7437
Sine 60.33 is 0.8689		Cosine 60.33 is 0.495		Tangent 60.33 is 1.7556
Sine 60.5 is 0.8704		Cosine 60.5 is 0.4924		Tangent 60.5 is 1.7675
Sine 60.67 is 0.8718		Cosine 60.67 is 0.4899		Tangent 60.67 is 1.7796
Sine 60.14 is 0.8673		Cosine 60.14 is 0.4978		Tangent 60.14 is 1.7421
Sine 60.29 is 0.8685		Cosine 60.29 is 0.4957		Tangent 60.29 is 1.7522
Sine 60.43 is 0.8697		Cosine 60.43 is 0.4935		Tangent 60.43 is 1.7624
Sine 60.57 is 0.871		Cosine 60.57 is 0.4913		Tangent 60.57 is 1.7726
Sine 60.12 is 0.8671		Cosine 60.12 is 0.4981		Tangent 60.12 is 1.7408
Sine 60.25 is 0.8682		Cosine 60.25 is 0.4962		Tangent 60.25 is 1.7496
Sine 60.38 is 0.8693		Cosine 60.38 is 0.4943		Tangent 60.38 is 1.7585
Sine 60.5 is 0.8704		Cosine 60.5 is 0.4924		Tangent 60.5 is 1.7675
Sine 60.11 is 0.867		Cosine 60.11 is 0.4983		Tangent 60.11 is 1.7398
Sine 60.22 is 0.868		Cosine 60.22 is 0.4966		Tangent 60.22 is 1.7477
Sine 60.33 is 0.8689		Cosine 60.33 is 0.495		Tangent 60.33 is 1.7556
Sine 60.44 is 0.8699		Cosine 60.44 is 0.4933		Tangent 60.44 is 1.7635
Sine 75.5 is 0.9681		Cosine 75.5 is 0.2504		Tangent 75.5 is 3.8667
Sine 75.33 is 0.9674		Cosine 75.33 is 0.2532		Tangent 75.33 is 3.8208
Sine 75.67 is 0.9689		Cosine 75.67 is 0.2476		Tangent 75.67 is 3.9136
Sine 75.25 is 0.967		Cosine 75.25 is 0.2546		Tangent 75.25 is 3.7983
Sine 75.5 is 0.9681		Cosine 75.5 is 0.2504		Tangent 75.5 is 3.8667
Sine 75.75 is 0.9692		Cosine 75.75 is 0.2462		Tangent 75.75 is 3.9375
Sine 75.2 is 0.9668		Cosine 75.2 is 0.2554		Tangent 75.2 is 3.7848
Sine 75.4 is 0.9677		Cosine 75.4 is 0.2521		Tangent 75.4 is 3.8391
Sine 75.6 is 0.9686		Cosine 75.6 is 0.2487		Tangent 75.6 is 3.8947
Sine 75.8 is 0.9694		Cosine 75.8 is 0.2453		Tangent 75.8 is 3.952
Sine 75.17 is 0.9667		Cosine 75.17 is 0.256		Tangent 75.17 is 3.776
Sine 75.33 is 0.9674		Cosine 75.33 is 0.2532		Tangent 75.33 is 3.8208
Sine 75.5 is 0.9681		Cosine 75.5 is 0.2504		Tangent 75.5 is 3.8667
Sine 75.67 is 0.9689		Cosine 75.67 is 0.2476		Tangent 75.67 is 3.9136
Sine 75.14 is 0.9666		Cosine 75.14 is 0.2564		Tangent 75.14 is 3.7696
Sine 75.29 is 0.9672		Cosine 75.29 is 0.254		Tangent 75.29 is 3.8079
Sine 75.43 is 0.9678		Cosine 75.43 is 0.2516		Tangent 75.43 is 3.8469
Sine 75.57 is 0.9685		Cosine 75.57 is 0.2492		Tangent 75.57 is 3.8867
Sine 75.12 is 0.9665		Cosine 75.12 is 0.2567		Tangent 75.12 is 3.7649
Sine 75.25 is 0.967		Cosine 75.25 is 0.2546		Tangent 75.25 is 3.7983
Sine 75.38 is 0.9676		Cosine 75.38 is 0.2525		Tangent 75.38 is 3.8322
Sine 75.5 is 0.9681		Cosine 75.5 is 0.2504		Tangent 75.5 is 3.8667
Sine 75.11 is 0.9664		Cosine 75.11 is 0.2569		Tangent 75.11 is 3.7612
Sine 75.22 is 0.9669		Cosine 75.22 is 0.2551		Tangent 75.22 is 3.7908
Sine 75.33 is 0.9674		Cosine 75.33 is 0.2532		Tangent 75.33 is 3.8208
Sine 75.44 is 0.9679		Cosine 75.44 is 0.2513		Tangent 75.44 is 3.8513
Sine 90.5 is 1.0		Cosine 90.5 is 0.0087		Tangent 90.5 is 114.5887
Sine 90.33 is 1.0		Cosine 90.33 is 0.0058		Tangent 90.33 is 171.8854
Sine 90.67 is 0.9999		Cosine 90.67 is 0.0116		Tangent 90.67 is 85.9398
Sine 90.25 is 1.0		Cosine 90.25 is 0.0044		Tangent 90.25 is 229.1817
Sine 90.5 is 1.0		Cosine 90.5 is 0.0087		Tangent 90.5 is 114.5887
Sine 90.75 is 0.9999		Cosine 90.75 is 0.0131		Tangent 90.75 is 76.39
Sine 90.2 is 1.0		Cosine 90.2 is 0.0035		Tangent 90.2 is 286.4777
Sine 90.4 is 1.0		Cosine 90.4 is 0.007		Tangent 90.4 is 143.2371
Sine 90.6 is 0.9999		Cosine 90.6 is 0.0105		Tangent 90.6 is 95.4895
Sine 90.8 is 0.9999		Cosine 90.8 is 0.014		Tangent 90.8 is 71.6151
Sine 90.17 is 1.0		Cosine 90.17 is 0.0029		Tangent 90.17 is 343.7737
Sine 90.33 is 1.0		Cosine 90.33 is 0.0058		Tangent 90.33 is 171.8854
Sine 90.5 is 1.0		Cosine 90.5 is 0.0087		Tangent 90.5 is 114.5887
Sine 90.67 is 0.9999		Cosine 90.67 is 0.0116		Tangent 90.67 is 85.9398
Sine 90.14 is 1.0		Cosine 90.14 is 0.0025		Tangent 90.14 is 401.0696
Sine 90.29 is 1.0		Cosine 90.29 is 0.005		Tangent 90.29 is 200.5336
Sine 90.43 is 1.0		Cosine 90.43 is 0.0075		Tangent 90.43 is 133.6877
Sine 90.57 is 1.0		Cosine 90.57 is 0.01		Tangent 90.57 is 100.2643
Sine 90.12 is 1.0		Cosine 90.12 is 0.0022		Tangent 90.12 is 458.3655
Sine 90.25 is 1.0		Cosine 90.25 is 0.0044		Tangent 90.25 is 229.1817
Sine 90.38 is 1.0		Cosine 90.38 is 0.0065		Tangent 90.38 is 152.7866
Sine 90.5 is 1.0		Cosine 90.5 is 0.0087		Tangent 90.5 is 114.5887
Sine 90.11 is 1.0		Cosine 90.11 is 0.0019		Tangent 90.11 is 515.6614
Sine 90.22 is 1.0		Cosine 90.22 is 0.0039		Tangent 90.22 is 257.8297
Sine 90.33 is 1.0		Cosine 90.33 is 0.0058		Tangent 90.33 is 171.8854
Sine 90.44 is 1.0		Cosine 90.44 is 0.0078		Tangent 90.44 is 128.9129

"""