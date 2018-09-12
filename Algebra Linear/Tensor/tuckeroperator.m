function [C] = tuckeroperator(A,U1,U2,U3)
    %%
    %Calcula o tucker product para um tensor de ordem 3
    %recebendo o tensor A e seus Us e retornado o resultado C
    %%
    
    %Aplica o nmode product no tensor A e de seus respectivos U.
    AT1 = nmode(A,U1,1);
    AT2 = nmode(AT1,U2,2);
    AT3 = nmode(AT2,U3,3);
    C = AT3;


end

