# 🎓 Algoritmo de Seleção Simultânea (MaxMin Select)

## 📝 Descrição do Projeto
Este projeto implementa o algoritmo de seleção simultânea do maior e menor elementos (MaxMin Select) em Python, utilizando a abordagem de divisão e conquista. O algoritmo é otimizado para encontrar o maior e o menor elemento de uma sequência de números com eficiência.

## 📚 Unidades de Ensino/Tópicos
- Análise de Algoritmos
- Complexidade Computacional
- Algoritmos de Divisão e Conquista
- Recursão
- Teorema Mestre

## 🔍 Análise do Algoritmo

### ⏱️ Medição de Tempo e Funções de Complexidade
O algoritmo MaxMin Select possui as seguintes características:
- **Tempo de Execução**: O(n)
- **Espaço**: O(log n) devido à pilha de recursão
- **Comparações**: 3n/2 - 2 comparações no pior caso

### 🔄 Análise de Algoritmos Iterativos e Recursivos
#### Versão Recursiva (Implementada)
```python
def max_min_select(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    mid = (low + high) // 2
    max1, min1 = max_min_select(arr, low, mid)
    max2, min2 = max_min_select(arr, mid + 1, high)
    return max(max1, max2), min(min1, min2)
```

### 📊 Teorema Mestre
A recorrência do algoritmo pode ser expressa como:
\[ T(n) = 2T\left(\frac{n}{2}\right) + O(1) \]

#### Análise:
- a = 2 (número de subproblemas)
- b = 2 (tamanho dos subproblemas)
- f(n) = O(1) (custo de combinar)
- log_b(a) = log_2(2) = 1

#### Caso do Teorema Mestre:
- Caso 2: f(n) = Θ(n^log_b(a))
- Solução: T(n) = Θ(n)

### 📈 Notações para Complexidade
- **Big O**: O(n) - Limite superior assintótico
- **Big Ω**: Ω(n) - Limite inferior assintótico
- **Big Θ**: Θ(n) - Limite assintótico justo

### 📉 Comportamento Assintótico e Classes de Complexidade
- **Melhor Caso**: Θ(n)
- **Pior Caso**: Θ(n)
- **Caso Médio**: Θ(n)

## 📚 Referências Bibliográficas
1. Cormen, T. H., et al. (2009). Introduction to Algorithms
2. Sedgewick, R., & Wayne, K. (2011). Algorithms
3. [Link para o repositório de referência](https://github.com/joaopauloaramuni/fundamentos-de-projeto-e-analise-de-algoritmos)

## 👥 Informações de Contato
- **Nome**: Mauricio Fernandes Leite
- **Email**: mauriciofernandes3001@gmail.com
- **GitHub**: [MF300175](https://github.com/MF300175)

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.x
- Git

### Instalação
```bash
git clone https://github.com/MF300175/FPAA_Trab_Indiv_2.git
cd FPAA_Trab_Indiv_2
```

### Execução
```bash
python src/main.py
```

### Execução dos Testes
```bash
python -m unittest tests/test_maxmin.py
```

## 📁 Estrutura do Projeto
```
FPAA_Trab_Indiv_2/
├── src/           # Código fonte
│   └── main.py    # Implementação do algoritmo
├── docs/          # Documentação
│   ├── analise_complexidade.md
│   └── teorema_mestre.md
├── tests/         # Testes unitários
│   └── test_maxmin.py
└── assets/        # Recursos visuais
```

## 📊 Documentação Detalhada
Para uma análise mais detalhada do algoritmo, consulte:
- [Análise de Complexidade](docs/analise_complexidade.md)
- [Análise do Teorema Mestre](docs/teorema_mestre.md)