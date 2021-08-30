clear;
clc;
close all;
pkg load image;

A = imread('../../Imagenes/log.jpg');
subplot(1, 2, 1);
imshow(A);
title('Imagen Original');

A = double(A);
[m, n] = size(A);
B = zeros(m, n);

c = 0.2;

B = c * log(1 + A);

subplot(1, 2, 2);
imshow(B);
title('Imagen Modificada');