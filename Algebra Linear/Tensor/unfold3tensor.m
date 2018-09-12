function [ A ] = unfold3tensor(tensor,mode) 
%%
%Essa função realiza o unfold de um tensor por meio de seas fibers ela
%recebe um tensor(tensor) e o devido mode(mode) para o unfold
%%

[m,n,z] = size(tensor);
A = 0;
if mode == 1 %Para o mode 1
    for j = 1:z%Primeiro for para recorrer a dimensao 3
        for i=1:n %Segundo for para recorrer a dimensao 2 
            if  j == 1 && i == 1
                A = reshape(tensor(:,1,1),m,1);%converte para uma vetor
            else
                A = [A reshape(tensor(:,i,j),m,1)];%converte para um vetor e stacka no formato de uma matrix
            end

        end
    end
    
elseif mode == 2 %Para o mode 1
    for j = 1:z %Primeiro for para recorrer a dimensao 3
        for i=1:m %Segundo for para recorrer a dimensao 1
            if  j == 1 && i == 1
                A = reshape(tensor(1,:,1),n,1);%converte para uma vetor
            else
                A = [A reshape(tensor(i,:,j),n,1)];%converte para uma vetor
            end
        end
    end
    
elseif mode == 3 %Para o mode 3   
    for j = 1:n %Primeiro for para recorrer a dimensao 2
        for i=1:m %Segundo for para recorrer a dimensao 1
            if  j == 1 && i == 1
                A = reshape(tensor(1,1,:),z,1);%converte para uma vetor
            else
                A = [A reshape(tensor(i,j,:),z,1)];%converte para uma vetor
            end
        end
    end
end
end
