pkg load image

function filtered_image = harmonic_mean_filter(img, kernel_dims)
    %This function applies the harmonic mean filter to an image in array format
    %image: array_like representing the image
    %kernel_dims: dimentions for the kernel
    %returns: array_like representing the image with the harmonic mean filter 
    [m, n] = size(img);
    filtered_image = zeros(m, n);    
    for i = 1:n
        for j = 1:m
            submatrix = get_submatrix(img, kernel_dims, kernel_dims, i , j);
            %subma = block(image, i , j, kernel_dims, kernel_dims);
            [m2, n2] = size(submatrix);
            sum_items = 0;
            for x = 1:n2
                for y = 1:m2
                    element = submatrix(y, x);
                    if (element != 0)
                        sum_items = sum_items + 1/(element);
                    endif
                endfor
            endfor
            filtered_image(j , i) = numel(submatrix)/sum_items;
        endfor
    endfor
    filtered_image = im2uint8(filtered_image);
endfunction


function submatrix = get_submatrix(image, size_x, size_y, i , j)
    %This function gets the submatrix of a new 
    %image: array_like representing the image
    %size_x: dimentions for the kernel in x axis
    %size_y: dimentions for the kernel in y axis
    %i: center in x
    %j:center in y
    %returns: array of the submatrix of the g
    distance_x = round(size_x/2) - 1;
    distance_y = round(size_y/2) - 1; 
    submatrix = get_submatrix_aux(image, distance_x, distance_x, distance_y, distance_y, i, j);
    
endfunction

function submatrix = get_submatrix_aux(image, size_x_right, size_x_left, size_y_up, size_y_down, i, j)
    %This recursive function adjusts the kernel size of elements in case of borders and corners
    %image: array_like representing the image
    %size_x_right: dimentions for the kernel in x axis in the right
    %size_x_left: dimentions for the kernel in x axis in the left
    %size_y_up: dimentions for the kernel in y axis in the up side
    %size_y_down: dimentions for the kernel in y axis in the down side
    %i: center in x
    %j:center in y
    %returns: array of the submatrix of the g
    [m, n] = size(image);
    if (i - size_x_left < 1)
        submatrix = get_submatrix_aux(image, size_x_right, size_x_left - 1, size_y_up, size_y_down, i, j);
    elseif (i + size_x_right > n)
        submatrix = get_submatrix_aux(image, size_x_right - 1, size_x_left, size_y_up, size_y_down, i, j);
    elseif (j - size_y_up < 1)
        submatrix = get_submatrix_aux(image, size_x_right, size_x_left, size_y_up - 1, size_y_down, i, j);
    elseif (j + size_y_down > m)
        submatrix = get_submatrix_aux(image, size_x_right, size_x_left, size_y_up, size_y_down - 1, i, j);
    else
        submatrix = image( (j - size_y_up):(j + size_y_down), (i - size_x_left):(i + size_x_right));
    endif
endfunction


img = imread("./Imagenes/T.jpeg");
[m, n] = size(img);
img = im2double(img);

subplot(1,2,1);
imshow(img);
title('Imagen original');




filtered_image = harmonic_mean_filter(img, 3);


subplot(1,2,2);
imshow(filtered_image)

title('Imagen con filtro');