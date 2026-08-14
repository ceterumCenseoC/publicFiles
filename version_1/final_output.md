# Edelstein Effect for a Rashba Fermion: Complete Model and Analysis Framework

---

## 1. Introduction and Physical Context

The **Edelstein effect (EE)**, also known as the *inverse galvanic effect*, describes the generation of a non-equilibrium spin density (magnetization) when an electric field is applied to a system with spin–orbit coupling. In a **Rashba two-dimensional electron gas (2DEG)**, the spin degeneracy of electronic bands is lifted, and the electron momentum direction is locked to its spin direction (*spin–momentum locking*). When an external electric field is applied, the Fermi surfaces are shifted, producing a non-equilibrium spin imbalance and thus a net magnetization perpendicular to both the applied field and the spin–orbit field [Edelstein, *Solid State Commun.* 73, 233 (1990); Gambardella & Miron, *Philos. Trans. R. Soc. A* 369, 3175 (2011)].

The **Rashba Hamiltonian** for a 2DEG at the $\Gamma$ point is [Bychkov & Rashba, *JETP Lett.* 39, 78 (1984)]:

$$
\boxed{\hat{H} = \frac{p^2}{2m} + \alpha\,\hat{z}\cdot(\mathbf{p}\times\boldsymbol{\sigma})}
$$

where:
- $m$ is the effective carrier mass,
- $\alpha$ is the Rashba spin–orbit coupling (SOC) strength,
- $\mathbf{p} = \hbar\mathbf{k}$ is the momentum,
- $\boldsymbol{\sigma}=(\sigma_x,\sigma_y,\sigma_z)$ are the Pauli matrices,
- $\hat{z}$ is the direction perpendicular to the 2D plane.

---

## 2. Model Hamiltonian and Band Structure

### 2.1 Energy Dispersion

The eigenenergies of the Rashba Hamiltonian are [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
\varepsilon_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} \pm \alpha\hbar k
$$

