FROM Ubuntu 
CMD sleep 5
# Chamando: docker run ubuntu-sleepist sleep 10
# Vai executar: sleep 10

FROM Ubuntu
ENTRYPOINT ["sleep"]
# Chamando: docker run ubuntu-sleepist 10
# Vai executar: sleep 10

FROM Ubuntu
ENTRYPOINT ["sleep"]
CMD ["5"]
# Chamando: docker run ubuntu-sleepist 10
# Vai executar: sleep 10

# Chamando: docker run --entrypoint dormir ubuntu-sleepist 10
# Vai executar: dormir 10