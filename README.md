# TERMI₿IT₿OT 🤖
A basic tool that tracks Bitcoin transactions in real time above or below a particular price target using a websocket API on your terminal. 

<img src="https://github.com/user-attachments/assets/c85e9a5f-ee02-418b-abac-f74f84e406a8" width = "800" alt ="TERM1B1TB0T_bootanimate" />


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##  STEP-BY-STEP: WINDOWS
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-Step 1: Install Python (if not already installed)<br>
``Download from python.org``<br>
``During install → make sure to check ✅ “Add Python to PATH”``<br>

-Open Windows Terminal / PowerShell<br>

-Navigate to your bot folder<br>
``cd \Users\<YourPCName>\Desktop\btc_tracker``<br>
  
-Step 2: Install dependencies (Only needed once)<br>
``pip install requests websocket-client``<br>

-Step 3: Run it<br>
`` python TERM1B1TB0T.py above 1000``<br>

-₿ Close the Websocket     
``CTRL + C``<br> 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## STEP-BY-STEP: LINUX
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Set up a <B>Virtual Environment</B> for the Bot<br>
  
  This is normal on Linux (or Debian-based distros with strict Python environments).
  You'll run into ``Python’s PEP 668`` restriction, 
  which prevents you from installing packages system-wide using pip3 to avoid breaking your OS-installed Python packages.

## Step 1: Create a Folder for Your Project
  -If you haven’t already:<br>


-Run:<br>
`` mkdir -p ~/btc_tracker``<br>
`` cd ~/btc_tracker``<br>


## Step 2: Create the Virtual Environment
  
   -Run:<br>
``python3 -m venv btc-env``<br>
 
  -This creates a folder btc-env/ inside your project that contains an isolated Python environment.<br>

  
## Step 3: Activate the Environment
   ``source btc-env/bin/activate``
    
-If successful, your terminal will now look something like:<br>
   ``(btc-env) username@kali:~/btc_tracker$``<br>
  
  -This means you’re inside the virtual environment.<br>


 ## Step 4: Install websocket-client
  -While the virtual environment is active, install the required library:<br>
  ``pip install websocket-client``<br>

  -This installs the package only inside your virtual environment — not system-wide.<br>

## Step 4.1: Install websocket-client
  -install requests:<br>
  ``pip install requests``<br>


## Step 5: Run the Bot
  -Still inside the virtual environment, start it with:<br>
   ``python TERM1B1TB0T.py above 500``<br>
  
## ₿ Stop the bot from running
   ``CTRL + C``

  
## Exit virtual environment
   ``deactivate``


## Re-activate it later
   ``source ~/btc_tracker/btc-env/bin/activate``
            
       
 ## List installed packages	
   ``pip list``
            
  
 ## Check Python used
   ``which python (should point inside btc-env)``
            
 
## Run the Bot With a Custom Limit

-Activate your virtual environment first:
  ``source ~/btc_tracker/btc-env/bin/activate``


-Run the bot with a custom price limit (in USD):
 ``python TERM1B1TB0T.py above 5000``


-That will only log BTC transactions worth more than $5000.

-If You Don’t Pass a Value

  If you run:
  ``python TERM1B1TB0T.py``


…it will default to $1000.


## View the Logs

After it's been running a while:

Open high_value_btc_tx.log in a text editor to see the stored transactions.
