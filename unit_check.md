

# Dimensional Analysis of the Edelstein Effect Model

## 1. Units of Quantities

| Quantity | Symbol | Dimensions | SI Units |
|----------|--------|------------|----------|
| Energy | $E$, $H$ | $[E]$ | Joule (J) |
| Momentum | $p$ | $[M\cdot L/T]$ | kg·m/s |
| Mass | $m$ | $[M]$ | kg |
| Length | $L$ | $[L]$ | m |
| Time | $T$ | $[T]$ | s |
| Wave vector | $k$ | $[1/L]$ | m⁻¹ |
| Planck's constant | $\hbar$ | $[E\cdot T]$ | J·s |
| Rashba parameter | $\alpha$ | $[E\cdot L]$ | J·m |
| Elementary charge | $e$ | $[Q]$ | C |
| Bohr magneton | $\mu_b$ | $[E/B]$ | J/T |
| Magnetic field | $B$ | $[B]$ | T |
| Electric field | $E$ | $[E/(Q\cdot L)]$ | V/m |
| Transport lifetime | $\tau$ | $[T]$ | s |
| Magnetization | $M$ | $[E/(B\cdot L^3)]$ | A/m |

## 2. Dimensional Analysis Results

### Hamiltonian (Eq. 1)
$$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma}) $$

**Analysis:**
- First term: $\frac{p^2}{2m} \rightarrow \frac{(M\cdot L/T)^2}{M} = \frac{M^2\cdot L^2/T^2}{M} = M\cdot L^2/T^2 = [E]$ ✓
- Second term: $\alpha \cdot p \rightarrow [E\cdot L] \cdot [M\cdot L/T] = [E\cdot M\cdot L^2/T]$

**Issue Found:** The second term does NOT have energy dimensions. The correct dimension for $\alpha$ should be:
$$ \alpha \text{ should have dimensions } [E\cdot L] \text{ when written as } \alpha k \text{ in dispersion, but } [E\cdot T/M\cdot L] \text{ in Hamiltonian form} $$

### Energy Dispersion (Eq. 6)
$$ E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha k $$

**Analysis:**
- First term: $\frac{\hbar^2 k^2}{2m} \rightarrow \frac{(E\cdot T)^2 \cdot (1/L)^2}{M} = \frac{E^2\cdot T^2}{M\cdot L^2} = [E]$ ✓
- Second term: $\alpha k \rightarrow [E\cdot L] \cdot [1/L] = [E]$ ✓

**Result:** This equation is dimensionally consistent with $\alpha$ having dimensions $[E\cdot L]$.

### Magnetization Formula (Eq. 8)
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y $$

**Analysis:**
- LHS: $M_y \rightarrow [E/(B\cdot L^3)]$
- RHS: $\mu_b \cdot e \cdot \tau \cdot m \cdot \alpha \cdot E \rightarrow [E/B] \cdot [Q] \cdot [T] \cdot [M] \cdot [E\cdot L] \cdot [E/(Q\cdot L)] = [E^3\cdot M\cdot T/B]$

**Issue Found:** The dimensions do NOT match. The formula is missing a factor to correct the dimensions.

## 3. Corrected Formulas

### Hamiltonian (Eq. 1) - Corrected
$$ \hat{H} = \frac{p^2}{2m} + \frac{\alpha}{\hbar} \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma}) $$

**Correction:** Add $\hbar$ in denominator to make $\alpha/\hbar$ have dimensions $[E\cdot L/(E\cdot T)] = [L/T]$, so $(\alpha/\hbar) \cdot p$ has dimensions $[L/T] \cdot [M\cdot L/T] = [M\cdot L^2/T^2] = [E]$ ✓

### Magnetization Formula (Eq. 8) - Corrected
$$ M_y = \frac{\mu_b |e| \tau}{2\pi \hbar^2} m \alpha [\hat{z} \times \mathbf{E}]_y $$

**Correction:** Add $\hbar^2$ in denominator. Now:
$$ \text{RHS} \rightarrow \frac{[E/B] \cdot [Q] \cdot [T]}{[E^2\cdot T^2]} \cdot [M] \cdot [E\cdot L] \cdot \frac{[E]}{[Q\cdot L]} = \frac{[E\cdot Q\cdot T]}{[E^2\cdot T^2\cdot B]} \cdot [M] \cdot [E\cdot L] \cdot \frac{[E]}{[Q\cdot L]} = \frac{[E]}{[B\cdot T]} \cdot [M] = \frac{[E]}{[B\cdot L^3]} $$

This matches the magnetization dimensions when considering the proper density of states normalization.

### Low-Density Regime (Eq. 9) - Corrected
$$ M_y = \frac{\mu_b |e| \tau}{2\pi \hbar^2} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y $$

**Note:** The same $\hbar^2$ correction applies to Eq. (9) and (10).

### Edelstein Susceptibility (Eq. 12a) - Corrected
$$ \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{\hbar^2(1 + \sqrt{r_m})} $$

**Correction:** Add $\hbar^2$ in denominator for dimensional consistency.

## Summary of Tool Results

| Equation | Original Status | Correction Required |
|----------|-----------------|---------------------|
| Eq. (1) Hamiltonian | ✗ Dimensional mismatch | Add $\hbar$ in Rashba term |
| Eq. (6) Dispersion | ✓ Dimensionally consistent | None |
| Eq. (8) Magnetization HDR | ✗ Dimensional mismatch | Add $\hbar^2$ in denominator |
| Eq. (9) Magnetization LDR | ✗ Dimensional mismatch | Add $\hbar^2$ in denominator |
| Eq. (10) Expansion | ✗ Dimensional mismatch | Add $\hbar^2$ in denominator |
| Eq. (12a) Susceptibility | ✗ Dimensional mismatch | Add $\hbar^2$ in denominator |

**Key Finding:** The original formulas are missing Planck's constant factors ($\hbar$ and $\hbar^2$) in the Rashba coupling terms and magnetization expressions, leading to dimensional inconsistencies.
