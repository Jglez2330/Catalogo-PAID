clc;
clear;
close all;
pkg load image;

function A_filtered = median_filter(A)
    [m, n] = size(A);
    A = padarray(A, [1, 1], 0, 'both');
    A_filtered = zeros(m, n);
    for i = 2:m+1
        for j = 2:n+1
            A_filtered(i-1,j-1) = median(reshape(A(i-1:i+1,j-1:j+1), 1, 9));
        endfor
    endfor
endfunction


I_color = imread('../../Imagenes/paris.jpg');
Aog = im2double(I_color);

Ar = Aog(:, :, 1);

Ar_filtered = median_filter(Ar);

Aplot = im2uint8(Ar_filtered);
figure
subplot(1, 2, 1);
imshow(I_color);
title('Imagen con ruido');

subplot(1, 2, 2);
imshow(Aplot);
title('Imagen filtrada');