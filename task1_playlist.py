#Шаг 1
playlist = []
playlist.append("Утро")
playlist.append("Дорога")
playlist.append("Тренировка")
print(playlist)

#Шаг 2
print(len(playlist))
print(playlist[0], playlist[-1])
print(playlist[0:2])
print("Дорога" in playlist)

#Шаг 3
playlist[1] = 'Дорога домой'
playlist.insert(0, "Интро")
playlist.insert(len(playlist), "Финал")
skipped = playlist[-1]
playlist.pop(-1)
playlist.remove("Утро")
print(f"{playlist} | пропустили: {skipped}")

#Шаг 4

# for i in playlist:
#     print(i + 1, i)

#Нельзя складывать строку с целым числом

for index,track in enumerate(playlist, start=1):
    print(f"{index}. {track}")

#Шаг 5

tracks = [("Интро", 95), ("Дорога домой", 214), ("Тренировка", 187), ("Финал", 241)]
print(tracks[0],type(tracks[0]))
title = tracks[0][0]
seconds = tracks[0][1]
print(title, seconds)

#Кортеж - неизменяемый тип данных,нельзя использовать first[1] = 100
#Шаг 6
total_seconds = 0
for track in tracks:
    total_seconds += track[1]

minutes,seconds = divmod(total_seconds, 60)
long_playlist = f"{minutes:02d}:{seconds:02d}"
print(f"Всего:{minutes:02d}:{seconds:02d}")

#Шаг 7
small_track = []
longest_track = tracks[0]
for track in tracks:
    if track[1] > longest_track[1]:
        longest_track = track
    if track[1] < 200:
        small_track.append(track[0])
print(f"самый длинный:{longest_track[0]},{longest_track[1]} сек")
print(f"Короче 200 секунд:{small_track}")

#Шаг 8
itog_title = f"🎧 Плейлист:{len(tracks)} трека. {long_playlist}" #Переменная заранее для 10 шага
names = ["Тренировка", "Интро", "Финал", "Дорога домой"]
print(sorted(names))
print(names)
result = names.sort()
print(result, names)
print(sorted(names, reverse = True)[0:2])

#Шаг 9

queue = playlist
queue.append("Бонус")
print(playlist)
playlist_backup = playlist.copy()
playlist_backup.append("Еще один")
print(len(playlist), len(playlist_backup))
print(queue is playlist, playlist_backup is playlist)

#Метод copy() создает новую ячейку памяти,а queue обращается к уже созданной

#Шаг 10
itog = [itog_title]
for index, track in enumerate(tracks, start = 1):
    m, s = divmod(track[1], 60)
    itog.append(f"{index}. {track[0]} - {m}:{s:02d}")

print("\n".join(itog))
