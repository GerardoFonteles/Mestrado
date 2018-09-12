clc; 
clear all;

% A = zeros(3,4,2);
% A(:,:,1) = [1 4 7 10; 2 5 8 11;3 6 9 12];
% A(:,:,2) = [13 16 19 22; 14 17 20 23; 15 18 21 24];

%Tensor gerado randomicamente
A = randn(5,4,3);

%Aplica a HOSVD no tensor A e obtem o core tensor S e suas devidas bases
%Aest é o tensor estimado
[S,U1,U2,U3]= HOSVD(A);
Aest = tuckeroperator(S,U1,U2,U3);
test = A-Aest;

% A2 = zeros(4,4,2);
% A2(:,:,1) = [2 1 2 1; 2 4 9 4;2 5 6 2;7 7 3 2];
% A2(:,:,2) = [7 8 8 8;8 5 0 5;3 3 0 8;4 1 5 6];
% 
% [S,U1,U2,U3]= HOOI(A);
% Aest2 = tuckeroperator(S,U1,U2,U3);
% test1 = A-Aest2;

