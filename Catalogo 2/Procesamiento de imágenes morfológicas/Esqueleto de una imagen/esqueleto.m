clc;
clear;
close all;
pkg load image;

A = im2bw(imread('../../Imagenes/cuerpo.jpg'), 0.4);
B = [0 1 0; 1 1 1; 0 1 0];

Xk = A;
S_A = A&~imopen(A, B);
while 1
    Xk = imerode(Xk, B);
    S_A = (Xk & ~imopen(Xk, B)) | S_A;
    if Xk == 0
        break;
    endif
endwhile

subplot(1,2,1);
imshow(A);
title('Imagen original');

subplot(1,2,2);
imshow(S_A);
title('Esqueleto')
