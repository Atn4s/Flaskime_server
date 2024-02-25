# Flaskime!
Um projeto pessoal feito para listar todos os animes que assisti ou pretendo assistir, tudo localmente sob licença: <br>
[![Licença](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.html)

## Interessante, como funciona?
Bom o sistema Flaskime (combinação da palavra Flask e Anime) é dividido em 2 repositórios: 
<br> 
<a href="https://github.com/Atn4s/Flaskime_server">Servidor Flaskime</a> (atual)
<br> 
<a href="https://github.com/Atn4s/Flaskime_web">Pagina web Flaskime</a>
<br>
<p> A lógica de obter a lista de animes é feito apartir da API <a href="https://jikan.moe/"> Jikan </a>
e a lógica de gravar os animes é feito pelo banco de dados SQLite3 criando um database 
listaanime.db que ao executar o servidor ele é criado automaticamente para facilitar 😃 (seu script está disponivel em banco.py)

![image](https://github.com/Atn4s/Flaskime_web/assets/61942303/61ea45fd-cc94-4547-af6f-f33c92f6b641)


## Como posso testar?

<b> 1 - Instale os requisitos do sistema listados no arquivo requirements.txt: </b>
<i>``pip install -r requirements.txt ``</i>
<br>
<b> 2 - Verifique se você possui as versões mais recentes das bibliotecas necessárias: </b>
<i> ``pip install --upgrade -r requirements.txt ``</i>
<br>
<b> 3 - Após instalar os requisitos basta executar: </b>
<i> python3 servidor.py {porta desejada para o Back-end da aplicação Flaskime!} </i>
<br>
<b> 4 - Agora se quiser testar pode usar aqui: <a href="https://atn4s.github.io/Flaskime_web/">Flaskime_web</a> 
(É o mesmo código do repositório <a href="https://github.com/Atn4s/Flaskime_web">Repositório Flaskime_web</a>
 onde ele está configurado também com Github Page, você só precisa configurar seu IP e PORTA) </b> 
<br>
<b>5 - Ou se quiser modificar ou copiar o front-end <a href="https://github.com/Atn4s/Flaskime_web">Front end!</a> aqui está o repositório</b> 
<br>
<b> Aproveite a aplicação Flaskime - Your personal haven for anime: private, secure, and always local.</b>
<br>

---
**Nota:**
Este projeto é licenciado sob os termos da [Licença Pública Geral GNU v3.0](https://www.gnu.org/licenses/gpl-3.0.html). Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
