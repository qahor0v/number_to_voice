from moviepy.editor import concatenate_audioclips, AudioFileClip, AudioClip
from moviepy.video.fx.speedx import speedx


v1 = AudioFileClip('1.mp3')
v2 = AudioFileClip('2.mp3')
v3 = AudioFileClip('3.mp3')
v4 = AudioFileClip('4.mp3')
v5 = AudioFileClip('5.mp3')
v6 = AudioFileClip('6.mp3')
v7 = AudioFileClip('7.mp3')
v8 = AudioFileClip('8.mp3')
v9 = AudioFileClip('9.mp3')
v10 = AudioFileClip('10.mp3')
v20 = AudioFileClip('20.mp3')
v30 = AudioFileClip('30.mp3')
v40 = AudioFileClip('40.mp3')
v50 = AudioFileClip('50.mp3')
v60 = AudioFileClip('60.mp3')
v70 = AudioFileClip('70.mp3')
v80 = AudioFileClip('80.mp3')
v90 = AudioFileClip('90.mp3')
v100 = AudioFileClip('100.mp3')
v1000 = AudioFileClip('1000.mp3')
v_mln =  AudioFileClip('mln.mp3')


n = int(input("Enter number: "))
son = []
lst = [v1,v1, v2, v3, v4, v5, v6, v7, v8, v9]
lst2 = [v1,v10, v20, v30, v40, v50, v60, v70, v80, v90]
lst3 = [v100, v1000, v_mln]
if n == 0:
    print("nol")
else:
    # bir
    if n % 10 != 0:
        son.insert(0, lst[n % 10])
    n //= 10
        # o'n
    if n % 10 != 0:
            son.insert(0, lst2[n % 10])
    n //= 10
        # yuzø
    if n % 10 != 0:
            son.insert(0, lst3[0])
            son.insert(0, lst[n % 10])
    n //= 10
        # ming
    if n % 10 != 0:
            son.insert(0, lst3[1])
            son.insert(0, lst[n % 10])
    n //= 10
        # 10 ming
    if n % 10 != 0:
            son.insert(0, lst2[n % 10])
    n //= 10
        # 100 ming
    if n % 10 != 0:
            son.insert(0, lst3[0])
            son.insert(0, lst[n % 10])
    n //= 10
        # million
    if n % 10 != 0:
            son.insert(0, lst3[2])
            son.insert(0, lst[n % 10])
    n //= 10
        # 10 million
    if n % 10 != 0:
            son.insert(0, lst2[n % 10])
    n //= 10
        # 100 million
    if n % 10 != 0:
            son.insert(0, lst3[0])
            son.insert(0, lst[n % 10])
res = concatenate_audioclips(son)

audio_fast = speedx(res, factor=1.5)

audio_fast.write_audiofile("result.mp3")

print("Completed")











