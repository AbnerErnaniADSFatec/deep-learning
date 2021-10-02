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

Para instalar as dependências específicas, abrir uma conexão com o ambiente virtual criado anteriormente:

~~~shell
(deep-learning) $ ipython kernel install --user --name deep-learning
~~~

Instalar as depêndencias:

~~~shell
(deep-learning) $ python -m pip install -r requirements.txt
~~~

Execução do ambiente Jupyter no Python.

~~~shell
(deep-learning) $ jupyter lab
~~~
