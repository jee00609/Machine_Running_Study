## Student Mat Pass Dataset

### Feature List

* school - 학생의 학교 
	* binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira
* sex - 학생의 성별
	* binary: 'F' - female or 'M' - male
* age - 학생의 나이 
	* numeric: from 15 to 22
* address - 학생의 주소 구분 
	* binary: 'U' - urban or 'R' - rural
* famsize - 가족 규모 
	* binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3
* Pstatus - 학생과 부모 동반거주 여부 
	* binary: 'T' - living together or 'A' - apart
* Medu - 학생 어머니 교육 수준  
	* numeric: 0 - none
	* 1 - primary education (4th grade)
	* 2 – 5th to 9th grade
	* 3 – secondary education 
	* 4 – higher education
* Fedu - 학생 아버지 교육 수준
 	* numeric: 0 - none
	* 1 - primary education (4th grade)
	* 2 – 5th to 9th grade
	* 3 – secondary education 
	* 4 – higher education
* Mjob - 학생 어머니 직업 
	*  'teacher'
	*  'health'  
	*  'services' 
	*  'at_home'
	*  'other'
* Fjob - 학생 아버지 직업
 	*  'teacher'
	*  'health'  
	*  'services' 
	*  'at_home'
	*  'other'
* reason - 학교를 선택한 이유 
	* close to 'home'
	* school 'reputation'
	* 'course' preference 
	* 'other'
* guardian - 학생의 보호자 
	* 'mother'
	* 'father'
	* 'other'
* traveltime - 집에서 학교까지 걸리는 시간 
	* numeric
	* 1 - <15 min.
	* 2 - 15 to 30 min.
	* 3 - 30 min. to 1 hour,
	* 4 - >1 hour
* studytime - 주간 공부 시간 
	* numeric
	* 1 - <2 hours
	* 2 - 2 to 5 hours
	* 3 - 5 to 10 hours
	* 4 - >10 hours
* failures - 지난 시험 pass 실패 횟수 
	* numeric: n if 1<=n<3, else 4
* paid - 추가 교육 여부(ex. 과외/학원) 
	* binary: yes or no
* activities - 외부활동 
	* binary: yes or no
* nursery - 유치원 졸업 여부 
 	* binary: yes or no
* internet - 집 인터넷 연결 여부 
	* binary: yes or no
* romantic - 이성친구 유무 여부 
	* binary: yes or no
* famrel - 가족내 화목한 정도 
	* numeric: from 1 - very bad to 5 - excellent
* freetime - 하교이후 자유시간 
	* numeric: from 1 - very low to 5 - very high
* goout - 친한 친구 수 
	* numeric: from 1 - very low to 5 - very high
* Dalc - 평일 알콜 섭취 정도 
	* numeric: from 1 - very low to 5 - very high
* Walc - 주말 알콜 섭취 정도 
	* numeric: from 1 - very low to 5 - very high
* health - 건강 정도 
	* numeric: from 1 - very bad to 5 - very good
* absences - 결석 횟수 
	* numeric: from 0 to 93
* Pass/Fail - 최종 시험 통과 여부(binary)

[참조 사이트: Kaggle](https://www.kaggle.com/uciml/student-alcohol-consumption)