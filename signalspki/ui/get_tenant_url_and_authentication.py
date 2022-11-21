## Import libraries and functions
import tkinter


### TENANT URL
## UI functions to get Tenant URL
def get_tenant_url_window():
    master = tkinter.Tk()
    master.geometry('800x100')
    master.title('Tenant URL')
    master.resizable(False,False)
    selection_label = tkinter.Label(master)
    selection_label.config(text='Insert the tenant URL')
    selection_label.pack()
    tentant_url_entry = tkinter.Entry(master, width=700)
    tentant_url_entry.pack()
    tentant_url_entry.focus_set()
    tentant_url_entry_button = tkinter.Button(master, text="Submit", width=10, command=lambda: get_tenant_url_from_ui(master, tentant_url_entry))
    tentant_url_entry_button.pack()
    master.mainloop()

def get_tenant_url_from_ui(ui: tkinter.Tk, tentant_url_entry: tkinter.Entry):
    global tenant_url
    tenant_url = tentant_url_entry.get()
    #print(tenant_url)
    ui.destroy()


### RADIOBUTTONS 
## UI function to get the authentication type
def get_authentication_type_radiobuttons():
    master = tkinter.Tk()
    master.geometry('350x120')
    master.title('Authentication method')
    master.resizable(False,False)
    auth_type = tkinter.StringVar(None)
    auth_type.set(None)
    selection_label = tkinter.Label(master)
    selection_label.config(text = 'Select the authentication method')
    selection_label.pack()
    basic_radiobutton = tkinter.Radiobutton(master, text='Basic', variable=auth_type, value='basic', command=lambda: get_authentication_type_from_ui(master, auth_type), state='disabled')
    basic_radiobutton.pack(anchor=tkinter.W)
    api_radiobutton = tkinter.Radiobutton(master, text='API key', variable=auth_type, value='api-key', command=lambda: get_authentication_type_from_ui(master, auth_type), state='normal')
    api_radiobutton.pack(anchor=tkinter.W)
    token_radiobutton = tkinter.Radiobutton(master, text='Bearer token', variable=auth_type, value='bearer-token', command=lambda: get_authentication_type_from_ui(master, auth_type), state='disabled')
    token_radiobutton.pack(anchor=tkinter.W)
    cookie_radiobutton = tkinter.Radiobutton(master, text='Core session cookie', variable=auth_type, value='core-session-cookie', command=lambda: get_authentication_type_from_ui(master, auth_type), state='normal')
    cookie_radiobutton.pack(anchor=tkinter.W)
    master.mainloop()

def get_authentication_type_from_ui(ui: tkinter.Tk, auth_type: tkinter.StringVar):
    global tenant_authentication_type
    tenant_authentication_type = str(auth_type.get())
    ui.destroy()
    #print('Using authentication type: ' + signals_inventa_authentication_type)
    #return(signals_inventa_authentication_type)


### API-KEY
## UI functions to get API key
def get_api_key_window():
    master = tkinter.Tk()
    master.geometry('800x100')
    master.title('API key')
    master.resizable(False,False)
    selection_label = tkinter.Label(master)
    selection_label.config(text='Insert the API key')
    selection_label.pack()
    api_key_entry = tkinter.Entry(master, width=700)
    api_key_entry.pack()
    api_key_entry.focus_set()
    api_key_entry_button = tkinter.Button(master, text="Submit", width=10, command=lambda: get_api_key_from_ui(master, api_key_entry))
    api_key_entry_button.pack()
    master.mainloop()

def get_api_key_from_ui(ui: tkinter.Tk, api_key_entry: tkinter.Entry):
    global tenant_api_key
    tenant_api_key = api_key_entry.get()
    #print(api_key)
    ui.destroy()


### CORE SESSION COOKIE
## UI functions to get CORE_SESSION cookie
def get_core_session_cookie_id_window():
    master = tkinter.Tk()
    master.geometry('800x100')
    master.title('Core Session Cookie')
    master.resizable(False,False)
    selection_label = tkinter.Label(master)
    selection_label.config(text='Insert the Core Session Cookie ID')
    selection_label.pack()
    core_session_cookie_id_entry = tkinter.Entry(master, width=700)
    core_session_cookie_id_entry.pack()
    core_session_cookie_id_entry.focus_set()
    core_session_cookie_id_entry_button = tkinter.Button(master, text="Submit", width=10, command=lambda: get_core_session_cookie_id_from_ui(master, core_session_cookie_id_entry))
    core_session_cookie_id_entry_button.pack()
    master.mainloop()

def get_core_session_cookie_id_from_ui(ui: tkinter.Tk, core_session_cookie_id_entry: tkinter.Entry):
    global tenant_core_session_cookie_id
    tenant_core_session_cookie_id = core_session_cookie_id_entry.get()
    print(tenant_core_session_cookie_id)
    ui.destroy()


### BASIC AUTHENTICATION
## UI functions to get BASIC authentication (username/password)
def get_basic_auth_info_window():
    master = tkinter.Tk()
    master.geometry('800x100')
    master.title('Basic authentication')
    master.resizable(False,False)
    selection_label = tkinter.Label(master)
    selection_label.config(text='Insert the credentials for Signals Notebook')
    selection_label.pack()
    username_entry = tkinter.Entry(master, width=700)
    username_entry.pack()
    username_entry.focus_set()
    password_entry = tkinter.Entry(master, width=700, show="*")
    password_entry.pack()
    credentials_entry_button = tkinter.Button(master, text="Submit", width=10, command=lambda: get_basic_auth_info_from_ui(master, username_entry, password_entry))
    credentials_entry_button.pack()
    master.mainloop()

def get_basic_auth_info_from_ui(ui: tkinter.Tk, username_entry: tkinter.Entry, password_entry: tkinter.Entry):
    global username, password
    username = username_entry.get()
    password = password_entry.get()
    print(username + " - " + password)
    ui.destroy()


### GET AUTHENTICATION TYPE AND PARAMETERS
## Get tenant authentication
# Initialise variables
tenant_url = ''
tenant_authentication = {}
tenant_authentication_type = ''
tenant_authentication_parameters = {}
tenant_api_key = ''
tenant_core_session_cookie_id = ''
username = ''
password = ''
# Get tenant URL
get_tenant_url_window()
# Get the authentication type selector
get_authentication_type_radiobuttons()
# Get the authentication parameters
if tenant_authentication_type == 'api-key':
    get_api_key_window()
    tenant_authentication_parameters['api_key'] = tenant_api_key
elif tenant_authentication_type == 'bearer-token':
    pass
elif tenant_authentication_type == 'core-session-cookie':
    get_core_session_cookie_id_window()
    tenant_authentication_parameters['core_session_cookie_id'] = tenant_core_session_cookie_id
elif tenant_authentication_type == 'basic':
    get_basic_auth_info_window()
    tenant_authentication_parameters['username'] = username
    tenant_authentication_parameters['password'] = password
else:
    pass
# Fill in the parameters to be passed then to functions 
tenant_authentication = {'authentication_type': tenant_authentication_type, 'authentication_parameters': tenant_authentication_parameters}