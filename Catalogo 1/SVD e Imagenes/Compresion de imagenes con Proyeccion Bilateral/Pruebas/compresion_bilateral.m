clc;
clear;
close all;
pkg load image;

function save_matrices(B, C, nameB, nameC)
    B = im2uint8(B);
    C = im2uint8(C);
    save(nameB, 'B');
    save(nameC, 'C');
endfunction

function [Acosito, Bcosito, Ccosito] = proyeccion_bilateral(A, r, p, n)
    Y2 = randn(n, r);

    for k = 1:p
        Y1 = A * Y2;
        Y2 = A' * Y1;
    endfor

    [Q,~] = qr(Y2);
    Q = Q(:,1:r);

    Bcosito = A * Q;
    Ccosito = Q';
    Acosito = Bcosito * Ccosito;
endfunction

I_color = imread('../../../Imagenes/Barbara.png');
A = im2double(I_color);
[m, n, c] = size(A);

Ar = A(:, :, 1);
Ag = A(:, :, 2);
Ab = A(:, :, 3);

r = 50;
p = 5;

[Arr, Brr, Crr] = proyeccion_bilateral(Ar, r, p, n);
[Agr, Bgr, Cgr] = proyeccion_bilateral(Ag, r, p, n);
[Abr, Bbr, Cbr] = proyeccion_bilateral(Ab, r, p, n);

Afinal = cat(3, Arr, Agr, Abr);

save_matrices(Brr, Crr, 'Br.mat', 'Cr.mat');
save_matrices(Bgr, Cgr, 'Bg.mat', 'Cg.mat');
save_matrices(Bbr, Cbr, 'Bb.mat', 'Cb.mat');

Aplot = im2uint8(Afinal); % Convertir a 8 bits para representar 
figure
subplot(1, 2, 1);
imshow(I_color);

subplot(1, 2, 2);
imshow(Aplot);