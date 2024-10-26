https://school.programmers.co.kr/learn/courses/30/lessons/70129


입출력 예 #1   

"110010101001"이 "1"이 될 때까지 이진 변환을 가하는 과정은 다음과 같습니다.   
회차	이진 변환 이전	제거할 0의 개수	0 제거 후 길이	이진 변환 결과   
1	"110010101001"	6		6		"110"   
2	"110"		1		2		"10"   
3	"10"		1		1		"1"   
3번의 이진 변환을 하는 동안 8개의 0을 제거했으므로, [3,8]을 return 해야 합니다.   

입출력 예 #2   
  
"01110"이 "1"이 될 때까지 이진 변환을 가하는 과정은 다음과 같습니다.   
회차	이진 변환 이전	제거할 0의 개수	0 제거 후 길이	이진 변환 결과   
1	"01110"		2		3		"11"   
2	"11"		0		2		"10"   
3	"10"		1		1		"1"   
3번의 이진 변환을 하는 동안 3개의 0을 제거했으므로, [3,3]을 return 해야 합니다.   
   
입출력 예 #3   
   
"1111111"이 "1"이 될 때까지 이진 변환을 가하는 과정은 다음과 같습니다.   
회차	이진 변환 이전	제거할 0의 개수	0 제거 후 길이	이진 변환 결과   
1	"1111111"	0	 		7	"111"   
2	"111"		0			3	"11"   
3	"11"		0			2	"10"   
4	"10"		1			1	"1"   
4번의 이진 변환을 하는 동안 1개의 0을 제거했으므로, [4,1]을 return 해야 합니다.    

초기 상태   
current: 주어진 입력 문자열 (예: "110010101001")   
answer: [0, 0] (변환 횟수와 제거된 0의 개수)   
while 루프 설명   
루프의 조건은 strcmp(current, "1") != 0입니다. 즉, current가 "1"이 아닐 때 계속해서 반복합니다.   
   
1. 첫 번째 회차      
변수 초기화      
   
length: "110010101001"의 길이 (12)   
oneCount: 0 (0을 제거한 1의 개수)      
for 루프 (문자열을 순회하며 1과 0의 개수 세기)   
   
i = 0: current[0]는 '1' → oneCount 증가 (1)   
i = 1: current[1]는 '1' → oneCount 증가 (2)   
i = 2: current[2]는 '0' → answer[1] 증가 (1)   
i = 3: current[3]는 '0' → answer[1] 증가 (2)   
i = 4: current[4]는 '1' → oneCount 증가 (3)   
i = 5: current[5]는 '0' → answer[1] 증가 (3)   
i = 6: current[6]는 '1' → oneCount 증가 (4)   
i = 7: current[7]는 '0' → answer[1] 증가 (4)   
i = 8: current[8]는 '0' → answer[1] 증가 (5)    
i = 9: current[9]는 '1' → oneCount 증가 (5)     
i = 10: current[10]는 '0' → answer[1] 증가 (6)    
i = 11: current[11]는 '1' → oneCount 증가 (6)    
변환 과정   
   
oneCount: 6 (남아 있는 1의 개수)   
newLength: 0 (새 문자열의 길이)    
temp를 통해 oneCount를 2진수로 변환 하여 newLength 계산:    
temp = 6 → 3 비트 필요 (110)   
메모리 해제 및 새 문자열 할당   
   
이전 문자열 current 메모리 해제   
current에 대해 새 메모리 할당 (4 바이트, 3 + 1 = 4)    
새로운 이진 문자열 설정    
   
current[3] = '\0'   
current를 2진수로 변환하여 설정:    
current[2] = '0' (6 % 2 = 0)   
current[1] = '1' (3 % 2 = 1)   
current[0] = '1' (1 % 2 = 1)    
변환 횟수 증가   
   
answer[0]++ (1회 변환)   
   
2. 두 번째 회차   
변수 초기화   
    
current: "110"   
length: 3    
oneCount: 0   
for 루프   
   
i = 0: current[0]는 '1' → oneCount 증가 (1)   
i = 1: current[1]는 '1' → oneCount 증가 (2)   
i = 2: current[2]는 '0' → answer[1] 증가 (7)   
변환 과정   
   
oneCount: 2   
newLength: 1 (2의 2진수는 10)   
메모리 해제 및 새 문자열 할당    
   
이전 문자열 current 메모리 해제   
새 메모리 할당 (2 바이트, 1 + 1 = 2)    
새로운 이진 문자열 설정   
   
current[2] = '\0'   
current[1] = '0' (2 % 2 = 0)    
current[0] = '1' (1 % 2 = 1)    
변환 횟수 증가   
   
answer[0]++ (2회 변환)   
   
3. 세 번째 회차   
변수 초기화   
   
current: "10"   
length: 2   
oneCount: 0   
for 루프   
    
i = 0: current[0]는 '1' → oneCount 증가 (1)    
i = 1: current[1]는 '0' → answer[1]++ (8)    
변환 과정   
   
oneCount: 1   
newLength: 0 (1의 2진수는 1)    
메모리 해제 및 새 문자열 할당    
   
이전 문자열 current 메모리 해제    
새 메모리 할당 (2 바이트, 1 + 1 = 2)    
새로운 이진 문자열 설정    
    
current[1] = '\0'    
current[0] = '1' (1 % 2 = 1)     
변환 횟수 증가    
    
answer[0]++ (3회 변환)     
최종 상태     
current: "1"    
answer: [3, 8] (총 3회 변환, 제거된 0의 총 개수 8)     
이 과정을 통해 최종적으로 current가 "1"이 되고, 변환 횟수와 제거된 0의 개수가 기록되어 반환됩니다.     
