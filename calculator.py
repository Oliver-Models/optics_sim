import numpy as np
import pandas as pd

#constants
speedOfLight = 2.99792458 * 10**8 #m/s
planksConstant =  6.6261*10 **-34 #J*s
assumedPower = 1**-3

fiberModels = {
    "Multimode Fiber Type": ["OM1", "OM2", "OM3", "OM4", "OM5"],
    "Standard Date": [1989, 1998, 2003, 2009, 2019],
    "Modal Bandwidth (MHz/km)": ["200", "500", "2000", "4700", "4700 @ 850 nm, 2470 @ 953 nm"],
    "Core Size (µm)": [62.5, 50, 50, 50, 50],
    "Jacket Color": ["Orange", "Orange", "Aqua", "Aqua", "Lime Green"],
    "Light Source": ["LED", "LED", "VCSEL", "VCSEL", "VCSEL"],
    "Typical Application": ["100 MbE", "1 GbE", "10 GbE", "25G/40/100 GbE", "40/100G SWDM4 & 400G-BD4.2"]
}
fiber = pd.DataFrame(fiberModels)
print(fiber)
input("Select MMF Model (1-5): ")



class FiberModel:
    def __init__(self, model_type, standard_date, bandwidth, core_size, jacket_color, light_source, application):
        self.model_type = model_type
        self.standard_date = standard_date
        self.bandwidth = bandwidth
        self.core_size = core_size
        self.jacket_color = jacket_color
        self.light_source = light_source
        self.application = application

class FiberOptics:
    
    #Doped SiO2 coefficients (core)
    b1_array = [0.7072363,0.4389641,0.8931482]
    c1_array = [0.0684611,0.1200138,10.090738]
    # SiO2 coefficients (clad)
    b2_array = [0.6961663,0.4079426,0.8974794]
    c2_array = [0.0684043,0.1162414,9.896161]
     

    
    def __init__(self):
        return None

    #gather laser wavelength
    def wavelength():
        wavelength_nm = float(input("Input laser wavelength 210-6700nm: "))
        if not (210 <= wavelength_nm <= 6700):
            raise ValueError("Wavelength must be between 210 and 6700 nm")
        wavelength_um = wavelength_nm / 1000
        return wavelength_um
        
    #Sellmeier's Equation, SiO2 + B2O2 (Core)
    def coreRefractionIndex(self, wavelength_um):
        contributions1 = []
        for b1, c1 in zip(self.b1_array, self.c1_array):
        #perform operations and append (sellmeiers equation)
            wl = wavelength_um
            calculate_term1 = (b1 * wl**2) / (wl**2 - c1**2)
            #append
            contributions1.append(calculate_term1)
            # +1 and sum
            u = 1 + sum(contributions1)
            #square root
            core_refraction = np.sqrt(u)
        #return
        return core_refraction

    #Sellmeier's Equation, SiO2 (Fiber Clad). Solve using input wavelength
    def cladRefractionIndex(self,wavelength_um):
        contributions2 = []
        for b2, c2 in zip(self.b2_array, self.c2_array):
            #perform operations and append to array. Uses wavelength
            wl = wavelength_um
            calculate_term = (b2* wl**2) / (wl**2 - c2**2)
            contributions2.append(calculate_term)
            #complete operation and root    
            n = 1 + sum(contributions2)
            clad_refraction = np.sqrt(n)
        #return
        return clad_refraction

#Critical Angle /Required for total internal reflection
    def snellsCriticalAngle(self,wavelength_um):
        #uses clad and core RI to find critical angle
        critical_angle_radians = self.cladRefractionIndex(wavelength_um)/self.coreRefractionIndex(wavelength_um)
        #arcsin for ???
        shorten_arcsin = np.arcsin(critical_angle_radians)
        #transforms to degrees
        critical_angle = np.degrees(shorten_arcsin)
        #return
        return critical_angle

    #speed of light in silicon
    def speedOfLightSilicon(self, wavelength_um): # v = c / n
        #finds v
        velocity = speedOfLight / self.coreRefractionIndex(wavelength_um) 
        return velocity

    def photonEnergy(self, wavelength_um): # e = h * c / wl
        #finds e
        energy = planksConstant *  self.speedOfLightSilicon(wavelength_um) / wavelength_um
        return energy

    # Photon flux calculation with assumed power
    def photonFlux(self,wavelength_um):
        energy_per_photon = self.photonEnergy(wavelength_um)
        flux = assumedPower / energy_per_photon  # photons per second
        return flux

    #attenuation code here (dispersion and scatter)

coreRI = FiberOptics.coreRefractionIndex(FiberOptics,wavelength_um=input)
cladRI = FiberOptics.cladRefractionIndex(FiberOptics,wavelength_um=input)
criticalA = FiberOptics.snellsCriticalAngle(FiberOptics,wavelength_um=input)
photonF = FiberOptics.photonFlux(FiberOptics,wavelength_um=input)


print(f"Critical Angle: {criticalA} degrees")
print(f"Core R: {coreRI}")
print(f"Clad R: {cladRI}")
print(f"Critical A: {criticalA}")
print(f"Photon Flux: {photonF} photons per second")

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