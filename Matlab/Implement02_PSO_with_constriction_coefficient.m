clc;
clear;
close all;

%% Problem Definition
problem.CostFunction = @(x) Sphere(x);
problem.nVar = 5;
problem.VarMin = -10;
problem.VarMax = 10;

%% Constrcition Coefficient
kappa =  1;
phi1 = 2.05;
phi2 = 2.05;
phi = phi1 + phi2;
chi = 2*kappa/abs(2-phi-sqrt(phi^2-4*phi));

params.w = chi; % Intertia coefficient
params.c1 = chi*phi1; % Personal Acceleration
params.c2 = chi*phi2; % Global Accelaration

%% Parameters of Particle Swarm Optimizer
params.MaxIt = 100;
params.nPop = 50;
params.wdamp = 0.99; % Damping corfficient
params.ShowIterInfo = true; % Show interation information

%% Calling PSO
out = PSO(problem, params);
BestSol = out.BestSol;
BestCosts = out.BestCosts;

%% Result
figure;
%plot(BestCosts, 'LineWidth', 2);
semilogy(BestCosts, 'LineWidth', 2)
xlabel('Iteriation');
ylabel('Best Cost');