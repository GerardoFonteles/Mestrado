clc;
clear all;
close all;

% %%%%%%%%%%% Declare tensor size and Rank %%%%%%%%%%%%
I = 3;
J = 5;
K = 4;
R = 6;


%%%%%%%% estimation of 3d tensors%%%%%%%%%%%%%%%%%%%%
%R = min([I*J I*K J*K]);
   
%Inicializa A(n) randomicamente
A1 = randn(I,R);
A2 = randn(J,R);
A3 = randn(K,R);

%Cria o tensor X aparte dos A(n)
X1 = A1*(KhatriRao(A3,A2)).';
X = fold(X1,K,1);
[I,J,K] = size(X);


%Executa 100 vezes o algoritmo ALS
for i=1:1    %recebe todos os A(n) estimados 
    [A1est,A2est,A3est,error] = ALS(X,R,0);
    
    %Esse fold é o  unfold do tensor estimado
    fold1 = A1est*(KhatriRao(A3est,A2est)).';

    %Aest1 é o nosso tensor estimado
    Aest1 = fold(fold1,K,1);
    
    %errors é o vetor que armazena os erros de cada iteração
    errors(i,:) = error;
    disp(i)
end

%Calcula a média do vetor de erros para as cem execuções.
errmean = mean(errors);

%plota o vetor de erro médio
semilogy(errmean);
title('ALS Test');
xlabel('Number of iteration in 100 executions.');
ylabel('Mean Error.');


%%%%%%%% estimation of 3d tensors%%%%%%%%%%%%%%%%%%%%
%R = min([I*J I*K J*K]);

% A1 = randn(I,R);
% A2 = randn(J,R);
% A3 = randn(K,R);
% 
% X2 = A1*(KhatriRao(A3,A2))';
% X2 = fold(X2,K,1);
% [I,J,K] = size(X2);
% 
% for i=1:100
%     
%     [A1est,A2est,A3est,error] = ALS_Known_As(X2,A2,A3);
% 
%     fold1 = A1est*(KhatriRao(A3est,A2est))';
% 
%     Aest2 = fold(fold1,K,1);
%     errors(i,:) = error;
%     disp(i)
% end
% 
% errmean = mean(errors);
% figure;
% plot(errmean);
% title('ALS Test');
% xlabel('Number of iteration in 100 executions.');
% ylabel('Mean Error.');

