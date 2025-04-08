# Guía de Uso de ChatAgentDB

Esta guía te enseñará cómo aprovechar al máximo ChatAgentDB para interactuar con tu base de datos PostgreSQL mediante lenguaje natural.

## 🚀 Primeros Pasos

Una vez que hayas conectado ChatAgentDB a tu base de datos (siguiendo las instrucciones en [setup.md](setup.md)), estarás listo para comenzar a hacer consultas.

### Interfaz Principal

La interfaz de ChatAgentDB consta de:

1. **Panel lateral** - Configuración de la conexión a la base de datos
2. **Área de chat** - Donde interactúas con el agente y ves los resultados
3. **Resumen de esquema** - Una vez conectado, muestra información sobre las tablas disponibles

## 💬 Haciendo Preguntas

Puedes hacer preguntas en lenguaje natural sobre tus datos. El agente:
- Traducirá tus preguntas a SQL
- Ejecutará las consultas en tu base de datos
- Presentará los resultados de manera comprensible

### Ejemplos de Preguntas Básicas

- "¿Qué tablas hay en la base de datos?"
- "Muestra los primeros 5 registros de la tabla usuarios"
- "¿Cuántos productos tenemos en total?"
- "¿Cuál es el precio promedio de los productos?"

### Ejemplos de Preguntas Intermedias

- "¿Cuáles son los 3 productos más vendidos este mes?"
- "Muestra las ventas totales por región, ordenadas de mayor a menor"
- "¿Qué clientes han gastado más de 1000 dólares en el último trimestre?"
- "Compara las ventas de este mes con las del mes anterior"

### Ejemplos de Preguntas Avanzadas

- "Calcula la tasa de retención de clientes mes a mes durante el último año"
- "Muestra un análisis de cohorte de los usuarios que se registraron en enero"
- "¿Cuál es la correlación entre el precio de los productos y su volumen de ventas?"
- "Identifica productos con patrones de venta estacional basados en datos históricos"

## 🧠 Técnicas Efectivas

### Proporcionar Contexto

Para obtener mejores resultados, es útil proporcionar contexto adicional:

❌ **Menos efectivo**: "Muestra los datos de ventas"

✅ **Más efectivo**: "Muestra las ventas totales por categoría de producto para el primer trimestre de 2024"

### Solicitudes Específicas de Formato

Puedes solicitar formatos específicos para los resultados:

- "Muestra los resultados ordenados por fecha descendente"
- "Presenta estos datos como porcentajes"
- "Calcula la diferencia porcentual entre estos períodos"

### Consultas Múltiples

Puedes encadenar análisis complejos:

"Primero muestra las ventas mensuales del año pasado, luego calcula la tasa de crecimiento mes a mes, y finalmente identifica los meses con crecimiento negativo"

### Consultas Exploratorias

Si no estás familiarizado con el esquema:

1. "¿Qué tablas hay en esta base de datos?"
2. "Muestra la estructura de la tabla clientes"
3. "¿Qué campos tiene la tabla pedidos?"

## 📊 Casos de Uso Comunes

### Análisis de Ventas

- "¿Cuál fue el ingreso total del último trimestre desglosado por línea de productos?"
- "Muestra la tendencia de ventas semanales durante los últimos 3 meses"
- "Compara el rendimiento de ventas de las regiones este y oeste"

### Análisis de Usuarios

- "¿Cuál es la tasa de conversión de usuarios registrados a compradores?"
- "Muestra la distribución de usuarios por grupo de edad y género"
- "¿Qué porcentaje de usuarios ha estado inactivo durante más de 30 días?"

### Gestión de Inventario

- "Identifica productos con menos de 10 unidades en stock"
- "¿Cuál es la rotación de inventario por categoría de producto?"
- "Muestra los productos que necesitan reabastecimiento basado en tendencias de ventas"

## 🔍 Depuración de Consultas

Si los resultados no son los esperados:

1. **Sé más específico**: "En la tabla 'ventas', muestra solo las transacciones completadas de abril 2024"
2. **Reformula la pregunta**: "De otra manera, ¿puedes mostrarme el total de ventas diarias del mes pasado?"
3. **Solicita explicación**: "¿Puedes explicar cómo llegaste a este resultado?"
4. **Corrige suposiciones**: "No, la tabla de usuarios no tiene un campo 'edad', usa 'fecha_nacimiento' para calcular la edad"

## 🚫 Limitaciones

Ten en cuenta estas limitaciones al usar ChatAgentDB:

- **Operaciones de escritura**: Por seguridad, el agente está configurado principalmente para consultas de lectura (SELECT)
- **Rendimiento con datasets grandes**: Las consultas complejas en bases de datos muy grandes pueden tardar
- **Consultas muy especializadas**: Algunas consultas muy específicas del dominio pueden requerir refinamiento
- **Tablas sin relaciones claras**: El agente funciona mejor con esquemas bien estructurados con relaciones explícitas

## 🔄 Mantener el Contexto

ChatAgentDB mantiene el contexto de la conversación, lo que te permite hacer preguntas de seguimiento:

1. "Muestra las ventas del mes pasado"
2. "¿Cuáles fueron los 3 productos más vendidos?"
3. "¿Qué clientes compraron estos productos?"

## 📋 Ejemplos Completos de Sesiones

### Ejemplo 1: Análisis de Rendimiento de Ventas

```
Usuario: "¿Cuántas ventas totales tuvimos en 2023?"
Agente: [Muestra total de ventas para 2023]

Usuario: "¿Cómo se compara eso con 2022?"
Agente: [Muestra comparación entre 2023 y 2022]

Usuario: "Desglosado por trimestre, ¿cuál fue nuestro mejor período?"
Agente: [Muestra análisis trimestral]

Usuario: "Para el mejor trimestre, muestra el desglose por producto"
Agente: [Muestra los productos vendidos en ese trimestre]
```

### Ejemplo 2: Investigación de Usuario

```
Usuario: "¿Cuántos usuarios nuevos se registraron en marzo?"
Agente: [Muestra conteo de nuevos usuarios]

Usuario: "¿De qué regiones provienen principalmente?"
Agente: [Muestra distribución geográfica]

Usuario: "¿Qué porcentaje de ellos ha realizado al menos una compra?"
Agente: [Muestra tasa de conversión]
```

## 🛠️ Mejores Prácticas

1. **Comienza con consultas simples** para familiarizarte con tus datos
2. **Construye gradualmente** hacia análisis más complejos
3. **Proporciona feedback** para ayudar al agente a refinar sus respuestas
4. **Verifica los resultados** para consultas críticas
5. **Usa términos consistentes** que coincidan con tu esquema de base de datos

## 📚 Recursos Adicionales

Para aprender más sobre cómo trabajar con bases de datos y análisis de datos:

- [Documentación oficial de PostgreSQL](https://www.postgresql.org/docs/)
- [Guía de SQL para análisis de datos](https://mode.com/sql-tutorial/)
- [Mejores prácticas de modelado de datos](https://www.datacamp.com/community/tutorials/database-design-tutorial)