curl https://get.modular.com | \
  MODULAR_AUTH=mut_a917079dd5264e1bb7254a0146a78c9f \
  sh -

apt install python3-venv

modular install mojo

echo 'export MODULAR_HOME="/root/.modular"' >> ~/.bashrc
echo 'export PATH="/root/.modular/pkg/packages.modular.com_mojo/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc