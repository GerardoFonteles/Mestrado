function D = nmode(A,U,mode)
    %%%%%%
    %Calcula o nmode product recebendo A e U assim como o mode para
    %dar um fold e unfold correto
    %%%%%%
    [m,n,z] = size(A);
    [p,q] = size(U);
    
    if mode == 1%para dar o unfold em 1
        A = unfold3tensor(A,1);
    elseif mode == 2%para dar o unfold em 2
        A = unfold3tensor(A,2);
    else%para dar o unfold em 3
        A = unfold3tensor(A,3);
        z = n;% o valor de z deve ser igual ao da segunda 
        %dimensao de acordo com a implementacao do fold
    end
    
    D = U*A;%multiplica U pelo tensor unfolded no mode correto obtendo uma matriz
    D = fold(D,z,mode);%da o fold na matriz para se obter um tensor
end

