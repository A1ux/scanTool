# scanTool

## Escaneo

Se apoya de tools instaladas en la web 



## Funciones


- [ ] Guardar todo en una base de datos sqlite
- [ ] Automatizar lanzar scripts o tools ya sea indicando comandos o lanzandolos la propia aplicacion
- [ ] Indicar si el objetivo donde se realiza el ataque es un windows o linux
- [ ] Para HTTP y HTTPS fusionar con eyewithness
- [x]

### Funciones faltantes a agregar

- [ ] Parsear las salidas de smb (message signing enable but no required)
- [ ] Testear puertos snmp con public y private

## Argumentos

-os objetivo linux o windows
-c crear la db sqlite
-f importar los datos a la sqlite de un solo archivo
-d importar los datos de un directorio
-d nombre de base de datos
-o Salidas para enviar comandos .bat o .sh
-op Salida por partes (supongamos 4 comandos)
-launch lanza los ataques el propio script

## Binarios

- snmpwalk.exe
- sslscan.exe
- eyewithness.exe


```bash
nmap --min-rate 4500 --max-rtt-timeout 1500ms -p- --open IP
No recomendado
nmap -sS -n -Pn -p- --max-rtt-timeout 100ms --min-parallelism 1000 10.10.10.182


default-http-login-hunter.sh urls.txt
```