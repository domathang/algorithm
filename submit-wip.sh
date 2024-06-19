#!/bin/bash

###############################################################################
# 데일리 과제 제출용 스크립트
#
# - 사용법
# 1. 본 스크립트를 임의의 파일로 저장합니다. 예) submit.sh
# 2. 사전 입력값을 사용자의 정보로 변경합니다.
# 3. 인수와 함께 스크립트를 실행합니다.
#    ```
#    bash <파일명>.sh <일차>-<문제 번호> <제출할 코드가 있는 파일 경로>
#    예) bash submit.sh 13-5 ./hh99/day13/5.py
#    ```
###############################################################################

###############################################################################
# 사전 입력값 - 변경 필수
###############################################################################
NAME="곽도현"            # 필수: 이름
TEAM_NUMBER=16        # 필수: 팀 번호 (1 ~ 16)
LANG_EXTENSION="py"   # 필수: 언어 확장자 ("py" 또는 "java")
GITHUB_OR_BLOG_URL="" # 선택: github 또는 블로그 URL

###############################################################################
# 설문지 URL 및 항목별 식별자
###############################################################################
FORM_URL="https://docs.google.com/forms/d/e\
/1FAIpQLSdhZ9MWuN6eiZorKGpu4pC9Z1Q-MQ_yYKxDyYJIOLYa-pNrqQ\
/formResponse"                             # 3주차 데일리 과제 제출 링크
NAME_FIELD="entry.770271090"               # 이름
TEAM_NUMBER_FIELD="entry.1417983599"       # 팀 번호
SOLVED_PROBLEM_FIELD="entry.586548838"     # 해결한 문제
RAW_CODE_FIELD="entry.420774658"           # 코드
GITHUB_OR_BLOG_URL_FIELD="entry.649430918" # github 또는 블로그 URL

###############################################################################
# 검증용 정규표현식
###############################################################################
TEAM_NUMBER_RANGE_REGEX="^([1-9]|1[0-6])$" # 1 ~ 16: 팀 번호 범위
DAY_RANGE_REGEX="([1-9]|1[0-5])"           # 1 ~ 15: 일차 범위
PROBLEM_NUMBER_REGEX="([1-9]|1[0-2])"      # 1 ~ 12: 문제 번호 범위
FILE_EXT_REGEX="^(py|java)$"               # py 또는 java: 언어별 확장자

###############################################################################
# 사전 입력값 검증
###############################################################################
if [[ ! "${NAME}" ]]; then
	echo "Error: 이름을 입력해 주세요."
	exit 1
fi

if [[ ! "${TEAM_NUMBER}" =~ ${TEAM_NUMBER_RANGE_REGEX} ]]; then
	echo "Error: 팀 번호가 옳지 않습니다."
	echo "       팀 범위: 1 ~ 16"
	exit 1
fi

if [[ ! "${LANG_EXTENSION}" =~ ${FILE_EXT_REGEX} ]]; then
	echo -e "Error: 파일 확장자가 옳지 않습니다."
	echo -e "       올바른 확장자: 'py' 또는 'java'"
	exit 1
fi

###############################################################################
# 인수 검증
###############################################################################
arg_count=$#
day_problem_number=$1
file_path=$2

file_extension="${file_path##*.}"

if [[ "${arg_count}" -ne 2 ]]; then
	echo "Error: 인수의 개수가 옳지 않습니다."
	echo "       사용법: $0 <일차-문제 번호> <파일 경로>"
	exit 1
fi

if [[ ! "${day_problem_number}" =~ ^${DAY_RANGE_REGEX}-${PROBLEM_NUMBER_REGEX}$ ]]; then
	echo "Error: 일차와 문제 번호의 형식 또는 범위가 옳지 않습니다."
	echo "       형식: <일차>-<문제 번호>"
	echo "       범위: <일차> 1 ~ 15, <문제 번호> 1 ~ 12"
	exit 1
fi

if [[ "${file_extension}" != "${LANG_EXTENSION}" ]]; then
	echo "Error: 파일의 확장자가 사전 입력된 언어의 확장자와 일치하지 않습니다."
	echo "       ${file_extension} != ${LANG_EXTENSION}"
	exit 1
elif [[ ! -f "${file_path}" ]]; then
	echo "Error: 파일을 찾을 수 없습니다."
	exit 1
elif [[ ! -s "${file_path}" ]]; then
	echo "Error: 파일이 비어있습니다."
	exit 1
fi

###############################################################################
# 제출
#
# - 주의사항
# Windows는 유니코드 지원에 문제가 있으므로, `국가 또는 지역` => `관리자 옵션`
# => `유니코드를 지원하지 않는 프로그램용 언어` => `시스템 로캘 변경`에서
# `Beta: 세계 언어 지원을 위해 Unicode UTF-8 사용`이 설정되어 있지 않다면,
# 아래의 `curl` 옵션값 중 `charset=UTF-8`을 `charset=EUC-KR`로 변경해야 합니다.
###############################################################################
solved_problem=$(echo "${day_problem_number}" | awk -F- '{printf "%d일차 - %d번", $1, $2}')
raw_code=$(<"${file_path}")

# Windows이면 charset 변경
charset="UTF-8"
if [[ $(uname -s) =~ ^(MINGW32|MINGW64|CYGWIN) ]]; then
	charset="EUC-KR"
fi

response=$(
	curl -s -k -w "%{http_code}" -o /dev/null \
		-X POST "${FORM_URL}" \
		-H "Content-Type: application/x-www-form-urlencoded; charset=${charset}" \
		--data-urlencode "${NAME_FIELD}=${NAME}" \
		--data-urlencode "${TEAM_NUMBER_FIELD}=${TEAM_NUMBER}" \
		--data-urlencode "${SOLVED_PROBLEM_FIELD}=${solved_problem}" \
		--data-urlencode "${RAW_CODE_FIELD}=${raw_code}" \
		--data-urlencode "${GITHUB_OR_BLOG_URL_FIELD}=${GITHUB_OR_BLOG_URL}"
)

if [ "${response}" -eq 200 ]; then
	echo "제출 성공"
else
	echo "Error: 제출 실패"
	echo "       HTTP 상태 코드: ${response}"
fi