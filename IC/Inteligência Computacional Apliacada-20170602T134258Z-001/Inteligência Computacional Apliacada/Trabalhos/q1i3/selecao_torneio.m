function S=selecao_torneio(P,Fn);
% selecao de individuos pelo metodo do sorteio

n=size(P);

S=[];

for i=1:n(1)/2,
  I=randperm(n(1));  % Numeros inteiros de 1 a n(1) em ordem aleatoria
  I1=I(1:round(n(1)/10)); % Pega os N/10 primeiros indices
  I2=I(1+round(n(1)/10):2*round(n(1)/10)); % Pega os N/10 proximos indices
  
  Pai=I1(find(Fn(I1)==min(Fn(I1)))); % Seleciona individuo de menor fitness
  Mae=I2(find(Fn(I2)==min(Fn(I2)))); % Seleciona individuo de menor fitness
  
  S=[S;Pai Mae];
endfor


%for i=1:n(1)/2,
  % Seleciona 1o. individuo do par (PAI)
 % I=randperm(n(1));  % Numeros inteiros de 1 a n(1) em ordem aleatoria
  %I1=I(1); I2=I(2); % Pega dois primeiros indices
    
  %if Fn(I1) < Fn(I2), % Seleciona individuo de maior fitness
    	Pai=I1;
%  else
%	  Pai=I2;
%  endif
 
  % Seleciona 2o. individuo do par (MAE)
%  I=randperm(n(1));  % Numeros inteiros de 1 a n(1) em ordem aleatoria
%  I1=I(1); I2=I(2);  % Pega dois primeiros indices  
%  if Fn(I1) < Fn(I2), % Seleciona individuo de maior fitness
%    Mae=I1;
%  else
%	  Mae=I2;
%  endif
%  S=[S;Pai Mae];
%endfor
    
