import math
from scipy.stats import norm

def black_scholes_option(S, K, T, r, sigma, option_type):
    """
    Fonction pour calculer le prix d'une option européenne (Call ou Put)
    en utilisant le modèle de Black-Scholes.
    
    :param S: Prix de l'actif sous-jacent
    :param K: Prix d'exercice (strike)
    :param T: Temps à l'échéance (en années)
    :param r: Taux d'intérêt sans risque (en décimal)
    :param sigma: Volatilité de l'actif sous-jacent (en décimal)
    :param option_type: "call" ou "put"
    :return: Prix de l'option
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == "call":
        return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Le type d'option doit être 'call' ou 'put'.")

if __name__ == "__main__":
    print("Bienvenue dans le pricer Black-Scholes pour options européennes.\n")

    # Récupérer les informations nécessaires auprès de l'utilisateur
    option_type = input("Type d'option ('call' ou 'put') : ").strip().lower()
    while option_type not in ["call", "put"]:
        print("Erreur : le type d'option doit être 'call' ou 'put'.")
        option_type = input("Type d'option ('call' ou 'put') : ").strip().lower()

    try:
        S = float(input("Prix de l'actif sous-jacent (S) : "))
        K = float(input("Prix d'exercice (K) : "))
        T = float(input("Temps à l'échéance en années (T) : "))
        r = float(input("Taux d'intérêt sans risque (r, en décimal, ex : 0.05 pour 5%) : "))
        sigma = float(input("Volatilité de l'actif sous-jacent (sigma, en décimal, ex : 0.2 pour 20%) : "))

        # Calculer le prix de l'option
        option_price = black_scholes_option(S, K, T, r, sigma, option_type)
        print(f"\nLe prix de l'option {option_type} est : {option_price:.2f}")

    except ValueError as e:
        print(f"Erreur dans la saisie : {e}")

