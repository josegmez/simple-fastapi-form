## Formulario Simple

Esta página Web simple que se componen de un servicio de API en FastApi, con persitencia basada en TinyDB y una página HTML para interactuar con el servicio backend.

Esta página está hecha con el propósito de realizar pruebas en el montaje de un servidor On Premise en las instalaciones de la red universitaria de la UdeA bajo el marco del curso de Comunicaciones II en el departamento de ingeniería de sistemas durante el periodo 2024 - 2.

## Stack Técnologico

Following technologies are used to build this project:

- [Python](https://www.python.org/): Python is a programming language that lets you work quickly and integrate systems more effectively.

- [FastAPI](https://fastapi.tiangolo.com/): FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

- [TinyDB](https://tinydb.readthedocs.io/en/latest/): TinyDB is a lightweight document oriented database optimized for your happiness :)

- [HTML](https://developer.mozilla.org/es/docs/Web/HTML): HTML (HyperText Markup Language) is the most basic building block of the Web. It defines the meaning and structure of web content.

- [JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript): JavaScript is a programming language that enables you to interact with the content of a webpage.

- [Docker](https://www.docker.com/): Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.

## Instalación

Para instalar este proyecto, primero clone el repositorio desde GitHub:

```bash
git clone git@github.com:josegmez/simple-fastapi-form.git simple-fastapi-form
```

Luego, instale las dependencias necesarias:

```bash
cd simple-fastapi-form
pip install -r requirements.txt
```

## Ejecución

Para ejecutar el proyecto, primero debe iniciar el servicio de FastAPI:

```bash
fastapi run
```

Luego, abra el archivo `index.html` en su navegador web.

> [!NOTE]
> También puede ejecutar el proyecto en un contenedor Docker. Para ello, primero construya la imagen Docker:

```bash
docker build -t simple-fastapi-form .
```

Luego, ejecute el contenedor Docker:

```bash
docker run -d -p 3000:80 simple-fastapi-form
```