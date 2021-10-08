pkg load image

function imagenEspecificada = especificacionHistograma(img_path_origen, img_path_especificada)
    % Esta funcion implementa el metodo de especificacion de histograma, el cual consiste
    % en aplicar el histograma de una imagen (imagen especificada) en otra imagen 
    % (imagen objetivo)
    %
    % Sintaxis: especificacionHistograma(img_path_origen, img_path_especificada)
    %
    % Entrada:
    %   img_path_origen -> string path de la imagen objetivo
    %   img_path_especificada -> string path de la imagen especificada
    %
    % Salida:
    %   imagenEspecificada -> Imagen final, tamaña de la imagen objetivo, matriz

    img = imread(img_path_origen);
    [img_m, img_n] = size(img);
    
    img_especificada = imread(img_path_especificada);
    [especificada_m, especificada_n] = size(img_especificada);

    hist_img = obtenerHistograma(img);
    hist_especificada = obtenerHistograma(img_especificada);

    acu_img = distribucionAcumulativa(hist_img, img_m, img_n);
    acu_espe = distribucionAcumulativa(hist_especificada, especificada_m, especificada_n);

    imagenEspecificada = zeros(img_m, img_n);
    img_double = double(img);

    mapeo = zeros(256);

    for i = 1:256
        [value, index] = min(abs(acu_espe - acu_img(i)));
        mapeo(i) = index;
    endfor
    for x = 1:img_m
        for y = 1:img_n         
            imagenEspecificada(x, y) = round(mapeo(img_double(x, y) + 1));
        endfor
    endfor
    imagenEspecificada = uint8(imagenEspecificada);
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

A = imread('../Imagenes/boat.jpg');
subplot(2, 3, 1);
imshow(A);
title('Imagen Original');

especi = imread('../Imagenes/peppers.jpeg');
subplot(2, 3, 2);
imshow(especi);
title('Imagen especificada');

img_final = especificacionHistograma('../Imagenes/boat.jpg', '../Imagenes/peppers.jpeg');
subplot(2, 3, 3);
imshow(img_final);
title('Imagen Modificada');

hist_ori = obtenerHistograma(A);
subplot(2, 3, 4);
bar(hist_ori);
title('Histograma Original');

hist_especi = obtenerHistograma(especi);
subplot(2, 3, 5);
bar(hist_especi);
title('Histograma Especificada');

hist_final = obtenerHistograma(img_final);
subplot(2, 3, 6);
bar(hist_final);
title('Histograma Imagen Final');