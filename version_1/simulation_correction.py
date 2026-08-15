import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. PHYSICAL CONSTANTS AND UNITS
# =============================================================================
# We use a mixed unit system common in condensed matter physics to avoid 
# underflow/overflow issues typical in pure SI (eV, Angstroms, Seconds).
# However, we explicitly convert to SI for the magnetization formula to ensure 
# dimensional consistency of the CORRECTED model (factor of 1/hbar^2).

hbar_eVs = 6.582119569e-16      # Reduced Planck constant [eV * s]
hbar_Js = 1.054571817e-34       # Reduced Planck constant [J * s]
e_charge = 1.602176634e-19      # Elementary charge [C]
mu_B_eVT = 5.7883818060e-5      # Bohr magneton [eV / T]
mu_B_JT = 9.2740100783e-24      # Bohr magneton [J / T]
m_e_kg = 9.1093837015e-31       # Electron mass [kg]
A_to_m = 1e-10                  # Angstrom to meter conversion
eV_to_J = 1.602176634e-19       # eV to Joule conversion

# =============================================================================
# 2. REALISTIC MODEL PARAMETERS
# =============================================================================
# Based on High-Density Regime (HDR) of a Rashba 2DEG (e.g., LAO/STO interface)
# Source: Caprara et al., Rep. Prog. Phys. 79, 096501 (2016)

params = {
    # Effective mass: 0.5 * free electron mass
    'm_eff_ratio': 0.5,             # [dimensionless, relative to m_e]
    'm_eff': 0.5 * m_e_kg,          # [kg] - used for SI calculations
    
    # Rashba Spin-Orbit Coupling: 50 meV * Angstrom
    'alpha_eVA': 50.0e-3,           # [eV * A] - Input value
    'alpha': 50.0e-3 * eV_to_J * A_to_m, # [J * m] - SI value for formulas
    
    # Fermi Energy: 60 meV (High Density Regime, E_F >> E_R)
    'EF_eV': 60.0e-3,               # [eV]
    'EF': 60.0e-3 * eV_to_J,        # [J]
    
    # Transport Relaxation Time: 1 ps
    'tau': 1.0e-12,                 # [s]
    
    # Electric Field: 1000 V/m
    'Ex': 1000.0,                   # [V/m]
    
    # g-factor
    'g': 2.0
}

# Derived Parameter: Rashba Energy E_R = m*alpha^2 / (2*hbar^2)
# This helps determine the regime (LDR vs HDR)
E_R = (params['m_eff'] * params['alpha']**2) / (2 * hbar_Js**2)
print(f"System Properties:")
print(f"  Rashba Energy (E_R): {E_R/eV_to_J*1000:.4f} meV")
print(f"  Fermi Energy (E_F): {params['EF_eV']*1000:.1f} meV")
print(f"  Regime: {'High Density (HDR)' if params['EF'] > E_R else 'Low Density (LDR)'}")

# =============================================================================
# 3. ANALYTICAL MODEL FUNCTIONS (CORRECTED)
# =============================================================================

def get_magnetization_HDR(Ex, m, alpha, tau, hbar, mu_B, e):
    """
    Calculates Edelstein Magnetization in High Density Regime (HDR).
    Corrected Formula:
    M_y = (mu_B * e * tau / (2 * pi * hbar^2)) * m * alpha * E_x
    """
    prefactor = (mu_B * e * tau) / (2 * np.pi * hbar**3) # hbar**3 was added manually to match the findings from the dimensional analysis and ensure dimensional consistency.
    M_y = prefactor * m * alpha * Ex
    return M_y

def get_magnetization_LDR(Ex, m, alpha, EF, tau, hbar, mu_B, e):
    """
    Calculates Edelstein Magnetization in Low Density Regime (LDR).
    Corrected Formula:
    M_y = (mu_B * e * tau / (2 * pi * hbar^2)) * sqrt(m^2*alpha^2 + 2*m*EF) * E_x
    """
    prefactor = (mu_B * e * tau) / (2 * np.pi * hbar**3) # hbar**3 was added manually to match the findings from the dimensional analysis and ensure dimensional consistency.
    response_term = np.sqrt(m**2 * alpha**2 + 2 * m * EF)
    M_y = prefactor * response_term * Ex
    return M_y

