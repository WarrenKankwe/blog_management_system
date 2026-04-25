# Setup Instructions

```bash
# clone repo
git clone https://github.com/<your-username>/blog_management_system.git
cd blog_management_system

# create & activate virtual-env
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# environment variables
cp .env.example .env           # edit if you like

# database
export FLASK_APP=run.py        # Windows PS: $env:FLASK_APP="run.py"
flask db upgrade               # applies migrations
python seed.py                 # loads demo users & data

# run the server
python run.py
