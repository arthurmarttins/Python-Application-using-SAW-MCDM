import numpy as np

# Função para normalizar a matriz de decisão
def normalize(matrix, criteria_types):
    norm_matrix = np.zeros_like(matrix, dtype=float)
    for j in range(matrix.shape[1]):
        if criteria_types[j] == 'beneficio':
            norm_matrix[:, j] = matrix[:, j] / np.max(matrix[:, j])
        else:  # Critério de custo
            norm_matrix[:, j] = np.min(matrix[:, j]) / matrix[:, j]
    return norm_matrix

# Função para calcular a soma ponderada
def weighted_sum(norm_matrix, weights):
    return np.dot(norm_matrix, weights)

# Dados dos materiais (Permissividade dielétrica relativa, Tangente de perdas, Espessura)
# Linha: material, Coluna: propriedades (ε_r, tan δ, h)
materials_data = np.array([
    [4.4, 0.02, 1.6],  # FR4
    [2.2, 0.0009, 0.787],  # Rogers RT/duroid 5880
    [2.1, 0.0001, 1.0]  # Teflon
])

# Pesos para os critérios (ε_r, tan δ, h)
weights = np.array([0.40, 0.30, 0.30])

# Definição dos tipos de critérios
criteria_types = ['beneficio', 'custo', 'beneficio'] 

# Normalizar a matriz de decisão
norm_matrix = normalize(materials_data, criteria_types)

# Calcular a soma ponderada para cada material
scores = weighted_sum(norm_matrix, weights)

# Classifique os materiais com base em suas pontuações (quanto maior, melhor)
ranking = np.argsort(scores)[::-1]

# Produzir os resultados
materials = ['FR4', 'Rogers RT/duroid 5880', 'Teflon']
print("Normalized Decision Matrix:")
print(norm_matrix)
print("\nWeighted Sum Scores:")
for i, score in enumerate(scores):
    print(f"{materials[i]}: {score:.4f}")

print("\nRanking of Materials:")
for rank, index in enumerate(ranking, start=1):
    print(f"Rank {rank}: {materials[index]} with score {scores[index]:.4f}")

# Escolha o melhor material (com base na classificação)
best_material_index = ranking[0]
chosen_material = materials[best_material_index]

# Parâmetros para o melhor material (FR4, Rogers RT/duroid 5880 ou outro com base na classificação)
eps_r_best = materials_data[best_material_index, 0]  # Permissividade dilétrica relativa (constante dielétrica)
tan_delta_best = materials_data[best_material_index, 1]  # Tangente de perdas
h_best = materials_data[best_material_index, 2]  # Espessura do substrato (em mm)

# Projeto de antena para f_r = 2,45 GHz (para material escolhido)
# Velocidade da luz mm/s
c = 3e11
f_r = 2.45e9  # Frequencia de rerssonência em Hz

# Calcule a largura (W) com base na fórmula para a largura do patch para uma determinada frequência de ressonância
W = c / (2 * f_r * np.sqrt((eps_r_best + 1) / 2))

# Calcular a constante dielétrica efetiva (ε_eff)
# 1) Calcular a relação de W/h -> h_best escolhida pelo metodo
W_h_ratio = W / h_best

# 2) Lógica condicional para calcular ε_eff com base na relação W/h
if W_h_ratio >= 1:
    epsilon_eff = ((eps_r_best + 1) / 2) + ((eps_r_best - 1) / 2) * (1 / (np.sqrt(1 + (12 * (h_best / W)))))
else:
    epsilon_eff = (((eps_r_best + 1) / 2) + ((eps_r_best - 1) / 2) * ((((1 / (np.sqrt(1 + (12 * (h_best / W))))))) + 0.04 * (1 - (W_h_ratio)**2)))

# Calcule o comprimento (L)
L = (c / (2 * f_r * np.sqrt(epsilon_eff))) - 0.824 * h_best * ((epsilon_eff + 0.3) * ((W / h_best) + 0.264)) / ((epsilon_eff - 0.258) * ((W / h_best) + 0.8))

# Conversão do comprimento e largura em milímetros
L_mm = L * 1000  # em mm
W_mm = W * 1000  # em mm

# Cálculo da largura da linha de alimentação (Wf) para uma linha de microfita de 50 ohms
Z0 = 50  # Impedância característica (geralmente 50 ohms)
Wf = (8 * h_best / np.pi) * (Z0 / (eps_r_best)) + 0.264 #ATENÇÃO: verificar a fórmula

# Cáculo das dimensões do plano de terra (Lg e Wg)
L_g = 3 * L
W_g = 3 * W

# Imprima o material escolhido e os parâmetros utilizados no projeto
print(f"\nChosen Material: {chosen_material}")
print(f"Material Properties for {chosen_material}:")
print(f"Relative Dielectric Permittivity (ε_r): {eps_r_best}")
print(f"Loss Tangent (tan δ): {tan_delta_best}")
print(f"Thickness (h): {h_best} mm")
print(f"\nAntenna Design Parameters for f_r = 2.45 GHz:")
print(f"Length of the Patch (L): {L:.2f} mm")
print(f"Width of the Patch (W): {W:.2f} mm")
print(f"Feed Line Width (Wf): {Wf:.2f} mm")
print(f"Ground Plane Length (Lg): {L_g:.2f} mm")
print(f"Ground Plane Width (Wg): {W_g:.2f} mm")
print(f"\nSome tests...")
print(epsilon_eff)
print(W_h_ratio)