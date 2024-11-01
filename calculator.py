import numpy as np
import math

#adjustable laser variables. add feature at a later date.
#def vcselComponents():

#gather laser wavelength
wavelength_str = input("Enter Laser Wavelength, um: ")
wavelength = int(wavelength_str)

b_array = [0.6961663,0.4079426,0.8974794]
c_array_root = [0.0684043,0.1162414,9.896161]

#Sellmeier's Equation, SiO2 (MMF Core). Solve using input wavelength
def coreRefractionIndex(wavelength):
    contributions = []
    for b, c in zip(b_array, c_array_root):
        calculate_term = (b * wavelength**2) / (wavelength**2 - c**2)
        contributions.append(calculate_term)
    core_refraction = 1 + sum(contributions)
    n = np.sqrt(core_refraction)
    return f"a wavelength of {wavelength} um has a refraction index of {n}"
print(coreRefractionIndex(wavelength))


"""
#Sellmeier's Equation, SiO2 + B2O2 Dopant (Outer cladding)
def cladRefractionIndex(wavelength):
    temporary = temporary
    for

#Entrance angle adjustment
def snellsLaw(coreRefractionIndex, cladRefractionIndex):
    SLE = coreRefractionIndex.sin() 

#Critical Angel Required for total reflection
def snellsCriticalAngle():


def m2():

def vcselToMmfAngle():

def acceptanceCone():



def speedOverTime():

#adjustable mmf variables. add feature sooner

#sio2


#include industry standards
def mmfCircumference():

def mmfLength():

def temperature():

def noise():

#Ideal BER calculations. Healthy variance.
"""