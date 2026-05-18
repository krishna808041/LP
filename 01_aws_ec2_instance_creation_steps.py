# ============================================================
# PRACTICAL 01
# TITLE: Case Study on Amazon EC2 and Learn about Amazon EC2 Web Services
# FILE PURPOSE:
# This Python file is for study/journal/viva preparation.
# It does NOT create a real EC2 instance.
# It prints the practical flow and includes all PDF steps as comments.
# ============================================================

# ============================================================
# BASIC THEORY
# ============================================================
# Amazon EC2 means Elastic Compute Cloud.
# EC2 is an AWS web service used to create virtual servers in the cloud.
# These virtual servers are called EC2 instances.
#
# In this practical, we are creating an EC2 instance by selecting:
# 1. AWS EC2 service
# 2. Instance name
# 3. AMI / operating system
# 4. Instance type / machine size
# 5. Key pair for secure login
# 6. Network, firewall/security group, and storage
# 7. Review and launch
# ============================================================


def show_ec2_steps():
    print("PRACTICAL: Amazon EC2 Instance Creation")
    print("-" * 55)

    # ------------------------------------------------------------
    # STEP 1: Login and Navigate to EC2 Dashboard
    # ------------------------------------------------------------
    # PDF instruction:
    # - Log in to AWS Management Console.
    # - From Services menu, choose EC2 under Compute section.
    # - Under Resources, click Instances (Running) to view running instances.
    #
    # Theory:
    # AWS Management Console is the web interface for AWS services.
    # EC2 Dashboard shows all virtual servers and their current status.
    print("Step 1: Login to AWS Console and open EC2 Dashboard")

    # ------------------------------------------------------------
    # STEP 2: Launch a New Instance
    # ------------------------------------------------------------
    # PDF instruction:
    # - Click Launch Instance.
    # - Enter instance name, for example: my-first-ec2-server.
    #
    # Theory:
    # Launch Instance starts the wizard for creating a new cloud server.
    print("Step 2: Click Launch Instance and enter instance name")

    # ------------------------------------------------------------
    # STEP 3: Choose Amazon Machine Image / AMI
    # ------------------------------------------------------------
    # PDF instruction:
    # - Select Amazon Machine Image, which is the OS for server.
    # - For beginners choose Amazon Linux 2, Ubuntu, or Windows.
    # - AMIs are preconfigured templates with OS and some software.
    #
    # Theory:
    # AMI works like an operating system image/template.
    # Example: Ubuntu AMI creates an Ubuntu cloud server.
    print("Step 3: Select AMI such as Amazon Linux, Ubuntu, or Windows")

    # ------------------------------------------------------------
    # STEP 4: Choose Instance Type
    # ------------------------------------------------------------
    # PDF has no clear separate text for this step, but EC2 creation
    # normally requires instance type selection before key pair.
    #
    # Theory:
    # Instance type decides CPU, RAM, and network capacity.
    # For free-tier practice, choose t2.micro or t3.micro if available.
    print("Step 4: Choose instance type like t2.micro/t3.micro")

    # ------------------------------------------------------------
    # STEP 5: Create or Select Key Pair
    # ------------------------------------------------------------
    # PDF image shows the Create Key Pair window.
    # - Enter key pair name.
    # - Select .pem for OpenSSH or .ppk for PuTTY.
    # - Create key pair and download private key securely.
    #
    # Theory:
    # Key pair is used for secure login to the EC2 instance.
    # AWS stores public key and user downloads private key.
    # Without private key, we cannot connect to Linux EC2 using SSH.
    print("Step 5: Create/select key pair for secure login")

    # ------------------------------------------------------------
    # STEP 6: Network and Storage Configuration
    # ------------------------------------------------------------
    # PDF instruction:
    # 1. Network Settings: Use default VPC and subnet unless needed.
    # 2. Firewall/Security Group: Allow SSH port 22 for Linux or
    #    RDP port 3389 for Windows.
    # 3. Storage Settings: Free tier allows up to 30 GB EBS gp2.
    #    Keep default 8 GB or increase as needed.
    #
    # Theory:
    # VPC is virtual private cloud network.
    # Security group is firewall controlling allowed traffic.
    # EBS is disk storage attached to EC2 instance.
    print("Step 6: Configure VPC, subnet, security group, and storage")

    # ------------------------------------------------------------
    # STEP 7: Review and Launch
    # ------------------------------------------------------------
    # PDF instruction:
    # - Review configurations and ensure Free Tier eligible.
    # - Click Launch Instance.
    # - Click View Instances to see server initialization.
    #
    # Theory:
    # After launch, instance state changes from pending to running.
    # When running, the server is ready to use.
    print("Step 7: Review settings, launch instance, and view instance")

    print("-" * 55)
    print("Conclusion: EC2 provides cloud virtual servers called instances.")
    print("Important: Stop or terminate unused instances to avoid charges.")


if __name__ == "__main__":
    show_ec2_steps()
