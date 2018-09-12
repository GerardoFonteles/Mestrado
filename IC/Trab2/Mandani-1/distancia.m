function mi = distancia(x)
% Retorna as pertinências da medida x aos conjuntos fuzzy
% definidos para a variável lingüística DISTANCIA.
%
% Funcoes de pertinencia TRIANGULARES/TRAPEZOIDAS
%
% Data: 19/09/2009
% Autor: Guilherme A. Barreto || Jose Gerardo Fonteles Lopes

% Conjunto de Distancia LE
if x<=10,
   mi(1)=1;
elseif x>10 & x<35,
   mi(1)=-(1/25)*(x-35);
else
   mi(1)=0;
end

% Conjunto de Distancias LC
if x>30 & x<=40,
   mi(2)=0;
elseif x>30 & x<=40,
   mi(2)=(1/10)*(x-30);
elseif x>40 & x<50,
   mi(2)=-(1/10)*(x-50);
else
   mi(2)=0;
end

% Conjunto de CE
if x>45 & x<=50,
   mi(3)=(1/5)*(x-45);
elseif x>50 & x<55,
   mi(3)=-(1/5)*(x-55);
else
   mi(3)=0;
end

% Conjunto de RC
if x>50 & x<=60,
   mi(4)=(1/10)*(x-50);
elseif x>60 & x<70,
   mi(4)=-(1/10)*(x-60);
else
   mi(4)=0;
end

% Conjunto de HI
if x>=90,
   mi(5)=1;
elseif x>=65 & x<=90,
   mi(5)=(1/25)*(x-65);
else
   mi(5)=0;
end
end

