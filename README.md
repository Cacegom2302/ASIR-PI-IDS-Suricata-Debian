# ASIR-PI-IDS-T-Pot-Debian

**Proyecto Integrado ASIR**  
**Instalación y administración de IDS Suricata + Honeypot T-Pot en Debian 13,junto a un servidor WEB y demostracion de ataque al entorno**

## Objetivo del proyecto
Desplegar un sistema completo de detección de intrusiones (Suricata) y honeypot (T-Pot) en Debian 13 para monitorizar y analizar ataques en una red.
Realizar ataque de prueba hacia el IDS y probar la efectividad de las alertas y los bloqueos.

## Tecnologías utilizadas
- Debian 13 (Trixie)
- Suricata (IDS)
- T-Pot 24.04 (Honeypot framework con Docker)
- Nginx (Servidor Web)
- HAProxy (balanceador de carga)
- Telegram e email (Servicio de mensajeria de alerta)
- Python / Bash (scripts de alertas)
- VirtualBox

## Estructura del repositorio
- `/config/suricata` → Reglas y configuración de Suricata  
- `/config/tpot`     → Archivos de configuración de T-Pot  
- `/scripts`         → Scripts de alertas y automatización  
- `/capturas`        → Pantallazos de pruebas y dashboard  
- `/docs`            → Documentación técnica  
- `/memoria`         → Propuesta PI y memoria final

## Cómo probar el proyecto
1. Arrancar la VM con Debian 13
2. Acceder al dashboard de T-Pot: `https://IP-DE-LA-VM:64297`
3. Ejecutar pruebas con Nmap desde otro equipo
4. Atacar al servidor
5. Probar las alertas
6. Probar la redundancia del Haproxy 

**Estado actual**: En preparacion
