# WaterClassifier

Esse projeto foi realizado buscando replicar as métricas e resultados do artigo "Water quality classification using machine learning algorithms" que pode ser encontrado em:
https://www.sciencedirect.com/science/article/pii/S2214714422003646?via%3Dihub

Nesse artigo, é utilizada uma base de dados referente a qualidade da água coletada em várias regiões e testada sob vários parâmetros como: Temperatura, Oxigênio Dissolvido, PH, Quantidade de Coliformes Fecais, Condutividade, Nitrato, Demanda biológica de Oxigênio, Coliformes totais.

A partir dessas informações e um cálculo que as integra, é possível classificar as águas coletadas em 4 estados: Clean (Limpo), Unclean (Não Limpo), Polluted (Poluído), Highly polluted (Altamente Poluído).

# Pré-processamento

Nessa etapa, foram implementadas funções para o cálculo e definição dos estados de cada uma das porções de água coletadas. Dessa forma, foi possível separar os dados de entrada (data) e seus respectivos rótulos (labels) para o início do processo de classificação através de aprendizado de máquina supervisionado.

# Classificação

A partir da separação desses dados, foi definido que 40% dos dados seriam usados para treinamento e o restante para teste. A partir disso, foram executados os métodos:

* KNN - K-Nearest Neighbor
* SVM - Support Vector Machine
* MLP - Multi-Layer Perceptron
* Árvore de Decisão
* Naive Bayes

Por fim, foram plotados gráficos utilizando matriz de confusão para demonstrar cada um dos resultados obtidos.