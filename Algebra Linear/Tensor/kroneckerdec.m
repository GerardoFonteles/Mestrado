function [Atil,Y1,Z1] = kroneckerdec(A,m,n,p,q)
%Realize kronecker factorization 
    [v,t] = size(A);
     for k=1:t/q
        for i = 1:v/p
                if k == 1 && i == 1
                    D = A(1:p,1:q);
                    D = D(:);
                    lin = p;
                    col = 0;
                    %disp(D)
                else 
                    %disp(size(A(lin:i*p,col+1:k*q)))
                    aux = A(lin+1:i*p,col+1:k*q);
                    aux = aux(:);
                    D =[D aux];
                    lin = i*p;
                end
                %disp(D)
        end
        lin = 0;
        col = k*q;
     end
     
    [U, S ,V] = svd(D);%calculate the SVD
    Y = sqrt(max(S(:,1))).*conj(V(:,1));%calculate the vec(Y) 
    Z = sqrt(max(S(:,1))).*(U(:,1));%calculate the vec(Z)

    
    Y1 = vectomat(Y,m);%unvec(Y_{MxN})
    Z1 = vectomat(Z,q);%unvec(Z_{PxQ})

    Atil =  kronecker(Y1,Z1);%the estimated kronecker 
end
