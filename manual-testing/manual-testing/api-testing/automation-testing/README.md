# Test Automation con Selenium

## 🤖 Automation Testing Documentation

Este directorio contiene tests automatizados usando Selenium y Python.

### 📁 Estructura del Proyecto
### 🧪 Test Files

#### test_login.py
- **TC-A001:** Login con credenciales válidas
- **TC-A002:** Login con password inválido
- **TC-A003:** Login con email vacío
- **TC-A004:** Logout functionality

#### test_search.py
- **TC-A005:** Buscar por keyword
- **TC-A006:** Filtrar por categoría
- **TC-A007:** Ordenar por precio
- **TC-A008:** Búsqueda sin resultados

#### test_checkout.py
- **TC-A009:** Agregar producto al carrito
- **TC-A010:** Completar checkout
- **TC-A011:** Procesar pago
- **TC-A012:** Confirmación de orden

### 📊 Test Results

| Test File | Total Tests | Passed | Failed | Status |
|-----------|------------|--------|--------|--------|
| test_login.py | 4 | 4 | 0 | ✅ PASS |
| test_search.py | 4 | 4 | 0 | ✅ PASS |
| test_checkout.py | 4 | 3 | 1 | ⚠️ 1 FAIL |
| **TOTAL** | **12** | **11** | **1** | **92% Success** |

### 🛠️ Tech Stack

- **Language:** Python 3.9+
- **Framework:** Selenium WebDriver
- **Test Runner:** pytest
- **Browser:** Chrome
- **Page Objects:** Implemented

### 🚀 How to Run Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_login.py

# Run with verbose output
pytest tests/ -v

# Generate HTML report
pytest tests/ --html=report.html
```

### 🎯 Test Automation Standards

- Page Object Model implementation
- Clear test case naming
- Proper assertion messages
- Error handling
- Screenshot on failure
- Test data management

### 📈 Skills Demonstrated

- ✅ Python programming
- ✅ Selenium WebDriver
- ✅ Pytest framework
- ✅ Page Object Model pattern
- ✅ Test assertions
- ✅ Error handling
- ✅ CI/CD ready

### 📚 Learning Resources

- Selenium: https://www.selenium.dev/
- Pytest: https://docs.pytest.org/
- Python: https://www.python.org/

---

**Last Updated:** Mayo 2026
