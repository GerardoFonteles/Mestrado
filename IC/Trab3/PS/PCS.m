% Implementacao da rede Percepton Simples 
% Usando as funcoes built-in (internas) do matlab
%
% Exemplo para disciplina de ICA
% Autor: Guilherme de A. Barreto
% Date: 06/07/2016

%
% X = Vetor de entrada
% d = saida desejada (escalar)
% W = Matriz de pesos Entrada -> Camada Oculta
% M = Matriz de Pesos Camada Oculta -> Camada saida
% eta = taxa de aprendizagem
% alfa = fator de momento

clear; clc; close all

% Carrega DADOS
%=================
load derm_input.txt;
load derm_target.txt;

dados=derm_input;  % Vetores (padroes) de entrada
alvos=derm_target; % Saidas desejadas correspondentes
 
clear derm_input;  % Libera espaco em memoria
clear derm_target;

% Embaralha vetores de entrada e saidas desejadas
[LinD ColD]=size(dados);

% Normaliza componetes para media zero e variancia unitaria
for i=1:LinD,
	mi=mean(dados(i,:));  % Media das linhas
    di=std(dados(i,:));   % desvio-padrao das linhas 
	dados(i,:)= (dados(i,:) - mi)./di;
end 
Dn=dados;

% Define tamanho dos conjuntos de treinamento/teste (hold out)
ptrn=0.8;    % Porcentagem usada para treino
ptst=1-ptrn; % Porcentagem usada para teste


% DEFINE ARQUITETURA DA REDE
%===========================
Ne = 200; % No. de epocas de treinamento
Nr = 100;   % No. de rodadas de treinamento/teste
Nh = 6;   % No. de neuronios na camada oculta

