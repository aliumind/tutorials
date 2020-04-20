Le istruzioni per scaricare anaconda:

1) Download ambiente: https://www.anaconda.com/distribution/

Comandi utili:

- creazione ambiente: conda create --name $nome_ambiente 
- attivazione ambiente: conda activate $nome_ambiente
- distruzione ambiente: conda remove --name $nome_ambiente --all
- disattivazione ambiente: conda deactivate
- backup package: conda env export  > environment.yml
- restore package: conda env create -f environment.yml -p /home/user/anaconda3/envs/env_name
- installazione pacchetti: conda install $package_name  
    pip install $package_name
