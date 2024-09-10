<div class = "coffee">
 <a class = "link" href="https://www.buymeacoffee.com/jartavia05" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" 
       style="height: 40px !important;width: 144px !important;">
 </a>

# El cifrado César
Uno de los sistemas de cifrado más sencillos es el cifrado César, utilizado hace más de 2000 años. El cifrado César desplaza la letra un número fijo de posiciones hacia la izquierda o hacia la derecha. 

El cifrado César puede utilizar una clave entre 1 y 25. Con una clave de 1, cada letra se desplaza una posición, donde A se convierte en B y Z en A. Con una clave de 25, cada letra se desplaza 25 posiciones, donde A se convierte en Z y B en A. Una clave de 0 significa que no hay cambios; además, una clave de 26 tampoco provocará cambios, ya que provocaría una rotación completa. En consecuencia, concluimos que el cifrado César tiene un espacio de claves de 25; hay 25 claves diferentes entre las que el usuario puede elegir.

Considere el caso en el que ha interceptado un mensaje cifrado con el cifrado César: "JXYJ JX FQUMF GWFAT HTSYFHYFSIT F RNPJ IJQ MTYJQ YFSLT". Se nos pide que lo descifremos sin conocer la clave. Podemos intentarlo mediante fuerza bruta, es decir, podemos probar todas las claves posibles y ver cuál tiene más sentido. En la siguiente figura, notamos que la clave 5 es la que tiene más sentido: “ESTE ES ALPHA BRAVO CONTACTANDO A MIKE DEL HOTEL TANGO”.
