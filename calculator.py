import numpy as np

# gather laser wavelength
wavelength_str = input("Enter Laser Wavelength, 210-6700 nm: ")
wavelength = float(wavelength_str) /1000

# SiO2 coefficients
b1_array = [0.6961663,0.4079426,0.8974794]
c1_array_root = [0.0684043,0.1162414,9.896161]

#Doped SiO2 coefficients
b2_array = [0.7072363,0.4389641,0.8931482]
c2_array = [0.0684611,0.1200138,10.090738]


#Sellmeier's Equation, SiO2 (Fiber Core). Solve using input wavelength
def coreRefractionIndex(wavelength):
    contributions = []
    for b, c in zip(b1_array, c1_array_root):
        #perform operations and append to array
        calculate_term = (b * wavelength**2) / (wavelength**2 - c**2)
        contributions.append(calculate_term)
    #complete operation and root    
    core_refraction = 1 + sum(contributions)
    n = np.sqrt(core_refraction)
    return n
print(coreRefractionIndex(wavelength))

#Sellmeier's Equation, SiO2 + B2O2 Dopant (Outer cladding)
def cladRefractionIndex(wavelength):
    contributions2 = []
    for b2, c2 in zip(b2_array, c2_array):
        #perform operations and append
         calculate_term2 = (b2 * wavelength**2) / (wavelength**2 - c2**2)
         contributions2.append(calculate_term2)
    clad_refraction = 1 + sum(contributions2)
    u = np.sqrt(clad_refraction)
    return u
print(cladRefractionIndex(wavelength))

#Critical Angle Required for total internal reflection
def snellsCriticalAngle(cladRefractionIndex, coreRefractionIndex ):
    critical_angle_radians = np.arcsin(coreRefractionIndex(wavelength)/cladRefractionIndex(wavelength))
    critical_angle = np.degrees(critical_angle_radians)
    return critical_angle
print(snellsCriticalAngle(cladRefractionIndex, coreRefractionIndex))

"""
#Finding NA, for acceptance cone angle
def numericalAp(cladRefractionIndex,coreRefractionIndex):
    na = np.sqrt(coreRefractionIndex(wavelength)**2 - cladRefractionIndex(wavelength)**2)
    acceptance_cone = np.arcsin(na)
    full_acceptance = acceptance_cone * 2
    return full_acceptance
print(numericalAp(cladRefractionIndex,coreRefractionIndex))
"""

#Entrance angle adjustment
#def snellsLaw(coreRefractionIndex, cladRefractionIndex):


"""




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