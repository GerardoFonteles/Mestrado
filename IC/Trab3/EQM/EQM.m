% Implementacao da rede Erro médio quardrático
% Usando as funcoes built-in (internas) do matlab
%
% Exemplo para disciplina de ICA
% Autor: Guilherme de A. Barreto
% Date: 06/07/2016

clear; clc; close all

% Carrega DADOS
%=================
load derm_input.txt;
load derm_target.txt;



dados=derm_input;  % Vetores (padroes) de entrada
alvos=derm_target; % Saidas desejadas correspondentes

[LinD ColD]=size(dados);

X = dados;
Y = alvos;

clear derm_input;  % Libera espaco em memoria
clear derm_target;

% Define tamanho dos conjuntos de treinamento/teste (hold out)
ptrn=0.8;    % Porcentagem usada para treino
ptst=1-ptrn; % Porcentagem usada para teste

Todos_diagnosticos = zeros(72,100);
Todos_saidas = zeros(72,100);
for Nr=1:100
    I=randperm(ColD); X=X(:,I); Y=Y(:,I);   % Embaralha pares entrada/saida 
        
    % Vetores para treinamento e saidas desejadas correspondentes
    J=floor(ptrn*ColD);
    
    Ytr = Y(:,1:J);
    Xtr = X(:,1:J);
    Xtest = X(:,J+1:end);
    Ytest = Y(:,J+1:end);
    

    A=Ytr*Xtr'*inv(Xtr*Xtr');
    
    Ypred = A*Xtest;    
    
    % Encontra os elementos de maior valor em cada coluna de Ypred
    [test indexmax_pred]= max(Ypred);

    % Encontra os elementos de maior valor em cada coluna de Ytest
    [test indexmax_test]= max(Ytest);
    
    erro(Nr) = 100*pdist2(indexmax_test,indexmax_pred,'hamming');
    
    Todos_diagnosticos(:,Nr)= indexmax_test;
    Todos_saidas(:,Nr) = indexmax_pred;
   
end

acertos = 100 - erro;

acertos_medios = mean(acertos);
acertos_mediana = median(acertos);
[Maxima indexmax]=max(acertos);
[Minima indexmin]=min(acertos);
acertos_std=std(acertos);

hist(acertos);
title('Histograma de Minimos Quadráticos');
ylabel('Número de ocorrências');
xlabel('Taxa de acerto');

%matriz de confusoes medias
TaxasPorClasses=calc_confusoes(Todos_diagnosticos,Todos_saidas);

%matriz de confusoes do pior caso
MatrizDeConfusoes_pior=calc_confusoes(Todos_diagnosticos(:,indexmin),Todos_saidas(:,indexmin));

%matriz de confusoes do melhor caso
MatrizDeConfusoes_melhor=calc_confusoes(Todos_diagnosticos(:,indexmax),Todos_saidas(:,indexmax));
    

    