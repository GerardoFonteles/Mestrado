function [A1,A2,A3,error] = ALS_Known_As(A,A2,A3)
[I,J,K] = size(A);
% 
% if dft == 1
%     A2 = dftmtx(R);
%     A3 = dftmtx(R);
% else
%     
% end
% %Initialize A(n)
% A2 = randn(J,R);
% A3 = randn(K,R);

iteration = 100;
error = zeros(1,iteration);
for i=1:iteration
         
     A1 = unfold3tensor(A,1)*pinv(KhatriRao(A3,A2)');  
     %A2 = unfold3tensor(A,2)*pinv(KhatriRao(A3,A1)');
     %A3 = unfold3tensor(A,3)*pinv(KhatriRao(A2,A1)');

     error(i) = norm(unfold3tensor(A,1),'fro') - norm(A1*(KhatriRao(A3,A2))','fro');
     
     
     if(error(i) < 1e-13)
        break;
     end
     %disp(error(i))
%disp(i)
end

%lambda1 = normc(A1);
%lambda2 = normc(A2);
%lambda3 = normc(A3);
end