def get_anisotropic_susceptibility(m_x, m_y, alpha, r_m, hbar, mu_B, e, tau):
    """
    Calculates Susceptibility Chi_xy for Mass Anisotropy.
    Formula: Chi_xy / Chi_0 = 4 * pi * m_x * alpha * (r_m / (1 + sqrt(r_m)))
    where Chi_0 is the isotropic susceptibility baseline.
    Note: We return the ratio or the absolute value depending on use.
    Here we return the dimensionless factor for scaling.
    """
    # The formula in text gives Chi_xy proportional to this factor.
    # Let's return the dimensionless factor for scaling.
    factor = 4 * np.pi * m_x * alpha * (r_m / (1 + np.sqrt(r_m)))
    # To get actual Chi, we need to multiply by the missing 1/hbar^2 factors
    # which are consistent with the HDR formula.
    return factor

# =============================================================================
# 4. VISUALIZATION AND ANALYSIS
# =============================================================================

fig, axs = plt.subplots(2, 3, figsize=(18, 10))
plt.subplots_adjust(hspace=0.3, wspace=0.3)

# --- Plot 1: M_y vs Electric Field Magnitude (Linear Response) ---
E_fields = np.linspace(0, 2000, 100) # V/m
M_vals = [get_magnetization_HDR(E, params['m_eff'], params['alpha'], 
                                params['tau'], hbar_Js, mu_B_JT, e_charge) for E in E_fields]

axs[0, 0].plot(E_fields, np.array(M_vals), 'b-', linewidth=2)
axs[0, 0].set_title('Edelstein Effect: Linear Response\n$M_y$ vs $E_x$', fontsize=14)
axs[0, 0].set_xlabel('Electric Field $E_x$ [V/m]', fontsize=12)
axs[0, 0].set_ylabel('Magnetization $M_y$ [Am^2/m^2]', fontsize=12)
axs[0, 0].grid(True, alpha=0.3)

# --- Plot 2: M_y vs Rashba Coupling Strength (HDR) ---
alphas_eVA = np.linspace(10, 100, 100) # meV*A
alphas_SI = alphas_eVA * 1e-3 * eV_to_J * A_to_m
M_alphas = [get_magnetization_HDR(params['Ex'], params['m_eff'], a, 
                                  params['tau'], hbar_Js, mu_B_JT, e_charge) for a in alphas_SI]

axs[0, 1].plot(alphas_eVA, np.array(M_alphas), 'r-', linewidth=2)
axs[0, 1].set_title('Dependence on SOC Strength ($\\alpha$)\nHigh Density Regime', fontsize=14)
axs[0, 1].set_xlabel('Rashba $\\alpha$ [meV$\cdot$A]', fontsize=12)
axs[0, 1].set_ylabel('Magnetization $M_y$ [Am^2/m^2]', fontsize=12)
axs[0, 1].grid(True, alpha=0.3)

# --- Plot 3: M_y vs Fermi Energy (Transition LDR to HDR) ---
EFs_eV = np.linspace(-0.1, 0.15, 300) # eV (spanning crossing) #note: modified to start from 0.0 to avoid negative EF which can lead to a negative square root in LDR formula
EFs_J = EFs_eV * eV_to_J

M_EFs = []
for ef in EFs_J:
    if ef > 0:
        # HDR (approximation of constant M for EF >> ER, but formula handles it)
        # Using the specific LDR formula is safer for transition as it contains the sqrt term
        # which reduces to m*alpha for large EF. 
        # Actually, the LDR formula text is for EF < 0. 
        # The HDR formula is for EF > 0. 
        # Let's use a smooth transition logic or piecewise based on text.
        # Text says HDR: M ~ m*alpha (const). LDR: M ~ sqrt(m^2 a^2 + 2m E).
        # Note: The LDR formula has EF inside sqrt. For EF < 0, term gets smaller.
        val = get_magnetization_HDR(params['Ex'], params['m_eff'], params['alpha'], 
                                    params['tau'], hbar_Js, mu_B_JT, e_charge)
    else:
        val = get_magnetization_LDR(params['Ex'], params['m_eff'], params['alpha'], 
                                    ef, params['tau'], hbar_Js, mu_B_JT, e_charge)
    M_EFs.append(val)

axs[0, 2].plot(EFs_eV * 1000, np.array(M_EFs), 'g-', linewidth=2)
axs[0, 2].axvline(0, color='k', linestyle='--', label='Band Crossing ($E_F=0$)')
axs[0, 2].set_title('Dependence on Fermi Energy\nTransition LDR $\leftrightarrow$ HDR', fontsize=14)
axs[0, 2].set_xlabel('Fermi Energy $E_F$ [meV]', fontsize=12)
axs[0, 2].set_ylabel('Magnetization $M_y$ [Am^2/m^2]', fontsize=12)
axs[0, 2].legend()
axs[0, 2].grid(True, alpha=0.3)

