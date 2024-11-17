import numpy as np
import pandas as pd

#constants
speedOfLight = 2.99792458 * 10**8 #m/s
planksConstant =  6.6261*10 **-34 #J*s
assumedPower = 1**-3

#gather laser wavelength
wavelength = input("Input laser wavelength 210-6700nm: ")
wavelength = float(wavelength)
wavelength = wavelength / 1000

# SiO2 coefficients
b1_array = [0.6961663,0.4079426,0.8974794]
c1_array_root = [0.0684043,0.1162414,9.896161]

#Doped SiO2 coefficients
b2_array = [0.7072363,0.4389641,0.8931482]
c2_array = [0.0684611,0.1200138,10.090738] 

#Sellmeier's Equation, SiO2 + B2O2 (Core)
def coreRefractionIndex(wavelength):
    contributions2 = []
    for b2, c2 in zip(b2_array, c2_array):
        #perform operations and append 
         calculate_term2 = (b2 * wavelength**2) / (wavelength**2 - c2**2)
         contributions2.append(calculate_term2)
    core_refraction = 1 + sum(contributions2)
    u = np.sqrt(core_refraction)
    return u


#Sellmeier's Equation, SiO2 (Fiber Clad). Solve using input wavelength
def cladRefractionIndex(wavelength):
    contributions = []
    for b, c in zip(b1_array, c1_array_root):
        #perform operations and append to array
        calculate_term = (b * wavelength**2) / (wavelength**2 - c**2)
        contributions.append(calculate_term)
    #complete operation and root    
    clad_refraction = 1 + sum(contributions)
    n = np.sqrt(clad_refraction)
    return n

#Critical Angle /Required for total internal reflection
def snellsCriticalAngle(cladRefractionIndex, coreRefractionIndex):

    critical_angle_radians = cladRefractionIndex(wavelength)/coreRefractionIndex(wavelength)
    shorten_arcsin = np.arcsin(critical_angle_radians)
    critical_angle = np.degrees(shorten_arcsin)
    return critical_angle

#speed of light in silicon
def speedOfLightSilicon(wavelength): # v = c / n
    #find speed of light (velocity)
    velocity = speedOfLight / coreRefractionIndex(wavelength) 
    return velocity

def photonEnergy(wavelength): # e = h * c / wl
    energy = planksConstant *  speedOfLightSilicon(wavelength) / wavelength
    return energy

    # Photon flux calculation with assumed power
def photonFlux(wavelength):
    energy_per_photon = photonEnergy(wavelength)
    flux = assumedPower / energy_per_photon  # photons per second
    return flux

#attenuation
#def attenuation(wavelength):
    
    
coreRI = coreRefractionIndex(wavelength)
cladRI = cladRefractionIndex(wavelength)
criticalA = snellsCriticalAngle(cladRefractionIndex, coreRefractionIndex)
print(f"Photon Flux: {photonFlux(wavelength)} photons per second")
print(f"Critical Angle: {snellsCriticalAngle(cladRefractionIndex, coreRefractionIndex)} degrees")

print(f"Core R: {coreRI}")
print(f"Clad R: {cladRI}")
print(f"Critical A: {criticalA}")

"""
calc_df = pd.DataFrame(index=['Core Refraction', 'Cladding Refraction', 'Critical Angle'])

class input:
    while True:
    # gather laser wavelength
        
        if wavelength_str.lower() == 'exit':
            print("Exiting program")
            break

        else:
            wavelength = float(wavelength_str) / 1000

        for input in calc_df:
            wavelength_str = input("Enter Laser Wavelength, 210-6700 nm or type 'exit' to quit: ")
            core_I = coreRefractionIndex(wavelength)
            clad_I = cladRefractionIndex(wavelength)
            critical_A = snellsCriticalAngle(cladRefractionIndex, coreRefractionIndex)
            wavelength_Append = wavelength

            calc_df = pd.DataFrame([core_I, clad_I, critical_A])


 #new_column = pd.Series([core_I, clad_I, critical_A], index=calc_df.columns, name=wavelength_str + " nm")
"""      

#Data frame
#temp solution. add dynamic pandas later. 
#print(calc_df)
#def acceptanceCone():
#def dispersion():
#def speedOverTime():


#Total refraction- error checker:
#def snellsRefraction(cladRefractionIndex, coreRefractionIndex):
"""
#Finding NA, for acceptance cone angle
def numericalAp(cladRefractionIndex,coreRefractionIndex):
    na = np.sqrt(coreRefractionIndex(wavelength)**2 - cladRefractionIndex(wavelength)**2)
    acceptance_cone = np.arcsin(na)
    full_acceptance = acceptance_cone * 2
    return full_acceptance
print(numericalAp(cladRefractionIndex,coreRefractionIndex))
"""


"""

#adjustable mmf variables. add feature sooner


#sio2

#include industry standards
def mmfCircumference():


def mmfLength():


def temperature():


def noise():


#Ideal BER calculations. Healthy variance.
"""