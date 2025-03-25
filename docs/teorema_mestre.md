# 📚 Análise do Teorema Mestre para o Algoritmo MaxMin Select

## 🔍 Introdução
O Teorema Mestre é uma ferramenta poderosa para analisar a complexidade de algoritmos recursivos que seguem um padrão específico. Este documento aplica o Teorema Mestre ao algoritmo MaxMin Select.

## 📊 Recorrência do Algoritmo
A recorrência do algoritmo MaxMin Select é:
\[ T(n) = 2T\left(\frac{n}{2}\right) + O(1) \]

## 🔢 Identificação dos Parâmetros
Para aplicar o Teorema Mestre, identificamos:
- a = 2 (número de subproblemas)
- b = 2 (tamanho dos subproblemas)
- f(n) = O(1) (custo de combinar)

## 📈 Cálculo de log_b(a)
\[ log_b(a) = log_2(2) = 1 \]

## 🔍 Análise dos Casos do Teorema Mestre

### Caso 1: f(n) = O(n^(log_b(a) - ε))
- f(n) = O(1)
- n^(log_b(a) - ε) = n^(1 - ε)
- Não se aplica, pois O(1) não é polinomialmente menor que n^(1 - ε)

### Caso 2: f(n) = Θ(n^(log_b(a)))
- f(n) = O(1)
- n^(log_b(a)) = n^1 = n
- Não se aplica, pois O(1) não é igual a Θ(n)

### Caso 3: f(n) = Ω(n^(log_b(a) + ε))
- f(n) = O(1)
- n^(log_b(a) + ε) = n^(1 + ε)
- Não se aplica, pois O(1) não é polinomialmente maior que n^(1 + ε)

## ⚠️ Limitações do Teorema Mestre
O Teorema Mestre não pode ser aplicado diretamente neste caso porque:
1. f(n) = O(1) não se encaixa em nenhum dos três casos
2. A diferença entre f(n) e n^(log_b(a)) não é polinomial

## 🔄 Solução Alternativa
Para este caso específico, utilizamos a análise por árvore de recursão:
1. Cada nível tem 2^i problemas
2. Cada problema tem custo O(1)
3. Total de níveis: log₂(n)
4. Custo total: O(n)

## 📊 Conclusão
Embora o Teorema Mestre não possa ser aplicado diretamente, a análise por árvore de recursão nos permite concluir que:
\[ T(n) = Θ(n) \]

## 📚 Referências
1. Cormen, T. H., et al. (2009). Introduction to Algorithms
2. Sedgewick, R., & Wayne, K. (2011). Algorithms 