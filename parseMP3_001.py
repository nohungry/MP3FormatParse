# import struct
#
# encodings = ["GBK", "UTF-16", "UTF-16BE", "UTF-8"]
#
# def parse_ID3V2_frames(frames_bin):
#     pointer = 0
#     frames_bin_size = len(frames_bin)
#     frames = {}
#     while pointer < frames_bin_size - 10:
#         frame_header_bin = frames_bin[pointer:pointer + 10]
#         frame_header = struct.unpack(">4sI2s", frame_header_bin)
#         frame_body_size = frame_header[1]
#         if frame_body_size == 0:
#             break
#         pointer += 10
#         frames[frame_header[0]] = frames_bin[pointer:pointer + frame_body_size]
#         pointer += frame_body_size
#     TIT2_bin = frames.get(b"TIT2", None)
#     TPE1_bin = frames.get(b"TPE1", None)
#     TALB_bin = frames.get(b"TALB", None)
#
#     if TALB_bin:
#         encoding = encodings[TALB_bin[0]]
#         frames[b"TALB"] = TALB_bin[1:].decode(encoding)
#
#     if TIT2_bin:
#         encoding = encodings[TIT2_bin[0]]
#         frames[b"TIT2"] = TIT2_bin[1:].decode(encoding)
#
#     if TPE1_bin:
#         encoding = encodings[TPE1_bin[0]]
#         frames[b"TPE1"] = TPE1_bin[1:].decode(encoding)
#
#     return frames
#
# def parse_ID3V2_head(head_bin):
#     if head_bin[:3] != b"ID3":
#         return None
#     frames_bin_size = (head_bin[6] << 21 | head_bin[7] << 14 | head_bin[8] << 7 | head_bin[9])
#
#     return frames_bin_size
#
# def read_mp3_tag_v2():
#     file = open("C:/Users/norman_cheng/Desktop/voice/spec_music/Wenzhou/music/G39_mu_lobby.mp3", "rb")
#     frames_bin_size = parse_ID3V2_head(file.read(10))
#     if frames_bin_size is None:
#         file.close()
#         return
#     frames_bin = file.read(frames_bin_size - 10)
#     file.close()
#     frames = parse_ID3V2_frames(frames_bin)
#     mp3Detail = {}
#     mp3Detail["title"] = frames[b"TIT2"]
#     mp3Detail["artist"] = frames[b"TPE1"]
#     mp3Detail["album"] = frames[b"TALB"]
#     print(mp3Detail)
#
# if __name__ == '__main__':
#     mp3detail = read_mp3_tag_v2()
#     print(mp3detail)