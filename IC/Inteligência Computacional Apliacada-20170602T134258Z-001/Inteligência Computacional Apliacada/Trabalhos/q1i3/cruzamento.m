function Pnew=cruzamento(P,S,Pc,Fn);
% selecao de individuos pelo metodo do sorteio

n=size(P);

Pnew=[];
for i=1:n(1)/2,
  % Recupera pais
  P1=P(S(i,1),:);
  P2=P(S(i,2),:);
  
  % Determina filhos
  Fn1=Fn(S(i,1));
  Fn2=Fn(S(i,2));
  if Fn1<=Fn2
    F1=(rand*(P1-P2))+P1;
    F2=(rand*(P1-P2))+P1;
  else
    F1=(rand*(P2-P1))+P2;
    F2=(rand*(P2-P1))+P2;
  endif
  Pnew=[Pnew;F1;F2];
endfor
    
    %u=rand;
    %if u<=Pc,
	    % Determina ponto de corte aleatoriamente
    %	    cut=floor((n(2)-1)*rand) + 1;
    
    	    % Determina filhos
    	%    F1=[P(S(i,1),1:cut) P(S(i,2),cut+1:end)];
    	 %   F2=[P(S(i,2),1:cut) P(S(i,1),cut+1:end)];
    
	    %Pnew=[Pnew;F1;F2];
    %else
	    % Determina filhos
    	%    F1=P(S(i,1),:);
    	 %   F2=P(S(i,2),:);
    
	    %Pnew=[Pnew;F1;F2];
   % endif