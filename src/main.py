def max_min_select(arr, low, high):
    """
    Implementação do algoritmo MaxMin Select usando divisão e conquista.
    
    Args:
        arr: Lista de números
        low: Índice inicial
        high: Índice final
        
    Returns:
        tuple: (maior_elemento, menor_elemento)
    """
    # Se houver apenas um elemento
    if low == high:
        return arr[low], arr[low]

    # Se houver apenas dois elementos
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divisão do array
    mid = (low + high) // 2

    # Recursão para encontrar o maior e o menor
    max1, min1 = max_min_select(arr, low, mid)
    max2, min2 = max_min_select(arr, mid + 1, high)

    # Combinação dos resultados
    return max(max1, max2), min(min1, min2)

def find_max_min(arr):
    """
    Interface para o usuário do algoritmo MaxMin Select.
    
    Args:
        arr: Lista de números
        
    Returns:
        tuple: (maior_elemento, menor_elemento)
    """
    if len(arr) == 0:
        return None, None
    return max_min_select(arr, 0, len(arr) - 1)

def main():
    """
    Função principal para demonstração do algoritmo.
    """
    # Exemplos de uso
    test_cases = [
        [3, 1, 5, 2, 4],
        [10, 20, 30, 40, 50],
        [5, 5, 5, 5, 5],
        [1],
        []
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"\nTeste {i}:")
        print(f"Array: {arr}")
        max_element, min_element = find_max_min(arr)
        print(f"Maior elemento: {max_element}")
        print(f"Menor elemento: {min_element}")

if __name__ == "__main__":
    main() 