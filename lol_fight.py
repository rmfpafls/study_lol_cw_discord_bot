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
        if '-' in participant:
            name, tier = participant.split('-')
            # 점수로 변환
            score = tier_scores.get(tier, 0)
            # 딕셔너리에 추가
            participant_scores[name] = score

    return participant_scores


def sort_and_split_teams(participant_scores):
    # 점수에 따라 참여자들을 오름차순으로 정렬
    sorted_participants = sorted(participant_scores.items(), key=lambda item: item[1], reverse=True)

    blue_team = {}
    red_team = {}

    n = len(sorted_participants)

    # 팀 배정
    for i, (name, score) in enumerate(sorted_participants):
        if i % 2 == 0:  # 짝수 인덱스 (0, 2, 4, ...)는 블루팀
            blue_team[name] = score
        else:  # 홀수 인덱스 (1, 3, 5, ...)는 레드팀
            red_team[name] = score

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