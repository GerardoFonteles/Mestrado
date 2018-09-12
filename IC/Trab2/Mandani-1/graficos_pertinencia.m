clear; clc; close all;

x=-90:0.1:270;  % Universo de discurso da variavel de interesse
phi = 0:0.1:270; % Universo de discurso da variavel de interesse
the = -30:0.1:30;
L=length(x); % No. total de medidas da variavel linguistica

M=[];
for i=1:L,
  %mi=velocidade(x(i));  % pertinencia aos conjuntos fuzzy (velocidade)
  %mi=curvatura(x(i));  % pertinencia aos conjuntos fuzzy (curvatura)
  %mi = distancia(x(i));
  mi=forca_pedal_freio(x(i));  % pertinencia aos conjuntos fuzzy (forca no pedal de freio)
  M=[M; mi];
end


%Para curvatura em theta
figure; hold on
plot(x,M(:,1),'r-'); % grafico conjunto fuzzy temperatura BAIXA
plot(x,M(:,2),'b-'); % grafico conjunto fuzzy temperatura MEDIA
plot(x,M(:,3),'m-'); % grafico conjunto fuzzy temperatura ALTA
plot(x,M(:,4),'k-')
plot(x,M(:,5),'g-')
plot(x,M(:,6),'y-')
plot(x,M(:,7),'Color',[0.7 0.7 0.7])
hold off
axis([-30 30 0 1.2]);
xlabel('CURVATURA');
legend('NB','NM','NS','ZE','PS','PM','PB')

%Para curvatura
% figure; hold on
% plot(x,M(:,1),'r-'); % grafico conjunto fuzzy temperatura BAIXA
% plot(x,M(:,2),'b-'); % grafico conjunto fuzzy temperatura MEDIA
% plot(x,M(:,3),'m-'); % grafico conjunto fuzzy temperatura ALTA
% plot(x,M(:,4),'k-')
% plot(x,M(:,5),'g-')
% plot(x,M(:,6),'y-')
% plot(x,M(:,7),'Color',[0.7 0.7 0.7])
% hold off
% axis([-90 270 0 1.2]);
% xlabel('CURVATURA');
% legend('RB','RU','RV','VE','LV','LU','LB')

%Para distancia
% figure; hold on
% plot(x,M(:,1),'r-'); % grafico conjunto fuzzy temperatura BAIXA
% plot(x,M(:,2),'b-'); % grafico conjunto fuzzy temperatura MEDIA
% plot(x,M(:,3),'m-'); % grafico conjunto fuzzy temperatura ALTA
% plot(x,M(:,4),'k-')
% plot(x,M(:,5),'g-')
% hold off
% axis([0 270 0 1.2]);
% xlabel('CURVATURA');
% legend('LE','LC','CE','RC','HI')