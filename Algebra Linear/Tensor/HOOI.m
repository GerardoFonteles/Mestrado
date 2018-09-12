function [G,U1,U2,U3] = HOOI(A)
[m,n,z] = size(A);

[S,U1,U2,U3] = HOSVD(A);

k = 1;

for i=1:k
   
        Y = tuckeroperator(A,U1',U2',U3');
        A1 = unfold3tensor(Y,1);
        A2 = unfold3tensor(Y,2);
        A3 = unfold3tensor(Y,3);

        [U1,S1,V1] = svd(A1);
        [U2,S2,V2] = svd(A2);
        [U3,S3,V3] = svd(A3);

end

G = tuckeroperator(A,U1',U2',U3');
%tuckeroperator(g,U1,U2,U3);
end 
