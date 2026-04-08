#!/usr/bin/env python3
"""
이미지 주석 추가 스크립트
규칙 7에 따라 모든 이미지 링크 아래에 LLM_Image_DESC 주석을 추가합니다.
파일명, 컨텍스트(섹션 헤더, alt text), 폴더명을 기반으로 주석을 생성합니다.
"""

import re
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

# 이미지 유형 판별 패턴
DIAGRAM_PATTERNS = [
    r"flow", r"diagram", r"sequence", r"architecture",
    r"overview_\d{2}", r"overview_\d{2}_", r"mapping_flow",
]

# 파일명 → 설명 매핑
FILENAME_DESCRIPTIONS = {
    # Flow diagrams
    "idp_login_flow": {"type": "Flowchart", "desc": "IdP 로그인 처리 흐름도", "detail": "Gamebase SDK의 IdP 로그인 요청부터 인증 결과 반환까지의 처리 흐름을 나타내는 순서도"},
    "login_for_last_logged_in_provider_flow": {"type": "Flowchart", "desc": "최근 로그인 Provider 자동 로그인 흐름도", "detail": "마지막으로 로그인한 Provider 정보를 이용한 자동 로그인 처리 흐름"},
    "auth_add_mapping_flow": {"type": "Flowchart", "desc": "계정 매핑 추가 흐름도", "detail": "기존 계정에 새로운 IdP를 매핑하는 처리 흐름을 나타내는 순서도"},
    "purchase_flow_001": {"type": "Sequence Diagram", "desc": "결제 처리 흐름도", "detail": "GameClient, GamebaseSDK, GameServer 간의 결제 요청 및 소비 처리 시퀀스"},
    "purchase_flow_002": {"type": "Sequence Diagram", "desc": "결제 처리 흐름도 (v2)", "detail": "GameClient, GamebaseSDK, GameServer 간의 결제 요청 및 소비 처리 시퀀스 (갱신된 버전)"},
    "purchase_retry_transaction_flow": {"type": "Sequence Diagram", "desc": "결제 재처리 흐름도", "detail": "미소비 결제 건에 대한 재처리 흐름을 나타내는 시퀀스 다이어그램"},
    "consume_flow": {"type": "Sequence Diagram", "desc": "아이템 소비 흐름도", "detail": "결제 후 아이템 소비 처리의 시퀀스 다이어그램"},

    # Overview
    "Gamebase_overview_00": {"type": "Diagram", "desc": "Gamebase 서비스 구성도", "detail": "Gamebase 플랫폼의 전체 서비스 아키텍처와 구성 요소를 나타내는 개요도"},
    "gamebase_overview_01": {"type": "Diagram", "desc": "Gamebase 핵심 기능 개요", "detail": "Gamebase의 주요 기능별 아이콘과 설명을 포함한 기능 소개 다이어그램"},
    "Gamebase_overview_02": {"type": "Diagram", "desc": "Gamebase Analytics 지표 개요", "detail": "실시간 지표, 매출 지표, 이용자 지표, 범용성 지표 4가지 카테고리의 분석 기능 소개"},
    "gamebase_overview_02": {"type": "Diagram", "desc": "Gamebase Analytics 지표 개요", "detail": "실시간 지표, 매출 지표, 이용자 지표, 범용성 지표의 분석 기능 소개"},
    "Gamebase_overview_03": {"type": "Diagram", "desc": "Gamebase 서비스 아키텍처", "detail": "Gamebase 플랫폼의 시스템 아키텍처와 연동 구조를 나타내는 다이어그램"},
    "gamebase_overview_03": {"type": "Diagram", "desc": "Gamebase 서비스 아키텍처", "detail": "Gamebase 플랫폼의 시스템 아키텍처와 연동 구조를 나타내는 다이어그램"},
    "Gamebase_Sample_App1": {"type": "Screenshot", "desc": "Gamebase Sample App 화면", "detail": "Gamebase Sample App의 주요 기능을 보여주는 실행 화면 스크린샷"},

    # Maintenance/Terms
    "gamebase_ban_01": {"type": "Screenshot", "desc": "이용 정지 팝업 화면", "detail": "이용 정지된 사용자에게 표시되는 Gamebase 팝업 화면"},
    "gamebase_maintenance": {"type": "Screenshot", "desc": "점검 안내 화면", "detail": "서비스 점검 시 사용자에게 표시되는 점검 안내 팝업/웹뷰 화면"},
    "termsView": {"type": "Screenshot", "desc": "약관 동의 화면", "detail": "Gamebase 약관 동의 UI 화면"},
}

