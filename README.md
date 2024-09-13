# PetStore API Tests

Este directorio contiene pruebas para la API de PetStore utilizando Postman. 

## Contenido del Proyecto

- **postman/collections/**: Contiene la colección de Postman para las pruebas de API.
- **postman/environments/**: Contiene el entorno de Postman utilizado para las pruebas.
- **README.md**: Documentación con instrucciones para ejecutar las pruebas.
- **conclusiones.txt**: Hallazgos y conclusiones de las pruebas realizadas.

## Cómo Ejecutar las Pruebas

### Importar Colecciones en Postman

1. Abrir Postman.
2. Hacer clic en el botón **Importar** en la esquina superior izquierda.
3. Selecciona el archivo `PetStore_API_Tests.postman_collection.json` desde `postman/collections/`.
4. Hacer clic en **Importar**.

### Importar Entornos en Postman

1. Abrir Postman.
2. Hacer clic en el ícono del engranaje en la esquina superior derecha y seleccionar **Administrar Entornos**.
3. Hacer clic en el botón **Importar**.
4. Seleccionar el archivo `PetStore_Environment.postman_environment.json` desde `postman/environments/`.
5. Haz clic en **Importar**.

### Ejecutar las Pruebas

- Las colecciones pueden ser ejecutadas manualmente desde Postman.
- Para ejecución automatizada, utilizar [Newman](https://www.npmjs.com/package/newman).