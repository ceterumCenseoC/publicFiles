import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_b = 9.274e-24  # Bohr magneton (J/T)
e_charge = 1.602e-19  # Elementary charge (C)
hbar = 1.054e-34  # Reduced Planck's constant (J·s)
m_e = 9.109e-31  # Electron mass (kg)

# Model parameters (default values for GaAs-based 2DEG)
def initialize_parameters():
    """
    Initialize model parameters with realistic starting values.
    Returns:
        dict: Dictionary containing model parameters.
    """
    params = {
        'm_eff': 0.067 * m_e,  # Effective mass (kg)
        'alpha_rashba': 5.0e4,  # Rashba spin-orbit coupling strength (m/s)
        'E_F': 10.0 * 1e-3 * e_charge,  # Fermi energy (J)
        'tau': 0.5e-12,  # Transport lifetime (s)
        'E_field': 1.0e5  # Electric field (V/m)
    }
    return params

# Isotropic case calculations
def calculate_isotropic_magnetization(params, regime='HDR'):
    """
    Calculate magnetization for the isotropic Rashba model.
    Args:
        params (dict): Dictionary containing model parameters.
        regime (str, optional): 'HDR' for High-Density Regime, 'LDR' for Low-Density Regime.
    Returns:
        float: Magnetization (A/m).
    """
    m = params['m_eff']
    alpha = params['alpha_rashba']
    E_F = params['E_F']
    tau = params['tau']
    E_x = params['E_field']

    numerator = mu_b * e_charge * tau * m * alpha * E_x
    denominator = 2 * np.pi * hbar**2

    if regime == 'HDR':
        M_y = numerator / denominator
    elif regime == 'LDR':
        sqrt_term = np.sqrt(m**2 * alpha**2 + 2 * m * E_F)
        M_y = (numerator * sqrt_term) / denominator
    else:
        raise ValueError("Invalid regime. Choose 'HDR' or 'LDR'.")

    return M_y

# Anisotropic case calculations
def calculate_anisotropic_susceptibility(params, r_m=1.0, r_alpha=1.0):
    """
    Calculate magnetization components for the anisotropic Rashba model.
    Args:
        params (dict): Dictionary containing model parameters.
        r_m (float, optional): Mass anisotropy ratio (m_y/m_x). Defaults to 1.0.
        r_alpha (float, optional): Rashba parameter anisotropy ratio (alpha_y/alpha_x). Defaults to 1.0.
    Returns:
        tuple: (M_x, M_y) magnetization components (A/m).
    """
    m = params['m_eff']
    alpha_x = params['alpha_rashba'] / np.sqrt(r_alpha)
    alpha_y = params['alpha_rashba'] * np.sqrt(r_alpha)
    E_x = params['E_field']
    E_y = E_x  # Assuming same magnitude for E_y for simplicity

    chi_0 = (mu_b * e_charge * params['tau']) / (2 * np.pi * hbar**2)

    # Mass anisotropy dependence
    chi_xy_mass = (4 * np.pi * m * alpha_y * r_m) / (1 + np.sqrt(r_m))

    # Rashba parameter anisotropy dependence
    chi_xy_alpha = (4 * np.pi * m * alpha_x * r_alpha) / (1 + r_alpha)

    # Calculate magnetization components
    M_x = chi_xy_mass * chi_0 * E_x
    M_y = chi_xy_alpha * chi_0 * E_y

    return M_x, M_y

# Visualization functions
def plot_magnetization_vs_E(params, E_range, regime='HDR'):
    """
    Plot magnetization vs electric field strength.
    Args:
        params (dict): Dictionary containing model parameters.
        E_range (numpy array): Range of electric field values (V/m).
        regime (str, optional): 'HDR' or 'LDR'. Defaults to 'HDR'.
    """
    M = [] ###HERE WAS MANUAL CORRECTION NEEDED; THE AGENT DID NOT UNDERSTAND THAT THE FUNCTION CALCULATE_ISOTROPIC_MAGNETIZATION NEEDS A SINGLE PARAMETER DICTIONARY, NOT AN ARRAY OF PARAMETER DICTIONARIES. I FIXED IT BY CREATING A COPY OF THE PARAMS DICTIONARY FOR EACH E FIELD VALUE.
    for i in range(len(E_range)):
        params['E_field'] = E_range[i]
        M.append(calculate_isotropic_magnetization(params, regime))
    plt.figure(figsize=(10, 6))
    plt.plot(E_range / 1e5, M, marker='o')
    plt.xlabel('Electric Field (V/cm)')
    plt.ylabel('Magnetization (A/m)')
    plt.title(f'Magnetization vs Electric Field ({regime})')
    plt.grid(True)
    plt.show()

def plot_magnetization_vs_alpha(params, alpha_range, regime='HDR'):
    """
    Plot magnetization vs Rashba coupling strength.
    Args:
        params (dict): Dictionary containing model parameters.
        alpha_range (numpy array): Range of Rashba coupling values (m/s).
        regime (str, optional): 'HDR' or 'LDR'. Defaults to 'HDR'.
    """
    M = [] ###HERE WAS MANUAL CORRECTION NEEDED; THE AGENT DID NOT UNDERSTAND THAT THE FUNCTION CALCULATE_ISOTROPIC_MAGNETIZATION NEEDS A SINGLE PARAMETER DICTIONARY, NOT AN ARRAY OF PARAMETER DICTIONARIES. I FIXED IT BY CREATING A COPY OF THE PARAMS DICTIONARY FOR EACH E FIELD VALUE.
    for i in range(len(alpha_range)):
        params['alpha_rashba'] = alpha_range[i]
        M.append(calculate_isotropic_magnetization(params, regime))

    plt.figure(figsize=(10, 6))
    plt.plot(alpha_range / 1e4, M, marker='o')
    plt.xlabel('Rashba Coupling (m/s × 1e4)')
    plt.ylabel('Magnetization (A/m)')
    plt.title(f'Magnetization vs Rashba Coupling ({regime})')
    plt.grid(True)
    plt.show()

