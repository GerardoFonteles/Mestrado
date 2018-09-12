function [mse] = MSE(X,Y)

    aux = (double(X(:))-double(Y(:)));
    aux = aux.^2;
    mse = (sum(aux))/(size(X,1));
    
end

