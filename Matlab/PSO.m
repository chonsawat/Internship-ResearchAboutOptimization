function out = PSO(problem, params)

    %% Problem Definition
    CostFunction = problem.CostFunction;
    nVar = problem.nVar;
    VarSize = [1 nVar];
    VarMin = problem.VarMin;
    VarMax = problem.VarMax;

    %% Parameters of Particle Swarm Optimizer
    MaxIt = params.MaxIt;
    nPop = params.nPop;
    w = params.w; % Intertia coefficient
    wdamp = params.wdamp; % Damping corfficient
    c1 = params.c1; % Personal Acceleration
    c2 = params.c2; % Global Accelaration
    ShowIterInfo = params.ShowIterInfo; % Params that show iteration info

    %% Initialization

    empty_particle.Position = [];
    empty_particle.Velocity = [];
    empty_particle.Cost = [];
    empty_particle.Best.Position = [];
    empty_particle.Best.Cost = [];

    particle = repmat(empty_particle, nPop, 1);
    GlobalBest.Cost = inf;

    for i=1:nPop
        particle(i).Position = unifrnd(VarMin, VarMax, VarSize);
        particle(i).Velocity = zeros(VarSize);
        particle(i).Cost = CostFunction(particle(i).Position);

        particle(i).Best.Position = particle(i).Position;
        particle(i).Best.Cost = particle(i).Cost;

        if particle(i).Cost < GlobalBest.Cost
            GlobalBest = particle(i).Best;
        end
    end

    BestCosts = zeros(MaxIt, 1);


    %% Main loop of PSO
    for it=1:MaxIt
       for i=1:nPop
           particle(i).Velocity = w*particle(i).Velocity ...
               + c1*rand(VarSize).*(particle(i).Best.Position - particle(i).Position) ...
               + c2*rand(VarSize).*(GlobalBest.Position - particle(i).Position);

           particle(i).Position = particle(i).Position + particle(i).Velocity;
           particle(i).Cost = CostFunction(particle(i).Position);

           if particle(i).Cost < particle(i).Best.Cost
              particle(i).Best.Position =  particle(i).Position;
              particle(i).Best.Cost = particle(i).Cost;
              if particle(i).Best.Cost < GlobalBest.Cost
                  GlobalBest = particle(i).Best;
              end
           end
       end

       BestCosts(it) = GlobalBest.Cost;
       
       if ShowIterInfo
            disp(['Iteration ' num2str(it) ': Best Cost = ' num2str(BestCosts(it))])
       end
       
       w = w * wdamp;
    end
    
    out.pop = particle;
    out.BestSol = GlobalBest;
    out.BestCosts = BestCosts;
    
end