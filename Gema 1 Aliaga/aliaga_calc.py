import os
import math
from colorama import init, Fore, Style

init(autoreset=True)

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def ejecutar_aliaga():
    while True:
        limpiar()
        print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * 78 + "╗")
        print(Fore.CYAN + Style.BRIGHT + "║" + Fore.WHITE + Style.BRIGHT + " CALCULADORA FINANCIERA REAL - DR. CARLOS ALIAGA VALDEZ ".center(78) + Fore.CYAN + "║")
        print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * 78 + "╝")

        try:
            print(Fore.YELLOW + Style.BRIGHT + "\n--- VARIABLES DE ENTRADA ---")
            p = float(input(Fore.WHITE + "1. Capital Principal (P) ...: "))
            j_porcentaje = float(input(Fore.WHITE + "2. Tasa Nominal (j %) ......: "))
            dias_tn = float(input(Fore.WHITE + "3. Periodo de la TN (días) .: "))
            dias_cap = float(input(Fore.WHITE + "4. Periodo Capitaliz. (días): "))
            plazo_total = float(input(Fore.WHITE + "5. Plazo del depósito (días): "))

            # --- LÓGICA MATEMÁTICA REAL ---
            j = j_porcentaje / 100
            m = dias_tn / dias_cap  # Frecuencia
            n = plazo_total / dias_cap  # Número de capitalizaciones
            i_efectiva = j / m
            s = p * math.pow((1 + i_efectiva), n)  # Fórmula S = P(1+i)^n
            interes = s - p

            print(Fore.CYAN + Style.BRIGHT + "\n" + "═" * 80)
            print(Fore.CYAN + Style.BRIGHT + "  REPORTES DE SALIDA (PRECISIÓN 8 DECIMALES)")
            print(Fore.CYAN + Style.BRIGHT + "═" * 80)
            
            print(Fore.WHITE + " Frecuencia (m) ...........: " + Fore.GREEN + Style.BRIGHT + f"{m:.8f}")
            print(Fore.WHITE + " Capitalizaciones (n) .....: " + Fore.GREEN + Style.BRIGHT + f"{n:.8f}")
            print(Fore.WHITE + " Tasa Efectiva del periodo : " + Fore.GREEN + Style.BRIGHT + f"{i_efectiva:.8f}")
            print(Fore.CYAN + "─" * 80)
            print(Fore.WHITE + Style.BRIGHT + " MONTO COMPUESTO (S) ......: " + Fore.YELLOW + Style.BRIGHT + f"{s:,.2f}")
            print(Fore.WHITE + Style.BRIGHT + " INTERÉS COMPUESTO (I) ....: " + Fore.YELLOW + Style.BRIGHT + f"{interes:,.2f}")
            print(Fore.CYAN + Style.BRIGHT + "═" * 80)
            
        except ValueError:
            print(Fore.RED + "\nError: Por favor, ingrese solo números.")

        opcion = input(Fore.WHITE + "\n¿Desea otro cálculo? (ENTER para sí / 'FIN' para salir): ")
        if opcion.upper() == 'FIN':
            break

if __name__ == "__main__":
    ejecutar_aliaga()
