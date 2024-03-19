#importing to GitHub
from getpass import getpass
import git
import os

#https://github.com/Hackathon2024-March/challenge-artifacts


github_token = ""
org_name = 'Hackathon2024-March'  # Replace with your GitHub username
repo_name = 'fraud_breakers/'  # Replace with your repository name
repo_url = f'https://github.com/{org_name}/{repo_name}.git'
clone_path = "/content/Github/"+repo_name

# Ensure the target directory doesn't already exist
if os.path.exists(clone_path):
    print(f"The directory {clone_path} already exists. Please remove it or use a different path.")
else:
    # Construct the HTTPS URL with authentication
    auth_repo_url = repo_url.replace('https://', f'https://{github_token}@')

    auth_repo_url = repo_url.replace('https://', f'https://x-access-token:{github_token}@')

    #auth_repo_url  = "https://"+user_name+":"+github_token+"@"+"github.com/"+org_name+"/"+repo_name 


    try:
        # Clone the repository
        git.Repo.clone_from(auth_repo_url, clone_path)
        print(f"Repository '{repo_name}' cloned into '{clone_path}'")
    except Exception as e:
        print(f"Failed to clone repository: {e}")

    # For security reasons, consider clearing the token variable after use
    del github_token
