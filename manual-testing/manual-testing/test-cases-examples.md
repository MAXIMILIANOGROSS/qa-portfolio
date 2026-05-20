# Test Cases Examples

## Ejemplo 1: TC-001 - Valid Login

| Field | Value |
|-------|-------|
| **Test ID** | TC-001 |
| **Feature** | Authentication |
| **Title** | User login with valid credentials |
| **Preconditions** | - User account exists<br>- User is on login page |
| **Test Steps** | 1. Enter email: user@example.com<br>2. Enter password: SecurePass123<br>3. Click "Login" button<br>4. Verify dashboard loads |
| **Expected Result** | - Login successful<br>- Dashboard displays<br>- User name shown in header<br>- No error messages |
| **Actual Result** | Login successful, dashboard loaded correctly |
| **Status** | ✅ PASS |
| **Date Executed** | 15/05/2026 |
| **Severity** | CRITICAL |
| **Comments** | Fast response time, no issues |

---

## Ejemplo 2: TC-016 - Add Item to Cart

| Field | Value |
|-------|-------|
| **Test ID** | TC-016 |
| **Feature** | Shopping Cart |
| **Title** | Add single product to shopping cart |
| **Preconditions** | - User is logged in<br>- Product search page loaded<br>- Product inventory > 0 |
| **Test Steps** | 1. Search for "laptop"<br>2. Click on first result<br>3. Verify product details load<br>4. Click "Add to Cart" button<br>5. Verify confirmation message<br>6. Click on cart icon |
| **Expected Result** | - Item added to cart<br>- Confirmation message displays<br>- Cart icon shows count (1)<br>- Product appears in cart summary |
| **Actual Result** | Item successfully added, count updated |
| **Status** | ✅ PASS |
| **Date Executed** | 16/05/2026 |
| **Severity** | CRITICAL |
| **Comments** | Cart functionality working perfectly |

---

## Ejemplo 3: TC-002 - Invalid Password

| Field | Value |
|-------|-------|
| **Test ID** | TC-002 |
| **Feature** | Authentication |
| **Title** | Login attempt with invalid password |
| **Preconditions** | - User account exists<br>- User is on login page<br>- Password is known to be incorrect |
| **Test Steps** | 1. Enter email: user@example.com<br>2. Enter password: WrongPass123<br>3. Click "Login" button<br>4. Observe error message |
| **Expected Result** | - Login fails<br>- Error message: "Invalid email or password"<br>- No sensitive information revealed<br>- User stays on login page |
| **Actual Result** | Error message displayed correctly |
| **Status** | ✅ PASS |
| **Date Executed** | 15/05/2026 |
| **Severity** | CRITICAL |
| **Comments** | Security handled properly |

---

## Ejemplo 4: TC-010 - Filter by Category

| Field | Value |
|-------|-------|
| **Test ID** | TC-010 |
| **Feature** | Product Search |
| **Title** | Filter products by category |
| **Preconditions** | - Search results loaded<br>- Multiple categories available<br>- Products in each category |
| **Test Steps** | 1. Click on "Electronics" category<br>2. Wait for results to load<br>3. Verify only electronics products shown<br>4. Check product count updates<br>5. Click "Clear filters" |
| **Expected Result** | - Only electronics displayed<br>- Product count updates<br>- Filter badge shows "Electronics"<br>- All products are relevant |
| **Actual Result** | Filter working, all products relevant |
| **Status** | ✅ PASS |
| **Date Executed** | 16/05/2026 |
| **Severity** | HIGH |
| **Comments** | Filter response time acceptable |

---

## Ejemplo 5: TC-025 - Enter Payment Information

| Field | Value |
|-------|-------|
| **Test ID** | TC-025 |
| **Feature** | Checkout |
| **Title** | Enter payment information during checkout |
| **Preconditions** | - Shopping cart has items<br>- Shipping address entered<br>- Shipping method selected<br>- On payment page |
| **Test Steps** | 1. Enter card number: 4111111111111111<br>2. Enter expiry: 12/26<br>3. Enter CVV: 123<br>4. Enter cardholder name<br>5. Click "Process Payment"<br>6. Wait for confirmation |
| **Expected Result** | - Payment processed<br>- Order confirmation page<br>- Order number displayed<br>- Email confirmation sent |
| **Actual Result** | Payment processed successfully |
| **Status** | ✅ PASS |
| **Date Executed** | 17/05/2026 |
| **Severity** | CRITICAL |
| **Comments** | Secure payment gateway working |

---
