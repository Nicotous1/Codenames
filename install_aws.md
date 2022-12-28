# INstall the game on AWS machine
sudo yum update
git clone https://github.com/Nicotous1/Codenames.git
cd client

## Install Node
https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.html

mkdir nodejs
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
. ~/.nvm/nvm.sh 
nvm install --lts OR 17 (works with 17)

## Install Codenames FrontEnd (client)
Follow classic install

## Install Miniconda
mkdir miniconda
cd miniconda
https://docs.conda.io/en/latest/miniconda.html
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Mini..
source /home/ec2-user/.bashrc

## Install Codenames Backend (server)
Follow classic install