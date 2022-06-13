from .imports import *

"""
Constants and values describing rates and variables
"""
'''
Settings from the paper
--------------------------------------------------------------------------------------------
 Notation       Definition                                                     Range of Value
--------------------------------------------------------------------------------------------
    π     Recruitment rate of susceptible human individuals                          Variable
    ŋ    Decay rate of Ebola virus in the environment                               (0, )
    α    Rate of hospitalization of infected individuals                               (0, 1)
        Disease-induced death rate of human individuals                               [0.4, 0.9]
    β1    Contact rate of infectious human individuals                               Variable
    β2    Contact rate of pathogen individuals/environment                           Variable
    β3    Contact rate of deceased human individuals                                   Variable
    β4    Contact rate of recovered human individuals                                   Variable
        Recovery rate of human individuals                                           (0, 1)
        Natural death rate of human individuals                                       (0, 1)
        Rate of  burial of deceased human individuals                               (0, 1)
        Rate of vaccination of individuals                                           (0, 1)
        Rate of response to hospital treatment                                       (0, 1)
        Rate response to vaccination                                               (0, 1)
'''

π=0.1 #Recruitment rate of susceptible human individuals
ŋ=np.random.rand() #Decay rate of Ebola virus in the environment
α=np.random.rand() #Rate of hospitalization of infected individuals
dis=random.uniform(0.4, 0.9)#Disease-induced death rate of human individuals
β_1=0.1#Contact rate of infectious human individuals
β_2=0.1#Contact rate of pathogen individuals/environment
β_3=0.1#Contact rate of deceased human individuals
β_4=0.1#Contact rate of recovered human individuals
rr=np.random.rand() #Recovery rate of human individuals
dr=np.random.rand() #Natural death rate of human individuals
br=np.random.rand() #Rate of  burial of deceased human individuals
vr=np.random.rand() #Rate of vaccination of individuals
hr=np.random.rand() #Rate of response to hospital treatment
vrr=np.random.rand() #Rate response to vaccination
qrr=np.random.rand()	#Rate of quarantine of infected individuals

modelrates = {
    "recruitment_rate": π,
    "decay_rate": ŋ,
    "hospitalization_rate": α,
    "disease_induced_death_rate": dis,
    "contact_rate_infectious": β_1,
    "contact_rate_pathogen": β_2,
    "contact_rate_deceased": β_3,
    "contact_rate_recovered": β_4,
    "recovery_rate": rr,
    "natural_death_rate": dr,
    "burial_rate": br,
    "vacination_rate": vr,
    "hospital_treatment_rate": hr,
    "vaccination_response_rate": vrr,
    "quarantine_rate": qrr
}