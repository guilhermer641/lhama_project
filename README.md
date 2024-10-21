Desafio IA - Vonix

Este repositório contém a solução para o Desafio IA da Vonix, onde foi criado um MVP de um atendente virtual utilizando o RASA para interagir com clientes e direcioná-los ao time correto (Suporte Técnico, Vendas ou Cobranças).

Objetivo

O projeto foi desenvolvido com o objetivo de identificar corretamente o contexto das interações dos usuários e redirecioná-los para o departamento apropriado. A solução foca na automação das interações e no uso de ferramentas open-source para maximizar a adaptabilidade e escalabilidade.
Tecnologias Utilizadas

•	RASA: Framework open-source utilizado para criação do atendente virtual.
•	WhatsApp: Para validação prática da solução, adicionei um número de WhatsApp onde é possível testar o MVP: (21) 98725-3915.

Funcionalidades

•	O bot identifica as intenções dos usuários e direciona o atendimento para Suporte Técnico, Vendas ou Cobranças.
•	A cada fallback (quando o bot não compreende a intenção), o sistema registra o evento em log. Isso permite que o processo seja aperfeiçoado posteriormente com base nos dados de falhas.

Melhorias Futuras
•	Automatização do Treinamento: Embora a ideia fosse automatizar o treinamento da IA com base nos logs de fallback, não houve tempo hábil para implementar essa funcionalidade. No entanto, a infraestrutura está preparada para facilitar essa automação no futuro.

Como Rodar o Projeto

1.	Clone o repositório:
bash
Copiar código
git clone https://github.com/guilhermer641/lhama_project.git

2.	Instale as dependências do RASA:
bash
Copiar código
pip install rasa

3.	Treine o modelo:
bash
Copiar código
rasa train

4.	Execute o servidor RASA:
bash
Copiar código
rasa run

5.	Para testar a integração via WhatsApp, utilize o número (21) 98725-3915.

Contribuições
Fique à vontade para sugerir melhorias e abrir issues no repositório. O feedback será muito bem-vindo!

