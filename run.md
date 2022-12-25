# Run flask server
cd server
conda activate codenames
flask run --host 0.0.0.0

# Run Vue server
cd client
npm run serve

# If change from windows or linux
RUn fix
npm run lint -- --fix