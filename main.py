from pydub import AudioSegment

def convert_audio(input_file, output_file, codec='mp3', bitrate='192k', vbr=True):
    # Carrega o arquivo de áudio
    audio = AudioSegment.from_file(input_file)
    
    # Se for para VBR, vamos usar o parâmetro '-q:a' do ffmpeg, que controla a qualidade (usado para MP3 e AAC)
    ffmpeg_options = {}
    if vbr:
        if codec == 'mp3':
            ffmpeg_options = {'format': 'mp3', 'codec': 'libmp3lame', 'audio_bitrate': bitrate, 'extra_args': ['-q:a', '0']}
        elif codec == 'aac':
            ffmpeg_options = {'format': 'aac', 'codec': 'libfdk_aac', 'audio_bitrate': bitrate, 'extra_args': ['-vbr', '5']}
    else:
        ffmpeg_options = {'format': codec, 'codec': codec, 'audio_bitrate': bitrate}
    
    # Salva o arquivo de áudio convertido
    audio.export(output_file, format=codec, **ffmpeg_options)

# Exemplo de uso
input_audio = 'entrada.wav'
output_audio_mp3 = 'saida.mp3'
convert_audio(input_audio, output_audio_mp3, codec='mp3', bitrate='192k', vbr=True)
