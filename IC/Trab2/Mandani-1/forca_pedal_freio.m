function mi=forca_pedal_freio(x)
%
% Retorna as pertinências da medida x aos conjuntos fuzzy
% definidos para a variável lingüística FORCA_NO_PEDAL_DE_FREIO.
%
% Funcoes de pertinencia TRIANGULARES/TRAPEZOIDAS
%
% Data: 19/09/2009
% Autor: Guilherme A. Barreto

% Conjunto de NB
if x>=-30 & x<-15,
   mi(1)=-(1/15)*(x+15);
else
   mi(1)=0;
end

% Conjunto de NM
if x>=-25 & x<-15,
   mi(2)=(1/10)*(x+25);
elseif x>=-15 & x<-5,
   mi(2)=-(1/10)*(x+5);
else
   mi(2)=0;
end

% Conjunto de NS
if x>-10 & x<-5,
   mi(3)=(1/5)*(x+10);
elseif x>=-5 & x < 0,
   mi(3)=-(1/5)*x;
else
    mi(3)=0;
end

% Conjunto ZE 
if x>-5 & x<0,
   mi(4)=(1/5)*(x+5);
elseif x>=0 & x<5,
   mi(4)=-(1/5)*(x-5);
else
   mi(4)=0;
end

% Conjunto PS 
if x>0 & x<5,
   mi(5)=(1/5)*(x);
elseif x>=5 & x<10,
   mi(5)=-(1/5)*(x-10);
else
   mi(5)=0;
end

% Conjunto PM 
if x>5 & x<15,
   mi(6)=(1/10)*(x-5);
elseif x>=15 & x<25,
   mi(6)=-(1/10)*(x-25);
else
   mi(6)=0;
end

% Conjunto PB 
if x>=15,
   mi(7)=(1/15)*(x-15);
else
   mi(7)=0;
end
