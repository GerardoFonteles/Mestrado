function [X,F,Fn]=aptidao(P);
% Calcula aptidao dos individuos da populacao P
% Entrada:
%    P - Matriz binaria representando os individuos de uma geracao
%    nas linhas e os genes nas colunas
% Saida:
%    X - Fenotipo,  i.e. valores correspondentes em base decimal aos 
%        numeros binarios codificados nos individuos da populacao P 
%    F - Valores correspondentes da funcao de aptidao para os individuos 
%        da populacao P
%    Fn - Valores normalizados das aptidoes dos individuos da populacao 

n=size(P);
for i=1:n(1),
    X(i,:)=[P(i,1) P(i,2)];
    %pause
    F(i)=20+(X(i,1)^2)+(X(i,2)^2)-10*(cos(2*pi*X(i,1))+cos(2*pi*X(i,2))); % Armazena aptidoes brutas
end
Fn=F/sum(F);  % Aptidoes normalizadas

X=X';
F=F';
Fn=Fn';