# 콘솔 기능별 설명 매핑 (폴더명 기반)
FOLDER_CONTEXT = {
    "oper-analytics": {"area": "Analytics", "desc_prefix": "Gamebase Analytics 콘솔"},
    "oper-app": {"area": "앱 설정", "desc_prefix": "Gamebase 앱 설정 콘솔"},
    "oper-customer-service": {"area": "고객센터", "desc_prefix": "Gamebase 고객센터 콘솔"},
    "oper-management": {"area": "관리", "desc_prefix": "Gamebase 관리 콘솔"},
    "oper-operation": {"area": "운영", "desc_prefix": "Gamebase 운영 콘솔"},
    "oper-purchase": {"area": "결제", "desc_prefix": "Gamebase 결제 콘솔"},
    "oper-push": {"area": "Push", "desc_prefix": "Gamebase Push 콘솔"},
    "oper-ban": {"area": "이용정지", "desc_prefix": "Gamebase 이용정지 콘솔"},
    "oper-coupon": {"area": "쿠폰", "desc_prefix": "Gamebase 쿠폰 콘솔"},
    "oper-member": {"area": "회원", "desc_prefix": "Gamebase 회원 관리 콘솔"},
    "oper-operating-indicator": {"area": "운영지표", "desc_prefix": "Gamebase 운영지표 콘솔"},
    "console-for-aws": {"area": "AWS Console", "desc_prefix": "Gamebase for AWS 콘솔"},
    "console-amazon-guide": {"area": "Amazon", "desc_prefix": "Amazon Appstore 콘솔"},
    "console-apple-guide": {"area": "Apple", "desc_prefix": "Apple 설정 콘솔"},
    "console-epicgames-guide": {"area": "Epic Games", "desc_prefix": "Epic Games Store 콘솔"},
    "console-google-guide": {"area": "Google", "desc_prefix": "Google Play Console"},
    "console-huawei-guide": {"area": "Huawei", "desc_prefix": "Huawei AppGallery 콘솔"},
    "console-mycard-guide": {"area": "MyCard", "desc_prefix": "MyCard 스토어 콘솔"},
    "console-steam-guide": {"area": "Steam", "desc_prefix": "Steam 스토어 콘솔"},
}

# 파일명 내 기능 키워드 → 섹션 설명
FILENAME_SECTION_MAP = {
    "analytics": "분석 지표",
    "purchase": "결제 관리",
    "push": "Push 알림",
    "operation": "운영 관리",
    "customer": "고객센터",
    "management": "관리 설정",
    "member": "회원 관리",
    "coupon": "쿠폰 관리",
    "ban": "이용정지",
    "app": "앱 설정",
    "auth": "인증 설정",
    "transfer": "기기 이전",
}


def is_diagram(filename):
    """이미지가 다이어그램인지 판별"""
    fname_lower = filename.lower()
    for pattern in DIAGRAM_PATTERNS:
        if re.search(pattern, fname_lower):
            return True
    return False


def get_section_header(content, img_pos):
    """이미지 위치 이전의 가장 가까운 섹션 헤더를 찾기"""
    before_img = content[:img_pos]
    headers = list(re.finditer(r"^(#{2,4})\s+(.+)$", before_img, re.MULTILINE))
    if headers:
        return headers[-1].group(2).strip()
    return None


