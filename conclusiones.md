# Conclusiones

## Resumen del ejercicio 1 demoBlaze - Selenium

Este proyecto tiene como objetivo automatizar la prueba del proceso de compra en el sitio DemoBlaze utilizando Selenium. Se ha implementado un script en Python que simula la compra de productos para verificar que el proceso funcione correctamente.

## Aspectos Clave

- **Automatización de Pruebas:**
  - Se ha desarrollado un script en Python con Selenium para simular la compra de productos en DemoBlaze.
  - Se verifica cada paso del proceso de compra, desde la selección del producto hasta la finalización de la compra.

- **Registro de Ejecución:**
  - Los detalles de la ejecución del script se registran en el archivo `reports/test_execution.log`.

- **Informes:**
  - Los resultados de las pruebas y un resumen se generan en `reports/compraArticulos.html`.

## Aprendizajes

- **Manejo de Errores:**
  - Se ha aprendido cómo manejar errores y excepciones durante la ejecución de pruebas automatizadas.

- **Configuración del Entorno:**
  - La correcta configuración del entorno de prueba es crucial para la ejecución exitosa del script.

## Recomendaciones

- **Revisión de Logs:**
  - Revisar los logs y el informe generado regularmente para asegurar que el proceso de compra esté funcionando como se espera.

- **Actualizar el Script:**
  - Adaptar y actualizar el script según los cambios en el sitio web para mantener su eficacia.

## Próximos Pasos

- **Añadir Más Pruebas:**
  - Incluir más escenarios de prueba para cubrir otras funcionalidades del sitio DemoBlaze.

- **Mejorar Informes:**
  - Explorar formas de hacer los informes más detallados y visuales para una mejor comprensión.


## Resumen del ejercicio 2 PetStore - Postman

Las pruebas de la API de PetStore se llevaron a cabo utilizando Postman. A continuación, se detallan los hallazgos y conclusiones del ejercicio.

## Pruebas Realizadas

1. **Añadir una Mascota a la Tienda**:
   - Se realizó correctamente. Se validó que la mascota fuera añadida con éxito.

2. **Consultar la Mascota por ID**:
   - La consulta devolvió la mascota correcta utilizando el ID proporcionado.

3. **Actualizar la Mascota**:
   - El nombre y el estado de la mascota fueron actualizados exitosamente. La mascota se marcó como "sold".

4. **Consultar la Mascota por Estatus**:
   - La búsqueda por estatus devolvió las mascotas con el estatus "sold" correctamente.

## Hallazgos

- La API responde de acuerdo con las especificaciones documentadas en [Swagger](https://petstore.swagger.io/).
- Todos los endpoints funcionaron según lo esperado y los datos fueron manipulados correctamente.

## Recomendaciones

- Verificar la consistencia de los datos en los endpoints de búsqueda.

---

¡Gracias por revisar el proyecto!
