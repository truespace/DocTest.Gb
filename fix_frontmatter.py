#!/usr/bin/env python3
"""
frontmatter 보완 스크립트
규칙 5에 따라 split, created_date_time, keyword 필드를 추가/수정합니다.
"""

import re
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"
NOW = datetime.now().strftime("%Y%m%d_%H%M%S")

# 키워드 사전 (규칙 5 기반)
PLATFORM_KEYWORDS = {
    "Android": r"\bAndroid\b",
    "iOS": r"\biOS\b",
    "Unity": r"\bUnity\b",
    "Unreal": r"\bUnreal\b",
    "Console": r"\bConsole\b|콘솔",
}

DEV_ENV_KEYWORDS = {
    "Gradle": r"\bGradle\b",
    "CocoaPods": r"\bCocoaPods\b",
    "XCode": r"\bXcode\b|\bXCode\b",
    "Java": r"\bJava\b",
    "Kotlin": r"\bKotlin\b",
    "Swift": r"\bSwift\b",
    "C++": r"\bC\+\+\b",
    "C#": r"\bC#\b",
    "Objective-C": r"\bObjective-C\b",
}

FEATURE_KEYWORDS = {
    "Login": r"\bLogin\b|로그인",
    "Logout": r"\bLogout\b|로그아웃",
    "Mapping": r"\bMapping\b|매핑",
    "Withdraw": r"\bWithdraw\b|탈퇴",
    "Purchase": r"\bPurchase\b|결제|구매",
    "Consume": r"\bConsume\b|소비",
    "Push": r"\bPush\b|푸시",
    "WebView": r"\bWebView\b|웹뷰",
    "Alert": r"\bAlert\b|알림",
    "Analytics": r"\bAnalytics\b|분석",
    "Logger": r"\bLogger\b|로거",
    "Initialize": r"\bInitialize\b|초기화",
    "Authentication": r"\bAuthentication\b|인증",
    "GraceBan": r"\bGraceBan\b|이용 정지 유예",
    "TemporaryWithdrawal": r"\bTemporaryWithdrawal\b|탈퇴 유예",
    "TransferAccount": r"\bTransferAccount\b|기기 이전",
    "Terms": r"\bTerms\b|약관",
    "ImageNotice": r"\bImageNotice\b|이미지 공지",
    "Contact": r"\bContact\b|고객센터",
    "Coupon": r"\bCoupon\b|쿠폰",
    "Error": r"\bError\b|에러|오류",
}

API_KEYWORDS = {
    "LoginForLastLoggedInProvider": r"\bLoginForLastLoggedInProvider\b|\bloginForLastLoggedInProvider\b",
    "RequestPurchase": r"\bRequestPurchase\b|\brequestPurchase\b",
    "ShowTermsView": r"\bShowTermsView\b|\bshowTermsView\b",
    "RequestItemListOfNotConsumed": r"\bRequestItemListOfNotConsumed\b|\brequestItemListOfNotConsumed\b",
    "RequestRetryTransaction": r"\bRequestRetryTransaction\b|\brequestRetryTransaction\b",
    "ShowImageNotices": r"\bShowImageNotices\b|\bshowImageNotices\b",
    "RegisterPush": r"\bRegisterPush\b|\bregisterPush\b",
    "ShowWebView": r"\bShowWebView\b|\bshowWebView\b",
}

# 파일명 기반 플랫폼 추출
FILENAME_PLATFORM_MAP = {
    "aos-": "Android",
    "ios-": "iOS",
    "unity-": "Unity",
    "unreal-": "Unreal",
    "oper-": "Console",
    "console-": "Console",
    "api-guide": "Server API",
    "release-notes-android": "Android",
    "release-notes-ios": "iOS",
    "release-notes-unity": "Unity",
    "release-notes-unreal": "Unreal",
    "release-notes-console": "Console",
    "release-notes-server": "Server API",
}


