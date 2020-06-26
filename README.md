# python-directory-sync-example
An example Flask app demonstrating Directory Sync with the [WorkOS Python SDK](https://github.com/workos-inc/workos-python).

## Setup
1. Clone the repo and install the dependencies by running the following:
    ```bash
    git clone https://github.com/workos-inc/python-directory-sync-example.git
    pip install -r requirements.txt
    ```

1. The example app looks for the following environment variables:
    - WORKOS_API_KEY - The WorkOS API key can be found [here](https://dashboard.workos.com/api-keys).
    - SCIM_ENDPOINT_ID - The SCIM endpoint ID for a directory. This can be retrieved from URL in the WorkOS dashboard.

## Running the app
Use the following command to run the app:
```bash
flask run
```

Once running, navigate to:
    - `http://localhost:5000/users` - Displays a list of all provisioned users.
    - `http://localhost:5000/groups` - Displays a list of all directory groups.
