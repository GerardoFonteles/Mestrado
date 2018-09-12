function [B] = KhatriRaodec(A,q)
%Realize kronecker factorization 
%A is the result of the Khatri-Rao product of B and C
%q is the number of columns of B and C 

    [m,n] = size(A);
    for i=1:n
        aux = A(:,i);%Take the i colloum of A
        ap = vectomat(aux,q);%Unvec(A(:,i)) into a matrix NxQ
        if i == 1
            [U,S,V] = svd(ap);%Calculate the SVD of ap 
            w = [sqrt(max(S(:,1))).*conj(V(:,1))];%first column of W
            x = [sqrt(max(S(:,1))).*U(:,1)];%first column of X
        else
            [U,S,V] = svd(ap); 
            w = [w sqrt(max(S(:,1))).*conj(V(:,1))];%The rest of the columns of W
            x = [x sqrt(max(S(:,1))).*U(:,1)];%The rest of the columns of X
        end    
    end
    B = KhatriRao(w,x);%Estimated Khatri-Rao
end
