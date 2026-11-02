# Checklist da Aula 23

Testes de publicação: 01/11/2026. Revisão final: 02/11/2026. URL: https://avd-20262-pratica-app-esinvgkzeu54ts2nfappsuq.streamlit.app/

## Preparação e publicação

- [x] Repositório público na conta Rodrigo603, origin configurado e commits das Aulas 21 e 22 enviados.
- [x] app.py na raiz; caminhos de dados relativos ao projeto.
- [x] CSV tratado versionado em data/clean/dataset.csv.
- [x] Tema e requisitos versionados no commit da Aula 22.
- [x] App publicado pelo autor no Streamlit Community Cloud.
- [x] Link real do app adicionado ao README.
- [x] Dependências do app separadas das dependências dos notebooks na preparação da Aula 23.
- [x] Alterações finais revisadas e autorizadas pelo autor para o commit da Aula 23.

## Teste público sem login

O agente testou o app publicado no navegador do aplicativo, sem sessão autenticada do Streamlit. O autor confirmou, em resposta nesta conversa, que abriu o app no Chrome em janela anônima e que as duas abas carregaram sem pedir login.

- [x] Abertura sem login.
- [x] Confirmação de janela anônima pelo autor.
- [x] Dashboard 1: mapa e histogramas carregaram.
- [x] Dashboard 2: quatro cartões e três visuais carregaram.
- [x] Slider de edições: 1930 produziu 18 registros; intervalo completo restaurado.
- [x] Métodos Pearson e Kendall responderam; Spearman é o padrão.
- [x] Seletor quantitativo: seleção vazia mostrou orientação; uma variável manteve histograma e orientação para correlação; várias variáveis restauradas.
- [x] Faixa de gols 0 a 0: 101 registros, dos quais 100 com placar.
- [x] Caixa de sem placar desmarcada: recorte acima passou para 100 registros com placar.
- [x] Seleção Brazil: 119 registros com placar.
- [x] Fases vazias: mensagem de recorte vazio, sem exceção; filtros restaurados.
- [x] Clique em 2022 no gráfico do Dashboard 2: 64 jogos e uma edição.
- [x] Shift + clique em 2026: 168 jogos e duas edições.
- [x] Limpeza da seleção: retorno a 1.068 jogos e 23 edições.
- [x] Revisão do conteúdo exibido: dados de partidas e estatísticas, sem credenciais ou informações pessoais do dataset.
- [x] Varredura de 29 arquivos textuais do projeto sem indícios dos padrões de tokens, chaves privadas e credenciais examinados. Não substitui a revisão individual.
- [x] Cinco testes locais passaram após as marcações de código e a fixação das versões de produção.

Evidência: evidencia-app-publicado.jpg. O link inserido no README é a mesma URL testada. A versão pública testada corresponde ao código da Aula 22; após o push final, é necessário confirmar o novo deploy.

## Entregáveis

- [x] EDA original preservada em notebooks/eda-rjdo.ipynb.
- [x] Notebook adaptado e dados tratados.
- [x] Dois rascunhos em entregas/.
- [x] Justificativas atualizadas com os motivos enviados pelo autor em sua reflexão.
- [x] Registro de usos, prompts e marcações de código preparados.
- [x] PDF final recebido do autor, com identificação, registros de uso, reflexão e assinatura gov.br.
- [x] Autor revisou e assinou sua versão final; informou ter conversado com a professora antes de autorizar o envio.
- [x] E-mail e data real de entrega fornecidos pelo autor e inseridos no PDF.
- [x] Reflexão individual enviada pelo autor e inserida integralmente no PDF.
- [x] Autor assinou o PDF em 02/11/2026.
- [x] Declaração assinada preservada localmente para entrega pelo Classroom; arquivo excluído do versionamento público por conter dados pessoais no certificado.
- [ ] Autor enviar os links e a declaração assinada no Classroom.

A cópia assinada original permanece preservada no computador do autor. Os registros de uso em Markdown continuam públicos, mas o PDF assinado será entregue pelo Classroom.