def plot_magnetization_vs_EF(params, EF_range, regime='LDR'):
    """
    Plot magnetization vs Fermi energy.
    Args:
        params (dict): Dictionary containing model parameters.
        EF_range (numpy array): Range of Fermi energy values (J).
        regime (str, optional): 'HDR' or 'LDR'. Defaults to 'LDR'.
    """
    M = [] ###HERE WAS MANUAL CORRECTION NEEDED; THE AGENT DID NOT UNDERSTAND THAT THE FUNCTION CALCULATE_ISOTROPIC_MAGNETIZATION NEEDS A SINGLE PARAMETER DICTIONARY, NOT AN ARRAY OF PARAMETER DICTIONARIES. I FIXED IT BY CREATING A COPY OF THE PARAMS DICTIONARY FOR EACH E FIELD VALUE.
    for i in range(len(EF_range)):
        params['E_F'] = EF_range[i]
        M.append(calculate_isotropic_magnetization(params, regime))

    plt.figure(figsize=(10, 6))
    plt.plot(EF_range / (1e-21), M, marker='o')
    plt.xlabel('Fermi Energy (J × 1e-21)')
    plt.ylabel('Magnetization (A/m)')
    plt.title(f'Magnetization vs Fermi Energy ({regime})')
    plt.grid(True)
    plt.show()

def plot_anisotropy_dependence(params, r_m_range, r_alpha_range):
    """
    Plot anisotropy dependence of magnetization.
    Args:
        params (dict): Dictionary containing model parameters.
        r_m_range (numpy array): Range of mass anisotropy ratios.
        r_alpha_range (numpy array): Range of Rashba parameter anisotropy ratios.
    """
    M_x = np.zeros(len(r_m_range))
    M_y = np.zeros(len(r_alpha_range))

    for i, r_m in enumerate(r_m_range):
        M_x[i], _ = calculate_anisotropic_susceptibility(params, r_m=r_m)

    for i, r_alpha in enumerate(r_alpha_range):
        _, M_y[i] = calculate_anisotropic_susceptibility(params, r_alpha=r_alpha)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(r_m_range, M_x, marker='o')
    plt.xlabel('Mass Anisotropy Ratio ($r_m$)')
    plt.ylabel('M_x (A/m)')
    plt.title('Mass Anisotropy Dependence')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(r_alpha_range, M_y, marker='o')
    plt.xlabel('Rashba Anisotropy Ratio ($r_\\alpha$)')
    plt.ylabel('M_y (A/m)')
    plt.title('Rashba Anisotropy Dependence')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_magnetization_vector_field():
    """
    Plot vector field showing magnetization direction relative to electric field.
    """
    E_x = np.linspace(0, 1e5, 5)
    E_y = np.linspace(0, 1e5, 5)
    E_x, E_y = np.meshgrid(E_x, E_y)

    params = initialize_parameters()
    M_x = np.zeros(E_x.shape)
    M_y = np.zeros(E_y.shape)

    for i in range(E_x.shape[0]):
        for j in range(E_x.shape[1]):
            params['E_field'] = np.sqrt(E_x[i,j]**2 + E_y[i,j]**2)
            M = calculate_isotropic_magnetization(params)
            M_x[i,j] = M * E_x[i,j] / np.sqrt(E_x[i,j]**2 + E_y[i,j]**2)
            M_y[i,j] = M * E_y[i,j] / np.sqrt(E_x[i,j]**2 + E_y[i,j]**2)

    plt.figure(figsize=(10, 8))
    plt.quiver(E_x/1e5, E_y/1e5, M_x, M_y, color='b')
    plt.xlabel('Electric Field x (V/cm)')
    plt.ylabel('Electric Field y (V/cm)')
    plt.title('Magnetization Vector Field')
    plt.grid(True)
    plt.show()

# Main execution
if __name__ == "__main__":
    params = initialize_parameters()

    # Example calculations
    print("Isotropic HDR Magnetization:")
    M_HDR = calculate_isotropic_magnetization(params, regime='HDR')
    print(f"M_y = {M_HDR:.2e} A/m")

    print("\nIsotropic LDR Magnetization:")
    M_LDR = calculate_isotropic_magnetization(params, regime='LDR')
    print(f"M_y = {M_LDR:.2e} A/m")

    print("\nAnisotropic Magnetization Components:")
    M_x, M_y = calculate_anisotropic_susceptibility(params)
    print(f"M_x = {M_x:.2e} A/m")
    print(f"M_y = {M_y:.2e} A/m")

    # Generate plots
    E_range = np.linspace(0, 2e5, 20)  # Electric field range (V/m)
    alpha_range = np.linspace(1e4, 1e5, 20)  # Rashba coupling range (m/s)
    EF_range = np.linspace(0, 50e-3*e_charge, 20)  # Fermi energy range (J)
    r_m_range = np.linspace(0.5, 1.5, 20)  # Mass anisotropy ratio
    r_alpha_range = np.linspace(0.5, 1.5, 20)  # Rashba parameter anisotropy ratio

    plot_magnetization_vs_E(params, E_range, regime='HDR')
    plot_magnetization_vs_alpha(params, alpha_range, regime='HDR')
    plot_magnetization_vs_EF(params, EF_range, regime='LDR')
    plot_anisotropy_dependence(params, r_m_range, r_alpha_range)
    plot_magnetization_vector_field()