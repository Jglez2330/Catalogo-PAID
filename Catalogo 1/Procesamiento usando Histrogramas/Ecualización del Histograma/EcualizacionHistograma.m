pkg load image
function imagenEcualizada = ecualizarImagen(img_path)
    %Esta funcion calcula una imagen ecualizada
    %
    %Sintaxis: ecualizarImagen(img_path)
    %
    %Entrada:
    %    img_path -> direccion de la imagen a ecualizar
    %
    %Salida:
    %    Imagen ecualizada del tamaño de la imagen original
    img = imread(img_path);
    hist = obtenerHistograma(img);
    [m, n] = size(img);
    dist_acu = distribucionAcumulativa(hist, m, n);
    
    imagenEcualizada = zeros(m, n);
    img_double = double(img);
    
    for x = 1:m
        for y = 1:n
            imagenEcualizada(x, y) = round(dist_acu(img_double(x , y) + 1) * 255);
        endfor
    endfor

    imagenEcualizada = uint8(imagenEcualizada);
    
    
endfunction

function histograma = obtenerHistograma(img)
    %Esta funcion calcula el histograma de una imagen
    %
    %Sintaxis: obtenerHistograma(img)
    %
    %Entrada:
    %    img -> Imagen a calcular el histograma
    %
    %Salida:
    %    Array de tamaño de 256 con el histograma
    
    histograma = zeros(256, 1);
    for i = 0:255
        histograma(i+1) = sum(sum(img == i));
    endfor
endfunction

function dist = distribucionAcumulativa(hist, m, n)
    %Esta funcion calcula la distribucion del histograma de una imagen
    %
    %Sintaxis: distribucionAcumulativa(hist, m, n)
    %
    %Entrada:
    %    hist -> direccion de la imagen a calcular el histograma
    %    m -> Entero, tamaño del ancho   
    %    n -> Entero, tamaño del alto
    %
    %Salida:
    %    Array de tamaño de 256 con la distribucion acumulada

    dist = zeros(256, 1);
    for i = 0: 255
        dist(i + 1) = sum(hist(1:i+1)/(m*n));
    endfor

endfunction

A = imread('../../Imagenes/boat.jpg');
subplot(1, 2, 1);
imshow(A);
title('Imagen Original');

img_final = ecualizarImagen('../Imagenes/boat.jpg');
subplot(1, 2, 2);
imshow(img_final);
title('Imagen Modificada');
