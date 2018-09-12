% Iniciar
x=(-5.12):0.01:5.12;
[~,N]=size(x);
X=zeros(3,N);
X(1,:)=x;
for i=1:N
  X(2,i)=X(1,i)^2;
  X(3,i)=-10*cos(2*pi*X(1,i));
endfor
% X(1,:) = x
% X(2,:) = x^2
% X(3,:) = -10(cos(2*pi*x))

% Calcular f(x1,x2)
f=20*ones(N,N);
for i=1:N
  x1=X(2,i)+X(3,i);
  for j=1:N
    x2=X(2,j)+X(3,j);
    f(i,j)=f(i,j)+x1+x2;
  endfor
endfor

% Plotar 
figure
surf(X(1,:),X(1,:),f);
figure
contour(X(1,:),X(1,:),f);