def extract_keywords(content, filename):
    """문서 내용과 파일명 기반으로 키워드 추출 (3~10개)"""
    keywords = []

    # 파일명 기반 플랫폼 키워드
    for prefix, platform in FILENAME_PLATFORM_MAP.items():
        if filename.startswith(prefix):
            keywords.append(platform)
            break

    # 내용 기반 키워드 추출 (코드블록 제외)
    # 코드블록 제거
    clean_content = re.sub(r"```[\s\S]*?```", "", content)

    all_keyword_dicts = [
        (FEATURE_KEYWORDS, 5),  # 기능 키워드 우선
        (API_KEYWORDS, 3),
        (DEV_ENV_KEYWORDS, 2),
        (PLATFORM_KEYWORDS, 2),
    ]

    for kw_dict, max_count in all_keyword_dicts:
        count = 0
        for kw_name, pattern in kw_dict.items():
            if kw_name in keywords:
                continue
            if re.search(pattern, clean_content):
                keywords.append(kw_name)
                count += 1
                if count >= max_count:
                    break

    # 릴리스 노트: 버전 키워드
    if "release-notes" in filename:
        keywords.append("Release Notes")
        versions = re.findall(r"\bv?\d+\.\d+\.\d+\b", content[:500])
        if versions:
            keywords.append(versions[0])

    # upgrade-guide
    if "upgrade-guide" in filename:
        keywords.append("Upgrade Guide")
        versions = re.findall(r"\bv?\d+\.\d+\.\d+\b", content[:500])
        if versions:
            keywords.append(versions[0])

    # error-code
    if "error-code" in filename:
        keywords.append("Error Code")

    # Overview
    if "overview" in filename.lower():
        keywords.append("Overview")

    # 중복 제거 및 3~10개 제한
    seen = set()
    unique_keywords = []
    for kw in keywords:
        if kw not in seen:
            seen.add(kw)
            unique_keywords.append(kw)

    # 최소 3개 보장
    if len(unique_keywords) < 3:
        # 일반 키워드 추가
        for kw_dict in [FEATURE_KEYWORDS, PLATFORM_KEYWORDS, DEV_ENV_KEYWORDS]:
            for kw_name, pattern in kw_dict.items():
                if kw_name not in seen and re.search(pattern, content):
                    unique_keywords.append(kw_name)
                    seen.add(kw_name)
                    if len(unique_keywords) >= 3:
                        break
            if len(unique_keywords) >= 3:
                break

    # 그래도 3개 미만이면 파일명에서 추출
    if len(unique_keywords) < 3:
        parts = filename.replace(".md", "").split("-")
        for part in parts:
            if part and part.capitalize() not in seen and len(unique_keywords) < 3:
                unique_keywords.append(part.capitalize())
                seen.add(part.capitalize())

    return unique_keywords[:10]


def parse_frontmatter(content):
    """frontmatter 파싱"""
    if not content.startswith("---"):
        return {}, content

    end = content.find("---", 3)
    if end == -1:
        return {}, content

    fm_text = content[3:end].strip()
    body = content[end + 3:].lstrip("\n")

    fm = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip().strip('"').strip("'")

    return fm, body


def build_frontmatter(fm_dict):
    """frontmatter 딕셔너리를 문자열로 변환"""
    lines = ["---"]
    for key, val in fm_dict.items():
        if key == "keyword":
            lines.append(f"keyword: {val}")
        elif key == "section":
            lines.append(f'section: "{val}"')
        else:
            lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines)


def process_content_file(filepath):
    """분할/미분할 파일의 frontmatter 보완"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fm, body = parse_frontmatter(content)
    if not fm:
        return False

    changed = False

    # split 필드 추가
    if "split" not in fm:
        fm["split"] = "true"
        changed = True

    # created_date → created_date_time 변환
    if "created_date" in fm and "created_date_time" not in fm:
        del fm["created_date"]
        fm["created_date_time"] = NOW
        changed = True
    elif "created_date_time" not in fm:
        fm["created_date_time"] = NOW
        changed = True

    # keyword 추가
    if "keyword" not in fm:
        keywords = extract_keywords(body, filepath.name)
        fm["keyword"] = ", ".join(keywords)
        changed = True

    if changed:
        # 키 순서 정리: source, section, order, split, created_date_time, keyword
        ordered = {}
        key_order = ["source", "section", "order", "split", "created_date_time", "keyword"]
        for key in key_order:
            if key in fm:
                ordered[key] = fm[key]
        for key in fm:
            if key not in ordered:
                ordered[key] = fm[key]

        new_content = build_frontmatter(ordered) + "\n\n" + body
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return changed


def process_index_file(filepath):
    """index 파일의 frontmatter에 created_date_time 추가"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fm, body = parse_frontmatter(content)
    if not fm:
        return False

    changed = False

    # created_date → created_date_time
    if "created_date" in fm and "created_date_time" not in fm:
        del fm["created_date"]
        fm["created_date_time"] = NOW
        changed = True

    if changed:
        new_content = build_frontmatter(fm) + "\n\n" + body
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return changed


def main():
    print("frontmatter 보완 시작...")
    content_updated = 0
    index_updated = 0

    # index 파일 처리
    for md_file in sorted(DOCS_DIR.glob("*.md")):
        if process_index_file(md_file):
            index_updated += 1

    # 분할/미분할 파일 처리
    for folder in sorted(DOCS_DIR.iterdir()):
        if not folder.is_dir():
            continue
        for md_file in sorted(folder.glob("*.md")):
            if process_content_file(md_file):
                content_updated += 1
                print(f"  보완: {md_file.relative_to(DOCS_DIR)}")

    print(f"\n{'=' * 60}")
    print(f"index 파일 {index_updated}개, 콘텐츠 파일 {content_updated}개 frontmatter 보완 완료")


if __name__ == "__main__":
    main()
