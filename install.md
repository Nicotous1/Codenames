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

# Run flask server
flask run --host 0.0.0.0

# Run Vue server
npm run serve

# If change from windows or linux
RUn fix
npm run lint -- --fix