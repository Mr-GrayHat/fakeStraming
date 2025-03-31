# 🎵 Music Trends Player (Fake Streaming)

¡Una aplicación que muestra tendencias musicales de YouTube con un reproductor "especial"! Proyecto educativo con fines humorísticos.


## 🌟 Características
- Lista de videos musicales populares de YouTube
- Interfaz estilo Spotify
- Efectos visuales "especiales"
- "Reproductor" simulado con sorpresa incluida

## 🛠 Requisitos
- Python 3.9+
- Pip
- Cuenta de Google Cloud (para API Key de YouTube)
- Git
- Railway CLI (para despliegue)

## 🚀 Ejecución local

### 1. Clonar repositorio

git clone https://github.com/tu-usuario/music-trends-player.git
cd music-trends-player


## 2. Configurar entorno virtual
python -m venv .venv
source .venv/bin/activate  ( Linux/Mac)

.venv\Scripts\activate  (Windows)

## 3. Instalar dependencias
pip install -r requirements.txt

## 4. Obtener API Key de YouTube
Ve a Google Cloud Console
https://developers.google.com/youtube/v3/getting-started?hl=es-419
- Crea un proyecto y activa YouTube Data API v3
- Genera una API Key en "APIs & Services > Credentials"
- Reemplaza YOUTUBE_API_KEY en app.py con tu clave

## 5. Ejecutar la aplicación

 python app.py 
 Visita http://localhost:5000
![image](https://github.com/user-attachments/assets/fec5197a-6c28-47ec-8327-6ed1bdf6a760)



## Despliegue en Railway
1. Instalar Railway CLI
npm install -g @railway/cli
2. Autenticación
railway login
3. Crear proyecto
railway init
4. Enlazar proyecto
railway link
6. Desplegar
railway up

### Asi se vera tu proyecto una vez despligado en https://railway.com/
![image](https://github.com/user-attachments/assets/77d41874-c41e-4125-b1e5-c67330b0ccc3)
![image](https://github.com/user-attachments/assets/38934652-62c3-4673-8669-3eb4fac41680)
![image](https://github.com/user-attachments/assets/3d1876f5-727f-4035-b6f5-dcf4c423c17a)




## ⚠️ Importante
La API Key incluida (AIzaSyD-Ql8AppLBZNjFKLiDD1DUHuJ95-mgMrw) es de ejemplo
El reproductor NO funciona realmente - ¡es parte de la broma!
Para uso prolongado, crear tu propia API Key de YouTube

## 🎭 ¿Cómo funciona?
Muestra tendencias musicales reales usando YouTube API

Al intentar reproducir:
Primera vez: Video sorpresa + efectos locos
Siguientes veces: Simulación de reproducción
Los controles del reproductor son decorativos
![image](https://github.com/user-attachments/assets/8a608467-16b5-431f-8caa-838ce91db945)
![image](https://github.com/user-attachments/assets/fe43e1d6-22d7-43c4-9bef-e3f47054d793)





## 📂 Estructura del proyecto
.
├── app.py              (Backend Flask)

├── templates

│   └── index.html     (Frontend principal)

├── requirements.txt   (Dependencias)

└── nixpacks.toml      ( Configuración de despliegue)




![image](https://github.com/user-attachments/assets/7d461c19-30f2-46f6-acc1-76646b92c8b0)



