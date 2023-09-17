import face_recognition
from FaceCapture import uk
from LoadDataEncodeFace import stud, student_encod, n


def identify_student(photo):
    try:
        # Se capturează încodarea pentru fotografia dată
        uk_encode = face_recognition.face_encodings(photo)[0]
    except IndexError as e:
        print(e)
        sys.exit(1)

    # Se compară încodările fețelor studenților cu încodarea feței din fotografie
    found = face_recognition.compare_faces(student_encod, uk_encode, tolerance=0.5)
    print(found)

    index = -1
    for i in range(n):
        # Se caută indexul primului student găsit
        if found[i]:
            index = i
    return index


stud_index = identify_student(uk)
