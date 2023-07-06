# cloudwalk-monitor

Inicialmente criei um planejamento da arquitetura do sistema
resolvi utilizar o postrges como banco de dados e python como backend, resolvi inicialmente não criar microserviços ja
que isso complicaria um pouco mais meu codigo e não sei se teria tempo, a primeira implemntação caso necessario seria no
EC2 da AWS caso de tempo. Para facilitar a utilização de outras ferramentas de nuvem para escabilidade.
Depois disso criei com ajuda do chatGPT um plano de desenvolvimento:

1 - Definir requisitos detalhados: Comece revisando os requisitos do sistema de monitoramento em tempo real e documente-os de forma detalhada. Identifique os recursos essenciais, as funcionalidades desejadas, as interfaces de usuário e os casos de uso relevantes. Isso ajudará a ter uma visão clara do escopo do projeto.

2 - Criar o ambiente de desenvolvimento: Configure o ambiente de desenvolvimento, incluindo a instalação do Python, do PostgreSQL e das bibliotecas que você decidiu usar. Certifique-se de ter todas as dependências necessárias instaladas e prontas para uso.

3 - Projetar a estrutura do banco de dados: Com base nos requisitos definidos, projete a estrutura do banco de dados no PostgreSQL. Crie a tabela para armazenar os dados das transações e defina as colunas necessárias. Considere também a adição de índices e restrições para otimizar o desempenho e a integridade dos dados.

4 - Implementar o backend básico: Comece implementando o backend em Python, utilizando o framework escolhido (como Flask ou Django). Crie as rotas e endpoints necessários para receber as transações, consultar os dados do banco de dados e fornecer as funcionalidades de análise e alerta.

5 - Conectar ao banco de dados: Utilize a biblioteca Psycopg2 para estabelecer a conexão entre o backend em Python e o banco de dados PostgreSQL. Implemente as consultas SQL necessárias para inserir, consultar e manipular os dados das transações.

6 - Implementar a lógica de análise e alerta: Utilize as bibliotecas adequadas, como Pandas e scikit-learn, para realizar análises em tempo real nos dados das transações. Implemente a lógica para detectar anomalias e gerar alertas com base nos critérios definidos.

7 - Testar e depurar: Realize testes unitários e de integração para garantir que o backend esteja funcionando corretamente. Depure quaisquer erros ou problemas que surjam durante o processo.

8 - Implementar APIs e interfaces de usuário: Crie APIs para fornecer acesso aos dados e funcionalidades do sistema. Se houver interfaces de usuário, como painéis de controle ou visualizações em tempo real, desenvolva-as nessa etapa.

9 - Documentar o código: À medida que você desenvolve, documente o código para facilitar a manutenção futura e o entendimento do sistema. Descreva as funcionalidades, os endpoints, as dependências e quaisquer outras informações relevantes.

10 - Realizar testes de integração e aceitação: Realize testes mais abrangentes, incluindo testes de integração para garantir que todas as partes do sistema estejam funcionando bem juntas. Verifique se os requisitos definidos estão sendo atendidos e se o sistema está pronto para ser implantado em um ambiente de produção.

11 - Implementar implantação e monitoramento: Planeje a implantação do sistema em um ambiente de produção, seja no AWS EC2 ou em outra infraestrutura. Configure ferramentas de monitoramento, como o Amazon CloudWatch, para acompanhar o desempenho e a disponibilidade do sistema em tempo real.

12 - Realizar testes finais e otimizações: Realize testes finais no ambiente de produção e otimize o desempenho, se necessário. Certifique-se de que o sistema esteja pronto para lidar com a carga de trabalho esperada e que esteja fornecendo os alertas e informações corretamente.

13 - Lançar o sistema: Após todos os testes e otimizações, faça o lançamento do sistema de monitoramento em tempo real. Certifique-se de que todos os componentes estejam funcionando corretamente e que os usuários finais possam acessar as funcionalidades conforme o planejado.

14 - Monitorar e realizar manutenção contínua: Após o lançamento, monitore o sistema regularmente para garantir que esteja operando corretamente. Realize manutenção contínua, como correção de bugs, atualizações de segurança e melhorias de desempenho, conforme necessário.

## Banco de dados

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  time TIMESTAMP,
  status VARCHAR(20),
  count INTEGER
);

- Resolvi por criar uma tabela simples inicialmente sem muitas restrições
- Com esta tabela ainda que basica é possivel criar indices de colunas e restriçoes adicionais caso seja necessario


