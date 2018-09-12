function [A1,A2,A3,error] = ALS(A,R,dft)
%%
%Essa funcao utiliza o algoritmo ALS para a estimacao de um tensor as
%entradas sao o tensor(A), o rank do tensor (R), e para o teste do dft(dft)
%
%%
[I,J,K] = size(A);

%testar para A2 e A3 sendo dfts
if dft == 1
    A2 = dftmtx(R);
    A3 = dftmtx(R);
else
    
end
%Inicialização de A2 e A3 randômicos
A2 = randn(J,R);
A3 = randn(K,R);

%quantidade de iterações
iteration = 1000;

%A evolucao dos erros de casa iteracao
error = zeros(1,iteration);
for i=1:iteration
     
     %Aplica a formula para a estimacao de cada A(n) de acordo com o
     %algortimo do ALS
     A1 = unfold3tensor(A,1)*pinv(KhatriRao(A3,A2)');  
     A2 = unfold3tensor(A,2)*pinv(KhatriRao(A3,A1)');
     A3 = unfold3tensor(A,3)*pinv(KhatriRao(A2,A1)');

     error(i) = norm(unfold3tensor(A,1)-A1*(KhatriRao(A3,A2))','fro');
     
     
     if(error(i) < 1e-13)
        break;
     end
     disp(error(i))
%disp(i)
end

%lambda1 = normc(A1);
%lambda2 = normc(A2);
%lambda3 = normc(A3);
end
