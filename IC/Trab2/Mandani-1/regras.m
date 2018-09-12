function RULE_OUT=regras(mi1,mi2,mi_out,y)
% Exemplo simples de base de regras nebulosas
%
% ENTRADA
%     mi1: graus de pertinencia da variavel x1 (velocidade, Km/h)
%     mi2: graus de pertinencia da variavel x2 (raio de curvatura, m)
%     mi_out: funcoes de pertinencia da variavel de saida y (forca no pedal de freio, N)
%
% SAIDA
%
%    RULE_OUT: Conjuntos fuzzy de saida modificados para todas as regras    
%
% Autor: Guilherme A. Barreto
% Data: 03/10/2009


%% Regras RB %%%%
%LExRB=PS
m1=min(mi1(1),mi2(1));
mi_out_LExRB=min(m1,mi_out(:,5));


%LCxRB=PM
m1=min(mi1(2),mi2(1));
mi_out_LCxRB=min(m1,mi_out(:,6));




%CExRB=PM
m1=min(mi1(3),mi2(1));
mi_out_CExRB=min(m1,mi_out(:,6));



%RCxRB=PB
m1=min(mi1(4),mi2(1));
mi_out_RCxRB=min(m1,mi_out(:,7));



%RIxRB=PB
m1=min(mi1(5),mi2(1));
mi_out_RIxRB=min(m1,mi_out(:,7));



%% Regras RU %%%%
%LExRU=NS
m1=min(mi1(1),mi2(2));
mi_out_LExRU=min(m1,mi_out(:,3));



%LCxRU=PS
m1=min(mi1(2),mi2(2));
mi_out_LCxRU=min(m1,mi_out(:,5));


%CExRU=PM
m1=min(mi1(3),mi2(2));
mi_out_CExRU=min(m1,mi_out(:,6));



%RCxRU=PB
m1=min(mi1(4),mi2(2));
mi_out_RCxRU=min(m1,mi_out(:,7));



%RIxRU=PB
m1=min(mi1(5),mi2(2));
mi_out_RIxRU=min(m1,mi_out(:,7));



%% Regras RV %%%%
%LExRV=NM
m1=min(mi1(1),mi2(3));
mi_out_LExRV=min(m1,mi_out(:,2));



%LCxRV=NS
m1=min(mi1(2),mi2(3));
mi_out_LCxRV=min(m1,mi_out(:,3));


%CExRV=PS
m1=min(mi1(3),mi2(3));
mi_out_CExRV=min(m1,mi_out(:,5));


%RCxRV=PM
m1=min(mi1(4),mi2(3));
mi_out_RCxRV=min(m1,mi_out(:,6));



%RIxRV=PB
m1=min(mi1(5),mi2(3));
mi_out_RIxRV=min(m1,mi_out(:,7));



%% Regras VE %%%%
%LExVE=NM
m1=min(mi1(1),mi2(4));
mi_out_LExVE=min(m1,mi_out(:,2));


%LCxVE=NM
m1=min(mi1(2),mi2(4));
mi_out_LCxVE=min(m1,mi_out(:,2));



%CExVE=ZE
m1=min(mi1(3),mi2(4));
mi_out_CExVE=min(m1,mi_out(:,4));


%RCxVE=PM
m1=min(mi1(4),mi2(4));
mi_out_RCxVE=min(m1,mi_out(:,6));



%RIxVE=PM
m1=min(mi1(5),mi2(4));
mi_out_RIxVE=min(m1,mi_out(:,6));



%% Regras LV %%%%
%LExLV=NB
m1=min(mi1(1),mi2(5));
mi_out_LExLV=min(m1,mi_out(:,1));



%LCxLV=NM
m1=min(mi1(2),mi2(5));
mi_out_LCxLV=min(m1,mi_out(:,2));



%CExLV=NS
m1=min(mi1(3),mi2(5));
mi_out_CExLV=min(m1,mi_out(:,3));



%RBxLV=PS
m1=min(mi1(4),mi2(5));
mi_out_RBxLV=min(m1,mi_out(:,5));



%RIxLV=PM
m1=min(mi1(5),mi2(5));
mi_out_RIxLV=min(m1,mi_out(:,6));



%% Regras LU %%%%
%LExLU=NB
m1=min(mi1(1),mi2(6));
mi_out_LExLU=min(m1,mi_out(:,1));



%LCxLU=NB
m1=min(mi1(2),mi2(6));
mi_out_LCxLU=min(m1,mi_out(:,1));



%CExLU=NM
m1=min(mi1(3),mi2(6));
mi_out_CExLU=min(m1,mi_out(:,2));


%RBxLU=NS
m1=min(mi1(4),mi2(6));
mi_out_RBxLU=min(m1,mi_out(:,3));


%RIxLU=PS
m1=min(mi1(5),mi2(6));
mi_out_RIxLU=min(m1,mi_out(:,5));



%% Regras LB %%%%
%LExLB=NB
m1=min(mi1(1),mi2(7));
mi_out_LExLB=min(m1,mi_out(:,1));



%LCxLB=NB
m1=min(mi1(2),mi2(7));
mi_out_LCxLB=min(m1,mi_out(:,1));



%CExLB=NM
m1=min(mi1(3),mi2(7));
mi_out_CExLB=min(m1,mi_out(:,2));



%RBxLB=NM
m1=min(mi1(4),mi2(7));
mi_out_RBxLB=min(m1,mi_out(:,2));



%RIxLB=NS
m1=min(mi1(5),mi2(7));
mi_out_RIxLB=min(m1,mi_out(:,3));






RULE_OUT=[mi_out_CExLB'; mi_out_CExLU'; mi_out_CExLV',; mi_out_CExRB'; mi_out_CExRU'; mi_out_CExRV'; mi_out_CExVE'; mi_out_LCxLB'; mi_out_LCxLU'; mi_out_LCxLV'; mi_out_LCxRB'; mi_out_LCxRU'; mi_out_LCxRV'; mi_out_LCxVE'; mi_out_LExLB'; mi_out_LExLU'; mi_out_LExLV'; mi_out_LExRB'; mi_out_LExRU'; mi_out_LExRV'; mi_out_LExVE'; mi_out_RBxLB'; mi_out_RBxLU'; mi_out_RBxLV'; mi_out_RCxRB'; mi_out_RCxRU'; mi_out_RCxRV'; mi_out_RCxVE'; mi_out_RIxVE'; mi_out_RIxLB'; mi_out_RIxLU'; mi_out_RIxLV'; mi_out_RIxRB'; mi_out_RIxRU'; mi_out_RIxRV'];



