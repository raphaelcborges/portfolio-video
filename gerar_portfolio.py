import yt_dlp

# URL da sua Playlist
playlist_url = 'https://www.youtube.com/playlist?list=PL29u2IywMvuDCeD_XnNlSxGL6XQbRSkN6'

def gerar_html_da_playlist(url):
    ydl_opts = {
        'extract_flat': True,  # Não baixa o vídeo, só pega os dados (rápido)
        'quiet': True,
        'ignoreerrors': True,
    }

    print("🔍 Lendo playlist... (isso pode demorar uns segundos)")
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        
        if 'entries' in info:
            print("\n--- COPIE O CÓDIGO ABAIXO PARA SEU INDEX.HTML ---\n")
            
            for video in info['entries']:
                video_title = video.get('title', 'Título Desconhecido')
                video_id = video.get('id')
                
                # Template HTML para cada vídeo
                html_block = f"""
                <div class="video-card">
                    <div class="video-wrapper">
                        <iframe src="https://www.youtube.com/embed/{video_id}" title="{video_title}" frameborder="0" allowfullscreen></iframe>
                    </div>
                    <h3>{video_title}</h3>
                    <p>Edição e Finalização.</p>
                </div>"""
                
                print(html_block)
                print("-" * 20)
        else:
            print("❌ Nenhuma entrada encontrada.")

if __name__ == "__main__":
    gerar_html_da_playlist(playlist_url)