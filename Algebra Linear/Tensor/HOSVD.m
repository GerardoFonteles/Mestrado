function [S,U1,U2,U3] = HOSVD(A)
    %%
    %Calcula a HOSVD para um tensor recebe um tensor de ordem 3(A) e
    %retorna o core tensor S e suas bases U1, U2, U3
    %%
    
    %Calcula todos os unfold do dado tensor
    A1 = unfold3tensor(A,1);
    A2 = unfold3tensor(A,2);
    A3 = unfold3tensor(A,3);

    %Calcula todas as svds para os unfold
    [U1,S1,V1] = svd(A1);
    [U2,S2,V2] = svd(A2);
    [U3,S3,V3] = svd(A3);

    %De posse das bases U1,U2,U3 usamos o tucker operator to calculate the 
    %core tensor of this tensor A
    S = tuckeroperator(A,U1',U2',U3');
    
    
end

