import random

# 티어별 점수
tier_scores = {
    '챌': 31,
    '그마': 30,
    '마스터': 29,
    '다1': 28,
    '다2': 27,
    '다3': 26,
    '다4': 25,
    '에1': 24,
    '에2': 23,
    '에3': 22,
    '에4': 21,
    '플1': 20,
    '플2': 19,
    '플3': 18,
    '플4': 17,
    '골1': 16,
    '골2': 15,
    '골3': 14,
    '골4': 13,
    '실1': 12,
    '실2': 11,
    '실3': 10,
    '실4': 9,
    '브1': 8,
    '브2': 7,
    '브3': 6,
    '브4': 5,
    '아1': 4,
    '아2': 3,
    '아3': 2,
    '아4': 1,
}

def parse_input(input_str):
    # 입력 문자열을 공백과 쉼표로 분리하여 리스트로 변환
    participants = input_str.split(', ')

    # 점수를 저장할 딕셔너리
    participant_scores = {}

    for participant in participants:
            name, tier = participant.split('-')
            # 점수로 변환
            score = tier_scores.get(tier, 0)
            # 딕셔너리에 추가
            participant_scores[name] = score
    # print(participant_scores)
    # {'승재': 17, '찬일': 19, '진산': 18, '영훈': 9, '이건': 19, '준희': 14, '효중': 5, '재민': 11, '유빈': 5, '성우': 11}
    return participant_scores


def sort_and_split_teams(participant_scores):
    # 점수에 따라 참여자들을 내림순으로 정렬
    sorted_participant = {k: v for k, v in sorted(participant_scores.items(), key=lambda item: item[1])}
    # print(sorted_participant)
    #{'효중': 5, '유빈': 5, '영훈': 9, '재민': 11, '성우': 11, '준희': 14, '승재': 17, '진산': 18, '찬일': 19, '이건': 19}
    blue_team = {}
    red_team = {}

    # (1,10) (2,9) (3,7) (4,6) 5 5 로 나누기
    for i in range(4):



    # # 참가자 목록을 리스트로 변환
    # participants = list(sorted_participant.items())
    # # print(participants)
    # #[('효중', 5), ('유빈', 5), ('영훈', 9), ('재민', 11), ('성우', 11), ('준희', 14), ('승재', 17), ('진산', 18), ('찬일', 19), ('이건', 19)]
    #
    # # 위에서부터 5명은 블루-레드-블루-레드-블루
    # for i in range(5):
    #     if i % 2 == 0:
    #         blue_team[participants[i][0]] = participants[i][1]
    #     else:
    #         red_team[participants[i][0]] = participants[i][1]
    # print(blue_team, red_team)
    #
    # # 아래 5명은 레드-블루-레드-블루-레드
    # for i in range(5, 10):
    #     if i % 2 == 0:
    #         red_team[participants[i][0]] = participants[i][1]
    #     else:
    #         blue_team[participants[i][0]] = participants[i][1]

    print("블루팀:", blue_team)
    print("레드팀:", red_team)

    return blue_team, red_team


# 예시 입력
input_str = "승재-플4, 찬일-플2, 진산-플3, 영훈-실4, 이건-플2, 준희-골3, 효중-브4, 재민-실2, 유빈-브4, 성우-실2"

# 점수 계산
scores = parse_input(input_str)

# 팀 분할
blue_team, red_team = sort_and_split_teams(scores)

# 결과 출력
print("블루팀:")
for name, score in blue_team.items():
    print(f"{name}: {score}")

print("\n레드팀:")
for name, score in red_team.items():
    print(f"{name}: {score}")