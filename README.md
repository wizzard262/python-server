# python-server
A Python server using Cloud Run Functions on Google Cloud Platform (GCP)

## 1. Create new GitHub Repo and connect it to Google Cloud

* Create new GitHub repo:
  https://github.com/wizzard262/python-server

* Login to Google Cloud Console:
  https://console.cloud.google.com/
  (Project: Development)

* Go to:
  Cloud Run → Create Service → Deploy from source

* Choose:
  "Continuously deploy from a repository"

* Connect GitHub via Developer Connect:
  - Authorise GitHub
  - Select the "python-server" repo

* Build Type:
  "Go, Node.js, Python, Java, .NET Core, Ruby or PHP via Google Cloud's buildpacks"

* Runtime:
  Select **Cloud Run functions** (event-driven serverless functions)

* Service name:
  python-server

* Allow public access (optional)

* Deployment URL example:
  https://python-server-576465670226.europe-west1.run.app

## 2. Cloud Run Functions – Python repo code

Inside the GitHub repo, create these two files in the repo root:

### main.py
This file contains the Cloud Run Function entrypoint.  
Cloud Run Functions will call the "main" function for every HTTP request.  
(See main.py in this repo for the actual server code.)

### requirements.txt
This file lists Python dependencies.
Cloud Run Functions requires:  
  _functions-framework_  
(Add any other packages here if needed.)

## 3. Automatic redeploy

Every push to the GitHub branch triggers Cloud Build:
  - Cloud Build rebuilds the function
  - Cloud Run redeploys it automatically

No Dockerfile required.
No container configuration needed.
