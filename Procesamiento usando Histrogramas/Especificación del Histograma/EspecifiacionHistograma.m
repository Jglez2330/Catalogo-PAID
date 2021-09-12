pkg load image

function imagenEspecificada = especificacionHistograma(img_path_origen, img_path_especificada)

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

    dist = zeros(256, 1);
    for i = 0: 255
        dist(i + 1) = sum(hist(1:i+1)/(m*n));
    endfor

endfunction

function histograma = obtenerHistograma(img)
    histograma = zeros(256, 1);
    for i = 0:255
        histograma(i+1) = sum(sum(img == i));
    endfor
endfunction


r = especificacionHistograma('../Imagenes/boat.jpg', '../Imagenes/peppers.jpeg');

imshow(r)