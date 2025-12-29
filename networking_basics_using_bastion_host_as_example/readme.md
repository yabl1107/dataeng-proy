## 🏗️ Arquitectura

La plantilla despliega los siguientes componentes dentro de una VPC personalizada:

### Red
* **1 Subred Pública:** Contiene un Bastion Host para acceso administrativo y un NAT Gateway.
* **2 Subredes Privadas:** Una para el servidor de aplicaciones y otra para la base de datos RDS.
* **Internet Gateway & NAT Gateway:** Permiten que las instancias privadas descarguen actualizaciones sin ser accesibles desde internet.

### Seguridad
* **Bastion SG:** Solo permite tráfico SSH a nuestra ip local **(Editar con propia IP)**.
* **Private SG:** Solo permite tráfico SSH proveniente exclusivamente del Bastion.
* **Postgres SG:** Solo permite conexiones en el puerto 5432 desde el Bastion.  

### Recursos
* **Instancias EC2:** Uso de imagen de Amazon Linux.
* **Base de Datos:** RDS PostgreSQL versión 16.