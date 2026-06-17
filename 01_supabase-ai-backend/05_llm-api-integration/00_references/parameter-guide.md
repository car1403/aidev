# Parameter Guide

LLM API 파라미터는 모델 응답의 성격을 조절하는 설정입니다.

## temperature

`temperature`는 응답의 무작위성과 창의성을 조절합니다.

```text
0.0에 가까움
-> 더 안정적이고 반복 가능한 응답

1.0에 가까움
-> 더 다양하고 창의적인 응답
```

## top_p

`top_p`는 모델이 다음 단어를 고를 때 고려하는 후보 범위를 조절합니다.

초보 수업에서는 `temperature`를 먼저 이해하고, `top_p`는 기본값에 가깝게 두는 것이 좋습니다.

## max_tokens

`max_tokens`는 모델이 생성할 수 있는 최대 출력 길이를 제한합니다.

출력 길이가 길어질수록 비용이 늘 수 있습니다. 실제 API 호출 전에는 `max_tokens`를 너무 크게 잡지 않습니다.

## thinkingLevel

`thinkingLevel`은 모든 LLM API에서 공통으로 제공되는 표준 파라미터는 아닙니다.

일부 모델이나 SDK에서는 모델이 얼마나 깊게 추론할지 조절하는 설정을 제공할 수 있습니다. 예를 들어 빠른 응답이 중요한 경우에는 낮은 수준을, 복잡한 분석이 필요한 경우에는 높은 수준을 선택할 수 있습니다.

다만 파라미터 이름, 지원 모델, 비용 영향은 서비스와 SDK 버전에 따라 달라질 수 있습니다. 수업에서 실제로 사용할 때는 반드시 공식 문서와 API 콘솔 화면에서 현재 지원 여부를 확인합니다.

## 같이 보면 좋은 문서

```text
model-parameter-comparison-guide.md
token-cost-safety-guide.md
```
