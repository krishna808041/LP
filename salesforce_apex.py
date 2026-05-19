# ============================================================
# PRACTICAL 03
# TITLE: Creating an Application in Salesforce.com using Apex Programming Language
# FILE PURPOSE:
# This Python file is for study/journal/viva preparation.
# It does NOT execute Apex code.
# It documents every PDF step and includes the Apex code as reference.
# ============================================================

# ============================================================
# BASIC THEORY
# ============================================================
# Salesforce is a cloud-based CRM and application platform.
# Apex is Salesforce's programming language.
# Apex is similar to Java and is used to write business logic inside Salesforce.
#
# In this practical, we:
# - Create/login to Salesforce Developer Org
# - Open Developer Console
# - Create Apex Class
# - Write arithmetic methods
# - Execute methods using Execute Anonymous Window
# - View output in Debug Log
# ============================================================

# ------------------------------------------------------------
# APEX CODE FROM PDF FOR REFERENCE ONLY
# This code must be typed in Salesforce Developer Console,
# not in Python.
# ------------------------------------------------------------
APEX_CODE = r'''
public class firstClass1 {
    public static void Addition() {
        Integer a = 4;
        Integer b = 5;
        Integer c = a + b;
        Integer d = 4 + 5;
        Integer e = a + 5;
        System.debug('Add = ' + c);
        System.debug('Add = ' + d);
        System.debug('Add = ' + e);
    }

    public static void Subtraction() {
        Integer a = 4;
        Integer b = 5;
        Integer c1 = a - b;
        Integer d1 = b - a;
        Integer e1 = 4 - 5;
        Integer f1 = a - 5;
        System.debug('Sub = ' + c1);
        System.debug('Sub = ' + d1);
        System.debug('Sub = ' + e1);
        System.debug('Sub = ' + f1);
    }

    public static void Multi() {
        Integer a = 4;
        Integer b = 5;
        Integer c = a * b;
        Integer d = 4 * 5;
        Integer e = a * 5;
        System.debug(c);
        System.debug(d);
        System.debug(e);
        Integer f = -4;
        Integer g = a * f;
        System.debug(g);
    }

    public static void Div() {
        Integer a = 4;
        Integer b = 5;
        Integer c = a / b;
        Integer d = 4 / 5;
        Integer e = a / 5;
        System.debug(c);
        System.debug(d);
        System.debug(e);
    }
}
'''

EXECUTE_ANONYMOUS_CODE = r'''
firstClass1.Addition();
firstClass1.Subtraction();
firstClass1.Multi();
firstClass1.Div();
'''


def show_apex_steps():
    print("PRACTICAL: Salesforce Apex Application")
    print("-" * 65)

    # STEP NO 1
    # Create new org using developer.salesforce.com/signup.
    # Org means Salesforce organization/account/environment.
    print("Step 1: Create new Salesforce Developer Org")

    # STEP NO 2
    # After signup, login using login.salesforce.com.
    # This opens Salesforce login page.
    print("Step 2: Open login.salesforce.com after signup")

    # STEP NO 3
    # Login Page: enter credentials to login.
    # Credentials include username and password.
    print("Step 3: Login using Salesforce credentials")

    # STEP 1 INSIDE SALESFORCE
    # Open Developer Console.
    # Developer Console is used to write, save, and execute Apex code.
    print("Step 4: Open Developer Console")

    # STEP 2 INSIDE DEVELOPER CONSOLE
    # File -> New -> Apex Class.
    # Create class named firstClass1.
    print("Step 5: File -> New -> Apex Class -> create firstClass1")

    # TYPE BELOW MENTIONED CODE
    # Type Apex class code with Addition, Subtraction, Multi, Div methods.
    print("Step 6: Type Apex code for arithmetic operations")

    # STEP 3 FROM PDF
    # Click Debug -> Open Execute Anonymous Window.
    # Execute Anonymous Window runs Apex method calls directly.
    print("Step 7: Debug -> Open Execute Anonymous Window")

    # STEP 4 FROM PDF
    # Type Apex method calls:
    # firstClass1.Addition();
    # firstClass1.Subtraction();
    # firstClass1.Multi();
    # firstClass1.Div();
    print("Step 8: Type method calls in Execute Anonymous Window")

    # STEP 5 FROM PDF
    # Click Open Log then Execute code.
    # Open Log lets us view debug output after execution.
    print("Step 9: Select Open Log and click Execute")

    # STEP 6 FROM PDF
    # Click Debug Only to see output clearly.
    # Debug logs display System.debug values.
    print("Step 10: Click Debug Only to view output")

    print("-" * 65)
    print("Apex class to type in Developer Console:")
    print(APEX_CODE)
    print("Execute Anonymous code to run:")
    print(EXECUTE_ANONYMOUS_CODE)
    print("Conclusion: Apex class methods are executed and output is viewed in debug log.")


if __name__ == "__main__":
    show_apex_steps()
