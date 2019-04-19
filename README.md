

# <center>Inys
## <center> Software desenvolvido com: </center>

![Python2.7](https://img.shields.io/badge/Python-v2.7-important.svg)  

![title](https://transformacaodigital.com/wp-content/uploads/2017/11/o-que-e-inteligencia-artificial-700x525.jpg)

Inys é um software para **auxiliar o usuário** em diversas coisas, afim de poupar o tempo do usuário.

Para que um comando seja **reconhecido** pela Inys, é necessário que o usuário **fale** determinadas **palavras-chaves** a fim de que ela entenda o que **você deseja**, desde que estejam desde já, nela programada.

****
**Observação:**
- **É normal que no reconhecimento de voz, ela entenda o própio nome como Ines, fique a vontade na pronúncia**
- **A Inys foi desenvolvida para sistemas Linux, logo, suas funções são voltadas apenas para o sistema em questão.**
****

- **Comandos** e suas **funções**:
	- "**Inys abra o firefox**" irá executar o firefox, caso esteja instalado no seu computador.
	- "**Inys abra o google**" irá executar o firefox e abrir o site do google.
	- "**Inys tudo bem?**" irá responder carinhosamente a pergunta =).
	- "**Inys quando o mundo vai acabar?**"
	- "**Inys abra o facebook**" irá executar o firefox e abrir o site do facebook.
	- "**Inys abra o WhatsApp**" irá executar o firefox e abrir o site do whatsapp web.
	- "**Inys abra o meu github**" irá executar o firefox e abrir o site do seu Github. **Obsercação: Modifique a URL no arquivo [interacoes.py](https://github.com/ProfessorJamesBach/Inys/blob/master/Inys/Inys_principal/interacoes.py), linha 60.**
	- "**Inys abra o Visual Studio Code**" irá executar o Vscode caso esteja instalado.
	- "**Inys que horas são?**".
	- "**Inys pesquise _Pesquisa_**", irá pesquisar o que foi passado no google e abrir o 1º link que ela encontrar, além de retornar no terminal 10 links que foram achados. Exemplo: **Inys pesquise como fazer um bolo.**
	 - "**Inys toque _Musica_**", irá pesquisar o que foi passado no google e abrir o 1º link que ela encontrar, além de retornar no terminal 10 links que foram achados. Exemplo: **Inys toque No Tears Left To Cry Arianna Grande**.
	 - "**Inys quem te criou?**"
	 - "**Inys qual o ip de _URL_?**", irá pingar um determinado site, caso esteja onlline irá retornar seu endereço ip. Exemplo: **Inys qual o ip de facebook.com**
	 - "**Inys qual o preço do _Criptomoeda/Moeda_**?" irá obter o preço atual da criptomoeda/moeda passada. **Observação: Na versão atual temos suporte apenas para as criptomoedas/moedas(palavras-chaves): dólar americano ou dólar dos estados unidos, dólar australiano, dólar canadense, bitcoin cash, bitcoin diamond, bitcoin gold, bitcoin, dogecoin, dash, litecoin, ethereum, cardano e aeternity.**
	 -  "**Inys meu nome é _Nome_**"  acrescentará seu nome a o banco de dados dela, explicaremos como configurá-lo mais a frente.
	 - "**Inys como está o clima?**" atravé do seu endereço IP, utilizará de APIs para retornar ao usuário o clima atual, temperatura, sensação e previsão.
	 - "**Inys gere um cpf**" irá gerar um cpf através de uma API, lembrando que esses cpf são puramente fictícios porém válidos para testes.
	 - "**Inys aonde fica o CEP _CEP_**" irá pegar o CEP informado e através de APIs retornanr sua lozalicação.
	 - "**Inys localize o ip _IP_**" irá através de APIs retornar ao usuário a localização do provedor de um IP.
	 - "**Inys que dia é hoje?**".
	 - "**Inys configura um despertador**" irá configurar em sua database um despertador e tocar quando for o horário. **Obsercação: Datas e Horas os zeros são utilizados somente em alguns casos, exemplo: 8:30, 19/4/2019. Caso deseje um alarme para ás dez e cinco, deverá configurar da seguinte maneira: 10:5**.
	 - "**Inys últimas notícias**" irá pegar as notícias mais recentes através do site de Notícias do UOL.
	 - "**Inys abra o jogo da forca**" irá abrir um jogo da forca feitoem C++.
	 - "**Inys abra o alarme**" inicia o script que irá checar os alarmes.
	 - "**Inys mandar um email**" irá abrir um menu para envio de um email.
	 
## Configurando a Database:

- Primeiro temos que instalar o serviço MySQL, seguindo esse link você pode encontrar detalhadamente como instalar: [Instalando o Sevidor MySQL no Linux](https://www.vivaolinux.com.br/dica/Instalando-o-Servidor-MySQL-no-Linux)
- Agora precisamos clonar o repositório:
	`git clone https://github.com/ProfesorJamesBach/Inys.git`
- Agora entramos no diretório que contém o arquivo de backup da database:
	`cd Inys/inys_db`
- Agora importamos a database:
	`mysql -u usuario -p Inys_db < arquivo.sql`
	O arquivo já contém instruções para criar a database caso ela não exista.

## Instalando os requerimentos:

- A Inys utiliza diversas bibliotecas para seu devido funcionamento, logo precisamos delas.
- Primeiros temos que instalar o Python 2.7
	`sudo apt-get install python2.7`
- Após instalado instalamos o PIP que é um gerenciador/instalador de bibliotecas para o python:
	`sudo apt-get install python-pip`
- Vamos a pasta que se encontra o arquivo requeriments.txt:
	`cd Inys`
- Agora instalamos os requerimentos com o comando:
	`sudo pip install -r requeriments.txt`

## Primeiro contato
- Agora que você já configurou a database e instalou os requerimentos necessários, precisamos apenas de 2 comandos para interagir com a Inys:
- Primeiro entramos na pasta Inys_principal:
	`cd Inys/inys_principal`
- E agora iniciamos ela com o comando:
	`python2 inys.py`

## Desenvolvedores

 [Hugo Henrique](https://www.facebook.com/hugo.henrique.3192479)
   
![Facebook Profile Picture](https://scontent.ffor11-1.fna.fbcdn.net/v/t1.0-9/26168696_1275556685879178_2815537246259700736_n.jpg?_nc_cat=108&_nc_oc=AQndgMYO4ZF-4FEx8KU3Q3O7gsVXc5ifl7ngB1SdA37JgA_ImxZV7uIEID1A1fvVmPrd6A-0gwlUUjDAB8JqYUMh&_nc_ht=scontent.ffor11-1.fna&oh=97782ac3c2c209cd200f287392b6b791&oe=5D340D47)


Um abraço especial ao pessoal dos grupos [PUG-SE](https://t.me/pugse) e [GDG e WTM Aracaju](https://t.me/gdgAracaju) que me auxiliaram em momentos de dúdidas.
