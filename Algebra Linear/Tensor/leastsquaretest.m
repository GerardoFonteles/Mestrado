%%%%%% Professor example %%%%%%%%
% B = [1 2; 3 4]; 
% C  = [0 7; -1 8];

% %%%%%% hadamard matrix %%%%%%%%
B = hadamard(4);
C = hadamard(4);

% %%%%%% DFTS %%%%%%%%
% t = 0:1/100:1-1/100;                     
% x = sin(2*pi*15*t) + sin(2*pi*40*t);
% y = cos(2*pi*15*t) + cos(2*pi*40*t);
% B = fft(x);
% C = fft(y);

%%%%%% Test %%%%%%%%
%  B = [1 2 3 4]; 
%  C  = [0 7 -1 8];


A = KhatriRao(B,C);
[m,n] = size(B);
N = 50;
resultado = zeros(N,1);
xaxis = linspace(1,N,1);
k = 1;
for i=1:0.5:N    
    A1 = awgn(A,i);

    WX = KhatriRaodec(A1,m);

    result(k) = (norm(A - WX,'fro')^2)/(norm(A,'fro')^2);
    k = k+1;
end

stem(result,'filled');
title('Least-Squares Khatri-Rao Factorization')
xlabel('Number of iteration') % x-axis label
ylabel('Normalized mean square error') % y-axis label
