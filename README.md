# ASIR-PI-IDS-Suricata-Debian
**Proyecto Integrado ASIR**  
**Instalación y administración de IDS Suricata en Debian 13, junto a un servidor WEB con alta disponibilidad y demostración de ataque al entorno**

## Objetivo del proyecto
Desplegar un sistema completo de detección y prevención de intrusiones (Suricata + Fail2ban) en Debian 13 para monitorizar y analizar ataques en una red.  
Configurar alta disponibilidad con HAProxy y un servidor secundario de respaldo.  
Realizar ataques de prueba hacia el IDS y probar la efectividad de las alertas y los bloqueos automáticos.

## Tecnologías utilizadas
- Debian 13 (Trixie)
- Suricata 7.0.10 (IDS/IPS)
- Fail2ban (bloqueo automático de IPs)
- Nginx (Servidor Web principal y secundario)
- HAProxy (balanceador de carga con failover)
- Telegram e Email (alertas en tiempo real)
- Python / Bash (scripts de alertas)
- UFW + iptables (cortafuegos)
- VirtualBox

## Estructura del repositorio
- `/Presentacion`        → Presentación del proyecto
- `/capturas`            → Pantallazos de pruebas y funcionamiento
- `/config/suricata`     → Reglas y configuración de Suricata
- `/config/haproxy`      → Configuración de HAProxy
- `/config/fail2ban`     → Configuración de Fail2ban y filtro para Suricata
- `/config/nginx`        → Páginas web del servidor principal y secundario
- `/config/systemd`      → Servicio de arranque automático de alertas
- `/scripts`             → Scripts de alertas (Telegram + Email)
- `/documentacion`       → Memoria final del proyecto

## Cómo probar el proyecto
1. Arrancar las dos VMs con Debian 13
2. Acceder a la web: `http://IP-DE-LA-VM:8080`
3. Ejecutar pruebas con Nmap desde otro equipo
4. Atacar al servidor (SQL Injection, XSS, fuerza bruta SSH)
5. Comprobar las alertas en Telegram y Email
6. Probar la redundancia de HAProxy parando Nginx en el servidor principal
7. Comprobar el bloqueo automático de IPs con Fail2ban

**Estado actual**: Completado
