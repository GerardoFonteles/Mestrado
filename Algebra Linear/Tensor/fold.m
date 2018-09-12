function [ A ] = fold(matrix,dim,mode)
%%
%Retorna um tensor recebendo a uma matrix(matrix) que a versao desse tensor
%unfolded a 3 dimensao(dim) referente ao tensor eo mode(mode) desejado
%para o unfolded 3 é necessário passar a dimensao de N de tensor da ordem
%MxNxZ
%%
[m,n] = size(matrix);

if mode == 1 %para o unfolded mode 1
    A = zeros(m,n/dim,dim);%criar o tensor com a dimensoes desejadas
    for i=1:dim%loop para percorrer a terceira dimensao do tensor
        if i == 1
            A(:,:,i) = matrix(:,1:n/dim);%corta a matrix o tamanho desejado e stacka esse corte no tensor
            aux = n/dim;
        else 
            A(:,:,i) = matrix(:,aux+1:i*n/dim);%percorre a matrix e stacka todos os resultados na terceira dimensao do tensor
            aux = i*n/dim;
        end
    end
elseif mode == 2%%para o unfolded mode 1
     A = zeros(n/dim,m,dim);%criar o tensor com a dimensoes desejadas
     for i=1:dim
        if i == 1
            A(:,:,i) = matrix(:,1:n/dim)';%Como esse é o unfolded mode 2 temos que pergar o transposto do resultado
            aux = n/dim;
        else 
            A(:,:,i) = matrix(:,aux+1:i*n/dim)';
            aux = i*n/dim;
        end
     end
elseif mode == 3%%para o unfolded mode 1
    %%%%%%%%%%%%%%%%%%%%%%%%%%
    %para dar o fold em tensor no modo 3 dim =  m 
     A = zeros(n/dim,dim,m);%Cria o tensor 
     for j=1:dim%Para esse caso foi utilizados as fibers da matrix por isso os dois loops
        for i=1:n/dim
        
            if i == 1 && j ==1
                A(1,1,:) = matrix(:,1);%O primeiro vetor será o primeiro vetor do tensor para (1,1,:)
                aux=1;
            else 
                A(i,j,:) = matrix(:,aux+1);%Os vetores são então stackados no tensor.
                aux = aux+1;
            end
        end
     end
end


end
