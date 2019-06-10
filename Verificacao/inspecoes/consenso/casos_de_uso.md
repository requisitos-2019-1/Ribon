# Verificação - Inspeção [Casos de Uso](https://github.com/requisitos-2019-1/Ribon/wiki/Casos-de-uso)

## Questões Avaliadoras


| Questão | Impacto | Justificativa do Impacto | Tipo |
| ------- | :-----: | :----------------------: | :--: |
| 1. O nome do ator revela seu papel no sistema? | Alto | Como é um modelo, é necessário que os elementos atendam esse modelo e sigam suas diretrizes | Binário |
| 2. Os nomes dos casos de uso são construidas em voz ativa, e utilizam o tempo presente? (ex.: "Sistema valida a quantia informada" em vez de "A quantia informada deve ser validada pelo sistema"). | Alto | Regra do modelo | Binário |
| 3. O nome do caso de uso é de fácil compreensão? | Médio | É importante clareza para se entender a abstração geral sobre o caso de uso | Numérico |
| 4. Quando ocorre relacionamentos entre casos de usos, estes relacionamentos são:Relacionamento de Inclusão, Relacionamento de Extensão, Relacionamento de Generalização? | Alto | Regra do modelo | Binário |
| 5. No diagrama, ao menos um caso de uso se relaciona com um ator? | Alto | Regra do modelo | Binário |
| 6. Nos relacionamentos de inclusão, o caso base é incompleto sem o caso que está sendo incluído? | Alto | Regra do Modelo | Binário |
| 7. Nos relacionamentos de extensão, o caso extendido (ou, caso base) é completo por si só? | Alto | Regra do modelo | Binário |
| 8. Nos relacionamentos de generalização, este é usado para funcionalidades que foram re-usadas? | Alto | Regra do modelo | Binário |
| 9. Possui descrição dos atores? | Baixo | Informações extras que possam ajudar a elucidar são bem-quistas | Binário |
| 10. Possui descrição dos casos de usos, com o fluxo principal e os alternativos descritos? | Alto | O objetivo, num documento completo, é que se haja no mínimo 3 cenários (podendo-se [estender para até 5](https://hientl.files.wordpress.com/2011/12/tnyc_discovering-require.pdf), página 120): <li>O caminho padrão para se atingir o objetivo</li><li>Fluxos alternativos</li><li>Fluxos de exceção (que podem ou não ser recuperados)</li><br />Sendo assim, não é exatamente uma regra do modelo, mas uma boa prática necessária | Numérico |
| 11. A descrição de caso de uso é a de um caso de uso representado no diagrama? | Alto | Regra do Modelo | Binário |
| 12. São evitados termos sem quantificação precisa, como "muito", "pouco", "adequado", "claro", "fácil" "longo" "curto", "rápido" "etc"? | Médio | Casos de uso são, via de regra, orientados à elementos mensuráveis | Numérica |
| 13. São evitados termos que indicam opção, como "possivelmente", "alternativamente", "no caso", "se", etc, sem especificar um fluxo alternativo? | Médio | Os casos de uso hão de ser concretos, e suas variações condicionais devem se tornar outros casos de uso | Numérico |
| 14. Os termos passiveis de mais de uma interpretação constam em glossário, com clara definição? | Alto | Auxilia no entendimento, sendo, portanto, uma boa prática necessária. | Numérico |
| 15. Uma vez utilizado um termo, ele é mantido para referenciar-se ao mesmo elemento? | Baixo | Para evitar interpretações dúbias | Numérico |
| 16. São evitados termos que indicam a prematura especificação de interface, tais como "checar", "botão" etc? | Médio | É importante não entrar numa operacionalização excessiva já que foge um pouco do propósito do diagrama | Numérico |
| 17. As funcionalidades se restringem ao quê o sistema deve fazer e não em como, evitando a definição explicita de código na especificação? | Médio | Boa prática, pois evita operacionalização excessiva | Binário |
| 18. A descrição evita requisitos de negócio sem ação direta ao sistema? | Médio | Normalmente regras de negócio implicam em requisitos não-funcionais, e estes últimos não têm espaço no modelo. Logo, normalmente, é uma questão de regra de modelo. | Binário |
| 19. Os nomes dos casos de uso são numeradas para que possibilitem a rastreabilidade? | Médio | Boa prática | Binário |
| 20. Os nomes dos casos de uso procuram ser objetivas, evitando redundâncias ou presença de informações evidentemente desnecessárias? | Baixo | Boa prática | Numérico |


## Auditorias Realizadas

* [Inspeção - Henrique Martins](https://github.com/requisitos-2019-1/Ribon/blob/master/Verificacao/inspecoes/henrique-martins/inspecao_caso_de_uso.md)
* [Inspeção - Victor Rodrigues](https://github.com/requisitos-2019-1/Ribon/blob/master/Verificacao/inspecoes/victor-rodrigues/inspecao_casos_de_uso.md)

## Consenso das Avaliações

|Casos de Uso| 1*     | 2*     | 3| 4*     | 5*     | 6*     | 7*     | 8*     |9*|10| 11*    |12|13|14|15| 16 | 17*    | 18*    | 19*    | 20     |
|------------| -      | -      | -| -      | -      | -      | -      | -      |- |--| --     |--|--|--|--| -- | --     | --     | --     | --     |
|    UC001   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC002   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC003   |&#10003;|&#10003;|7 |&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC004   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC005   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC006   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC007   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC008   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10|10  |&#10003;|&#10003;|&#10003;|10      |
|    UC009   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10|10  |&#10003;|&#10003;|&#10003;|10      |
|    UC010   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10|10  |&#10003;|&#10003;|&#10003;|10      |
|    UC011   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC012   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC013   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC014   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC015   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 5  |x       |&#10003;|&#10003;|10      |
|    UC016   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC018   |&#10003;|&#10003;|7 |&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 10 |&#10003;|&#10003;|&#10003;|10      |
|    UC019   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 10 |&#10003;|&#10003;|&#10003;|10      |
|    UC020   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 10 |&#10003;|&#10003;|&#10003;|10      |
|    UC021   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC022   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC023   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 10 |&#10003;|&#10003;|&#10003;|10      |
|    UC024   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC025   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 5  |x       |&#10003;|&#10003;|10      |
|    UC026   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |
|    UC027   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 10 |&#10003;|&#10003;|&#10003;|10      |
|    UC028   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 10 |&#10003;|&#10003;|&#10003;|10      |
|    UC029   |&#10003;|&#10003;|10|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|x |10|&#10003;|10|10|10|10| 7  |x       |&#10003;|&#10003;|10      |


# Justificativas

## UC001

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|Utilização do termo "botão"|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC002

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|Utilização do termo "botão"|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC003

| Questão | Justificativa |
|-| ------------- |
|3|O nome "Selecionar causa" pode não significar muito para uma pessoa não familiarizada com o app|
|9|Não existe descrição dos atores|
|16|O termo "abrir menu" refencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC004

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "card" refencia  um elemento de interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC005

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "card" refencia  um elemento de interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC006

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "card" refencia  um elemento de interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC007

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "card" refencia  um elemento de interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC008

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|

## UC009

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|

## UC010

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|

## UC011

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "abrir menu" refencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC012

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "abrir menu" refencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC013

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "botão" refencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC014

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "botão" refencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC015

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo 2 do fluxo de eventos referencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC016

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "botão" refencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC018

| Questão | Justificativa |
|-| ------------- |
|3|O nome "Selecionar causa" pode não significar muito para uma pessoa não familiarizada com o app|
|9|Não existe descrição dos atores|

## UC019

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|

## UC020

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|

## UC021

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "botão" refencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC022

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "botão" refencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC023

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|

## UC024

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|"Ícone de presente" referencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC025

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|Os termos "botão" e "Página de pacotes" refenciam interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC026

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "botão" refencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|

## UC027

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|

## UC028

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|

## UC029

| Questão | Justificativa |
|-| ------------- |
|9|Não existe descrição dos atores|
|16|O termo "botão" refencia interface|
|17| O Caso de Uso diz como o sistema deve realizar a funcionalidade utilizando elementos de interface|