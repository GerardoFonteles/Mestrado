%%%%%% Professor example %%%%%%%%

B = [1 2; 3 4]; 
C  = [0 7; -1 8];
B = [1 2 3 ; 3 2 1];
C = [2 1 ; 2 3];
%%%%%% hadamard matrix %%%%%%%%
% B = hadamard(16);
% C = hadamard(16);

% %%%%%% DFTS %%%%%%%%
% t = 0:1/10:10-1/10;                     % Time vector
% x = sin(2*pi*15*t) + sin(2*pi*40*t);
% y = cos(2*pi*15*t) + cos(2*pi*40*t);
% B = fft(x);
% C = fft(y);

%%%%%% Test %%%%%%%%
%  B = [1 2 3 4]; 
%  C  = [0 7 -1 8];

[m,n] = size(B);
[p,q] = size(C);

A = kronecker(B,C);

N = 50;
result = zeros(N,1);
xaxis = linspace(1,N,1);
k = 1;
% for i=1:0.5:N
%     
%     A1 = awgn(A,i);
% 
%     [Atil,Y,Z] = kroneckerdec(A,m,n,p,q);
%     D = kronecker(Y,Z);
%     
%     result(k) = (norm(A - D,'fro')^2)/(norm(A,'fro')^2);
%     k = k+1;
% end

% stem(result,'filled');
% title('Least-Squares Kron Factorization')
% xlabel('SNR in dB') % x-axis label
% ylabel('Normalized mean square error') % y-axis label

