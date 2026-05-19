# ============================================================
# PRACTICAL 02
# TITLE: Installation and Configure Google App Engine
# FILE PURPOSE:
# This Python file is for study/journal/viva preparation.
# It does NOT create a real Google Cloud project.
# It prints the practical flow and includes all PDF steps as comments.
# ============================================================

# ============================================================
# BASIC THEORY
# ============================================================
# Google App Engine is a Platform as a Service (PaaS) from Google Cloud.
# It is used to deploy and run web applications without managing servers.
#
# In this practical, we configure Google App Engine by:
# - Creating/selecting Google Cloud project
# - Opening App Engine
# - Creating App Engine application
# - Enabling App Engine Admin API
# - Opening Cloud Shell
# - Creating GitHub repository
# - Cloning repository in Cloud Shell
# - Running Python code
# ============================================================


def sample_python_program():
    # This is a small sample program similar to what can be created
    # in GitHub as the Python file in PDF Step 16.
    print("Hello from Google Cloud Shell Python program")


def show_gae_steps():
    print("PRACTICAL: Google App Engine Configuration")
    print("-" * 60)

    # STEP 1
    # Search Google Cloud Platform in a search engine and click Console.
    # Google Cloud Console is the browser UI to manage GCP resources.
    print("Step 1: Search Google Cloud Platform and open Console")

    # STEP 2
    # Click on Select New Project.
    # A project is a container for all GCP resources.
    print("Step 2: Click Select New Project")

    # STEP 3
    # Give project name and click Create.
    # Example project name: MyAppEngineProject.
    print("Step 3: Enter project name and click Create")

    # STEP 4
    # Click Select Project.
    # Selecting project ensures all further services belong to this project.
    print("Step 4: Select the created project")

    # STEP 5
    # In search bar, type App Engine.
    # Search helps to open required GCP service quickly.
    print("Step 5: Search App Engine in Google Cloud search bar")

    # STEP 6
    # Click App Engine and click Create Application.
    # This starts App Engine application creation.
    print("Step 6: Open App Engine and click Create Application")

    # STEP 7
    # Click Next.
    # Usually region/location selection is shown before next step.
    print("Step 7: Click Next after required App Engine setup details")

    # STEP 8
    # Scroll down and click I'll do this later.
    # This skips local SDK setup because Cloud Shell can be used.
    print("Step 8: Click I'll do this later for SDK/local setup")

    # STEP 9
    # In search bar type App Engine Admin API.
    # This API is used to manage App Engine applications.
    print("Step 9: Search App Engine Admin API")

    # STEP 10
    # Click Enable.
    # Enabling API allows App Engine management/deployment operations.
    print("Step 10: Enable App Engine Admin API")

    # STEP 11
    # Click Activate Cloud Shell.
    # Cloud Shell is browser-based Linux terminal provided by GCP.
    print("Step 11: Activate Cloud Shell")

    # STEP 12
    # Cloud Shell screen appears.
    # It already has tools like git, python, and gcloud.
    print("Step 12: Wait for Cloud Shell terminal to open")

    # STEP 13
    # Login to GitHub account and click New Repository.
    # GitHub stores the source code remotely.
    print("Step 13: Login to GitHub and click New Repository")

    # STEP 14
    # Give name to repository and click Create.
    # Example repository name: app-engine-demo.
    print("Step 14: Give repository name and create repository")

    # STEP 15
    # Click creating new file.
    # This is used to add Python file in GitHub repository.
    print("Step 15: Click create new file in GitHub")

    # STEP 16
    # Give name to Python file and type code.
    # Example file name: program.py.
    print("Step 16: Create Python file and type program code")

    # STEP 17
    # Click Code and copy repository URL.
    # The URL is needed for git clone.
    print("Step 17: Click Code button and copy repository URL")

    # STEP 18
    # Go to Cloud Shell and type: git clone <repository-url>
    # This downloads GitHub repository in Cloud Shell.
    print("Step 18: In Cloud Shell run: git clone <repository-url>")

    # STEP 19
    # Type ls.
    # ls lists files/folders and confirms repo was cloned.
    print("Step 19: Run ls to list files/folders")

    # STEP 20
    # Enter cd repository-name.
    # cd changes directory into the cloned repository.
    print("Step 20: Run cd <repository-name>")

    # STEP 21
    # Type ls and run Python code using python program name.
    # Example: python program.py
    print("Step 21: Run ls, then run python program.py")

    print("-" * 60)
    print("Sample program output:")
    sample_python_program()
    print("Conclusion: App Engine environment and Cloud Shell were configured.")


if __name__ == "__main__":
    show_gae_steps()
