

# Model for Calculating the Edelstein Effect in a Rashba Fermion System

## 1. Theoretical Framework and Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian describing the Rashba fermion at the $\Gamma$ point of the Brillouin zone is given by:

$$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma}) \tag{1} $$

where:
- $p$ is the momentum operator.
- $m$ is the effective carrier mass.
- $\alpha$ is the Rashba spin-orbit coupling strength.
- $\hat{z}$ is the unit vector perpendicular to the 2D plane.
- $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ is the vector of Pauli matrices.

The energy dispersion relation for the two chiral (helicity) bands $\nu = \pm$ is:

$$ E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha k \tag{6} $$

where $k = |\mathbf{k}|$ and $\nu = +1$ corresponds to the outer branch and $\nu = -1$ to the inner branch (or vice versa depending on the sign convention of $\alpha$). The helicity operator is defined as $\hat{S} = \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma})/p$, with eigenvalues $s = \pm 1$.

## 2. Calculation of Magnetization (Edelstein Effect)

The Direct Edelstein Effect (DEE) describes the generation of a non-equilibrium spin density (magnetization) $\mathbf{M}$ under an applied electric field $\mathbf{E}$. Within the semiclassical Boltzmann approach, the magnetization at first order in the electric field is given by:

$$ \mathbf{M} = -\mu_b \sum_{\mathbf{k}, \nu} |e| (\mathbf{v}_\nu(\mathbf{k}) \cdot \mathbf{E}) \delta [E_\nu(\mathbf{k}) - E_F] \langle \boldsymbol{\sigma} \rangle^\nu_\mathbf{k} \tag{2} $$

where:
- $\mu_b$ is the Bohr magneton.
- $|e|$ is the elementary charge.
- $\mathbf{v}_\nu(\mathbf{k}) = \nabla_\mathbf{k} E_\nu(\mathbf{k})$ is the group velocity.
- $\bar{\tau}^\nu_\mathbf{k}$ is the transport lifetime (often assumed constant $\tau$ for simplicity).
- $\langle \boldsymbol{\sigma} \rangle^\nu_\mathbf{k}$ is the spin expectation value for the eigenstates.

For the isotropic Rashba model, the spin expectation value is:

$$ \langle \boldsymbol{\sigma} \rangle^\pm_\mathbf{k} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix} \tag{3} $$

where $\theta$ is the angle between $\mathbf{k}$ and the $\hat{x}$ axis.

### 2.1. Magnetization Magnitude and Direction

Assuming an electric field applied along the $\hat{x}$ direction, $\mathbf{E} = E_x \hat{x}$, the resulting magnetization is perpendicular to the electric field and lies in the plane (along $\hat{y}$). The magnitude depends on the filling regime:

#### High-Density Regime (HDR)
When both chiral bands are occupied ($E_F > 0$ relative to the band crossing):

$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y \tag{8} $$

In this regime, the spin density is **constant** and independent of the Fermi energy $E_F$. It scales linearly with the spin-orbit coupling $\alpha$ and the effective mass $m$.

#### Low-Density Regime (LDR)
When only the lowest energy band is occupied ($E_F < 0$ relative to the band crossing, or near the band minimum):

$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y \tag{9} $$

In this regime, the spin density increases linearly with the Fermi energy $E_F$ for small $E_F$. For values of $E_F$ around the band crossing, the expression can be expanded as:

$$ M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2} \frac{E_F}{\alpha} \right) [\hat{z} \times \mathbf{E}]_y \tag{10} $$

### 2.2. Edelstein Susceptibility

The linear Edelstein susceptibility $\chi_{ij}$ is defined by $M_j = \chi_{ij} E_i$. For the isotropic case with $\mathbf{E} = E_x \hat{x}$:

$$ \chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle \sigma_y \rangle^\nu_\mathbf{k} \delta(E^\nu_\mathbf{k} - \mu) v^\nu_x(\mathbf{k}) \tag{7} $$

where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$.

