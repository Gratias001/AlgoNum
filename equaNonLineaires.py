from math import exp
from math import fabs


def f(x):
    return exp(x) - 1


def fprime(x):
    return x


def intermediaire(fonc, a, b):
    if fonc(a) * fonc(b) < 0:
        return True
    else:
        return False


def dichotomie(precision, a, b):
    """
        LA méthode de la sécante ou de la corde:
        Elle prend en paramètre :
            ~precision: qui constitue la précision sur laquelle on travaillera
            ~a: qui constitue la borne ineférieur de l'intervalle de travail
            ~b: qui constitue la borne supérieur de l'intervalle de travail
        Elle affiche à l'écran une phrase sur le zero approché
    """

    intervalle = [a, b]

    while fabs(a - b) > precision:
        c = (a + b) / 2
        if f(c) * f(a) == 0:
            print(f'\tla solution de cette équation est {c}')
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    intervalle_solution = [a, b]

    print(f"Dans l'intervalle {intervalle}: la valeur approchée du zero de f est dans {intervalle_solution}"
          f",\n\tSoit x_zero = {(a + b) / 2}")


def secante(precision, a, b):
    """
    LA méthode de la sécante ou de la corde:
    Principe: Join à chaque fois les bouts Xn et Xn+1 et le Xn+2 est l'intersection
    entre la droite (XnXn+1) et (OX) absisses
    Elle prend en paramètre :
        ~precision: qui constitue la précision sur laquelle on travaillera
        ~a: qui constitue la borne inférieur de l'intervalle de travail
        ~b: qui constitue la borne supérieur de l'intervalle de travail
    Elle affiche à l'écran une phrase sur le zero approché
    """
    intervalle = [a, b]
    while fabs(a - b) > precision:
        c = a - (b - a) * f(a) / (f(b) - f(a))
        a = b
        b = c
        if f(c) == 0:
            print('Solution retrouvé: ', c)
            break
    intervalle_solution = [a, b]
    print(f"Dans l'intervalle {intervalle}: la valeur approchée du zero de f est dans {intervalle_solution}"
          f",\n\tSoit x_zero = {((a + b) / 2):.2f}")


def newton(fonc, fprime, precision, x0):
    """La méthode de Newton:
    Principe: à partir  d'un x0 donné par l'utilisateur, on trace les tengantes
    et le Xn+1 est l'intersection entre la tengante et les absisses
    fonc: la fonction sur laquelle on va opérer
    fonc_prime: dérivée f' de la fonction
    precision: Précision de l'opération
    x0: absisse du point d'initialisation
    """


def substitution(fonc, precision, x0):
    """Pour ce qui concerne cette méthode, d'autres l'appelle la méthode des points fixes,
            Prend en paramètre:
                fonc: la fonction à traiter
                precision: la précision à laquelle on veut trouver le resultat
                x0 valeur d'initialisation du point fixe
        """
    x_now = x0
    x_next = fonc(x_now)
    while fabs(x_next - x_now) / x_next > 0:
        x_now = x_next
        x_next = fonc(x_now)
        # Si un x_next donne 0, alors le x_now serait probablement une solution
        if x_next == 0:
            print(f"La solution est {x_now}")
            break
    print(f"Solution x de x = g(x)= {x_next}")


secante(0.0001, -1, 9)
