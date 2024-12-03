import subprocess

# Função para conversão de áudio usando ffmpeg diretamente
def convert_with_ffmpeg(input_file, output_file, codec='mp3', vbr=True, bitrate='320k'):
    # Comando básico do ffmpeg
    command = ['ffmpeg', '-i', input_file, '-vn']  # '-vn' desativa a parte de vídeo
    
    # Se for VBR, ajusta os parâmetros
    if vbr:
        if codec == 'mp3':
            command.extend(['-q:a', '0'])  # Qualidade máxima para MP3 VBR
        elif codec == 'aac':
            command.extend(['-vbr', '5'])  # VBR para AAC
    
    # Adiciona o codec e a taxa de bits
    command.extend([output_file, '-b:a', bitrate])
    
    # Executa o comando usando subprocess
    subprocess.run(command)
    print(f"Arquivo convertido e salvo em {output_file}")

# Exemplo de uso
input_audio = 'A Ele.aac'  # Substitua com o caminho para seu arquivo de entrada
output_audio_mp3 = 'A Ele.mp3'  # Substitua com o caminho de saída desejado
convert_with_ffmpeg(input_audio, output_audio_mp3, codec='mp3', vbr=True, bitrate='320k')
    