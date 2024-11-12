import numpy as np
import pandas as pd

# Gather laser wavelength
wavelength = input("Input laser wavelength 210-6700nm: ")
wavelength = float(wavelength)
wavelength = wavelength / 1e9  # Convert nm to meters

# SiO2 coefficients
b1_array = [0.6961663, 0.4079426, 0.8974794]
c1_array_root = [0.0684043, 0.1162414, 9.896161]

# Doped SiO2 coefficients
b2_array = [0.7072363, 0.4389641, 0.8931482]
c2_array = [0.0684611, 0.1200138, 10.090738]

# Sellmeier's Equation, SiO2 + B2O2 (Core)
def coreRefractionIndex(wavelength):
    contributions2 = []
    for b2, c2 in zip(b2_array, c2_array):
        calculate_term2 = (b2 * wavelength**2) / (wavelength**2 - c2**2)
        contributions2.append(calculate_term2)
    core_refraction = 1 + sum(contributions2)
    return np.sqrt(core_refraction)

# Sellmeier's Equation, SiO2 (Fiber Clad)
def cladRefractionIndex(wavelength):
    contributions = []
    for b, c in zip(b1_array, c1_array_root):
        calculate_term = (b * wavelength**2) / (wavelength**2 - c**2)
        contributions.append(calculate_term)
    clad_refraction = 1 + sum(contributions)
    return np.sqrt(clad_refraction)

# Critical Angle Calculation for total internal reflection
def snellsCriticalAngle(wavelength):
    n_clad = cladRefractionIndex(wavelength)
    n_core = coreRefractionIndex(wavelength)
    critical_angle_radians = n_clad / n_core
    critical_angle = np.degrees(np.arcsin(critical_angle_radians))
    return critical_angle

# Constants
speedOfLight = 2.99792458 * 10**8  # m/s
planksConstant = 6.6261 * 10**-34  # J·s

# Speed of light in silicon
def speedOfLightSilicon(wavelength):
    velocity = speedOfLight / coreRefractionIndex(wavelength)
    return velocity

# Photon energy calculation
def photonEnergy(wavelength):
    energy = planksConstant * speedOfLightSilicon(wavelength) / wavelength
    return energy

# Photon flux calculation, given power
def photonFlux(power, wavelength):
    energy_per_photon = photonEnergy(wavelength)
    flux = power / energy_per_photon  # photons per second
    return flux

# Example usage
power = 1e-3  # Example power in watts (1 mW)

# Calculations
coreRI = coreRefractionIndex(wavelength)
cladRI = cladRefractionIndex(wavelength)
criticalA = snellsCriticalAngle(wavelength)
flux = photonFlux(power, wavelength)

# Outputs
print(f"Photon Flux: {flux:.2e} photons per second")
print(f"Critical Angle: {criticalA:.2f} degrees")
print(f"Core Refractive Index: {coreRI}")
print(f"Cladding Refractive Index: {cladRI}")
print(f"Critical Angle for TIR: {criticalA}")

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

