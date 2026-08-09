# python-server
A Python web server deployed to Google Cloud Run using Buildpacks.

## 1. Create new GitHub Repo and connect it to Google Cloud

* Create new GitHub repo:
  https://github.com/wizzard262/python-server

* Login to Google Cloud Console:
  https://console.cloud.google.com/ (Project: Development)

* Go to:
  Cloud Run → Create Service → Deploy from source

* Choose:
  "Continuously deploy from a repository"

* Connect GitHub via Developer Connect:
  - Authorise GitHub
  - Select the "python-server" repo

* Build Type:
  "Go, Node.js, Python, Java, .NET Core, Ruby or PHP via Google Cloud's buildpacks"

  **Note:** Buildpacks automatically create a container image.  
  This means the Python code must run a real web server.  
  We use **Flask**, a lightweight Python web framework.

* Runtime:
  Select **Python** (this is for Buildpacks, not Cloud Run Functions)

* Service name:
  python-server

* Allow public access

* Deployment URL example:
  https://python-server-576465670226.europe-west1.run.app

## 2. Python web server code (Flask)

Inside the GitHub repo, create these two files in the repo root:

* **main.py**  
This file contains the Flask application that Cloud Run will run.  
Flask listens on the $PORT environment variable provided by Cloud Run.  
_(See main.py in this repo for the actual server code.)_

* **requirements.txt**  
This file lists Python dependencies.  
Because Buildpacks generate the container automatically, you only need:  
```flask```  
_(Add any other packages here if needed.)_

## 3. Automatic redeploy

Every push to the GitHub branch triggers Cloud Build:
  - Cloud Build rebuilds the container using Buildpacks
  - Cloud Run redeploys the updated service automatically

No Dockerfile required.  
No manual container configuration needed.
