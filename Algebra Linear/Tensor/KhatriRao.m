function C = KhatriRao(A,B)
%Realize the Khatri-Rao Product

[m,n] = size(A); 
[p,q] = size(B);

if q==n
    for i=1:n
        aux = kronecker(A(:,i),B(:,i));
        if i == 1
            C = aux;
        else
            C = [C aux];
        end
    end
%Handle if the number of collouns ara not the same    
else
    disp('matrices collouns did not match')
    return
end
end