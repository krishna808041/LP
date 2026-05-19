# ============================================================
# PRACTICAL 04
# TITLE: Design and Develop Custom Application Mini Project using Salesforce Cloud
# FILE PURPOSE:
# This Python file is for study/journal/viva preparation.
# It does NOT create a real Salesforce app.
# It prints every PDF step as comments and output.
# ============================================================

# ============================================================
# BASIC THEORY
# ============================================================
# Salesforce Cloud allows creation of business applications using
# low-code/no-code tools.
#
# Lightning App is a container that groups objects, tabs, navigation
# items, branding, and user access.
#
# Example Mini Project:
# Student Management App
# - App stores/manages student-related data using Salesforce objects.
# - In PDF output, navigation items like Contacts and Calendar are shown.
# ============================================================


def show_salesforce_custom_app_steps():
    print("PRACTICAL: Salesforce Custom Lightning App")
    print("-" * 70)

    # STEP 1
    # Open Salesforce in Lightning Experience.
    # Lightning Experience is the modern Salesforce UI.
    print("Step 1: Open Salesforce in Lightning Experience")

    # STEP 2
    # Open App Launcher -> View All -> Quick Search -> App Manager ->
    # Click New Lightning App.
    # App Manager is used to create and manage apps.
    print("Step 2: App Launcher -> View All -> App Manager -> New Lightning App")

    # STEP 3
    # Fill the mentioned information in App Details and Branding.
    # Enter app name, developer name, description, image/logo, and color.
    # Example: Student Management App.
    print("Step 3: Fill App Details and Branding")

    # STEP 4
    # Click Next -> App Option optional.
    # App options include navigation style, form factor, and personalization.
    # Usually Standard Navigation and Desktop are used for simple app.
    print("Step 4: Click Next and keep/change App Options")

    # STEP 5
    # Click Next -> Add Utility optional.
    # Utility items are optional footer tools like notes, history, etc.
    # For simple mini project, we can skip or keep default.
    print("Step 5: Click Next and optionally add Utility Items")

    # STEP 6
    # Click Next -> Navigation Item.
    # Add items/tabs that should appear inside the app.
    # PDF shows items like Contacts and Calendar.
    # For Student Management, add Students tab if custom object is created.
    print("Step 6: Add Navigation Items like Contacts, Calendar, Students")

    # STEP 7
    # Click Next -> User Profile -> Save and Finish.
    # Select the user profile that can access this app.
    # Example: System Administrator.
    print("Step 7: Select User Profiles and click Save & Finish")

    # STEP 8
    # You will get Lightning Experience App Manager Window.
    # This confirms app is created and listed in App Manager.
    print("Step 8: Verify app appears in Lightning Experience App Manager")

    # STEP 9
    # Search your app by name in App Launcher.
    # Enter some characters to see app name with logo.
    print("Step 9: Open App Launcher and search app by name")

    # STEP 10
    # Click on app to see application appearance/output window.
    # Output shows app navigation such as Contacts and Calendar.
    print("Step 10: Open app and verify final output/navigation")

    print("-" * 70)
    print("Optional Student Management data storage extension:")
    print("1. Object Manager -> Create -> Custom Object -> Student")
    print("2. Add fields: Roll Number, Email, Phone, Department, Year")
    print("3. Create Students tab and add it to app navigation")
    print("4. Open app -> Students -> New -> enter student record -> Save")
    print("Conclusion: Custom Salesforce Lightning App is created using cloud tools.")


if __name__ == "__main__":
    show_salesforce_custom_app_steps()
