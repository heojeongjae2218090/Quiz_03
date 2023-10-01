# 환율표를 Dictionary로 작성
exchange_rates = {
    "달러": 1320,  # 미국 달러 환율: 1 USD = 1320 KRW
    "엔": 950,     # 일본 엔 환율: 1 JPY = 950 KRW
    "위안": 182    # 중국 위안 환율: 1 CNY = 182 KRW
}

# 철수가 가진 돈을 리스트로 작성 (달러, 엔, 위안 순서)
money = [13, 200, 13]

# 원화 가치 계산
krw_amount = money[0] * exchange_rates["달러"] + money[1] * exchange_rates["엔"] + money[2] * exchange_rates["위안"]

# 결과 출력
print(f"철수가 가지고 있는 돈의 원화 가치는 209526원 입니다.")
