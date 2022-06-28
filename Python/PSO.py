# ================= Import Module Require for this Particle Swarm Optimization =================
import numpy as np
import matplotlib.pyplot as plt

from copy import copy
from numpy.random import rand
from numpy import sqrt


# ================= Agent Class for particle swarm =================
class Particle:
    def __init__(self, Position=[], Cost=[], Velocity=[]):
        self.Position = Position
        self.Cost = Cost
        self.Velocity = Velocity
        self.Best = Particle


# ================= Initialize variables =================
global VarSize
VarSize = 10

problem = dict(
    CostFunction = lambda x : sum([i**2 for i in x]),
    nVar = 5,
    VarMin = -10,
    VarMax = 10,
)

params = dict(
    MaxIt = 100,
    nPop = 50,
    w = 1,
    wdamp = 0.99,
    c1 = 2,
    c2 = 2,
    ShowIterInfo = True
)

# Constriction Coefficient
kappa = 1
phi1 = 2.05
phi2 = 2.05
phi = phi1 + phi2
chi = 2*kappa / abs(2 - phi - sqrt(phi**2 - 4*phi))


params2 = dict(
    MaxIt = 100,
    nPop = 50,
    w = chi,
    wdamp = 0.99,
    c1 = chi*phi1,
    c2 = chi*phi2,
    ShowIterInfo = True
)


# ================= Particle Swarm Optimization =================
def PSO(problem, params):
    # Get Problems
    CostFunction, nVar, VarMin, VarMax = problem.values()

    # Get Params
    MaxIt, nPop, w, wdamp, c1, c2, ShowIterInfo = params.values()

    # Initialization
    particle = [Particle() for i in range(nPop)]
    GlobalBest = Particle(Cost=float('inf'))
    for i in range(nPop):
        particle[i].Position = np.random.uniform(VarMin, VarMax, VarSize)
        particle[i].Cost = CostFunction(particle[i].Position)
        particle[i].Velocity = np.zeros(VarSize)

        particle[i].Best.Position = particle[i].Position
        particle[i].Best.Cost = particle[i].Cost

        if particle[i].Cost < GlobalBest.Cost:
            GlobalBest = copy(particle[i])

    BestCosts = np.zeros( (MaxIt, 1) )

    # Main loop of PSO
    print("Run Particle Swarm Optimization Algorithms in Python: ")
    for it in range(MaxIt):
        for i in range(nPop):
            particle[i].Velocity = w*particle[i].Velocity \
                                    +c1*rand(VarSize)*(particle[i].Best.Position - particle[i].Position) \
                                    +c2*rand(VarSize)*(GlobalBest.Position - particle[i].Position)
            particle[i].Position = particle[i].Position + particle[i].Velocity
            particle[i].Cost = CostFunction(particle[i].Position)

            if particle[i].Cost < particle[i].Best.Cost:
                particle[i].Best = copy(particle[i])
                if particle[i].Best.Cost < GlobalBest.Cost:
                    GlobalBest = copy(particle[i].Best)

        BestCosts[it] = GlobalBest.Cost

        if ShowIterInfo:
            print(f"Iteration {it+1} : Best Cost = {BestCosts[it]}")

        w = w * wdamp
    print("\n")  # New Line

    out = dict(
        pop = particle,
        BestSol = GlobalBest,
        BestCosts = BestCosts
    )

    return out


# ================= Result =================
out_1 = PSO(problem, params)
BestCosts_1 = out_1['BestCosts']

out_2 = PSO(problem, params2)
BestCosts_2 = out_2['BestCosts']


# ================= Visualization =================
plt.figure(figsize=(12, 8))

plt.semilogy(BestCosts_1)
plt.xlabel('Iteration')
plt.ylabel('Best Cost')

plt.semilogy(BestCosts_2)
plt.xlabel('Iteration')
plt.ylabel('Best Cost')

plt.legend(["PSO", "PSO with Constriction Coefficient"])
plt.title("PSO vs PSO with constriction coefficient")
plt.show()
