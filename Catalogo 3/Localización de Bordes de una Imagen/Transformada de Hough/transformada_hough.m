clc;
clear;
close all;
pkg load image;

tStep = 1;
rStep = 1;

A = imread('../../Imagenes/linea3.jpg');
subplot(2, 2, 1);
imshow(A);
title('Imagen Original');

A = im2double(A);
[m, n] = size(A);

A(A < 0.5) = 0;
A(A >= 0.5) = 1;

subplot(2, 2, 2);
imshow(A);
title('Imagen Binaria');

thetas = deg2rad(0:tStep:180);

d = sqrt((m^2) + (n^2));
rhos = -d:rStep:d;

Acc = zeros(length(thetas), length(rhos));

[x, y] = find(A == 1);
positions = size(x)(1);

for i = 1:positions
  
  for ti = 1:length(thetas)
        
    theta = thetas(ti);
    rho = (x(i) * cos(theta)) + (y(i) * sin(theta));
    [~, ri] = min(abs(rhos - rho));
    Acc(ti, ri)++;
    
  endfor
  
endfor

subplot(2, 2, 3);
surface(thetas, rhos, Acc', 'EdgeColor', 'none');
title('Acumulacion');
ylabel('Rho');
xlabel('Theta');

subplot(2, 2, 4);
hold on;
imshow(im2uint8(A));
title('Imagen Final');

lineTries = 10;

for r = 1:lineTries
  
  [xp, yp] = find(Acc == max(max(Acc)));
  
  for k = 1:length(xp)
    
    thetaMax = thetas(xp(1));
    rhoMax = rhos(yp(1));
    
    if (abs(sin(thetaMax)) < 10^-4)
    
      xv = rhoMax / cos(thetaMax);
      line([n 1], [xv xv], 'LineWidth', 2);
      
    else
      
      pend = -cos(thetaMax) / sin(thetaMax);
      inter = rhoMax / sin(thetaMax);
      
      y1 = pend + inter;
      ym = pend * m + inter;

      x1 = (1 - inter) / pend;
      xn = (n - inter) / pend;  
      
      if (pend > 0)
        
        if (0 < y1)

          line([y1 n], [1 xn], 'LineWidth', 2);    
          
        else
          
          line([1 ym], [x1 n], 'LineWidth', 2);   
          
        endif
        
      else
        
        if (y1 > m)
          
          line([ym m], [m xn], 'LineWidth', 2);    
          
        else
          
          line([y1 1], [1 x1], 'LineWidth', 2);    
          
        endif
        
      endif
      
    endif
    
    Acc(xp(k), yp(k)) = 0;
    
  endfor
  
endfor