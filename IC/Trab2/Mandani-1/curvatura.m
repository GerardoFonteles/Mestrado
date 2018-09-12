function mi=curvatura(x)
%
% Retorna as pertinências da medida x aos conjuntos fuzzy
% definidos para a variável lingüística RAIO_DE_CURVATURA.
%
% Funcoes de pertinencia TRIANGULARES/TRAPEZOIDAS
%
% Data: 19/09/2009
% Autor: Guilherme A. Barreto

%Conjunto RB de curvatura
if x<=-30,
   mi(1)=(1/60)*(x+90);
elseif x>-30 & x<10,
   mi(1)=-(1/40)*(x-10);
else
   mi(1)=0;
end

% Conjunto RU de curvatura
if x>0 & x<25,
   mi(2)=(1/25)*(x);
elseif x>=25 & x<50,
   mi(2)=-(1/25)*(x-50);
else
   mi(2)=0;
end

% Conjunto RV de curvatura
if x>40 & x<65,
   mi(3)=(1/25)*(x-40);
elseif x>=65 & x<90,
   mi(3)=-(1/25)*(x-90);
else
   mi(3)=0;
end

% Conjunto VE de curvatura
if x>75 & x<90,
   mi(4)=(1/15)*(x-75);
elseif x>=90 & x<105,
   mi(4)=-(1/15)*(x-105);
else
   mi(4)=0;
end

% Conjunto LV de curvatura
if x>90 & x<115,
   mi(5)=(1/25)*(x-90);
elseif x>=115 & x<140,
   mi(5)=-(1/25)*(x-140);
else
   mi(5)=0;
end

% Conjunto LU de curvatura
if x>130 & x<155,
   mi(6)=(1/25)*(x-130);
elseif x>=155 & x<180,
   mi(6)=-(1/25)*(x-180);
else
   mi(6)=0;
end

% Conjunto LB de curvatura
if x>170 & x<210,
   mi(7)=(1/40)*(x-170);
elseif x>=210,
   mi(7)=-(1/60)*(x-270);
else
   mi(7)=0;
end

