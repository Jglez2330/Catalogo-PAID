function ejemploFiltroLaplaciano
  % Ejemplo
  
  pkg load image;
  clear;
  clc;
  close all;
  
  filtroLaplaciano();
  
endfunction

function filtroLaplaciano()
  % Esta funcion aplica el filtro laplaciano a una imagen
  % en escala de grises
  
  A = imread('../../Imagenes/baby_yoda.jpg');
  subplot(1, 2, 1);
  imshow(A);
  title('Imagen Original');

  A = im2double(A);
  B = [1 1 1; 1 -8 1; 1 1 1];
  C = conv2(A, B, 'same');
  C = im2uint8(C);
  
  subplot(1, 2, 2);
  imshow(C);
  title('Imagen Modificada');
  
endfunction