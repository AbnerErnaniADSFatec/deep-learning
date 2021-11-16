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

Instalar as depêndencias da linguagem Python:

~~~shell
(deep-learning) $ python -m pip install -r requirements.txt
~~~

Para instalar as dependências específicas e abrir uma conexão com o ambiente virtual criado anteriormente execute o comando abaixo:

~~~shell
(deep-learning) $ ipython kernel install --user --name deep-learning
~~~

Execução do ambiente Jupyter no Python:

~~~shell
(deep-learning) $ jupyter lab
~~~
