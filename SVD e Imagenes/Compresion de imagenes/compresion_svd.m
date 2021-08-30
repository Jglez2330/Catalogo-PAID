clear;
clc;
close all;
pkg load image;

function A = aproximage(U, S, V, r)
    A = U(:, 1:r) * S(1:r, 1:r) * V(:, 1:r)';
endfunction

function save_matrices(U, S, V, r, nameB, nameC)
    B = U(:, 1:r) * S(1:r, 1:r);
    C = V(:, 1:r)';
    B = im2uint8(B);
    C = im2uint8(C);
    save(nameB, 'B');
    save(nameC, 'C');
endfunction

I_color = imread('../../Imagenes/Barbara.png');
[m, n, c] = size(I_color);
Aog = im2double(I_color);

Ar = Aog(:, :, 1);
Ag = Aog(:, :, 2);
Ab = Aog(:, :, 3);

[Ur, Sr, Vr] = svd(Ar);
[Ug, Sg, Vg] = svd(Ag);
[Ub, Sb, Vb] = svd(Ab);

r = 50;
Arr = aproximage(Ur, Sr, Vr, r);
Agr = aproximage(Ug, Sg, Vg, r);
Abr = aproximage(Ub, Sb, Vb, r);

Afinal = cat(3, Arr, Agr, Abr);

save_matrices(Ur, Sr, Vr, r, 'Br.mat', 'Cr.mat');
save_matrices(Ug, Sg, Vg, r, 'Bg.mat', 'Cg.mat');
save_matrices(Ub, Sb, Vb, r, 'Bb.mat', 'Cb.mat');

Aplot = im2uint8(Afinal); % Convertir a 8 bits para representar 
figure
subplot(1,2,1);
imshow(I_color);

subplot(1,2,2);
imshow(Aplot);