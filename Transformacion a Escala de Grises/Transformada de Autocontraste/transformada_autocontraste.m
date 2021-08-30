clear;
clc;
close all;
pkg load image;

A = imread('../../Imagenes/boat_new.jpg');
subplot(1, 2, 1);
imshow(A);
title('Imagen Original');

A = double(A);
[m, n] = size(A);
B = zeros(m, n);

rmin = min(min(A));
rmax = max(max(A));

B = (255 / (rmax - rmin)) * (A - rmin);

B = uint8(B);
subplot(1, 2, 2);
imshow(B);
title('Imagen Modificada');