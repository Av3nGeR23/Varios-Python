from flask import Flask, request, render_template
import yt_dlp as youtube_dl
import os
import glob

app = Flask(__name__)

def download(url, path=None):
    if path is None:
        path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    
    # Para depuración: Imprimir la ruta de descarga
    print(f"Descargando en la ruta: {path}")
    
    ydl_opts = {
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'verbose': True,
        'noprogress': True,  # Deshabilitar barra de progreso
        'force_overwrite': True  # Sobrescribir archivos existentes
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            return f"Video descargado exitosamente en {path}"
        except Exception as e:
            return f"Error al descargar el video: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_youtube = request.form['url']
        path = request.form['path']
        if not path.strip():
            path = None
        message = download(url_youtube, path)
        return render_template('index.html', message=message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
