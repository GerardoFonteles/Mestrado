% Programa que raliza a quantização de imagens

clc;
clear all;
close all;



% Imagem de baixos detalhes
lena = imread('crowd2.jpg');
lena = lena(:,:,1);

max = 255;
c = double(lena) / max;

figure(8);
set(8,'Name','8Bits');
imshow(lena);

lena_results = zeros(length(lena),length(lena),7);
MSE_results = zeros(7);

for i=1:7 
    f = (2^i-1);
    s = imadjust(uint8(round(f * c)), [0 f/max],[0 1]);
    figure(i);
    set(i,'Name','7bits');
    imshow(s);
    lena_results(:,:,i) = s;
    results_MSE(i) = immse(lena,uint8(lena_results(:,:,i)));
    
end


