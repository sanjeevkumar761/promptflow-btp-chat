cf login --sso
cf push

cf set-env promptflowchatapp AZURE_OPENAI_API_KEY <AOAI API Key>
cf set-env promptflowchatapp AZURE_OPENAI_API_BASE <AOAI API Base Endpoint>

cf restage promptflowchatapp

