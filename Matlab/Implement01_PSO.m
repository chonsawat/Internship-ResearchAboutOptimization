clc;
clear;
close all;

%% Problem Definition
problem.CostFunction = @(x) Sphere(x);
problem.nVar = 5;
problem.VarMin = -10;
problem.VarMax = 10;

%% Parameters of Particle Swarm Optimizer
params.MaxIt = 100;
params.nPop = 50;
params.w = 1; % Intertia coefficient
params.wdamp = 0.99; % Damping corfficient
params.c1 = 2; % Personal Acceleration
params.c2 = 2; % Global Accelaration
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