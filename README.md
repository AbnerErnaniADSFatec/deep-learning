# Deep Learning

This space is reserved to class notes for Deep Learning.

## Criação do Ambiente Virtual MiniConda

Criar um ambiente com o miniconda:

~~~shell
$ conda create --name deep-learning python==3.9
~~~

Ativar o ambiente:

~~~shell
$ conda activate deep-learning
~~~

Instalando a dependência `IPython` para utilizar o ambiente conda no jupyter:

~~~shell
(deep-learning) $ conda install notebook ipykernel gdal
~~~

Instalando as dependências `r-base 3.6.1`:

~~~shell
(deep-learning) $ conda install -c conda-forge r-base==3.6.1
~~~

Instalando o pacote `ncurses` para o uso da biblioteca `rpy2` para executar _scripts_ em R em um programa Python:

~~~shell
(deep-learning) $ conda install -c anaconda ncurses
(deep-learning) $ sudo apt-get install libncurses5
~~~

Atualizando os pacotes instalados para configurar as bibliotecas instaladas anteriormente:


~~~shell
(deep-learning) $ conda update --all -c r
~~~

Instalar as bibliotecas que serão utilizadas nos _scripts_ em linguagem R:

~~~shell
(deep-learning) $ conda install -c conda-forge --file requirements-r.txt
~~~

Para instalar as dependências específicas e abrir uma conexão com o ambiente virtual criado anteriormente execute o comando abaixo:

~~~shell
(deep-learning) $ ipython kernel install --user --name deep-learning
~~~

Instalar as depêndencias da linguagem Python:

~~~shell
(deep-learning) $ python -m pip install -r requirements-py.txt
~~~

Execução do ambiente Jupyter no Python:

~~~shell
(deep-learning) $ jupyter lab
~~~
