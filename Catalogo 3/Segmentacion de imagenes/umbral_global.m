clc; clear; close all;
pkg load image;

A = imread("../Imagenes/imagen3.jpg");
A = im2double(A);
[m,n] = size(A);
B = zeros(m,n);

iter = 20;
T = 0.5;
for k=1:iter;
I1 = A>T;
I2 = A<=T;

B1 = A.*I1;
B2 = A.*I2;

m1 = sum(sum(B1))/sum(sum(I1));
m2 = sum(sum(B2))/sum(sum(I2)); 
T = 0.5*(m1+m2);
 
endfor

subplot(1,2,1);
imshow(A);
title('Imagen original');
  
C = zeros(m,n);
C(A>T) = 1;
C(A<=T) = 0;

subplot(1,2,2);
imshow(C);
title(['Imagen Umbral T=' num2str(T)]);
