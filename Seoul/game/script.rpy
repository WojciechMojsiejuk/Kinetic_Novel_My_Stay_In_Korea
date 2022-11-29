# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define w = Character('보이치에흐', color="#c8ffc8")

# 여기에서부터 게임이 시작합니다.
label start:
    scene flight
    voice "/audio/1.ogg"
    "8월 25일..."
    voice "/audio/2.ogg"
    "...오늘 나는 한국에가요..."

    scene near campus 01

    show wojtek  at right with moveinright
    voice "/audio/3.ogg"
    w "내 이름은 보이치에흐. 나는 25살여요"

    scene near campus 02
    show wojtek  at right with moveinright
    voice "/audio/4.ogg"
    w "나는 폴란드사람 입니다. 지금은 핀란드에서 공부해요."

    scene near campus 03
    show wojtek happy at right with moveinright
    voice "/audio/5.ogg"
    w "나는 서울테크를교환학생입니다.반가워요."

    show wojtek smile at offscreenleft with easeoutleft
    voice "/audio/6.ogg"
    w "대학에 가자!"

    scene seoultech gate with slideawayleft

    show wojtek smile at left with moveinleft
    voice "/audio/7.ogg"
    w "이거가 내 대학교"

    show wojtek smile at offscreenright with easeoutright

    scene seoultech fountains with dissolve
    show wojtek smile at left with moveinleft
    voice "/audio/8.ogg"
    w "서울테크의캠퍼스예뻐요"

    scene seoultech park with dissolve
    show wojtek smile at left with moveinleft
    voice "/audio/9.ogg"
    w "기숙사 가자!"

    show wojtek smile at offscreenleft with moveoutleft

    scene dormitory with slideawayleft
    voice "/audio/10.ogg"
    w "기숙사를커요!"

    scene room with slideawayleft
    voice "/audio/11.ogg"
    w "이거가 내 기숙사방"

    scene food 02 with slideawayleft
    
    show wojtek smile at left with moveinleft

    voice "/audio/12.ogg"
    w "한국 음식은 너무 맛있어요."
    

    scene food 03 with slideawayleft
    show wojtek smile at left with moveinleft
    # voice "/audio/13.ogg"
    w "내 친구들은 삼겹살을 먹어요."
    voice "/audio/14.ogg"
    w "나는냉면을 먹어요. 배불러요."
    voice "/audio/15.ogg"
    w "나는고기를안먹어요."

    show wojtek sad at left 
    voice "/audio/16.ogg"
    w "채식가한국에서어려워요."

    scene food 01 with slideawayleft
    show wojtek smile at left with moveinleft
    voice "/audio/17.ogg"
    w "한국음식은도매워요."
    voice "/audio/18.ogg"
    w "김치찌개더주세요~!"
 
    scene seoultech autumn with slideawayleft

    show wojtek smile at left with moveinleft
    voice "/audio/19.ogg"
    w "날씨가 좋아요."
    w "서울 도심을 방문합시다!"

    show wojtek smile at offscreenleft with moveoutleft

    scene palace with slideawayleft
    show wojtek smile at left with moveinleft
    w "이거가 창경궁에요.창경궁은아름다워요.이 공원을 좋아요. " 
    
    show wojtek smile at offscreenleft with moveoutleft

    scene king with slideawayleft
    show wojtek smile at left with moveinleft

    "이거가세종국왕에요. 그는 한글을 만들었어요. 한글은 배우기 쉬워요."

    scene palace night with slideawayleft
    show wojtek smile at left with moveinleft
    w "이거가 경복궁에요. 유명해요."

    scene ntower with slideawayleft
    show wojtek smile at left with moveinleft
    w "이거가 N 서울타워여요. 너무커요."

    scene temple with slideawayleft
    show wojtek smile at left with moveinleft
    w "이거가무덤에요."

    scene temple 02 with slideawayleft
    show wojtek smile at left with moveinleft
    w "이거가불교 사원에요."

    scene busan 01 with slideawayleft
    show wojtek smile at left with moveinleft

    w "나는 여행을 좋아요. 부산과 제주도를에갔어요."
    
    scene busan 02 with slideawayleft
    scene busan 03 with slideawayleft
    w "나는 더 여행하고싶에요"
    scene busan 04 with slideawayleft
    scene busan 05 with slideawayleft
    w "하지만공부해야 해요, 바빠요..."
    scene busan 06 with slideawayleft
    scene busan 07 with slideawayleft
    w "한국 학생들은 항상 도서관에서 매우 열심히 공부해요."
    scene busan 08 with slideawayleft
    scene busan 09 with slideawayleft

    scene jeju hello with slideawayleft
    show wojtek smile at left with moveinleft
    w "시험들은 어려워요.싫어"
    scene jeju cave with slideawayleft
    scene jeju 02 with slideawayleft
    w "그건나의 한국 체류"
    scene jeju 03 with slideawayleft
    show wojtek happy at left with moveinleft
    w "감사합니다!"
    show wojtek smile at offscreenleft with moveoutleft
    return
