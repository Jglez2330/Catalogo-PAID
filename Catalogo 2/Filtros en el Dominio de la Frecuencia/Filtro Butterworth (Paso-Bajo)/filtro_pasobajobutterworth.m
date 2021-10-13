function ejemploFiltroPasoBajoButterworth
  % Ejemplo
  
  pkg load image;
  clear;
  clc;
  close all;
  
  filtroPasoBajoButterworth(230, 2);
  
endfunction

function filtroPasoBajoButterworth(D0, o)
  % Esta funcion aplica el filtro paso bajo butterworth a una imagen
  % en escala de grises
  % Parametros de entrada: D0 = valor del radio del
  %                        circulo del filtro pasobajo butterworth
  %                        o = orden del filtro
  
  A = imread('../../Imagenes/edificio_china.jpg');
  subplot(3, 2, 1);
  imshow(A);
  title('Imagen Original');

  A = im2double(A);
  F = fft2(A);
  subplot(3, 2, 2);
  imshow(log(1 + abs(F)), []);
  title('Imagen Fourier');
  
  Fshift = fftshift(F);
  subplot(3, 2, 3);
  imshow(log(1 + abs(Fshift)), []);
  title('Imagen Fourier (shift)');
  
  [m, n] = size(A);
  D = zeros(m, n);
  for u = 1:m
    for v = 1:n
      D(u, v) = sqrt((u - (m / 2)) ^ 2 + (v - (n / 2)) ^ 2);
    endfor
  endfor
  
  Fmask = 1 ./ (1 + (D ./ D0).^(2 * o));
  subplot(3, 2, 4);
  imshow(log(1 + abs(Fmask)), []);
  title('Mascara Fourier');
  
  Fmask = fftshift(Fmask);
  
  Fresult = fftshift(F .* Fmask);
  subplot(3, 2, 5);
  imshow(log(1 + abs(Fresult)), []);
  title('Resultado Fourier');
  
  Fresult = fftshift(Fresult);
 
  B = ifft2(Fresult);
  B = im2uint8(abs(B));
  subplot(3, 2, 6);
  imshow(B);
  title('Resultado');
  
endfunction