def generate_annotation(filename, alt_text, section_header, folder_name, md_filename):
    """이미지 주석 생성"""
    fname_base = filename.rsplit(".", 1)[0] if "." in filename else filename

    # 1. 사전에 정의된 매핑 확인
    for key, info in FILENAME_DESCRIPTIONS.items():
        if fname_base.startswith(key) or key in fname_base:
            keywords = []
            if folder_name in FOLDER_CONTEXT:
                keywords.append(FOLDER_CONTEXT[folder_name]["area"])
            keywords.append(info["type"])
            if section_header:
                keywords.append(section_header[:30])
            return {
                "type": info["type"],
                "desc": info["desc"],
                "detail": info["detail"],
                "keywords": ", ".join(keywords[:5]),
            }

    # 2. 폴더 컨텍스트 기반 (콘솔 스크린샷)
    folder_ctx = FOLDER_CONTEXT.get(folder_name)
    if folder_ctx:
        section_desc = section_header if section_header else folder_ctx["area"]
        # 번호 추출 (analytics_01 → 01)
        num_match = re.search(r"_(\d{2})_", filename)
        num_str = f" #{num_match.group(1)}" if num_match else ""

        img_type = "Screenshot"
        desc = f"{folder_ctx['desc_prefix']} {section_desc} 화면{num_str}"
        detail = f"{folder_ctx['desc_prefix']}의 {section_desc} 기능 설정/조회 화면 스크린샷"
        keywords = [folder_ctx["area"], "Console", "Screenshot"]
        if section_header:
            keywords.append(section_header[:30])

        return {
            "type": img_type,
            "desc": desc,
            "detail": detail,
            "keywords": ", ".join(keywords[:5]),
        }

    # 3. SDK 관련 이미지
    if is_diagram(filename):
        img_type = "Flowchart"
        desc = f"{section_header or fname_base} 흐름도"
        detail = f"{section_header or fname_base}의 처리 흐름을 나타내는 다이어그램"
        keywords = ["Diagram", "Flow"]
    elif "Console_App" in filename or "console_" in filename.lower():
        img_type = "Screenshot"
        # Console_App_Auth_appleid → Apple ID 인증 설정
        desc = f"콘솔 설정 화면 ({fname_base})"
        detail = f"Gamebase 콘솔의 앱 설정 관련 스크린샷"
        keywords = ["Console", "Screenshot", "App Settings"]
    elif "developers-guide" in filename.lower():
        img_type = "Screenshot"
        desc = f"SDK 가이드 화면 ({section_header or fname_base})"
        detail = f"SDK 설정/사용 가이드 관련 스크린샷"
        keywords = ["SDK", "Screenshot"]
    elif "google-oauth" in filename.lower():
        img_type = "Screenshot"
        desc = "Google OAuth 설정 화면"
        detail = "Google OAuth 인증 설정을 위한 콘솔 화면 스크린샷"
        keywords = ["Google", "OAuth", "Screenshot"]
    elif "pre_server_address" in filename.lower():
        img_type = "Screenshot"
        desc = "서버 주소 사전 설정 화면"
        detail = "API 서버 주소 사전 등록/설정 화면"
        keywords = ["Server", "API", "Screenshot"]
    elif "unreal-developers-guide" in filename.lower():
        img_type = "Screenshot"
        desc = f"Unreal 개발 환경 설정 화면"
        if "android" in filename.lower():
            desc = "Unreal Android 빌드 설정 화면"
            detail = "Unreal Engine의 Android 빌드를 위한 프로젝트 설정 화면"
        elif "ios" in filename.lower():
            desc = "Unreal iOS 빌드 설정 화면"
            detail = "Unreal Engine의 iOS 빌드를 위한 프로젝트 설정 화면"
        elif "windows" in filename.lower():
            desc = "Unreal Windows 빌드 설정 화면"
            detail = "Unreal Engine의 Windows 빌드를 위한 프로젝트 설정 화면"
        else:
            detail = "Unreal Engine 개발 환경 설정 스크린샷"
        keywords = ["Unreal", "Screenshot", "Settings"]
    else:
        img_type = "Screenshot"
        desc = f"{section_header or fname_base} 관련 화면"
        detail = f"{section_header or folder_name} 관련 스크린샷"
        keywords = ["Screenshot"]

    # 플랫폼 키워드 추가
    platform_map = {"aos": "Android", "ios": "iOS", "unity": "Unity", "unreal": "Unreal"}
    for prefix, platform in platform_map.items():
        if folder_name.startswith(prefix) or md_filename.startswith(prefix):
            keywords.insert(0, platform)
            break

    if section_header:
        keywords.append(section_header[:30])

    return {
        "type": img_type,
        "desc": desc,
        "detail": detail,
        "keywords": ", ".join(keywords[:5]),
    }


def add_annotations_to_file(filepath, folder_name):
    """파일의 모든 이미지 참조에 주석 추가"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 이미 주석이 있는 경우 스킵
    if "LLM_Image_DESC" in content:
        return 0

    # 이미지 참조 찾기 (역순으로 처리하여 위치 변경 방지)
    img_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    matches = list(img_pattern.finditer(content))

    if not matches:
        return 0

    count = 0
    # 역순으로 처리
    for match in reversed(matches):
        alt_text = match.group(1)
        img_path = match.group(2)
        img_filename = img_path.split("/")[-1]
        pos = match.end()

        # 섹션 헤더 찾기
        section_header = get_section_header(content, match.start())

        # 주석 생성
        annotation = generate_annotation(
            img_filename, alt_text, section_header, folder_name, filepath.name
        )

        comment = f"""
<!-- LLM_Image_DESC_{TIMESTAMP}
    유형: {annotation['type']}
    내용: {annotation['desc']}
    구성: {annotation['detail']}
    Keyword: {annotation['keywords']}
-->"""

        # 이미지 라인 끝 다음에 주석 삽입
        # 이미지 다음 줄바꿈 위치 찾기
        next_newline = content.find("\n", pos)
        if next_newline == -1:
            content = content + comment
        else:
            content = content[:next_newline] + comment + content[next_newline:]

        count += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return count


def main():
    print("이미지 주석 추가 시작...")
    total_annotations = 0
    files_modified = 0

    for folder in sorted(DOCS_DIR.iterdir()):
        if not folder.is_dir():
            continue

        folder_name = folder.name
        for md_file in sorted(folder.glob("*.md")):
            count = add_annotations_to_file(md_file, folder_name)
            if count > 0:
                files_modified += 1
                total_annotations += count
                print(f"  {md_file.relative_to(DOCS_DIR)}: {count}개 주석 추가")

    print(f"\n{'=' * 60}")
    print(f"총 {files_modified}개 파일에 {total_annotations}개 이미지 주석 추가 완료")


if __name__ == "__main__":
    main()
