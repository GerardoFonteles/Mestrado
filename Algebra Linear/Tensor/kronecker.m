function D = kronecker(A,B)
%Realize the kronecker product
    
[m,n] = size(A); 
[p,q] = size(B);

%This loop stack all the a(i,j)*B as column    
    for i=1:m
       for j=1:n
          aux = A(i,j)*B;
          if i==1 && j==1
              C = aux;
          else
            C = [C aux];
           end     
       end
    end
%reorganized matrix C in D spliting the C matrix and stack the result rowise.   
    [t, v] = size(C);
    for k=1:v/(n*q)
            if k ==1
                D = C(:,1:(n*q));
                aux2 = n*q;
            else
                D = [D;C(:,aux2+1:(k*n*q))];
                aux2 = k*n*q;
            end
    end        
    
end