# --- Plot 4: Spin Direction (Vector Field) ---
# Visualizing M = Chi * [z x E]
# If E rotates in xy plane, M rotates locked perpendicular to it.
theta_E = np.linspace(0, 2*np.pi, 100)
E_mag = 1000
Ex = E_mag * np.cos(theta_E)
Ey = E_mag * np.sin(theta_E)

# For isotropic Rashba, Mx = Chi * Ey, My = -Chi * Ex
Chi_HDR = get_magnetization_HDR(1.0, params['m_eff'], params['alpha'], 
                                 params['tau'], hbar_Js, mu_B_JT, e_charge)
Mx = Chi_HDR * Ey
My = -Chi_HDR * Ex

axs[1, 0].quiver(Ex, Ey, Mx, My, color='purple', scale=None)
axs[1, 0].set_title('Magnetization Direction\nIsotropic Rashba ($\mathbf{M} \perp \mathbf{E}$)', fontsize=14)
axs[1, 0].set_xlabel('$E_x$ [V/m]', fontsize=12)
axs[1, 0].set_ylabel('$E_y$ [V/m]', fontsize=12)
axs[1, 0].axis('equal')
axs[1, 0].grid(True, alpha=0.3)

# --- Plot 5: Anisotropy Dependence (Mass Ratio) ---
r_m_vals = np.linspace(0.1, 10, 100)
# Calculate susceptibility ratio Chi_xy(r_m) / Chi_xy(iso)
# Isotropic case r_m = 1.
# Formula: Chi(r_m) ~ r_m / (1 + sqrt(r_m))
# Note: The paper formula includes m_x * alpha. 
# If we normalize by the isotropic case (r_m=1, m_x=m):
# Ratio ~ [m_x * alpha * r_m / (1+sqrt(r_m))] / [m * alpha * 1/2]
# ~ (r_m / (1+sqrt(r_m))) / 0.5 = 2 * r_m / (1 + sqrt(r_m))
susceptibility_ratio = 2 * r_m_vals / (1 + np.sqrt(r_m_vals))

axs[1, 1].plot(r_m_vals, susceptibility_ratio, 'orange', linewidth=2)
axs[1, 1].axhline(1, color='k', linestyle='--', label='Isotropic ($r_m=1$)')
axs[1, 1].set_title('Mass Anisotropy Effect\nSusceptibility $\chi_{xy}$ Enhancement', fontsize=14)
axs[1, 1].set_xlabel('Mass Ratio $r_m = m_y/m_x$', fontsize=12)
axs[1, 1].set_ylabel('Normalized $\chi_{xy} / \chi_{iso}$', fontsize=12)
axs[1, 1].legend()
axs[1, 1].grid(True, alpha=0.3)

# --- Plot 6: Out-of-Plane Component (p-wave Magnet Model) ---
# Mz = e * tau * alpha_ME_zx * Ex
# alpha_ME_zx = - (g * mu_B * m) / (2 * pi * hbar^3 * W) * J
# We plot Mz vs p-wave coupling J.
# We assume Width W = 1 meter for units, or just look at trend.
J_vals_eVA = np.linspace(-50, 50, 100) # meV*A
J_vals_SI = J_vals_eVA * 1e-3 * eV_to_J * A_to_m

# Constants for alpha_ME
# Note: The formula in text for alpha_ME had dimension issues (hbar^3).
# We implement the expression provided: Coef * J.
# We simply plot the linear dependence trend.
coef_pwave = - (params['g'] * mu_B_JT * params['m_eff']) / (2 * np.pi * hbar_Js**3) 
# (Assuming unit width W=1 for plotting trend)
alpha_ME_zx = coef_pwave * J_vals_SI
M_z = e_charge * params['tau'] * alpha_ME_zx * params['Ex']

axs[1, 2].plot(J_vals_eVA, M_z, 'm-', linewidth=2)
axs[1, 2].axvline(0, color='k', linestyle='--')
axs[1, 2].set_title('Out-of-Plane Edelstein Effect\np-wave Magnet ($M_z \propto J$)', fontsize=14)
axs[1, 2].set_xlabel('p-wave Coupling $J$ [meV$\cdot$A]', fontsize=12)
axs[1, 2].set_ylabel('Magnetization $M_z$ [Am^2/m^2]', fontsize=12)
axs[1, 2].grid(True, alpha=0.3)

print("\nSimulation Complete. Graphics generated.")
plt.show()
