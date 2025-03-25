# 📊 Análise de Complexidade do Algoritmo MaxMin Select

## 🔍 Visão Geral
O algoritmo MaxMin Select é uma implementação eficiente para encontrar simultaneamente o maior e o menor elemento de uma sequência de números. Esta análise detalha os aspectos de complexidade do algoritmo.

## ⏱️ Análise Temporal

### Recorrência
A recorrência do algoritmo pode ser expressa como:
\[ T(n) = 2T\left(\frac{n}{2}\right) + O(1) \]

### Análise por Níveis
1. **Nível 0**: 1 problema de tamanho n
2. **Nível 1**: 2 problemas de tamanho n/2
3. **Nível 2**: 4 problemas de tamanho n/4
4. **Nível i**: 2^i problemas de tamanho n/2^i

### Número de Níveis
O número de níveis é log₂(n), pois:
\[ \frac{n}{2^i} = 1 \Rightarrow i = log_2(n) \]

### Custo por Nível
- Cada nível tem 2^i problemas
- Cada problema faz 2 comparações
- Custo por nível: 2^i * 2 = 2^(i+1)

### Custo Total
\[ \sum_{i=0}^{log_2(n)-1} 2^{i+1} = 2(n-1) \]

## 📈 Complexidade Assintótica

### Big O (Limite Superior)
\[ O(n) \]

### Big Ω (Limite Inferior)
\[ Ω(n) \]

### Big Θ (Limite Justo)
\[ Θ(n) \]

## 💾 Análise Espacial

### Pilha de Recursão
- Profundidade máxima: log₂(n)
- Espaço por chamada: O(1)
- Espaço total: O(log n)

## 🔄 Comparação com Abordagens Alternativas

### Abordagem Ingênua
- Comparações: 2(n-1)
- Espaço: O(1)

### MaxMin Select
- Comparações: 3n/2 - 2
- Espaço: O(log n)

## 📊 Tabela Comparativa

| Método | Comparações | Espaço |
|--------|-------------|---------|
| Ingênuo | 2(n-1) | O(1) |
| MaxMin Select | 3n/2 - 2 | O(log n) |

## 🎯 Conclusão
O algoritmo MaxMin Select oferece uma solução eficiente para encontrar o maior e o menor elemento simultaneamente, com complexidade temporal O(n) e espacial O(log n). Embora use mais espaço que a abordagem ingênua, ele reduz o número de comparações necessárias. 