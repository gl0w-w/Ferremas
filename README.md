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

---------------------------------------

>[!NOTE]
>Recomendamos dejar los campos talcual se muestran, solo cambiar la contraseña a la que usted tiene en su MySQL.

---------------------------------------

**Ahora que tenemos conectada nuestra base de datos, tenemos que migrar para que se muestren las tablas en nuestra bd dentro de MySQL.**
- Si no sabes como crear una te dejare una imagen de como se hace:


![](https://translate.google.com/website?sl=en&tl=es&hl=es&client=srp&u=https://itknowledgeexchange.techtarget.com/coffee-talk/files/2020/06/create-mysql-schema.png)

-----------------------------------



<pre><code>python.exe manage.py migrate</code></pre>



