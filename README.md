### In order to start prototype you need to install **docker** and **docker-compose** first.
Inside of project directory run: </br>
```sudo docker-compose up --build -d```
In order to download ollama and python binaries, and start fastapi server.</br>
After that run:
```sudo docker exec ollama ollama create money-llama3 -f /app/models/Modelfile```</br>
To create llama3 model with applyed changes for this app.
### After all set and done you should be able to access app on your machine IP address
```http://your.machine.ip.address:10000/docs```
