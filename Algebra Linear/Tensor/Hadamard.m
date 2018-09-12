function C = Hadamard(A,B)

%A = [1 2;3 4];
%B = [0 7; -1 8];

[m,n] = size(A); 
[p,q] = size(B);

C = zeros(m,n);
for i=1:m
   for j=1:n
        C(i,j) = A(i,j)*B(i,j);
   end
end
