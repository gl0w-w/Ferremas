<h1>Hola! Bienvenido al archivo README con las intrucciones del repositorio creado para el proyecto Ferremas.</h1>

**<h2></h2>**

**<h1>INSTALACIÓN</h1>** 

>[!IMPORTANT] 
> Es importante seguir el paso a paso que veras a continuación.
>1. En este caso se uso como IDE Visual Studio Code, esta la opción de utilizar otro, pero por cualquier cosa, por favor usar este.
>2. También tenemos que tener instalado una de estas dos opciones para poder abrir los puertos de MySQL y que funcione nuestra base de datos, puedes utilizar xampp o MySQL WorkBench.
>3. Dentro de alguna terminal verificar si tienes python y pip instalados, puedes revisar esto utilizando los siguientes comandos.
>**Para ver la version de python:**
><pre><code>python --version</code></pre>
>**Para ver la version de pip:**
><pre><code>pip --version</code></pre>

>[!CAUTION]
>**También tienes que utilizar el siguiente comando para poder ver utilizar más adelante el Swagger (Esto funcionara siempre y cuando tengas instalado pip)**
><pre><code>pip install -U drf-yasg</code></pre>
-------------------------------
Luego de verificar que tanto python como pip esten instalados, tenemos que clonar o descargar como zip el repositorio.
-------------------------------
**En caso de no saber como clonar acá te dejamos el comando, este solo tienes que copiar y pegarlo dentro de una carpeta**
<pre><code>git clone https://github.com/gl0w-w/Ferremas.git</code></pre>
-------------------------------
Una vez hayas instalado el repositorio, abrelo con tu IDE de confianza y tendremos que ver un crud como el que te mostrare en la siguiente imagen:

![](https://i.ibb.co/fGxmxp8j/kk.png)

-------------------------------

Ahora que ya tenemos el repositorio tenemos que configurar algunas cosas, primero que nada tenemos que abrir la consola, esto clickeando en la parte superior izquierda de la IDE, ahí veremos Terminal y al clickearla saldra la opción para abrir la terminal

![](https://i.ibb.co/gMMfGzRH/sdsd.png) 

-------------------------------

Luego tenemos que que instalar algunas cosas que nos serviran para iniciar el codigo, primero empecemos con instalar el archivo txt \requirements.txt
<pre><code>pip install -r requirements.txt</code></pre>

-------------------------------

Una vez lo hayamos instalado, tendremos que configurar algunas cosas, primero nos dirigiremos dentro del crud y buscaremos la carpeta llamada **ferremas**, dentro de esta carpeta buscaremos el archivo .py llamado **settings.py**. Aquí buscaremos la parte de la base de datos, esta se llama **DATABASES**

![](https://i.ibb.co/QF5TVBMR/bd.png) 

------------------------------

>[!IMPORTANT] 
Si no sabes como crear una te dejare una imagen de como se hace:
>
![](https://translate.google.com/website?sl=en&tl=es&hl=es&client=srp&u=https://itknowledgeexchange.techtarget.com/coffee-talk/files/2020/06/create-mysql-schema.png)

------------------------------

>[!NOTE]
>Recomendamos dejar los campos tal cual se muestran, solo cambiar la contraseña a la que usted tiene en su MySQL.

---------------------------------------

**Ahora que tenemos conectada nuestra base de datos, tenemos que migrar para que se muestren las tablas en nuestra bd dentro de MySQL.**

<pre><code>python.exe manage.py migrate</code></pre>

Una vez que hayamos migrado dentro de nuestra bd creada mostrar las siguiente tablas:

![image](https://github.com/user-attachments/assets/a9c2cf92-9cb6-49a9-bb9c-03924e9d0cf6)

---------------------------------------

Ahora tenemos que nuestra base de datos lista, podemos iniciar nuestro proyecto!. Empecemos con el siguiente comando:
<pre><code>python.exe manage.py runserver</code></pre>

---------------------
>[!CAUTION]
En caso de que al intentar iniciar el proyecto te de un error, probablemente sea por que fallo la instalación de Django a la hora de instalar el archivo \requirements.txt.
>
Ingresa este codigo para instalarlo:
<pre><code>py -m pip install django==5.2.1</code></pre>
----------------------

# ¿Cómo saber si esta funcionando?
Veremos en la consola que ya no tenemos ningun erro y también algo así:
>
![asdasd](https://github.com/user-attachments/assets/7a073bb6-d12b-4c55-a6ce-134d26b0160a)
>
Con tan solo pulsar ctrl + click en lo que esta marcado o copiar y pegar en nuestro navegador de confianza se nos abrira la consola.

# Disfruta!
Perfecto! ahora que tenemos el proyecto funcionando podemos ver como funciona la página! disfruta e interactua con la página.




