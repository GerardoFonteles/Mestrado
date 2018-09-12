function [ A ] = unfold3tensor2(tensor,mode)
[m,n,z] = size(tensor);
A = 0;
if mode ==1
    for k=1:m
       if k==1
           A = reshape(tensor(k,:,:),z,n);
       else
           A = [A; reshape(tensor(k,:,:),z,n)];
       end

    end
    
elseif mode == 2
    for k=1:n
       if k==1
           A = reshape(tensor(:,k,:),m,z);
       else
           A = [A; reshape(tensor(:,k,:),m,z)];
       end

    end
    
elseif mode == 3
    for k=1:z
       if k==1
           A = reshape(tensor(:,:,k),m,n);
       else
           A = [A; reshape(tensor(:,:,k),m,n)];
       end

    end

    
end

end

