import json

file_name = input('file name: ')

with open(f'{file_name}', encoding='utf-8') as f:
    line = f.readline()
    ri = line.rfind('}')
    line = line[:ri+1]
    data = json.loads(line)

    for track in data['tracks']:
        track['mainRef']['database']['name'] = ''
        track['mainRef']['database']['language'] = ''
        track['mainRef']['database']['phoneset'] = ''
        track['mainRef']['database']['languageOverride'] = ''
        track['mainRef']['database']['phonesetOverride'] = ''
        track['mainRef']['database']['backendType'] = ''

    with open(f'new_{file_name}', 'w', encoding='utf-8') as nf:
        json.dump(data, nf)