**Parameter Dependencies:**
- **Spin-Orbit Coupling ($\alpha$):** In the HDR, $\chi_{xy}$ increases linearly with $\alpha$ (see Eq. 8).
- **Fermi Energy ($E_F$):** In the HDR, $\chi_{xy}$ is constant (plateau). In the LDR, it depends on $\sqrt{m^2 \alpha^2 + 2m E_F}$.
- **Chirality:** The contribution comes from the difference in transport times and Fermi momenta of the two chiral bands ($\bar{\tau}^+ k^+_F - \bar{\tau}^- k^-_F$).
- **Fermi Velocity:** Implicit in the group velocity $\mathbf{v}_\nu(\mathbf{k})$ and the density of states.

## 3. Anisotropic Rashba Model (C$_{2v}$ Symmetry)

If the system exhibits anisotropy in effective mass ($m_x \neq m_y$) or Rashba parameters ($\alpha_x \neq \alpha_y$), the Hamiltonian becomes:

$$ \hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y \tag{11} $$

The Edelstein susceptibility in the HDR depends on the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$:

$$ \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}} \tag{12a} $$
$$ \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha} \tag{12b} $$

The susceptibility can be boosted by rendering $r_m$ and $r_\alpha$ greater than one.

## 4. Explicit Graphics Description

Based on the extracted data, the following graphics should be generated to visualize the model results:

1. **Edelstein Susceptibility vs. Chemical Potential ($\mu$):**
   - **Description:** Plot $\chi_{xy}/\chi_0$ on the y-axis and $\mu$ on the x-axis.
   - **Behavior:** Shows a plateau in the High-Density Regime (constant value) and a rising curve in the Low-Density Regime.
   - **Source:** Figure 2 (Left panel) and Figure 3 (Left panel) in Source [1].

2. **Edelstein Susceptibility vs. Rashba Parameter ($\alpha$):**
   - **Description:** Plot $\chi_{xy}/\chi_0$ on the y-axis and $\alpha$ on the x-axis at fixed $\mu$.
   - **Behavior:** Linear increase with $\alpha$ in the high-density regime.
   - **Source:** Figure 3 (Right panel) in Source [1].

3. **Fermi Surface and Spin Texture:**
   - **Description:** 2D plot in $k_x$-$k_y$ space showing the Fermi circles (inner and outer) and the spin orientation vectors (tangential to the circles).
   - **Behavior:** Shows spin-momentum locking.
   - **Source:** Figure 1 and Figure 2 (Right panel) in Source [1].

4. **Anisotropy Dependence:**
   - **Description:** Surface plot or contour plot of $\chi_{xy}/\chi_0$ as a function of $r_m$ and $r_\alpha$.
   - **Behavior:** Susceptibility increases with both ratios, saturating for large $r_\alpha$.
   - **Source:** Figure 6 in Source [1].

## 5. Scientific Citations

- **Rashba Hamiltonian and Basic Formalism:**
  - Equation (1) and Introduction: Gaillardoni, I., et al., "Edelstein Effect in Isotropic and Anisotropic Rashba Models", *arXiv:2503.20712v1* (2025) [1].
  - Original Prediction: Edelstein, V. M., "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems", *Solid State Communications* **73**, 233 (1990) [29].

- **Analytical Expressions (HDR/LDR):**
  - Equations (8), (9), (10): Gaillardoni et al. (2025) [1].
  - Derivations: Appendix A in Gaillardoni et al. (2025) [1].

- **Anisotropic Case:**
  - Equations (11), (12): Gaillardoni et al. (2025) [1].
  - Derivations: Appendix B in Gaillardoni et al. (2025) [1].

- **Boltzmann Transport Approach:**
  - Equation (2): Gaillardoni et al. (2025) [1].
  - Reference: Inoue, J.-i., et al., "Diffuse transport and spin accumulation in a rashba two-dimensional electron gas", *Physical Review B* **67**, 033104 (2003) [19].

---

**References:**
[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models", *arXiv:2503.20712v1* [cond-mat.mes-hall] (2025).
[29] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems", *Solid State Communications* **73**, 233 (1990).
[19] J.-i. Inoue, G. E. Bauer, and L. W. Molenkamp, "Diffuse transport and spin accumulation in a rashba two-dimensional electron gas", *Physical Review B* **67**, 033104 (2003).
