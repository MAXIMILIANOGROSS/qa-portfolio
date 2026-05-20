# API Testing con Postman

## 🔗 API Testing Documentation

Este directorio contiene ejemplos de testing de APIs usando Postman.

### 📋 APIs Testeadas

#### 1. OpenWeather API
- **Base URL:** https://api.openweathermap.org
- **Tests:**
  - GET /weather - Obtener clima actual
  - GET /forecast - Obtener pronóstico
  - Query validation
  - Error handling (invalid city)

#### 2. JSONPlaceholder
- **Base URL:** https://jsonplaceholder.typicode.com
- **Tests:**
  - GET /posts - Listar posts
  - GET /users - Listar usuarios
  - POST /posts - Crear post
  - PUT /posts/1 - Actualizar post
  - DELETE /posts/1 - Eliminar post

#### 3. PokéAPI
- **Base URL:** https://pokeapi.co/api/v2
- **Tests:**
  - GET /pokemon/{name} - Obtener pokemon
  - Validación de respuesta JSON
  - Validación de status code

### 🧪 Test Examples

**Test 1: GET /weather**
