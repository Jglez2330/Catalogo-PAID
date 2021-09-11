pkg load image
function imagenEcualizada = ecualizarImagen(img_path)
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
    histograma = zeros(256, 1);
    for i = 0:255
        histograma(i+1) = sum(sum(img == i));
    endfor
endfunction

function dist = distribucionAcumulativa(hist, m, n)

    dist = zeros(256, 1);
    for i = 0: 255
        dist(i + 1) = sum(hist(1:i+1)/(m*n));
    endfor

endfunction

img_final = ecualizarImagen('../Imagenes/boat.jpg');
imshow(img_final)