eta=0.1;   % Passo de aprendizagem

    for r=1:Nr,  % LOOP de rodadas de treinamento/teste

        rodada=r,

        I=randperm(ColD); Dn=Dn(:,I); alvos=alvos(:,I);   % Embaralha pares entrada/saida 

        % Vetores para treinamento e saidas desejadas correspondentes
        J=floor(ptrn*ColD);
        P = Dn(:,1:J); T1 = alvos(:,1:J);
        [lP cP]=size(P);   % Tamanho da matriz de vetores de treinamento

        % Vetores para teste e saidas desejadas correspondentes
        Q = Dn(:,J+1:end); T2 = alvos(:,J+1:end);
        [lQ cQ]=size(Q);   % Tamanho da matriz de vetores de teste

        % Inicia matrizes de pesos
        WW=0.01*rand(Nh,lP+1);   % Pesos entrada -> camada oculta


        %%% ETAPA DE TREINAMENTO
        for t=1:Ne,

            Epoca=t;

            I=randperm(cP); P=P(:,I); T1=T1(:,I);   % Embaralha vetores de treinamento e saidas desejadas

            EQ=0;
            for tt=1:cP,   % Inicia LOOP de epocas de treinamento
                % CAMADA OCULTA
                X=[-1; P(:,tt)];      % Constroi vetor de entrada com adicao da entrada x0=-1
                Ui = WW * X;          % Ativacao (net) dos neuronios da camada oculta
                Yi = (Ui>0);          % Saida entre [0,1] (funcao logistica)

                % CALCULO DO ERRO
                Ek = T1(:,tt) - Yi;           % erro entre a saida desejada e a saida da rede
                EQ = EQ + 0.5*sum(Ek.^2);     % soma do erro quadratico de todos os neuronios p/ VETOR DE ENTRADA

                WW = WW + eta*Ek*X';
            end   % Fim de uma epoca

            % MEDIA DO ERRO QUADRATICO P/ EPOCA
            EQM(t,r) = EQ/cP;
        end   % Fim do loop de treinamento

        %% ETAPA DE GENERALIZACAO  %%%
        EQ2=0;
        OUT2=[];
        HID2=[];
        for tt=1:cQ,
            % CAMADA OCULTA
            X=[-1; Q(:,tt)];      % Constroi vetor de entrada com adicao da entrada x0=-1
            Ui = WW * X;          % Ativacao (net) dos neuronios da camada oculta
            Yi = (Ui > 0);        % Saida entre [0,1] (funcao logistica)
            OUT2=[OUT2 Yi];



            % Gradiente local da camada de saida
            Ek = T2(:,tt) - Yi;   % erro entre a saida desejada e a saida da rede

            % ERRO QUADRATICO GLOBAL (todos os neuronios) POR VETOR DE ENTRADA
            EQ2 = EQ2 + 0.5*sum(Ek.^2);

        end

        % MEDIA DO ERRO QUADRATICO COM REDE TREINADA (USANDO DADOS DE TREINAMENTO)
        EQM2=EQ2/cQ;

        % CALCULA TAXA DE ACERTO
        count_OK=0;  % Contador de acertos
        for t=1:cQ,
            [T2max iT2max]=max(T2(:,t));  % Indice da saida desejada de maior valor
            [OUT2_max iOUT2_max]=max(OUT2(:,t)); % Indice do neuronio cuja saida eh a maior
            if iT2max==iOUT2_max,   % Conta acerto se os dois indices coincidem
                count_OK=count_OK+1;
            end
        end

        % Plota curva de aprendizagem
        % Se quiser visualizar a curva de aprendizagem para uma rodada
        % basta fazer Nr=1 e descomentar a linha de codigo abaixo.
        %figure; plot(EQM);  

        % Taxa de acerto global
        Tx_OK(r)=100*(count_OK/cQ);
        
        % Todas a saídas      
        [dummy Todos_diagnosticos(:,r)]=max(T2);
        [dummy Todos_saidas(:,r)]=max(OUT2);


    end

    % Estatisticas Descritivas
    Media=mean(Tx_OK);
    Mediana=median(Tx_OK);
    [Maxima indexmax]= max(Tx_OK);
    [Minima indexmin]= min(Tx_OK);
    DevPadrao=std(Tx_OK);
    
    
    %matriz de confusoes medias
    TaxasPorClasses=calc_confusoes(Todos_diagnosticos,Todos_saidas);

    %matriz de confusoes do pior caso
    MatrizDeConfusoes_pior=calc_confusoes(Todos_diagnosticos(:,indexmin),Todos_saidas(:,indexmin));

    %matriz de confusoes do melhor caso
    MatrizDeConfusoes_melhor=calc_confusoes(Todos_diagnosticos(:,indexmax),Todos_saidas(:,indexmax));
    
    EQM_MEDIO = mean(EQM,2);
    plot(EQM_MEDIO)
    title('Erro médio Quadrático para o Perceptron Simples')
    ylabel('Erro médio Quadrático')
    xlabel('Quantidade de épocas')
    
    figure;
    hist(Tx_OK);
    title('Perceptron Simples (PS)')
    ylabel('Número de ocorrências')
    xlabel('Taxa de acerto')
    
     %%Converti T2 e OUT2 para binario com o intuito de utilizar a funcao
    %%consionmat para se obter as matrizes de confusioes
%     [linhas,colunas] = size(T2); 
%     T2dec = [];
%     T2decmax = [];
%     OUT2dec = [];
%     OUT2decmin = [];
%     OUT2decmax = [];


%     T2dec =  bi2de(T2');
%     T2decmax = bi2de(Todos_diagnosticos(:,:,indexmax)');
%     T2decmin = bi2de(Todos_diagnosticos(:,:,indexmin)');
%     OUT2dec = bi2de(OUT2');
%     OUT2decmin = bi2de(Todos_saidas(:,:,indexmin)');
%     OUT2decmax = bi2de(Todos_saidas(:,:,indexmax)');



%     %Matriz de confusão
%     Matriz_Confusao_media = confusionmat(OUT2dec,T2dec);
% 
%     %Matriz de confusão 
%     Matriz_Confusao_min = confusionmat(OUT2decmin,T2dec);