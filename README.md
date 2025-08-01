# Python Application using SAW MCDM for Microstrip Antennas Synthesis

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-green)
![Linguagem](https://img.shields.io/badge/linguagem-Python-blue?logo=python)
![Ambiente](https://img.shields.io/badge/ambiente-Node.js-green?logo=node.js)

Este é um projeto em **Python** que utiliza o método de tomada de decisão multicritério **SAW (Simple Additive Weighting)** para selecionar o substrato ideal para o projeto de uma antena de microfita. O script realiza a síntese da antena para uma frequência de ressonância específica, com base nas propriedades do material escolhido.

---

## 🏁 Sobre o Desafio

O objetivo principal deste projeto é aplicar o método SAW para classificar e selecionar o melhor material para uma antena de microfita com base em múltiplos critérios, como permissividade dielétrica relativa ($\epsilon_r$), tangente de perdas ($\tan\delta$) e espessura ($h$). Após a seleção, o script calcula as dimensões de uma antena de microfita para uma frequência de 2.45 GHz.

---

## ✨ Funcionalidades (Implementação Básica)

-   **Seleção de Material:** Aplicação do método SAW para ranquear e escolher o melhor substrato dentre as opções `FR4`, `Rogers RT/duroid 5880` e `Teflon`.
-   **Síntese da Antena:** Cálculo das dimensões do patch (`W` e `L`), da linha de alimentação (`W_f`) e do plano de terra (`W_g` e `L_g`).
-   **Saída de Resultados:** Exibição do ranking dos materiais, do material escolhido e dos parâmetros da antena projetada.

---

## 🛠️ Tecnologias Utilizadas

-   `Python`
-   `Numpy`



Certifique-se de ter o [Python](https://www.python.org/) e a biblioteca `numpy` instalados em sua máquina.

Para instalar o `numpy`, utilize o comando:

```bash
pip install numpy
