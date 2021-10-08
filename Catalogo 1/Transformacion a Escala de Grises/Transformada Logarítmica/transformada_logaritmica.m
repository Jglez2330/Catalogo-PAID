function ejemploTransformacionLogaritmica
  % Ejemplo
  
  pkg load image;
  clear;
  clc;
  close all;
  
  transformacionLogaritmica(0.2);
  
endfunction

function transformacionLogaritmica(c)
  % Esta funcion aplica una transformacion de logaritmica a una imagen 
  % en escala de grises, se utiliza para expandir los valores de los
  % pixeles claros y comprime los pixeles oscuros
  % Parametros de entrada: c = constante utilizada por la funcion
  
  A = imread('../../Imagenes/log.jpg');
  subplot(1, 2, 1);
  imshow(A);
  title('Imagen Original');

  A = double(A);
  [m, n] = size(A);
  B = zeros(m, n);

  B = c * log(1 + A);

  subplot(1, 2, 2);
  imshow(B);
  title('Imagen Modificada');
  
endfunction