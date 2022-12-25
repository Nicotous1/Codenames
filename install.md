# Install Vue App via npm
cd client
npm install

# Create a python env
conda create --name codenames python=3.9

# Install game libray
conda activate codenames
cd game
pip install -e .

# Install flask app
cd server
pip install -r requirements.txt