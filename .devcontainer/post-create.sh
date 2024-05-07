# Blow the security and upgrade
whoami
sudo chmod -R 777 /opt/conda/pkgs/
conda upgrade -y scikit-image
conda install -y -c conda-forge ipympl