with $k = |\mathbf{k}| = \sqrt{k_x^2 + k_y^2}$. The two bands are labeled by the *helicity* $\nu = \pm 1$, defined through the helicity operator [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
\hat{S} = \frac{\hat{z}\cdot(\mathbf{p}\times\boldsymbol{\sigma})}{p}, \qquad \text{eigenvalues } s = \pm 1
$$

### 2.2 Spin Eigenstates

The spin expectation values on the eigenstates of the two bands are [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
\boxed{\langle\boldsymbol{\sigma}\rangle^{\pm}_{\mathbf{k}} = \frac{1}{k}\begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix}}
$$

where $\theta$ is the angle between $\mathbf{k}$ and the $x$-axis. This shows the characteristic **tangential (in-plane) spin texture** of the Rashba system—spin is always perpendicular to the momentum.

### 2.3 Fermi Wavenumbers

The Fermi wavenumbers for each band depend on the electron density regime:

**High-Density Regime (HDR)** — both bands occupied ($E_F > 0$ above the band crossing) [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
k^{+}_{F} = -k_0 + \sqrt{k_0^2 + \frac{2mE_F}{\hbar^2}}, \qquad k^{-}_{F} = +k_0 + \sqrt{k_0^2 + \frac{2mE_F}{\hbar^2}}
$$

**Low-Density Regime (LDR)** — only the lowest band occupied ($E_F < 0$ below the band crossing) [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
k^{+}_{F} = +k_0 - \sqrt{k_0^2 + \frac{2mE_F}{\hbar^2}}, \qquad k^{-}_{F} = +k_0 + \sqrt{k_0^2 + \frac{2mE_F}{\hbar^2}}
$$

where $k_0 = m\alpha/\hbar$.

---

## 3. Boltzmann Transport Framework for the Edelstein Effect

### 3.1 Magnetization Formula

Within the **semiclassical Boltzmann approach**, the magnetization (total spin density) at first order in the electric field $\mathbf{E}$ is [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
\boxed{\mathbf{M} = -\mu_B \sum_{\mathbf{k},\nu} |e|\,\bar{\tau}^{\nu}_{\mathbf{k}}\,(\mathbf{v}^{\nu}(\mathbf{k})\cdot\mathbf{E})\,\delta[E^{\nu}(\mathbf{k}) - E_F]\,\langle\boldsymbol{\sigma}\rangle^{\nu}_{\mathbf{k}}}
$$

where:
- $\mu_B$ is the Bohr magneton,
- $\bar{\tau}^{\nu}_{\mathbf{k}}$ is the transport lifetime,
- $\mathbf{v}^{\nu}(\mathbf{k}) = \nabla_{\mathbf{k}}\varepsilon^{\nu}_{\mathbf{k}}$ is the group velocity,
- $e$ is the electron charge.

### 3.2 Equivalent Formulation via Perturbed Distribution Function

Following Ezawa [arXiv:2501.01888 (2025)], the magnetization can be written using the first-order correction to the Fermi distribution function:

$$
f^{(1)} = \frac{e\tau}{\hbar}\,\mathbf{E}\cdot\nabla_{\mathbf{k}} f^{(0)}
$$

giving the magnetization:

$$
\boxed{\mathbf{M} = \frac{e\tau}{\hbar}\,g\mu_B \int \frac{d^3 k}{(2\pi)^3}\,\mathbf{S}(\mathbf{k})\,f^{(1)}}
$$

where $\mathbf{S}(\mathbf{k}) \equiv \langle\psi_{\mathbf{k}}|\boldsymbol{\sigma}|\psi_{\mathbf{k}}\rangle$ and $g$ is the $g$-factor. At zero temperature this reduces to:

$$
\mathbf{M} = e\tau g\mu_B \int \frac{d^3 k}{(2\pi)^3}\,\mathbf{S}(\mathbf{k})\,(\mathbf{E}\cdot\mathbf{v})\,\delta(\varepsilon_{\mathbf{k}}-\mu)
$$

### 3.3 Linear Response: Edelstein Susceptibility

The linear Edelstein effect is defined through the susceptibility tensor $\chi_{ij}$ [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
\boxed{m_j = \chi_{ij} E_i}
$$

or equivalently [Ezawa, arXiv:2501.01888 (2025)]:

$$
M_i = e\tau\,\alpha^{ME}_{ij} E_j
$$

with the **magnetoelectric susceptibility**:

$$
\alpha^{ME}_{ix} = \frac{g\mu_B}{(2\pi)^2 W}\sum_{\pm}\int d\phi\,\frac{k\,v_x\,S_i(k)}{\left|\frac{\partial\varepsilon}{\partial k}\right|}\Bigg|_{k=k_{\pm}(\phi)}
$$

where $W^{-1} \equiv \int dk/(2\pi)$ is the sample width and $k_{\pm}(\phi)$ is obtained from $\varepsilon(k_{\pm}(\phi)) = \mu$.

---

## 4. Analytical Results for the Isotropic Rashba Model

### 4.1 Magnetization in the High-Density Regime (HDR)

For an electric field $\mathbf{E} = E_x\hat{x}$, the spin density along $\hat{y}$ in the HDR (both bands occupied) is [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
\boxed{M_y = \frac{\mu_B |e|\tau}{2\pi\hbar^2}\,m\alpha\,[\hat{z}\times\mathbf{E}]_y}
$$

**Key result:** In the HDR, the magnetization is **constant, independent of the Fermi energy** $E_F$, and proportional to the Rashba SOC parameter $\alpha$ and the effective mass $m$.
*(Note: The factor $\hbar^{-2}$ is added here to ensure dimensional consistency in SI units, derived from the density of states $m/\pi\hbar^2$.)*

### 4.2 Magnetization in the Low-Density Regime (LDR)

In the LDR (only the lower band occupied) [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
\boxed{M_y = \frac{\mu_B |e|\tau}{2\pi\hbar^2}\,\sqrt{m^2\alpha^2 + 2mE_F}\,[\hat{z}\times\mathbf{E}]_y}
$$

For small $E_F$ near the band crossing, this can be expanded as:

$$
M_y \approx \frac{\mu_B |e|\tau}{2\pi\hbar^2}\left(\alpha m + \frac{1}{2}\frac{E_F}{\alpha}\right)[\hat{z}\times\mathbf{E}]_y
$$

The spin density **increases linearly with the Fermi energy**. In the limit $\alpha \to 0$, the second term vanishes because $E_F$ has a quadratic dependence on $\alpha$.

### 4.3 Vector Form of the Edelstein Magnetization

The general vector form of the Edelstein magnetization for the isotropic Rashba model is:

$$
\boxed{\mathbf{M} = \chi_{EE}\,[\hat{z}\times\mathbf{E}]}
$$

This means the magnetization is **in-plane and perpendicular** to the applied electric field. For example, if $\mathbf{E} = E_x\hat{x}$, then $\mathbf{M} = M_y\hat{y}$.

---

## 5. Anisotropic Rashba Model ($C_{2v}$ Symmetry)

### 5.1 Anisotropic Hamiltonian

For systems with $C_{2v}$ symmetry, the Rashba Hamiltonian generalizes to [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
\boxed{\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y}
$$

with anisotropic effective masses $m_x \neq m_y$ and anisotropic SOC parameters $\alpha_x \neq \alpha_y$.

### 5.2 Edelstein Susceptibility with Mass Anisotropy

In the HDR, the Edelstein susceptibility as a function of the mass ratio $r_m = m_y/m_x$ is [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
\boxed{\frac{\chi_{xy}}{\chi_0}(r_m) = 4\pi m_x \alpha \frac{r_m}{1+\sqrt{r_m}}}
$$

### 5.3 Edelstein Susceptibility with SOC Anisotropy

As a function of the SOC ratio $r_\alpha = \alpha_y/\alpha_x$ [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
\boxed{\frac{\chi_{xy}}{\chi_0}(r_\alpha) = 4\pi m\alpha_x \frac{r_\alpha}{1+r_\alpha}}
$$

**Key results:**
- When $r_m < 1$ or $r_\alpha < 1$, the susceptibility is **lower** than in the isotropic case.
- When $r_m > 1$ or $r_\alpha > 1$, the susceptibility **increases**.
- The susceptibility **saturates** for $r_\alpha \gg 1$.
- It is possible to **boost the Edelstein response** by engineering the anisotropy.

---

## 6. Dependence on Model Parameters

### 6.1 Dependence on Rashba SOC Strength $\alpha$

The Edelstein susceptibility **increases linearly with $\alpha$** in the HDR [Gaiardoni et al., arXiv:2503.20712 (2025)]:

$$
\chi_{xy} \propto \alpha \quad \text{(HDR)}
$$

This is confirmed numerically and analytically. As $\alpha$ increases, the value of $\chi_{xy}/\chi_0$ at which it reaches a plateau also increases [Gaiardoni et al., arXiv:2503.20712 (2025), Fig. 3].

### 6.2 Dependence on Fermi Energy / Chemical Potential

- In the **HDR**: $\chi_{xy}$ is **constant** as a function of $E_F$ [Gaiardoni et al., arXiv:2503.20712 (2025)].
- In the **LDR**: $\chi_{xy}$ **increases linearly** with $E_F$ [Gaiardoni et al., arXiv:2503.20712 (2025), Eq. (10)].

### 6.3 Dependence on Chirality and Sign of $\alpha$

The sign of the Rashba parameter $\alpha$ determines the **chirality** of the spin texture. For $\alpha > 0$ and $\alpha < 0$, the spin orientations on the Fermi surfaces reverse [Auvray et al., 2018; Funato & Matsuo, arXiv:2107.03115 (2021)]. This flips the sign of the Edelstein magnetization.

The **sign of the effective mass** $m^*$ also matters: it determines the splitting order of inner and outer energy branches ($E_+$, $E_-$) [Auvray et al., 2018].

### 6.4 Dependence on Fermi Velocity

Through the density of states and transport time, the Fermi velocity $v_F$ enters the Edelstein susceptibility. The spin density can be expressed through the dimensionless Rashba parameter [Funato & Matsuo, arXiv:2107.03115 (2021)]:

$$
\tilde{\alpha}_R = \frac{m\alpha}{k_F} = \frac{\alpha}{v_F}
$$

Thus, for fixed $\alpha$, increasing the Fermi velocity (decreasing $\tilde{\alpha}_R$) reduces the dimensionless Edelstein response.

---

## 7. Out-of-Plane Edelstein Effect in p-Wave Magnets

### 7.1 Two-Band Model with p-Wave and Rashba Terms

Ezawa [arXiv:2501.01888 (2025)] proposed a model combining a p-wave magnet with Rashba SOC:

$$
\boxed{H(\mathbf{k}) = \frac{\hbar^2(k_x^2+k_y^2)}{2m}\sigma_0 + \lambda(k_x\sigma_y - k_y\sigma_x) + Jk_x\,\mathbf{n}\cdot\boldsymbol{\sigma}}
$$

where $\lambda$ is the Rashba coupling, $J$ is the p-wave Néel coupling, and $\mathbf{n}$ is the p-wave Néel vector.

### 7.2 Out-of-Plane Néel Vector ($\mathbf{n} = \hat{z}$)

The energy spectrum is:

$$
\varepsilon_{\pm} = \frac{\hbar^2 k^2}{2m} \pm k\sqrt{F(\phi)}, \qquad F(\phi) \equiv \lambda^2 + J^2\cos^2\phi
$$

The spin expectation values are:

$$
S^{\pm}_x = \mp\frac{\lambda\sin\phi}{\sqrt{F(\phi)}}, \qquad
S^{\pm}_y = \pm\frac{\lambda\cos\phi}{\sqrt{F(\phi)}}, \qquad
S^{\pm}_z = \pm\frac{J\cos\phi}{\sqrt{F(\phi)}}
$$

The Edelstein susceptibility components (up to first order in $J$ and $\lambda$ for $\mu > 0$) are [Ezawa, arXiv:2501.01888 (2025)]:

$$
\boxed{
\begin{aligned}
\alpha^{ME}_{xx} &= 0, \\
\alpha^{ME}_{yx} &= -\frac{g\mu_B m}{2\pi\hbar^3 W}\,\lambda, \\
\alpha^{ME}_{zx} &= -\frac{g\mu_B m}{2\pi\hbar^3 W}\,J
\end{aligned}}
$$

**Key result:** For an out-of-plane p-wave Néel vector, an in-plane electric field $\mathbf{E} = E_x\hat{x}$ induces an **out-of-plane magnetization** $M_z = e\tau\alpha^{ME}_{zx}E_x$ proportional to $J$, in addition to the in-plane component $M_y$ proportional to $\lambda$.

- $\alpha^{ME}_{zx} = 0$ when $J = 0$ **or** $\lambda = 0$ (both are required for the out-of-plane effect).
- The sign of $\alpha^{ME}_{zx}$ depends on the sign of $J$ but not on $\lambda$.

### 7.3 In-Plane Néel Vector ($\mathbf{n} = \hat{y}$)

The Edelstein susceptibility is [Ezawa, arXiv:2501.01888 (2025)]:

$$
\boxed{
\begin{aligned}
\alpha^{ME}_{yx} &= -\frac{mg\mu_B}{4\pi\hbar^3 W}\,(J + 2\lambda), \\
\alpha^{ME}_{xx} &= \alpha^{ME}_{zx} = 0
\end{aligned}}
$$

---

## 8. Acoustic (Mechanical) Edelstein Effect

Funato & Matsuo [arXiv:2107.03115 (2021)] studied the *acoustic Edelstein effect* (AEE)—spin density induced by lattice distortion dynamics. The spin density from the Fermi surface term is:

$$
\langle\hat{\sigma}_\alpha\rangle^{k}_{\text{surf}} = i\omega\,\alpha_R\,m\,\nu_0\,\tilde{a}_2\,\tau\,[\hat{z}\times\mathbf{u}_{q,\omega}]_\alpha
$$

where $\mathbf{u}_{q,\omega}$ is the lattice velocity field. The **current–spin conversion efficiency** for the AEE is:

$$
\lambda_A = -\frac{\tilde{\alpha}_R}{k_F}\frac{e}{\mu}\left[\frac{a_3}{\tilde{a}_2} - 2\tilde{\alpha}_R^2\left(1 - \frac{\tilde{a}_2}{2a_1}\right)\right]
$$

while for the conventional electric EE:

$$
\lambda_e = -\frac{\tilde{\alpha}_R}{k_F}\frac{e}{\mu}\left(1 - \frac{a_1}{\tilde{a}_2}\right)\left[\frac{a_3}{\tilde{a}_2} - 2\tilde{\alpha}_R\left(2 - \frac{\tilde{a}_2}{a_1} - \frac{a_1}{\tilde{a}_2}\right)\right]
$$

The AEE and conventional EE show **different $\alpha_R$-dependencies**, indicating they are distinct mechanisms [Funato & Matsuo, arXiv:2107.03115 (2021)].

---

## 9. Effect of Magnetic Field: Out-of-Plane Polarization

Engel, Rashba, and Halperin [arXiv:cond-mat/0609078 (2006)] showed that with parallel in-plane electric and magnetic fields, **out-of-plane spin polarization** can be generated for anisotropic impurity scattering or non-parabolic bands.

For the Rashba model with $\mathbf{B} = B\hat{x}$ and $\mathbf{E} = E\hat{x}$, the spin-orbit field is:

$$
\mathbf{b}(\mathbf{k}) = 2\alpha\,\hat{z}\times\mathbf{k} + \Delta_x\hat{x}, \qquad \Delta_x = g^*\mu_B B
$$

The **Bloch equations** for the total spin polarization are [Engel et al., arXiv:cond-mat/0609078 (2006)]:

$$
\dot{\mathbf{s}} = \langle\mathbf{b}\rangle\times\mathbf{s} - \overleftrightarrow{\tau}^{-1}_s\,\mathbf{s} + \boldsymbol{\Gamma}
$$

with generation rate:

$$
\boldsymbol{\Gamma} = \left(\frac{1}{2}\nu\Delta_x\tau^{-1}_{xy},\; \frac{1}{2}\nu\langle b_y\rangle\tau^{-1}_{xy},\; \frac{1}{4}\nu\langle b_y\rangle\Delta_x\tilde{\gamma}_0\right)
$$

The **static (dc) out-of-plane polarization** is:

$$
\boxed{s_z = \frac{1}{2}\nu\,\alpha\,eE_x\tau\,\frac{\Delta_x\tau_z}{1+\Delta_x^2\tau_{xy}\tau_z}\,\tilde{\gamma}_0}
$$

where $\tilde{\gamma}_0$ characterizes the anisotropy of impurity scattering and/or band non-parabolicity ($\tilde{\gamma}_0 = \zeta + 3$ for small-angle scattering).

**Key result:** The out-of-plane polarization $s_z$ is **proportional to $\Delta_x \propto B$**, so it reverses sign with the magnetic field. It vanishes for isotropic scattering and parabolic bands ($\tilde{\gamma}_0 = 0$).

---

## 10. Numerical Implementation Guidelines

### 10.1 Algorithm for Computing the Edelstein Magnetization

1. **Define parameters**: $m$, $\alpha$, $E_F$ (or $\mu$), $\tau$, $T$, and grid in $\mathbf{k}$-space.

2. **Compute band energies**: $\varepsilon_{\pm}(\mathbf{k}) = \frac{\hbar^2k^2}{2m} \pm \alpha\hbar k$.

3. **Compute spin expectation values** on each band: $\langle\boldsymbol{\sigma}\rangle^{\pm}_{\mathbf{k}} = (\pm\sin\theta,\;\mp\cos\theta,\;0)$.

4. **Compute group velocities**: $\mathbf{v}^{\pm}(\mathbf{k}) = \nabla_{\mathbf{k}}\varepsilon^{\pm}(\mathbf{k})$.

5. **Apply the linear-response formula**:

$$
\mathbf{M} = -\mu_B\sum_{\mathbf{k},\nu}|e|\,\bar{\tau}^{\nu}_{\mathbf{k}}\,(\mathbf{v}^{\nu}\cdot\mathbf{E})\,\delta(\varepsilon^{\nu}_{\mathbf{k}} - E_F)\,\langle\boldsymbol{\sigma}\rangle^{\nu}_{\mathbf{k}}
$$

or the equivalent zero-temperature form:

$$
\mathbf{M} = e\tau g\mu_B\int\frac{d^2k}{(2\pi)^2}\,\mathbf{S}(\mathbf{k})\,(\mathbf{E}\cdot\mathbf{v})\,\delta(\varepsilon_{\mathbf{k}}-\mu)
$$

6. **Extract susceptibility tensor**: $\chi_{ij} = \partial M_i/\partial E_j$.

### 10.2 Python Code Skeleton

```python
import numpy as np

# Parameters
m = 0.152          # effective mass in eV^-1 Å^-2 (oxide interfaces)
alpha = 52.0       # Rashba SOC in meV·Å
EF = 60.0          # Fermi energy in meV
tau = 1e-12        # transport time in seconds
mu_B = 5.788e-5    # Bohr magneton in eV/T
e = 1.602e-19      # electron charge (C)
hbar = 6.582e-16   # hbar in eV·s

def dispersion(k, m, alpha):
    """Rashba energy dispersion."""
    return hbar**2 * k**2 / (2*m) + np.array([-1, 1]) * alpha * k

def spin_expectation(theta):
    """Spin expectation values for the two chiral bands."""
    return np.array([np.sin(theta), -np.cos(theta), 0.0]), \
           np.array([-np.sin(theta), np.cos(theta), 0.0])

def group_velocity(k, theta, m, alpha):
    """Group velocities for the two bands."""
    vx = hbar*k*np.cos(theta)/m + np.array([-alpha, alpha])*np.cos(theta)
    vy = hbar*k*np.sin(theta)/m + np.array([-alpha, alpha])*np.sin(theta)
    return vx, vy

# Build k-grid in polar coordinates
Nk, Ntheta = 500, 500
kmax = 0.5  # in units of inverse Angstrom
k = np.linspace(1e-6, kmax, Nk)
theta = np.linspace(0, 2*np.pi, Ntheta)

# Compute magnetization for E along x
Mx, My = 0.0, 0.0
for ki in k:
    eps_plus, eps_minus = dispersion(ki, m, alpha)
    for tj in theta:
        # Band + (helicity +1)
        vx_plus, vy_plus = group_velocity(ki, tj, m, alpha)
        s_plus = spin_expectation(tj)[0]
        delta = abs(eps_plus - EF) < 1e-3  # delta-function approximation
        My += -mu_B*e*tau*(vx_plus*Ex)*delta*s_plus[1]*ki

# Normalize by area factors...
```

### 10.3 Expected Graphics

The following explicit plots should be produced:

1. **Spin density $M_y$ vs. electric field magnitude $|E|$** — linear relationship (since we are in the linear-response regime).

2. **Spin density components vs. electric field direction** — $M_x = \chi_{xx}E_x + \chi_{xy}E_y$; for the isotropic Rashba model, $\chi_{xx} = 0$, $\chi_{xy} = -\chi_{yx}$, so $\mathbf{M}$ is always perpendicular to $\mathbf{E}$.

3. **$M_y$ vs. $\alpha$** — linear increase in HDR [Gaiardoni et al., Fig. 3, right panel].

4. **$M_y$ vs. $E_F$ (or $\mu$)** — plateau in HDR, linear increase in LDR [Gaiardoni et al., Fig. 2, left panel; Fig. 3, left panel].

5. **$M_y$ vs. anisotropy ratios $r_m$, $r_\alpha$** — increasing function saturating for large $r_\alpha$ [Gaiardoni et al., Fig. 6].

6. **Out-of-plane component $M_z$ vs. $J$ (p-wave parameter)** — linear in $J$, zero for $J=0$ [Ezawa, Fig. 2(a1)].

7. **$M_z$ vs. $\lambda$ (Rashba)** — for the p-wave model with out-of-plane Néel vector, $M_z \propto J$ (independent of $\lambda$ for small $\lambda$) [Ezawa, Fig. 2(b1)].

8. **$M_z$ vs. magnetic field $B$** (for anisotropic scattering) — linear in $B$ near $B=0$, with Hanle-type saturation [Engel et al., Eq. (16)].

---

## 11. Summary of Key Formulas for the Model

| Quantity | Formula | Source |
|----------|---------|--------|
| Rashba Hamiltonian | $\hat{H} = \frac{p^2}{2m} + \alpha\hat{z}\cdot(\mathbf{p}\times\boldsymbol{\sigma})$ | Bychkov & Rashba (1984) |
| Band energies | $\varepsilon_{\pm} = \frac{\hbar^2k^2}{2m} \pm \alpha\hbar k$ | Gaiardoni et al. (2025) |
| Spin texture | $\langle\boldsymbol{\sigma}\rangle^{\pm}_{\mathbf{k}} = (\pm\sin\theta,\;\mp\cos\theta,\;0)$ | Gaiardoni et al. (2025) |
| HDR magnetization | $M_y = \frac{\mu_B\|e\|\tau}{2\pi\hbar^2}m\alpha\,[\hat{z}\times\mathbf{E}]_y$ | Gaiardoni et al. (2025), Eq. (8) + Corr. |
| LDR magnetization | $M_y = \frac{\mu_B\|e\|\tau}{2\pi\hbar^2}\sqrt{m^2\alpha^2+2mE_F}\,[\hat{z}\times\mathbf{E}]_y$ | Gaiardoni et al. (2025), Eq. (9) + Corr. |
| Anisotropic (mass) | $\chi_{xy}/\chi_0 = 4\pi m_x\alpha\,r_m/(1+\sqrt{r_m})$ | Gaiardoni et al. (2025), Eq. (12) |
| Anisotropic (SOC) | $\chi_{xy}/\chi_0 = 4\pi m\alpha_x\,r_\alpha/(1+r_\alpha)$ | Gaiardoni et al. (2025), Eq. (12) |
| Out-of-plane (p-wave) | $\alpha^{ME}_{zx} = -\frac{g\mu_B m}{2\pi\hbar^3 W}J$ | Ezawa (2025), Eq. (13) |
| Out-of-plane (B-field) | $s_z = \frac{1}{2}\nu\alpha eE_x\tau\frac{\Delta_x\tau_z}{1+\Delta_x^2\tau_{xy}\tau_z}\tilde{\gamma}_0$ | Engel et al. (2006), Eq. (16) |

---

## 12. References

1. **V. M. Edelstein**, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Commun.* **73**, 233 (1990). [Original prediction of the Edelstein effect.]

2. **Y. A. Bychkov and É. I. Rashba**, "Properties of a 2D electron gas with lifted spectral degeneracy," *JETP Lett.* **39**, 78 (1984). [Original Rashba Hamiltonian.]

3. **P. Gambardella and I. M. Miron**, "Current-induced spin-orbit torques," *Philos. Trans. R. Soc. A* **369**, 3175–3197 (2011). [Edelstein effect review and experimental context.]

4. **I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, R. Citro**, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," arXiv:2503.20712 (2025). [Primary source for the analytical DEE formulas in isotropic and anisotropic Rashba models.]

5. **M. Ezawa**, "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets," arXiv:2501.01888 (2025). [Source for out-of-plane Edelstein effect and p-wave magnet model.]

6. **H.-A. Engel, E. I. Rashba, B. I. Halperin**, "Out-of-plane spin polarization from in-plane electric and magnetic fields," arXiv:cond-mat/0609078 (2006). [Source for out-of-plane polarization via combined E and B fields.]

7. **T. Funato and M. Matsuo**, "Acoustic Rashba–Edelstein effect," arXiv:2107.03115 (2021). [Source for acoustic Edelstein effect and conversion efficiencies.]

8. **F. Auvray, J. Puebla, M. Xu, B. Rana, D. Hashizume, Y. Otani**, "Spin accumulation at nonmagnetic interface induced by direct Rashba-Edelstein effect," (2018). [Experimental characterization of the DREE, spin accumulation and Kerr effect detection.]

9. **E. I. Rashba and V. I. Sheka**, "Electric-Dipole Spin Resonances," arXiv:1812.01721 (2018). [Historical context: spin–orbit interaction, combined resonances, Rashba physics.]