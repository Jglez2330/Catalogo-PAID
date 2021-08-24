clear;
clc;
close all;
pkg load image;

function A = aproximage(U,S,V,r)
    A = U(:,1:r) * S(1:r,1:r) * V(:,1:r)';
endfunction

I_color = imread('../Imagenes/barbara.png');
[m,n,c] = size(I_color)
Aog = im2double(I_color);

Ar = Aog(:,:,1);
Ag = Aog(:,:,2);
Ab = Aog(:,:,3);

[Ur,Sr,Vr] = svd(Ar);
[Ug,Sg,Vg] = svd(Ag);
[Ub,Sb,Vb] = svd(Ab);

r = 50;
Arr = aproximage(Ur,Sr,Vr,r);
Agr = aproximage(Ug,Sg,Vg,r);
Abr = aproximage(Ub,Sb,Vb,r);

Afinal = cat(3,Arr,Agr,Abr);

B = Ur(:,1:r) * Sr(1:r,1:r);
C = Vr(:,1:r)';
B = im2uint8(B);
C = im2uint8(C);
save('B.mat', 'B');
save('C.mat', 'C');

Aplot = im2uint8(Afinal); % Convertir a 8 bits para representar 
figure
subplot(1,2,1);
imshow(I_color);

subplot(1,2,2);
imshow(Aplot);