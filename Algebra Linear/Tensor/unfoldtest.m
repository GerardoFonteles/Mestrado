A = zeros(3,4,2);
%A(:,:,1) = [0 2 4 6; 8 10 12 14; 16 18 20 22];
%A(:,:,2) = [1 3 5 7; 9 11 13 15; 17 19 21 23];
A(:,:,1) = [1 4 7 10; 2 5 8 11;3 6 9 12];
A(:,:,2) = [13 16 19 22; 14 17 20 23; 15 18 21 24];

A1 = unfold3tensor(A,1);

A2 = unfold3tensor(A,2);

A3 = unfold3tensor(A,3);

B1 = unfold3tensor2(A,1);
B2 = unfold3tensor2(A,2);
B3 = unfold3tensor2(A,3);

