# 👋 ¡Hola! Bienvenido al archivo README con las instrucciones del repositorio creado para el proyecto **Ferremas**.

---

> \[!IMPORTANT]
> Estas son las credenciales para poder hacer el testeo de una compra con WebPay:
> 
> `N° 4051 8856 0044 6623 | Fecha: 11/11 | CVC: 123`
>
> `11.111.111-1 | 123`

## 📦 INSTALACIÓN

> \[!IMPORTANT]
> Es importante seguir el paso a paso que verás a continuación:

1. En este caso se usó como IDE **Visual Studio Code**. Puedes usar otro, pero por facilidad, recomendamos este.
2. Necesitas tener instalado **XAMPP** o **MySQL Workbench** para poder abrir los puertos de MySQL y hacer funcionar la base de datos.
3. Verifica si tienes Python y pip instalados ejecutando los siguientes comandos en tu terminal:

> **Ver versión de Python:**
>
> <pre><code>python --version</code></pre>

> **Ver versión de pip:**
>
> <pre><code>pip --version</code></pre>

> \[!CAUTION]
> Para poder utilizar **Swagger**, instala esta herramienta con pip (si ya está instalado):
>
> <pre><code>pip install -U drf-yasg</code></pre>

---

Después de verificar que tanto Python como pip estén instalados, **clona o descarga el repositorio**:

> **Para clonar** (solo copia y pega este comando en tu terminal):

<pre><code>git clone https://github.com/gl0w-w/Ferremas.git</code></pre>

---

Una vez descargado, **abre el repositorio con tu IDE** de preferencia (preferiblemente VS Code) y deberías ver un CRUD como este:


![](https://i.ibb.co/fGxmxp8j/kk.png)

---

Luego, abre la consola desde tu IDE (Terminal > Nueva Terminal):


![](https://i.ibb.co/gMMfGzRH/sdsd.png)

---

Ahora instala las dependencias del proyecto desde el archivo `requirements.txt`:



<pre><code>pip install -r requirements.txt</code></pre>

---

Luego dirígete a la carpeta `ferremas` y abre el archivo **`settings.py`**. Busca la sección llamada **`DATABASES`** para configurar la base de datos:


![](https://i.ibb.co/QF5TVBMR/bd.png)

> \[!IMPORTANT]
> Si no sabes cómo crear una base de datos, te dejamos una imagen de referencia:
> ![](https://translate.google.com/website?sl=en\&tl=es\&hl=es\&client=srp\&u=https://itknowledgeexchange.techtarget.com/coffee-talk/files/2020/06/create-mysql-schema.png)

> \[!NOTE]
> Recomendamos dejar los campos tal como se muestran, cambiando únicamente la contraseña por la tuya en MySQL.

---

## 🧩 Migraciones

Conecta tu base de datos y luego ejecuta la migración para crear las tablas necesarias:

<pre><code>python.exe manage.py migrate</code></pre>

Después de esto, deberías ver las siguientes tablas en tu base de datos:


![image](https://github.com/user-attachments/assets/a9c2cf92-9cb6-49a9-bb9c-03924e9d0cf6)

---

## 🚀 Iniciar el proyecto

¡Hora de arrancar el servidor!
Ejecuta el siguiente comando:

<pre><code>python.exe manage.py runserver</code></pre>

> \[!CAUTION]
> Si aparece un error relacionado con Django, puede que no se haya instalado correctamente. Instálalo así:
>
> <pre><code>py -m pip install django==5.2.1</code></pre>

---

## ✅ ¿Cómo saber si está funcionando?

Si todo va bien, verás algo como esto en la terminal:

![asdasd](https://github.com/user-attachments/assets/7a073bb6-d12b-4c55-a6ce-134d26b0160a)

Presiona `Ctrl + click` sobre el enlace o cópialo en tu navegador. Tendría que mostrarse algo así:

![image](https://github.com/user-attachments/assets/a4d098a2-c574-44a9-b1f2-fd7bdb504b81)

---

## 🎉 ¡Disfruta!

Perfecto, ahora que tienes el proyecto funcionando, explora, prueba e interactúa con la página. ¡Esperamos que te diviertas y aprendas mucho!
