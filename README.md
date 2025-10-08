# BTC_tracker_bot
A basic tool that tracks Bitcoin transactions in real time above or below a particular price target using a websocket API on your terminal. 
Example >>> 
           
           -----------To track transactions below $9000 for example, your terminal will display;
           -----------!----------------------------------------------------------------------------------------------------------------
           ----------------------------------------------------------------------------------------------------------------------------
           Connected to Blockchain WebSocket. Tracking high-value BTC transactions...
           
           [2025-08-01 18:02:15] a13358d87e94202ae20770a68d755bd965a688fb4527f20a9515eff8ccde2c0d - BTC: 0.0617, USD: $1,790.42
           [2025-08-01 18:02:15] 3f14c0d18a728a0b40694527cdaf770dd542274bee25746884d938c7b4a363f0 - BTC: 0.1580, USD: $4,582.11
           [2025-08-01 18:02:15] e70b2ed6c20188f781b4754eca46b464da1c85d3715aad59cc89501e562635d6 - BTC: 0.0649, USD: $1,881.02
           [2025-08-01 18:02:20] b1d7f03f38fa6f9df71820797d29b8966e7e220bcc1bdbf8cf9c61d1a2017dfb - BTC: 0.1119, USD: $3,245.38
           [2025-08-01 18:02:20] ad88f9421e5590c99d8db61dc28661ef93999b520f6c31c2d9ea2c3538757447 - BTC: 0.0760, USD: $2,203.46
           [2025-08-01 18:02:21] 31e668925a1e607936b28fc3f7fb1b36944d634734f60f8102ec664246054a1f - BTC: 0.1803, USD: $5,228.49
           [2025-08-01 18:02:21] 96076b507a0008b31c36800bf076aae6040b7e6410df7ed89a4511409ace2118 - BTC: 0.1094, USD: $3,171.92
           [2025-08-01 18:02:21] e9feceb5aee32866ca4fd699b47bcc6266e08c0dca3853efefd303904743042a - BTC: 0.0760, USD: $2,204.48
           [2025-08-01 18:02:24] 58788f9fb0945a851deb884f0674cd595d1b9f226ea32d140034b4a218dd0465 - BTC: 0.0480, USD: $1,393.12
           [2025-08-01 18:02:24] 93d8fd1ed537424783059677d0df2cf0f1f88a67bf1ca6362787af5709419f26 - BTC: 0.0515, USD: $1,493.66
           [2025-08-01 18:02:25] 150cd246638ffb1a047f4f243701462c49dd10f980728a9f759241c5696bc080 - BTC: 0.0598, USD: $1,733.54
           [2025-08-01 18:02:25] 98af9881453dd93ae69138ea79c5161cd50234bb758abe07ea5c0fb38590a1b2 - BTC: 0.0596, USD: $1,727.66
<img src ="https://github.com/user-attachments/assets/4b10acee-70ec-46bc-97e8-b3ae9745b0b2" alt ="[terminal3_BTC_tracker below pricemarker]" size ="800" />

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
₿
  STEP-BY-STEP: LINUX
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Set up a <B>Virtual Environment</B> for the Bot
  This is normal on Linux (or Debian-based distros with strict Python environments).
  You'll run into <code>Python’s PEP 668</code> restriction, 
  which prevents you from installing packages system-wide using pip3 to avoid breaking your OS-installed Python packages.

  Step 1: Create a Folder for Your Project
  If you haven’t already:


Run:
<code>

    mkdir -p ~/btc_tracker
    cd ~/btc_tracker
</code>
₿
  Step 2: Create the Virtual Environment
  
Run:
<code>

    python3 -m venv btc-env
</code>  
  This creates a folder btc-env/ inside your project that contains an isolated Python environment.
  
₿
  Step 3: Activate the Environment
  <code>
  
    source btc-env/bin/activate
  </code>
  If successful, your terminal will now look something like:
  <code>
    
    (btc-env) username@kali:~/btc_tracker$
  </code>
  This means you’re inside the virtual environment.

₿
  Step 4: Install websocket-client
  While the virtual environment is active, install the required library:
  <code>
  
    pip install websocket-client
  </code>
  This installs the package only inside your virtual environment — not system-wide.

  Step 4.1: Install websocket-client
  install requests:
  <code>
  
    pip install requests
  </code>

₿
  Step 5: Run the Bot
  Still inside the virtual environment, start it with:
  <code>
  
    python btc_tracker.py above 500
  </code>
  You should now see:
  
 <img src ="https://github.com/user-attachments/assets/eab4f0de-212b-4ef2-8072-550cb6062bd1" alt ="[terminal4_BTC_tracker above pricemarker]" size ="800" />

₿ Stop the bot from running
  <code>
       CTRL + C
  </code>
 
₿ Exit virtual environment
  <code>
       deactivate
  </code>
       
  Re-activate it later

  <code>
       
       source ~/btc_tracker/btc-env/bin/activate
  </code>
       
  List installed packages	
  
  <code>

        pip list 
  </code>
        
  Check Python used
  <code>
        
        which python (should point inside btc-env)
  </code>
  
Run the Bot With a Custom Limit

Activate your virtual environment first:

<code>
    
    source ~/btc_tracker/btc-env/bin/activate
</code>

Run the bot with a custom price limit (in USD):

<code>
  
    python btc_tracker.py above 5000
</code>

That will only log BTC transactions worth more than $5000.

If You Don’t Pass a Value

  If you run:
<code>

    python btc_tracker.py
</code>

…it will default to $1000.

 View the Logs

After it's been running a while:

Open high_value_btc_tx.log in a text editor to see the stored transactions.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
₿
  STEP-BY-STEP: WINDOWS
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 1: Install Python (if not already installed)

           Download from python.org

           During install → make sure to check ✅ “Add Python to PATH”

Open Windows Terminal / PowerShell

Navigate to your bot folder

           <code>
           cd C:\Users\<YourName>\Desktop\btc_tracker
           </code>
  
Step 2: Install dependencies (Only needed once)
<code>

           pip install requests websocket-client
</code>

Step 3: Run it
<code>
           
           python btc_tracker.py above 1000
</code>

₿ Close the Websocket 

<code>
           
          CTRL + C 

</code>
