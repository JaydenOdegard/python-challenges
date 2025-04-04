### Hint 1 – Input Type Mismatch

**Issue:**  
Used `input()` but tried to compare it directly to numbers like `if user_input == 1`

**Fix:**  
Remember `input()` always returns a string. Use `int(input())` if you want to compare to a number.

**Study:**  
- `input()` return types  
- Type conversion (`int()`, `str()`)
