# Manual Testing

## 📋 Test Cases Documentation

Este directorio contiene documentación completa de pruebas manuales para una aplicación de ecommerce.

### 📄 Test Cases

Documentación de 30+ test cases cubriendo:
- **Authentication:** Login, signup, password recovery
- **Product Search:** Search, filters, sorting
- **Shopping Cart:** Add, remove, update items
- **Checkout:** Shipping, payment, order confirmation
- **User Account:** Profile, order history, settings

### 📊 Test Case Structure

Cada test case incluye:
- **ID:** TC-001, TC-002, etc
- **Feature:** Módulo testeado
- **Description:** Objetivo del test
- **Preconditions:** Requisitos previos
- **Steps:** 1. Step 1, 2. Step 2, etc
- **Expected Result:** Qué debe pasar
- **Status:** PASS, FAIL, PENDING

### ✅ Features Testeadas

#### 1. Authentication (7 tests)
- TC-001: Valid login
- TC-002: Invalid password
- TC-003: Empty email field
- TC-004: Empty password field
- TC-005: Account lockout (5 failed attempts)
- TC-006: Password recovery
- TC-007: Logout

#### 2. Product Search (8 tests)
- TC-008: Search by keyword
- TC-009: Search with no results
- TC-010: Filter by category
- TC-011: Filter by price range
- TC-012: Sort by price (ascending)
- TC-013: Sort by price (descending)
- TC-014: Sort by rating
- TC-015: Clear filters

#### 3. Shopping Cart (7 tests)
- TC-016: Add single item to cart
- TC-017: Add multiple items
- TC-018: Update item quantity
- TC-019: Remove item from cart
- TC-020: Apply coupon code
- TC-021: Cart subtotal calculation
- TC-022: Cart persistence (refresh page)

#### 4. Checkout (5 tests)
- TC-023: Enter shipping address
- TC-024: Select shipping method
- TC-025: Enter payment information
- TC-026: Order confirmation
- TC-027: Email receipt sent

#### 5. User Account (3 tests)
- TC-028: Update profile information
- TC-029: View order history
- TC-030: Manage saved addresses

### 📊 Metrics

| Metric | Value |
|--------|-------|
| Total Test Cases | 30 |
| Features | 5 |
| Manual Testing Hours | ~8 |
| Pass Rate | 90% |
| Coverage | 95% |

### 🎯 Test Execution

**Test Environment:** Chrome, Firefox
**Test Data:** Real user credentials and products
**Test Period:** 2 weeks
**Tester:** Maximiliano Olmos

### 🐛 Bugs Found

During testing, identified 3 bugs:
- BUG-001: Cart not updating after logout (CRITICAL)
- BUG-002: Search filter delay (HIGH)
- BUG-003: Email receipt missing attachment (MEDIUM)

### 📈 Skills Demonstrated

- ✅ Detailed test case design
- ✅ Comprehensive documentation
- ✅ Feature coverage analysis
- ✅ Test execution tracking
- ✅ Bug identification and reporting
- ✅ QA best practices

---

**Last Updated:** Mayo 2026
