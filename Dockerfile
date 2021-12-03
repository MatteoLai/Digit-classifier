FROM continuumio/miniconda3

# Create the environment:
#COPY requirements.txt .
RUN conda update conda
RUN conda install -c anaconda python=3.8
#RUN conda install --file requirements.txt
#RUN pip install -r requirements.txt
# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "base", "/bin/bash", "-c"]
